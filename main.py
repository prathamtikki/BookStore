from fastapi import FastAPI
from typing import Annotated
import models as models
from database import engine
from routes import books,rating


app=FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(books.router)
app.include_router(rating.router)
print(90)
