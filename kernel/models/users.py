# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from services.engine_service import Base

# from services.engine_service import engine


# Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    telegram_id = Column(Integer, unique=True, nullable=False)
    reminders = relationship("Reminder", back_populates="owner")


class Reminder(Base):
    __tablename__ = 'reminders'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(Text(50), default='')
    description = Column(Text, default='')
    owner_id = Column(Integer, ForeignKey('users.telegram_id'), nullable=False)
    date = Column(DateTime, nullable=False)
    owner = relationship("User", back_populates="reminders")


# # Создание таблиц в базе данных
# Base.metadata.create_all(engine)

# # Создание сессии
# Session = sessionmaker(bind=engine)
# session = Session()
