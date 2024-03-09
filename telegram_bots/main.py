import telebot
from constants import bot
import sys

sys.path.append('./commands')

from help_start import func_help
from newrem import new_reminder

bot_token = telebot.TeleBot(bot)

@bot.message_handler(commands=['help', 'start'])
def handle_help(message):
    func_help(bot, message)

@bot.message_handler(commands=['newrem'])
def handle_newrem(message):
    new_reminder(bot, message)


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
