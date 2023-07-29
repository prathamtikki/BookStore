from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,DATE,LargeBinary,Float

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    author = Column(String(20), index=True)
    published_date = Column(String(20))
    isbn_number = Column(Integer, unique=True, index=True)
    price = Column(Float)
    

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_name = Column(String(20), index=True)
    rating = Column(Integer)
    review = Column(String(100))
    
