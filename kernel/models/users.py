from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    telegram_id = Column(Integer, nullable=False, unique=True)

class Reminder(Base):
    __tablename__ = 'reminders'

    id = Column(Integer, primary_key=True, nullable=False)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(DateTime, nullable=False)

# Установка отношений между моделями
Reminder.owner = relationship("User", back_populates="reminders")
User.reminders = relationship("Reminder", order_by=Reminder.id, back_populates="owner")
