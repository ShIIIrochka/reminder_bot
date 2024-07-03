# -*- coding: utf-8 -*-

import telebot

from constants import bot
from kernel.commands.start import start_

@bot.message_handler(commands=['start'])
def start(message):
    start_(message)
        
if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
