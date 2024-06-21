# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    telegram_id = Column(Integer, unique=True, nullable=False)

    reminders = relationship("Reminders")
class Reminders(Base):
    __tablename__ =  'reminders'

    id = Column(Integer, primary_key=True, nullable=False)
    description = Column(String)
    owner_id = Column(Integer, nullable=False, ForeignKey('User.id'))
    date = Column(DateTime, nullable=False)

