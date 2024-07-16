# -*- coding: utf-8 -*-

from constants import bot
from models import User
from services.engine_service import session
from services.listrem import listrem_command


@bot.message_handler(commands=['start'])
def start_(message):
    telegram_id = message.from_user.id
    result = session.query(User).filter(
        User.telegram_id == telegram_id).count()
    if result > 0:
        bot.send_message(message.from_user.id, "привет! твои напоминания:")
        listrem_command(message)
    else:
        new_user = User(telegram_id=telegram_id)
        session.add(new_user)
        session.commit()
        bot.send_message(message.from_user.id, "привет, новый пользователь!")
