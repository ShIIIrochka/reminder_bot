import telebot
from constants import bot

from commands.newrem import  newrem_command
from commands.newrem import callback_worker
from commands.newrem import report

from commands.help_start import func_help
from commands.help_start import send_list_of_commands

bot_token = telebot.TeleBot(bot)

@bot.message_handler(commands=['help', 'start'])
def handle_help(message):
    func_help(message)

@bot.message_handler(content_types=['text'])
def not_command(message):
    send_list_of_commands(message)

def handle_newrem(message):
    newrem_command(message)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    callback_worker(call)

@bot.message_handler(content_types=['text'])
def date(message):
    report(message)
        
if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
