# -*- coding: utf-8 -*-

from services.start import start_
from services.newrem import newrem_command
from services.listrem import listrem_command
from services.delrem import delrem_command
from constants import bot
from services.engine_service import Base, engine

Base.metadata.create_all(engine)


@bot.message_handler(commands=['start'])
def start(message):
    start_(message)


@bot.message_handler(commands=['newrem'])
def handle_newrem_command(message):
    newrem_command(message)


@bot.message_handler(commands=['listrem'])
def handle_listrem_command(message):
    listrem_command(message)


@bot.message_handler(commands=['delrem'])
def handle_delrem_command(message):
    delrem_command(message)


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
