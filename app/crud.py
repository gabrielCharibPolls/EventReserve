
from sqlalchemy.orm import Session
from app.models.models import Client, Reservation
from app.schemas.schemas import ClientCreate, ReservationCreate



# ------------------------
# CRUD Clients
# ------------------------

def create_client(db: Session, client: ClientCreate):
    db_client = Client(
        nom=client.nom,
        prenom=client.prenom,
        mail=client.mail,
        adresse=client.adresse,
        numero=client.numero
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client