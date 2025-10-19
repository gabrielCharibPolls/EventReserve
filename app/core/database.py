from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Remplace USER, PASSWORD, HOST, PORT, DB_NAME par tes infos
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@127.0.0.1:3306/event_reserve"

# moteur SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)

# Session locale
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base pour les modèles
Base = declarative_base()


