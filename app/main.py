from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
# from pydantic import randrange
import psycopg2
from psycopg2.extras import RealDictCursor

from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()



try:
    conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',password='charmz007', cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connection was successfull!")
except Exception as error:
    print("Connecting to database failed")
    print("Error: ", error)

@app.get("/")
def root():
    return {"message": "Welcome to our api"}

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}



