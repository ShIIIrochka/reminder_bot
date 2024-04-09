import sqlite3

def table_users():

  connection = sqlite3.connect('my_database.db')
  cursor = connection.cursor()

  # Создаем таблицу Users
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS Users (
  id INTEGER PRIMARY KEY,
  telegram_id INTEGER NOT NULL,
  timezone TEXT NOT NULL
  )
  ''')

  connection.commit()
  connection.close()

def table_reminders():
  connection = sqlite3.connect('my_database.db')
  cursor = connection.cursor()

  cursor.execute('''
  CREATE TABLE IF NOT EXISTS Reminders(
  id INTEGER PRIMARY KEY,
  description TEXT,
  remind_date DATETIME NOT NULL,
  remind_time TIMESTAMPL NOT NULL,
  user_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES Users(id)
  )
  ''')

  connection.commit()
  connection.close()


