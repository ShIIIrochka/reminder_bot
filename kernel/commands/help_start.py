# -*- coding: utf-8 -*-

import telebot

from ..constants import bot

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.from_user.id, "")