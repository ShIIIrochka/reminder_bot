import telebot
from telebot import types
from constants import bot

@bot.message_handler(commands=['newrem'])
def new_reminder(message):

	keyboard = types.InlineKeyboardMarkup()

	key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»
	key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')

	keyboard.add(key_yes); #добавляем кнопку в клавиатуру
	keyboard.add(key_no);
	bot.send_message(message.from_user.id, text='поставить новое напоминание?', reply_markup=keyboard)
	
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": 
        bot.send_message(call.message.chat.id, text='на какую дату поставить напоминание? \nвведи в формате дд.мм.гггг');
    elif call.data == "no":
        bot.send_message(call.message.chat.id, text= 'понял, обращайся :)')