import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)

command_help = types.BotCommand(command='help', 
								   		description='список возможностей бота')

command_newrem = types.BotCommand(command='newrem', 
								   		  description='новое напоминание')

command_remlist = types.BotCommand(command='remlist', 
								   		  description='список напоминаний')

command_delrem = types.BotCommand(command='deleterem', 
								   		  description='удалить напоминание')

command_delall = types.BotCommand(command='delall', 
								   		  description='удалить все напоминания')

list_commands = [command_newrem, command_remlist, 
				 command_delrem, command_delall]

# @bot.message_handler(commands=['help', 'start'])
# def help(message):
	# response = 'Привет! Я - бот-менеджер для напоминаний :)!\nВот что я могу:\n'
	# for command in list_commands:
		# response += f'/{command.command} - {command.description}\n'
	# bot.send_message(message.from_user.id, response)
        # 
# @bot.message_handler(commands=['newrem'])
# def new_reminder(message):
# 
	# keyboard = types.InlineKeyboardMarkup()
# 
	# key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»
	# key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
# 
	# keyboard.add(key_yes); #добавляем кнопку в клавиатуру
	# keyboard.add(key_no);
	# bot.send_message(message.from_user.id, text='поставить новое напоминание?', reply_markup=keyboard)
# 
# 
# bot.polling(none_stop=True, interval=0)