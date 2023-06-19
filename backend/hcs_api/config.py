from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_port: str
    postgres_db: str

    @property
    def postgres_host(self):
        """Postgres host in docker network is always 'database'"""
        return "database"


settings = Settings()
