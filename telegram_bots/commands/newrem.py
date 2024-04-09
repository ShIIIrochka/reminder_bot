import sqlite3 as sql 
import telebot
from telebot import types
from constants import bot
from services.db import table_reminders

def new_reminder(message):
	'''
	создает кнопки 'да', 'нет'
	'''
	keyboard = types.InlineKeyboardMarkup()

	#кнопка «Да»
	key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
	key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')

	keyboard.add(key_yes) #добавляем кнопку в клавиатуру
	keyboard.add(key_no)
	bot.send_message(message.from_user.id, text='поставить новое напоминание?',
                  	 reply_markup=keyboard)
	
def callback_worker(call):
	'''
	взаимодействие пользователя с кнопками
	'''

	# взаимодействие с кнопкой 'да'
	if call.data == "yes": 
		bot.send_message(call.message.from_user.id, text='на какую дату поставить напоминание? \nвведи в формате дд.мм.гггг')
		report(call.message)
	
	# взаимодействие с кнопкой 'нет'
	elif call.data == "no":
		bot.send_message(call.message.from_user.id, text= 'понял, обращайся :)')

def report(message):
	'''
	получает дату напоминания и записывает в бд
	'''

	# подключение к бд
	connection = sql.connect('my_database.db')
	cursor = connection.cursor()
	table_reminders()

	# Спросить у пользователя дату и время одновременно
	bot.send_message(message.from_user.id, text='на какую дату и время поставить напоминание? \nвведите в формате дд.мм.гггг чч:мм через пробел')

	date_time = message.text

	date = date_time.split()[0]
	time = date_time.split()[1]
	
	# Вставляем дату и время в бд
	cursor.execute('INSERT INTO Reminders(remind_date, remind_time) VALUES (?, ?)', (date, time))
	connection.commit()

	bot.send_message(message.from_user.id, text='отлично! описание напоминания?')

	connection.close()
		
        