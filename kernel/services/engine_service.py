# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:////home/ksenia/reminder_bot/sqlite3.db')
engine.connect()

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
