# -*- coding: utf-8 -*-

from sqlalchemy import create_engine

engine = create_engine('sqlite:////home/ksenia/reminder_bot/sqlite3.db')
engine.connect()
