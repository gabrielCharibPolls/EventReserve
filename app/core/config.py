# app/core/config.py
class Settings:
    DB_USER: str = "root"
    DB_PASSWORD: str = "root"
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 3306
    DB_NAME: str = "event_reserve"

settings = Settings()
