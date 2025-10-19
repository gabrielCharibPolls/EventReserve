from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.core.database import get_db
from app.schemas import schemas



router = APIRouter(prefix="/clients", tags=["clients"])

@router.post("/", response_model=schemas.ClientResponse)
def add_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db, client)

