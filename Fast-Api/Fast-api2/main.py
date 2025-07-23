from fastapi import Body, Depends, FastAPI, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, Field, constr
from typing import Optional
from jwt_utils import createToken, validate_token
from bd.database import Session, engine, Base
from models.movie import Movie as ModelMovie
from fastapi.encoders import jsonable_encoder

app = FastAPI(
    title="FastAPI",
    description="Ejemplo1"
)

headers = {"content-type": "charset=utf-8"}


Base.metadata.create_all(bind=engine)

# ------------------- MODELOS -------------------

class MovieCreate(BaseModel):
    id: Optional[int] = None
    title: constr(min_length=2, max_length=66)  # type: ignore
    overview: constr(min_length=2, max_length=66)  # type: ignore
    year: int = Field(default=2025)
    rating: float = Field(default=0.0)
    category: constr(min_length=2, max_length=66)  # type: ignore

class User(BaseModel):
    email: constr(min_length=3, max_length=66)  # type: ignore
    password: constr(min_length=2, max_length=22)  # type: ignore

# ------------------- AUTENTICACIÓN -------------------

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request) -> dict:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            try:
                payload = validate_token(credentials.credentials)
                return payload
            except Exception as e:
                raise HTTPException(status_code=403, detail=f"Token inválido: {str(e)}")
        else:
            raise HTTPException(status_code=403, detail="Token no proporcionado")

# ------------------- BASE DE DATOS FALSA -------------------

movies = [
    {
        'id': 1,
        'title': 'The Shawshank Redemption',
        'overview': 'Two imprisoned men bond over a number of years...',
        'year': 1994,
        'rating': 9.3,
        'category': 'Drama'
    },
    {
        'id': 2,
        'title': 'The Godfather',
        'overview': 'The aging patriarch of an organized crime dynasty...',
        'year': 1972,
        'rating': 9.2,
        'category': 'Crime'
    },
    {
        'id': 3,
        'title': 'The Dark Knight',
        'overview': 'When the menace known as the Joker wreaks havoc...',
        'year': 2008,
        'rating': 9.0,
        'category': 'Action'
    }
]

# ------------------- RUTAS -------------------

@app.get("/", tags=["Default"])
async def read_root():
    return HTMLResponse('<h2>HOLA MUNDO</h2>')

@app.get('/movies/', tags=['Movies'])
async def get_movies():
    db = Session()
    data = db.query(ModelMovie).all()
    return JSONResponse(content=jsonable_encoder(data))



@app.get('/movies/id/{id}', tags=['Movies'])
async def get_movie_by_id(id: int = Path(ge=1, le=100)):
    db = Session()
    try:
        movie = db.query(ModelMovie).filter(ModelMovie.id == id).first()
        if movie:
            return JSONResponse(
                content={
                    "id": movie.id,
                    "title": movie.title,
                    "overview": movie.overview,
                    "year": movie.year,
                    "rating": movie.rating,
                    "category": movie.category
                },
                headers=headers
            )
        raise HTTPException(status_code=404, detail="Película no encontrada")
    finally:
        db.close()


@app.get("/movies/category/{category}", tags=['Movies'])
async def get_movies_by_category(category: str):
    db = Session()
    try:
        movies = db.query(ModelMovie).filter(ModelMovie.category == category).all()
        if movies:
            result = []
            for movie in movies:
                result.append({
                    "id": movie.id,
                    "title": movie.title,
                    "overview": movie.overview,
                    "year": movie.year,
                    "rating": movie.rating,
                    "category": movie.category
                })
            return JSONResponse(content=result, headers=headers)
        raise HTTPException(status_code=404, detail="Película no encontrada")
    finally:
        db.close()


@app.post("/movies/crear", tags=["Movies"])
async def crear_movie(movie: MovieCreate):
    db = Session()
    try:
        # Verificar si ya existe una película con ese ID
        if movie.id is not None:
            existing = db.query(ModelMovie).filter(ModelMovie.id == movie.id).first()
            if existing:
                raise HTTPException(status_code=400, detail="Ya existe una película con ese ID")

        # Crear nueva instancia
        new_movie = ModelMovie(**movie.dict())

        db.add(new_movie)
        db.commit()
        db.refresh(new_movie)  # Para obtener los valores generados como el ID

        return JSONResponse(
            content={"message": "Película creada", "movie": {
                "id": new_movie.id,
                "title": new_movie.title,
                "overview": new_movie.overview,
                "year": new_movie.year,
                "rating": new_movie.rating,
                "category": new_movie.category
            }},
            headers=headers
        )
    finally:
        db.close()


@app.put("/movies/actualizar/{id}", tags=["Movies"])
async def actualizar_movie(id: int, movie: MovieCreate):
    db = Session()
    data = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if not data:
         raise HTTPException(status_code=404, detail="Película no actualizada")
    data.title = movie.title
    data.overview = movie.overview
    data.year = movie.year
    data.rating = movie.rating
    data.category = movie.category
    db.commit()

    return JSONResponse(content={'message': 'Se ha modificado la pelicula'})
    

@app.delete("/movies/delete/{id}", tags=["Movies"])
async def delete_movie(id: int = Path(ge=1, le=100)):
    db = Session()
    try:
        db_movie = db.query(ModelMovie).filter(ModelMovie.id == id).first()
        if not db_movie:
            raise HTTPException(status_code=404, detail="Película no encontrada")

        db.delete(db_movie)
        db.commit()

        return JSONResponse(
            content={"message": "Película eliminada", "movie": {
                "id": db_movie.id,
                "title": db_movie.title,
                "overview": db_movie.overview,
                "year": db_movie.year,
                "rating": db_movie.rating,
                "category": db_movie.category
            }},
            headers=headers
        )
    finally:
        db.close()


# ------------------- RUTA PROTEGIDA -------------------

@app.post("/login", tags=["Authentication"])
async def login(user: User):
    token: str = createToken(user.dict())
    return {"access_token": token}


@app.get("/usuario", tags=["Authentication"], dependencies=[Depends(JWTBearer())])
async def protected_user_data():
    return {"message": "Acceso autorizado. Bienvenido usuario autenticado"}
