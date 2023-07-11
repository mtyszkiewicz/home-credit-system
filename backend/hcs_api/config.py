from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_port: str
    postgres_db: str
    postgres_host: str


settings = Settings()
