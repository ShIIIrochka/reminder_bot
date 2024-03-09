import telebot
from constants import list_commands
from constants import bot

@bot.message_handler(commands=['help', 'start'])
def func_help(message):
	response = 'Привет! Я - бот-менеджер для напоминаний :)!\nВот что я могу:\n'
	for command in list_commands:
		response += f'/{command.command} - {command.description}\n'
	bot.send_message(message.from_user.id, response)