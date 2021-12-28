from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://app:secret@localhost:5432/app'
PUBLIC_SCHEMA_NAME = 'public'

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    connect_args={"sslmode": 'disable'},
    echo=True,
)

Base = declarative_base()
