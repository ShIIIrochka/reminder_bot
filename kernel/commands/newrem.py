# -*- coding: utf-8 -*-

import telebot
from telebot import types
import threading
from datetime import datetime

from constants import bot
from models import Reminder, User
from models.users import session

class NewReminder():
    ''' класс для записи нового напоминания '''

    def __init__(self, message):
        self.user_data:dict = {}
        self.chat_id:int = message.chat.id

    @bot.message_handler(commands=['newrem'])
    def newrem_command(self, message):
        ''' функция для обработки последующих функций '''

        bot.send_message(self.chat_id, "Введите название напоминания:")
        bot.register_next_step_handler(message, self.process_name_step)

    def process_name_step(self, message):
        ''' функция для обработки названия напоминания'''

        self.user_data['name'] = message.text

        bot.send_message(self.chat_id, "Введите описание напоминания:")
        bot.register_next_step_handler(message, self.process_description_step)

    def process_description_step(self, message):
        '''функция для обработки описания напоминания'''

        self.user_data['description'] = message.text

        bot.send_message(self.chat_id, "Введите дату напоминания в формате YYYY-MM-DD HH:MM")
        bot.register_next_step_handler(message, self.process_date_step)

    def process_date_step(self, message):
        '''функция для обработки даты напоминания'''
        
        date_str = message.text
        try:
            reminder_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
            self.user_data['date'] = reminder_date

            # Сохранение напоминания в базу данных
            telegram_id = message.from_user.id
            user = session.query(User).filter_by(telegram_id=telegram_id).first()
            if not user:
                user = User(telegram_id=telegram_id)
                session.add(user)
                session.commit()
            
            new_reminder = Reminder(
                name=self.user_data['name'],
                description=self.user_data['description'],
                date=reminder_date,
                owner=user
            )
            session.add(new_reminder)
            session.commit()

            bot.send_message(self.chat_id, "Напоминание успешно создано!")

        except ValueError:
            bot.send_message(self.chat_id, "Некорректный формат даты. Пожалуйста, введите дату и время в формате 'YYYY-MM-DD HH:MM':")
            bot.register_next_step_handler(message, self.process_date_step)
