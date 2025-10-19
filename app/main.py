from typing import Union
from fastapi import Depends, FastAPI
from sqlmodel import Session
from app import crud
from app.api import event_routes
from app.core.database import engine
from app.database.connection import SessionLocal
from app.models import models

import sys, os

from app.schemas import schemas

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        models.Base.metadata.create_all(bind=engine)

@app.get("/clients/")
def read_clients(db: Session = Depends(get_db)):
    return db.query(models.Client).all()

app.include_router(event_routes.router)