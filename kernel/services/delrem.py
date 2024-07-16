# -*- coding: utf-8 -*-

from telebot import types
from sqlalchemy import select

from constants import bot
from models.users import Reminder
from services.engine_service import session

@bot.message_handler(commands=['listrem'])
def delrem_command(message):
    markup = types.InlineKeyboardMarkup()
    telegram_id = message.from_user.id
    reminders = select(Reminder).where(Reminder.owner_id == telegram_id)
    results = session.scalars(reminders).all()

    for result in results:

        key = types.InlineKeyboardButton(
            text=f"{result.name}",
            callback_data='delete'
            )

        markup.add(key)

    bot.send_message(
        message.chat.id,
        "выбери напоминание для удаления",
        reply_markup=markup
        )
