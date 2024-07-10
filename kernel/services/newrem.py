# -*- coding: utf-8 -*-

from threading import Timer
from datetime import datetime

from constants import bot
from models import Reminder, User
from models.users import session


user_data = {}


@bot.message_handler(commands=['newrem'])
def newrem_command(message):
    ''' функция для обработки последующих функций '''

    bot.send_message(message.chat.id, "Введите название напоминания:")
    bot.register_next_step_handler(message, process_name_step)


def process_name_step(message):
    ''' функция для обработки названия напоминания'''

    user_data['name'] = message.text

    bot.send_message(message.chat.id, "Введите описание напоминания:")
    bot.register_next_step_handler(message, process_description_step)


def process_description_step(message):
    '''функция для обработки описания напоминания'''

    user_data['description'] = message.text

    bot.send_message(
        message.chat.id,
        "Введите дату напоминания в форматe YYYY-MM-DD HH:MM")
    bot.register_next_step_handler(message, process_date_step)


def process_date_step(message):
    '''функция для обработки даты напоминания'''

    date_str = message.text
    try:
        reminder_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
        user_data['date'] = reminder_date

        # Сохранение напоминания в базу данных
        telegram_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=telegram_id).first()
        if not user:
            user = User(telegram_id=telegram_id)
            session.add(user)
            session.commit()
        new_reminder = Reminder(
            name=user_data['name'],
            description=user_data['description'],
            date=reminder_date,
            owner=user
        )
        session.add(new_reminder)
        session.commit()
        bot.send_message(
            message.chat.id,
            "Напоминание успешно создано!"
        )
    except ValueError:
        bot.send_message(
            message.chat.id,
            "Некорректный формат даты.\
            Пожалуйста, введите дату и время форматe\
            'YYYY-MM-DD HH:MM'"
        )


def send_reminder(message, Reminder: Reminder):
        bot.send_message(
            message.chat.id,
            f"Напоминание: {Reminder.name}\n\
            Описание: {Reminder.description}\n\
            Дата: {Reminder.date}"
        )