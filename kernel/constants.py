# -*- coding: utf-8 -*-

import telebot

import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)