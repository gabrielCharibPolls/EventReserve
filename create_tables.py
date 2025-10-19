from app.core.database import Base, engine
from app.models.models import Client, Reservation

# Crée toutes les tables définies dans tes modèles
Base.metadata.create_all(bind=engine)

print("Tables créées avec succès !")
