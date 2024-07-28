# -*- coding: utf-8 -*-

from threading import Timer
from datetime import datetime
import base64

from telebot.types import Message

from constants import bot
from models import Reminder, User
from services.engine_service import session
from services.redis_service import user_connection as r


@bot.message_handler(commands=['newrem'])
def newrem_command(message: Message) -> None:
    """Функция для обработки команды /newrem"""

    bot.send_message(message.chat.id, "Введите название напоминания:")
    bot.register_next_step_handler(message, process_name_step)


def process_name_step(message: Message) -> None:
    """Функция для обработки названия напоминания."""

    r.set(name=f'name_{message.chat.id}', value=message.text)

    bot.send_message(message.chat.id, "Введите описание напоминания:")
    bot.register_next_step_handler(message, process_description_step)


def process_description_step(message: Message) -> None:
    """Функция для обработки описания напоминания"""

    r.set(name=f'description_{message.chat.id}', value=message.text)

    bot.send_message(
        message.chat.id,
        "Введите дату напоминания в формате YYYY-MM-DD HH:MM"
    )
    bot.register_next_step_handler(message, process_date_step)


def process_date_step(message: Message) -> None:
    """Функция для обработки даты напоминания."""
    date_str: str = message.text

    try:
        reminder_date: datetime = datetime.strptime(date_str, '%Y-%m-%d %H:%M')

        if datetime.now() > reminder_date:
            raise ValueError

        date: bytes = base64.b64encode(date_str.encode())
        r.set(name=f'date_{message.chat.id}', value=date)

        # Сохранение напоминания в базу данных
        telegram_id: int = message.from_user.id
        user: User = (
            session.query(User).filter_by(telegram_id=telegram_id).first()
            )

        if not user:
            user = User(telegram_id=telegram_id)
            session.add(user)
            session.commit()

        redis_date: bytes = r.get(f'date_{message.chat.id}')
        rem_date: datetime = datetime.strptime(
            base64.b64decode(redis_date).decode(), '%Y-%m-%d %H:%M'
        )

        new_reminder: Reminder = Reminder(
            name=r.get(f'name_{message.chat.id}'),
            description=r.get(f'description_{message.chat.id}'),
            date=rem_date,
            owner=user
        )

        r.delete(
            f'name_{message.chat.id}',
            f'description_{message.chat.id}',
            f'date_{message.chat.id}'
        )

        session.add(new_reminder)
        session.commit()
        bot.send_message(message.chat.id, "Напоминание успешно создано!")
        timer(chat_id=message.chat.id, reminder=new_reminder)

    except ValueError:
        bot.send_message(
            message.chat.id,
            """
            Некорректный формат даты.\
 Пожалуйста, введите дату и время в формате 'YYYY-MM-DD HH:MM'
            """
        )
        r.delete(
            f'date_{message.chat.id}'
        )
        bot.register_next_step_handler(message, process_date_step)


def send_reminder(chat_id: int, reminder: Reminder) -> None:
    bot.send_message(
        chat_id,
        f"""
        *Напоминание*: {reminder.name}\n
*Описание*: {reminder.description}\n
*Дата*: {reminder.date}
        """
    )
    session.delete(reminder)
    session.commit()


def timer(chat_id: int, reminder: Reminder) -> None:
    interval: float = (reminder.date - datetime.now()).total_seconds()
    t: Timer = Timer(
        interval=interval,
        function=send_reminder,
        args=(chat_id, reminder)
        )
    t.start()
