# -*- coding: utf-8 -*-

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int]

class Reminders(Base):
    __tablename__ =  'reminders'

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(String(150))
    owner_id: Mapped[int] 