from telebot.types import Message
from loader import bot
from keyboards.inline.main_menu import request_main_menu
import sqlite3


path_db = 'C:\\Me\\Coding_Python\\Projects\\Bookshelf_Bot\\database\\bookshelf.db'
conn = sqlite3.connect(path_db, check_same_thread=False)
cur = conn.cursor()


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    """Function for starting a bot and adding a username to database"""

    try:
        user_name = (message.from_user.username, )
        db_insertion = "INSERT INTO all_users (user_name) VALUES (?)"
        cur.execute(db_insertion, user_name)
        conn.commit()
        conn.close()

        bot.send_message(message.from_user.id, f"Привет, {message.from_user.full_name}! Записал твой ник в базу"
                              f"\nЧитаем книги, шикарно. Что хочешь? - Жми на кнопку!", reply_markup=request_main_menu())

    except sqlite3.Error:
        print(f'User - {message.from_user.username} is already in the base')
        bot.send_message(message.from_user.id, f"Здравствуй снова, {message.from_user.full_name}!"
                                               f"\nТы уже в нашей базе, жми на кнопку!")





