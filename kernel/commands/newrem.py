# -*- coding: utf-8 -*-

import telebot
from telebot import types
import threading
from datetime import datetime


class NewReminder():
    ''' класс для записи нового напоминания '''

    def __init__(self, message):
        self.user_data:dict = {}
        self.chat_id:int = message.chat.id

    def newrem_command(self, message):
        ''' функция для обработки последующих функция'''
        bot.send_message(self.chat_id, "Введите название напоминания:")
        bot.register_next_step_handler(message, process_name_step)

    def process_name_step(self, message):
        ''' функция для обработки названия напоминания'''

        name:str = message.text
        self.user_data[name] = name
        bot.send_message(self.chat_id, "Введите описание напоминания:")
        bot.register_next_step_handler(message, process_description_step)