from pydantic import BaseModel
from datetime import date
from typing import List, Optional


class ReservationBase(BaseModel):
    nom_reservation: str
    date_debut: date
    date_fin: date
    prix: float


class ReservationCreate(ReservationBase):
    id_client: int


class ReservationResponse(ReservationBase):
    id: int

    class Config:
        orm_mode = True


class ClientBase(BaseModel):
    nom: str
    prenom: str
    mail: str
    adresse: Optional[str] = None
    numero: Optional[str] = None


class ClientCreate(ClientBase):
    pass


class ClientResponse(ClientBase):
    id: int
    reservations: List[ReservationResponse] = []

    class Config:
        orm_mode = True
