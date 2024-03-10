import telebot
from constants import bot
import sys

sys.path.append('./commands')

from help_start import func_help, send_list_of_commands
from newrem import new_reminder

bot_token = telebot.TeleBot(bot)

@bot.message_handler(commands=['help', 'start'])
def handle_help(message):
    func_help(message)

@bot.message_handler(commands=['newrem'])
def handle_newrem(message):
    new_reminder(message)

@bot.message_handler(content_types=['text'])
def not_command(message):
    send_list_of_commands(message)
        
if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
