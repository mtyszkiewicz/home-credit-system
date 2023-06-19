from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_host: str = "database:5432"
    postgres_db: str = "home"


settings = Settings()
