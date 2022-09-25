from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean
from datetime import datetime

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost:5434/med_service")
engine.connect()

metadata = MetaData()

patient = Table('patient', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(200), nullable=False),
    Column('gender', String(200),  nullable=False),
    Column('birthday', DateTime(), nullable=False),
    Column('address', String(200), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
)

metadata.create_all(engine)