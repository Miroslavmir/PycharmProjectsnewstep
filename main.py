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


@app.get("/")
def root():
    try:
        cursor.execute("SELECT * FROM project")
        result = cursor.fetchall()
        response = []
        for i in result:
            response.append({"id": i[0], "name": i[1], "lead_name": i[2], "count_user": i[3], "is_finish": i[4]})
        return response
    except Exception as e:
        print(e)
        return e