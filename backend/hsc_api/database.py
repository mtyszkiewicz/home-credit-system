from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

USERNAME = "default"
PASSWORD = "zOLWlj2ky3rf"
HOST = "ep-twilight-wildflower-510519.eu-central-1.postgres.vercel-storage.com"
CONNSTR = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}/verceldb'

engine = create_engine(CONNSTR, connect_args={'sslmode':'require', 'options=project': 'ep-twilight-wildflower-510519'})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()