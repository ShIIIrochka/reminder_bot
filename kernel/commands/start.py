# -*- coding: utf-8 -*-

import telebot

from constants import bot
from ..models import User
from ..models.users import session

@bot.message_handler(commands = ['start'])
def start_(message):

	telegram_id = message.from_user.id
	result = session.query(User).filter(User.telegram_id == telegram_id).count()

	if result > 0:
		pass
	else: 
		new_user = User(telegram_id=telegram_id)
		session.add(new_user)
		session.commit()
		bot.send_message(message.from_user.id, "привет, новый пользователь!")
