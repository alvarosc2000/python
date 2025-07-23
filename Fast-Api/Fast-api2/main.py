from fastapi import Body, Depends, FastAPI, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, Field, constr
from typing import Optional
from jwt_utils import createToken, validate_token

app = FastAPI(
    title="FastAPI",
    description="Ejemplo1"
)

headers = {"content-type": "charset=utf-8"}

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

@app.get('/movies', tags=['Movies'])
async def get_movies():
    return JSONResponse(content=movies, headers=headers)

@app.get('/movies/id/{id}', tags=['Movies'])
async def get_movie_by_id(id: int = Path(ge=1, le=100)):
    result = next((item for item in movies if item["id"] == id), None)
    if result:
        return JSONResponse(content=result, headers=headers)
    raise HTTPException(status_code=404, detail="Película no encontrada")

@app.get("/movies/category/{category}", tags=['Movies'])
async def get_movies_by_category(category: str):
    result = [item for item in movies if item["category"].lower() == category.lower()]
    if result:
        return JSONResponse(content=result, headers=headers)
    raise HTTPException(status_code=404, detail="No movies found in this category")

@app.post("/movies/crear", tags=["Movies"])
async def crear_movie(movie: MovieCreate):
    if movie.id is None:
        movie.id = max((m["id"] for m in movies), default=0) + 1
    elif any(m["id"] == movie.id for m in movies):
        raise HTTPException(status_code=400, detail="Ya existe una película con ese ID")

    new_movie = movie.dict()
    movies.append(new_movie)
    return JSONResponse(content={"message": "Película creada", "movie": new_movie}, headers=headers)

@app.put("/movies/actualizar/{id}", tags=["Movies"])
async def actualizar_movie(id: int, movie: MovieCreate):
    for item in movies:
        if item["id"] == id:
            item.update(movie.dict(exclude={"id"}))
            return JSONResponse(content={"message": "Película actualizada", "movie": item}, headers=headers)
    raise HTTPException(status_code=404, detail="Película no encontrada")

@app.delete("/movies/delete/{id}", tags=["Movies"])
async def delete_movie(id: int = Path(ge=1, le=100)):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(content={"message": "Película eliminada", "movie": item}, headers=headers)
    raise HTTPException(status_code=404, detail="Película no encontrada")

# ------------------- RUTA PROTEGIDA -------------------

@app.post("/login", tags=["Authentication"])
async def login(user: User):
    token: str = createToken(user.dict())
    return {"access_token": token}


@app.get("/usuario", tags=["Authentication"], dependencies=[Depends(JWTBearer())])
async def protected_user_data():
    return {"message": "Acceso autorizado. Bienvenido usuario autenticado"}
