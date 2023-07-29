#importing the required modules
from fastapi import FastAPI
import models as models
from database import engine
from routes import books,rating

# creating the fastapi instance
app=FastAPI()

# creating the database tables
models.Base.metadata.create_all(bind=engine)

# including the routers
app.include_router(books.router)
app.include_router(rating.router)

