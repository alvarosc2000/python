from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from models.boardgame import BoardGame
from db.database import Base, engine, Session
from pydantic_models.BoardGameModel import BoardGameCreate
from fastapi.encoders import jsonable_encoder


app = FastAPI(
    title="Board Game API",
    description="API para juegos de mesa"
)

Base.metadata.create_all(bind=engine)


@app.get("/boardgames",tags=["Juegos"])
async def get_all_games():
    db = Session()
    try:
        data = db.query(BoardGame).all()
        return JSONResponse(content=jsonable_encoder(data))
    finally:
        db.close()


@app.get("/boardgames/{id}",tags=["Juegos"])
async def get_game_by_id(id:int):
    db = Session()
    try:
        data = db.query(BoardGame).filter(BoardGame.id == id).first()
        if not data:
            raise HTTPException(status_code=404, detail="Juego no encontrado")
        return jsonable_encoder(data)
    finally:
        db.close()

@app.get("/boardgames/genre/{genre}", tags=["Juegos"])
async def get_game_by_genre(genre: str):
    db = Session()
    try:
        data = db.query(BoardGame).filter(BoardGame.genre == genre).first()  # sin comillas
        if not data:
            raise HTTPException(status_code=404, detail="Juego no encontrado")
        return jsonable_encoder(data)
    finally:
        db.close()


@app.post("/boardgames/create", tags=["Juegos"])
async def create_game(game: BoardGameCreate):
    db = Session()
    try:
        # No buscar por id si es None, solo crear directamente
        if game.id is not None:
            existing_game = db.query(BoardGame).filter(BoardGame.id == game.id).first()
            if existing_game:
                raise HTTPException(status_code=400, detail="Juego ya existe con ese id")
        new_game = BoardGame(**game.model_dump(exclude={"id"}))  # excluye id para que DB lo genere
        db.add(new_game)
        db.commit()
        db.refresh(new_game)
        return jsonable_encoder(new_game)
    finally:
        db.close()



@app.put("/boardgames/update" , tags=["Juegos"])
async def update_game(id: int, game: BoardGameCreate):
    db = Session()
    try:
        existing = db.query(BoardGame).filter(BoardGame.id == id).first()  # <--- aquí estaba el error
        if not existing:
            raise HTTPException(status_code=404, detail="Juego no encontrado")
        for field, value in game.dict(exclude={"id"}).items():  # evitar sobrescribir el ID
            setattr(existing, field, value)
        db.commit()
        db.refresh(existing)
        return jsonable_encoder(existing)
    finally:
        db.close()


@app.delete("/boardgames/{id}", tags=["Juegos"])
async def delete_game(id: int):
    db = Session()
    try:
        game = db.query(BoardGame).filter(BoardGame.id == id).first()
        if not game:
            raise HTTPException(status_code=404, detail="Juego no encontrado")
        db.delete(game)
        db.commit()
        return {"message": "Juego eliminado"}
    finally:
        db.close()