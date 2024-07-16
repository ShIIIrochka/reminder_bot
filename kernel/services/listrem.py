# -*- coding: utf-8 -*-

from sqlalchemy import select

from constants import bot
from models import Reminder
from services.engine_service import session


@bot.message_handler(commands=['listrem'])
def listrem(message):
    '''функция получения всех напоминаний пользователя'''

    telegram_id = message.from_user.id
    reminders = select(Reminder).where(Reminder.owner_id == telegram_id)
    results = session.scalars(reminders).all()

    reminder_messages = []
    for result in results:
        reminder_info = {
            'Name': result.name,
            'Description': result.description,
            'Date': str(result.date),
        }
        reminder_messages.append(
            f"""
            напоминание: {reminder_info['Name']}\n
            описание: {reminder_info['Description']}\n
            дата: {reminder_info['Date']}
            """
        )

    # Если у пользователя нет напоминаний, отправляем соответствующее сообщение
    if not reminder_messages:
        bot.send_message(message.chat.id, "У вас нет напоминаний.")
    else:
        # Собираем все напоминания в одно сообщение
        all_reminders_message = "\n".join(reminder_messages)
        bot.send_message(message.chat.id, all_reminders_message)
