from telebot.types import Message
from loader import bot
from keyboards.inline.main_menu import request_main_menu


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.send_message(message.from_user.id, f"Привет, {message.from_user.full_name}!"
                          f"\nЧитаем книги, шикарно. Что хочешь? - Жми на кнопку!", reply_markup=request_main_menu())


# @bot.message_handler() "📝 прочёл книгу"
