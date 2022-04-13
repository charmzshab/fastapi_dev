from turtle import title
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel

from sqlalchemy.orm import Session
from . import models, schemas
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




