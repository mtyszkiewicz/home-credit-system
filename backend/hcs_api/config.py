from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_host: str = "localhost:5432"
    postgres_db: str = "home"


settings = Settings()
