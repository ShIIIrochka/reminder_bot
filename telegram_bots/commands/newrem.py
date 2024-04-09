import sqlite3 as sql
import telebot
from telebot import types
from constants import bot
from services.db import table_reminders

# Добавляем словарь для отслеживания состояния пользователя
user_states = {}

def new_reminder(message):
    '''
    Создает кнопки 'да', 'нет'
    '''
    keyboard = types.InlineKeyboardMarkup()

    # кнопка «Да»
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')

    keyboard.add(key_yes) # добавляем кнопку в клавиатуру
    keyboard.add(key_no)
    bot.send_message(message.from_user.id, 
                     text='Поставить новое напоминание?',
                     reply_markup=keyboard)

def callback_worker(call):
    '''
    Взаимодействие пользователя с кнопками
    '''
    
    # Проверяем, является ли пользователь ботом
    if call.from_user.is_bot:
        return 

    # взаимодействие с кнопкой 'да'
    if call.data == "yes":
        user_states[call.from_user.id] = True # Устанавливаем состояние пользователя в True
        ask_for_date_and_time(call.from_user.id) # Запрашиваем дату и время у пользователя

    # взаимодействие с кнопкой 'нет'
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 
                         text='Понял, обращайся :)')

def ask_for_date_and_time(user_id):
    '''
    Запрашивает у пользователя дату и время напоминания
    '''
    bot.send_message(user_id, 
                     text='На какую дату и время поставить напоминание? \n'
                          'Введите в формате дд.мм.гггг чч:мм через пробел')

def report(message):
    '''
    Получает дату напоминания и записывает в БД
    '''
    #  id пользователя
    user_id = message.from_user.id

    # Проверяем, что пользователь ожидает ввода даты и времени
    if user_id in user_states and user_states[user_id]: 

        # подключение к БД
        connection = sql.connect('my_database.db')
        cursor = connection.cursor()
        table_reminders()

        date_time = message.text

        date = date_time.split()[0]
        time = date_time.split()[1]

        # Вставляем дату и время в БД
        cursor.execute('INSERT INTO Reminders(remind_date, remind_time) VALUES (?, ?)', 
                       (date, time))
        connection.commit()

        bot.send_message(user_id, 
                         text='Отлично! Описание напоминания?')

        connection.close()

        # Сбрасываем состояние пользователя
        user_states[user_id] = False
    else:
        # Если пользователь не ожидал ввода даты и времени
        pass
