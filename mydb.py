from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///users.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)
    email = Column(String)
    phone = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()