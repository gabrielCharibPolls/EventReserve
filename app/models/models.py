"""
Cette classe représente un modèle de données ou une entité spécifique. 
Elle encapsule les attributs et les comportements associés, facilitant la gestion et la manipulation de ces données dans l'application.
"""


from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)
    mail = Column(String(100), unique=True, nullable=False)
    adresse = Column(String(255))
    numero = Column(String(20))

    reservations = relationship("Reservation", back_populates="client")

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    id_client = Column(Integer, ForeignKey("clients.id"))
    nom_reservation = Column(String(100), nullable=False)
    date_debut = Column(Date, nullable=False)
    date_fin = Column(Date, nullable=False)
    prix = Column(Float, nullable=False)

    client = relationship("Client", back_populates="reservations")
