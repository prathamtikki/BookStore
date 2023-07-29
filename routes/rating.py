from fastapi import Depends,APIRouter,HTTPException
from typing import Annotated
from models import Rating
from database import SessionLocal
from pydantic import BaseModel,Field
from starlette import status

router=APIRouter(prefix='/rating',tags=['rating'])

# creating a dependency to get the database connection
def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()

db_dependancy=Annotated[SessionLocal,Depends(get_db)]

# creating a pydantic model for the request body
class Ratings(BaseModel):
    book_id: int
    user_name : str
    rating : int=Field(...,gt=0,lt=6)
    review : str

# Creating the api endpoints

# add a book
@router.post('/addrating',status_code=status.HTTP_201_CREATED)
async def add_rating(db:db_dependancy,add_rating:Ratings):
    existing_rating = (
        db.query(Rating)
        .filter(Rating.book_id == add_rating.book_id, Rating.user_name == add_rating.user_name)
        .first()
    )
    if existing_rating:
        raise HTTPException(status_code=400, detail="User already rated this book")
    if add_rating.rating > 5:
        
        return {'Rating should be between 1 to 5'}
    db.add(Rating(**add_rating.dict()))
    db.commit()
    return {'Rating has been added successfully'}

# get all rating
@router.get('/getratings',status_code=status.HTTP_200_OK)
async def get_ratings(db:db_dependancy):
    rating= db.query(Rating).all()
    if rating is None:
        return {'No ratings found'}
    return rating

# get a rating by book id
@router.get('/getrating/{book_id}',status_code=status.HTTP_200_OK)
async def get_rating(db:db_dependancy,book_id:int):
    rating= db.query(Rating).filter(Rating.book_id==book_id).all()
    if rating is not None:
        return rating
    else:
        raise HTTPException(status_code=404,detail='Not found')