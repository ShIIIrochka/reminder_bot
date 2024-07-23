# -*- coding: utf-8 -*-

from threading import Timer
from datetime import datetime
import base64

from constants import bot
from models import Reminder, User
from services.engine_service import session
from services.redis_service import user_connection as r


@bot.message_handler(commands=['newrem'])
def newrem_command(message):
    ''' функция для обработки последующих функций '''

    print('вызов /newrem')
    bot.send_message(message.chat.id, "Введите название напоминания:")
    bot.register_next_step_handler(message, process_name_step)


def process_name_step(message):
    ''' функция для обработки названия напоминания'''

    r.set(
        name=f'name_{message.chat.id}',
        value=message.text
    )

    bot.send_message(message.chat.id, "Введите описание напоминания:")
    bot.register_next_step_handler(message, process_description_step)


def process_description_step(message):
    '''функция для обработки описания напоминания'''

    r.set(
        name=f'description_{message.chat.id}',
        value=message.text
    )

    bot.send_message(
        message.chat.id,
        "Введите дату напоминания в форматe YYYY-MM-DD HH:MM")
    bot.register_next_step_handler(message, process_date_step)


def process_date_step(message):
    '''функция для обработки даты напоминания'''

    date_str = message.text

    try:

        reminder_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M')

        if datetime.now() > reminder_date:
            raise ValueError

        date = base64.b64encode(date_str.encode())

        r.set(
            name=f'date_{message.chat.id}',
            value=date
        )

        # Сохранение напоминания в базу данных
        telegram_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=telegram_id).first()

        if not user:
            user = User(telegram_id=telegram_id)
            session.add(user)
            session.commit()

        redis_date = r.get(f'date_{message.chat.id}')
        rem_date = datetime.strptime(
            base64.b64decode(redis_date).decode(),
            '%Y-%m-%d %H:%M'
            )

        new_reminder = Reminder(
            name=r.get(f'name_{message.chat.id}'),
            description=r.get(f'description_{message.chat.id}'),
            date=rem_date,
            owner=user
        )

        session.add(new_reminder)
        session.commit()
        bot.send_message(
            message.chat.id,
            "напоминание успешно создано!"
        )
        timer(chat_id=message.chat.id, reminder=new_reminder)

    except ValueError:
        bot.send_message(
            message.chat.id,
            "Некорректный формат даты. Пожалуйста, введите дату и время формате 'YYYY-MM-DD HH:MM'"
        )
        bot.register_next_step_handler(message, process_date_step)


def send_reminder(chat_id, reminder: Reminder):
    bot.send_message(
        chat_id,
        f"""
        Напоминание: {reminder.name}\n\
        Описание: {reminder.description}\n\
        Дата: {reminder.date}
        """
    )
    session.delete(reminder)
    session.commit()


def timer(chat_id, reminder: Reminder):
    interval = (reminder.date - datetime.now()).total_seconds()
    t = Timer(
        interval=interval,
        function=send_reminder,
        args=(chat_id, reminder)
    )
    t.start()
