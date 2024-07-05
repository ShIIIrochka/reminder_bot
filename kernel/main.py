# -*- coding: utf-8 -*-

import telebot

from commands.start import start_
from commands import NewReminder
from constants import bot 

@bot.message_handler(commands=['start'])
def start(message):
    start_(message)

@bot.message_handler(commands=['newrem'])
def handle_newrem_command(message):
    new_reminder = NewReminder()
    new_reminder.newrem_command(message)

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
