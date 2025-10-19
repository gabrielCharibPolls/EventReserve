from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.core.database import get_db
from app.schemas import schemas



routerClients = APIRouter(prefix="/clients", tags=["clients"])

@routerClients.post("/", response_model=schemas.ClientResponse)
def add_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db, client)


@routerClients.get("/{client_id}", response_model=schemas.ClientResponse)
def read_client(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.get_client(db, client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client


@routerClients.get("/", response_model=list[schemas.ClientResponse])
def read_clients(db: Session = Depends(get_db)):
    return crud.get_clients(db)


@routerClients.put("/{client_id}", response_model=schemas.ClientResponse)
def update_client(client_id: int, client: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_client = crud.update_client(db, client_id, client)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

routerReservations = APIRouter(prefix="/reservations", tags=["reservations"])

@routerReservations.post("/", response_model=schemas.ReservationResponse)
def add_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(get_db)):
    return crud.create_reservation(db, reservation) 

@routerReservations.get("/{reservation_id}", response_model=schemas.ReservationResponse)
def read_reservation(reservation_id: int, db: Session = Depends(get_db)):
    db_reservation = crud.get_reservation(db, reservation_id)
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return db_reservation


