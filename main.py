from fastapi import FastAPI
import psycopg2
from dotenv import dotenv_values
from pydantic import BaseModel

config = dotenv_values(".env")
connect = psycopg2.connect(
    host=config["HOST"],
    port=config["PORT"],
    user=config["USERID"],
    password=config["USERPW"],
    database=config["DBNAME"]

)

cursor = connect.cursor()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
