from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel

from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth



models.Base.metadata.create_all(bind=engine)

app = FastAPI()


try:
    conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',password='charmz007', cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connection was successfull!")
except Exception as error:
    print("Connecting to database failed")
    print("Error: ", error)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Welcome to our api"}










