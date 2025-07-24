from fastapi import HTTPException
from fastapi import FastAPI
from models.book import Book
from db.database import Session, engine, Base
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic_models.BookModel import BookCreate

app = FastAPI(
    title = "FastAPI",
    description="Prueba de libros"
)

headers = {"content-type": "charset=utf-8"}

Base.metadata.create_all(bind=engine)

@app.get("/books", tags=["Obtener libros"])
async def get_books():
    db = Session()
    data = db.query(Book).all()
    if data:
        return JSONResponse(content=jsonable_encoder(data))
    return []

@app.get("/books/{id}", tags=["Obtener libros"])
async def get_books_by_id(id:str):
    db = Session()
    try:
        books = db.query(Book).filter(Book.id == id).first()
        if book:
            result = []
            for book in books:
                result.append({
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "year": book.year,
                    "rating": book.rating,
                    "genre": book.genre
                })
                return JSONResponse(content = result, headers=headers)
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    finally:
        db.close()

@app.get("/books/genre/{genre}", tags=["Obtener libros"])
async def get_books_by_genre(genre:str):
    db = Session()
    try:
        result = db.query(Book).filter(Book.genre == genre).all()
        lista = []
        if result:
           for book in result:
               lista.append({
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "year": book.year,
                    "rating": book.rating,
                    "genre": book.genre
               })
               return JSONResponse(content = lista, headers = headers)
           raise HTTPException(status_code = 404, detail="Libro no encontrado")
    finally:
        db.close()

@app.post("/books/crear", tags=["Crear libro"])
async def create_books(b: BookCreate):
    db = Session()
    try:
        if b.id is not None:
            existing = db.query(Book).filter(Book.id == b.id).first()
            if existing:
                raise HTTPException(status_code = 404, detail="Ya existe un libro con ese id")
        new_book = Book(**b.dict())
        db.add(new_book)
        db.commit()
        db.refresh(new_book)

        return JSONResponse(
            content= {"message": "Libro creado", "book":{
                    "id": new_book.id,
                    "title": new_book.title,
                    "author": new_book.author,
                    "year": new_book.year,
                    "rating": new_book.rating,
                    "genre": new_book.genre
            }},
            headers = headers
        )
    finally:
        db.close()

@app.put("/books/actualizar/", tags=["Actualizar "])
async def update_books(id:str, book:BookCreate):
    db = Session()
    try:
        data = db.query(Book).filter(Book.id == id).first()
        if not data:
            raise HTTPException(code_status = 404, detail="Libro no encontrado")
        data.id = book.id
        data.title = book.title
        data.author = book.author
        data.year = book.year
        data.rating = book.rating
        data.genre = book.genre
        db.commit()

        return JSONResponse(content={'message': 'Se ha modificado la pelicula'})
    
    finally:
        db.close()
    

@app.delete("/books/delete/", tags=["Borrar"])
async def delete_book(id:str):
    db = Session()
    try:
        db_book = db.query(Book).filter(Book.id == id).first()
        if not db_book:
            raise HTTPException(status_code = 404, detail="Libro no encontrado")
        db.delete(db_book)
        db.commit()

        return JSONResponse(
            content= {"message": "Libro creado", "book":{
                    "id": db_book.id,
                    "title": db_book.title,
                    "author": db_book.author,
                    "year": db_book.year,
                    "rating": db_book.rating,
                    "genre": db_book.genre
            }},
            headers = headers
        )

    finally:
        db.close()