from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///mydb.db", echo=True)


Base = declarative_base()
metadata = Base.metadata
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_telegram_id = Column(String, unique=True)
    username = Column(String)
    created = Column(DateTime)
    messages = relationship("Messaglar", back_populates="user")


class Messaglar(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    text = Column(String())
    user_id = Column(Integer, ForeignKey("users.id"))
    created = Column(DateTime)
    user = relationship("User", back_populates="messages")



Base.metadata.create_all(engine)