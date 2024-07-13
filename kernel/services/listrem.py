# -*- coding: utf-8 -*-

from constants import bot
from models import Reminder, User
from models.users import session


@bot.message_handler(commands=['listrem'])
def listrem(message):
    '''функция получения всех напоминаний пользователя'''

    pass