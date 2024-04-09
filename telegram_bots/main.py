import telebot
from constants import bot

bot_token = telebot.TeleBot(bot)

@bot.message_handler(commands=['help', 'start'])
def handle_help(message):
    from commands.help_start import func_help
    func_help(message)

@bot.message_handler(commands=['newrem'])
def handle_newrem(message):
    from commands.newrem import new_reminder
    new_reminder(message)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    from commands.newrem import callback_worker
    callback_worker(call)


@bot.message_handler(content_types=['text'])
def not_command(message):
    from commands.help_start import send_list_of_commands
    send_list_of_commands(message)
        
if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
