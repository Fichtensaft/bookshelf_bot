from loader import bot
from telebot.types import Message
from states.read_books_st import UserReadState
import os




# @bot.message_handler(content_types=['text'])
# def text_handler(message: Message):
#     if message.text == "📝 Прочёл книгу":
#         bot.set_state(message.from_user.id, UserReadState.book_name, message.chat.id)
#         bot.send_message(message.from_user.id, 'Какую книгу ты прочитал?')


@bot.message_handler(commands=['text'])
def text_handler(message: Message):
    bot.set_state(message.from_user.id, UserReadState.book_name, message.chat.id)
    bot.send_message(message.from_user.id, text='Bubba! Какую книгу ты прочитал?')




@bot.message_handler(state=UserReadState.book_name)
def get_book_name(message: Message) -> None:
    """Получили название книги, спрашиваем автора """
    if message.text:
        bot.send_message(message.from_user.id, text='Записал название. А кто автор?')
        bot.set_state(message.from_user.id, UserReadState.book_author)

        with bot.retrieve_data(message.from_user.id) as data:
            data['Book name'] = message.text


@bot.message_handler(state=UserReadState.book_author)
def get_book_author(message: Message) -> None:
    """Получили автора, спрашиваем рейтинг книги """
    bot.send_message(message.from_user.id, text='Записал автора. Как тебе книга-то? От 0 до 10')
    bot.set_state(message.from_user.id, UserReadState.book_rate)