from fastapi import Depends,APIRouter
from typing import Annotated
from sqlalchemy.orm import Session
from models import Book
from database import engine, SessionLocal
from pydantic import BaseModel

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

@router.post('/addbook')
async def add_book(db:db_dependancy,addbook:AddBook):
    db.add(Book(**addbook.dict()))
    db.commit()
    return {'success'}

@router.get('/getbooks')
async def get_books(db:db_dependancy):
    return db.query(Book).all()