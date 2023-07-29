from fastapi import Depends,APIRouter,HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from models import Book
from database import engine, SessionLocal
from pydantic import BaseModel
from starlette import status

router=APIRouter()

def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()

db_dependancy=Annotated[SessionLocal,Depends(get_db)]

class AddBook(BaseModel):
    title: str
    author : str
    published_date : str
    isbn_number : int
    price: float

@router.post('/addbook',status_code=status.HTTP_201_CREATED)
async def add_book(db:db_dependancy,addbook:AddBook):
    db.add(Book(**addbook.dict()))
    db.commit()
    return {'Book has been added successfully'}

@router.get('/getbooks',status_code=status.HTTP_200_OK)
async def get_books(db:db_dependancy):
    book= db.query(Book).all()
    if book is None:
        return {'No books found'}
    return book

@router.get('/getbook/{book_id}',status_code=status.HTTP_200_OK)
async def get_book(db:db_dependancy,book_id:int):
    book= db.query(Book).filter(Book.id==book_id).first()
    if book is not None:
        return book
    else:
        raise HTTPException(status_code=404,detail='Not found')
    

@router.put("/books/{book_id}")
def update_book(db:db_dependancy,book_id: int, updated_book: AddBook):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = updated_book.title
    book.author = updated_book.author
    book.published_date = updated_book.published_date
    book.isbn_number = updated_book.isbn_number
    book.price = updated_book.price
    db.commit()
    return {"message": "Book has been updated successfully"}

@router.delete("/books/{book_id}")
def delete_book(db:db_dependancy,book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    db.close()
    return {"message": "Book deleted successfully"}