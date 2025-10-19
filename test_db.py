# test_db.py
from app.database.connection import engine, SessionLocal

def test_connection():
    try:
        # teste la connexion avec le moteur
        with engine.connect() as connection:
            result = connection.execute("SELECT * FROM clients LIMIT 1;")
            print("Connexion réussie :", result.fetchone())
    except Exception as e:
        print("Erreur de connexion :", e)

if __name__ == "__main__":
    test_connection()
