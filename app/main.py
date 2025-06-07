import time
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from app.db.session import engine
from fastapi import FastAPI
from app.api.v1 import api

app = FastAPI()

@app.on_event("startup")
def wait_for_db():
    retries = 10
    while retries > 0:
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("Database is ready!")
            break
        except OperationalError:
            print("Database not ready, waiting...")
            time.sleep(2)
            retries -= 1
    else:
        raise Exception("Database connection failed after retries")

app.include_router(api.router, prefix="/api", tags=["api"])