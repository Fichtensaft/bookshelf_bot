from telebot.types import Message
from loader import bot
from keyboards.inline.main_menu import request_main_menu


@bot.message_handler(commands=['menu'])
def bot_start(message: Message):
    bot.send_message(message.from_user.id, text='Главное меню', reply_markup=request_main_menu())
