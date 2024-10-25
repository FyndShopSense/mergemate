from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_connection(db_url):
    engine = create_engine(db_url)
    base.metadata.bind = engine
    dbsession = sessionmaker(bind=engine)
    return dbsession()
