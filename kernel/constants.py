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

command_delrem = types.BotCommand(command='delrem', 
								description='удалить напоминание')

command_delall = types.BotCommand(command='delall', 
								description='удалить все напоминания')

list_commands = [command_newrem, command_remlist, 
				command_delrem, command_delall]
