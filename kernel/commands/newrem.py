# -*- coding: utf-8 -*-

import telebot
from telebot import types
import threading
from datetime import datetime

def newrem_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Введите название напоминания:")
    bot.register_next_step_handler(message, process_name_step)

