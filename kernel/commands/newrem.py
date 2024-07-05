# -*- coding: utf-8 -*-

import telebot
from telebot import types
import threading
from datetime import datetime

from constants import bot
from models import Reminder
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