from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

# POSTGRES_USER = "default"
# POSTGRES_PASSWORD = "zOLWlj2ky3rf"
# POSTGRES_HOST = "ep-twilight-wildflower-510519.eu-central-1.postgres.vercel-storage.com"
# POSTGRES_DB ="verceldb"
POSTGRES_USER = "admin"
POSTGRES_PASSWORD = "5o3B1Lh6kJsH5ZEACndao3eG"
POSTGRES_HOST = "localhost:5432"
POSTGRES_DB ="home"
CONNSTR = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}'

engine = create_engine(CONNSTR)#, connect_args={'sslmode':'require', 'options=project': 'ep-twilight-wildflower-510519'})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()