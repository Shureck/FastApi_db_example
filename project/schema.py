import time
from datetime import datetime
import os
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine, ForeignKeyConstraint, \
    UniqueConstraint, exc, and_, desc, Boolean
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

#docker_ip = "localhost"
#docker_port = 5434

docker_ip = "db"
docker_port = 5432

class Patient(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    gender = Column(String(100), nullable=False, default=None)
    birthday = Column(DateTime, nullable=False, default=None)
    address = Column(String(100), default=None)

engine = create_engine(f"postgresql+psycopg2://postgres:admin@{docker_ip}:{docker_port}/med_service")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

Patient.__table__.drop(engine)
Base.metadata.create_all(engine)

def add_new_user(name: str, gender: str, address:str = None):
    session = Session()
    scene = Patient(name=name, gender=gender, birthday=datetime.now(), address=address)
    session.add(scene)
    session.commit()


def get_user():
    session = Session(expire_on_commit=False)
    user = session.query(Patient).all()
    if user is None:
        return ''
    print(user)
    return user