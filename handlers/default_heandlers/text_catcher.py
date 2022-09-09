from telebot.types import Message
from states.save_book_states import SaveBookState

from loader import bot

DOC_NAME = 'C:\\Me\\Coding_Python\\Projects\\Bookshelf_Bot\\utils\\read_books.txt'

@bot.message_handler(content_types=['text'])
def write_book_catcher(message: Message) -> None:
    """Func for catching a command to start saving a read book in database (notepad :) )"""

    if message.text == 'Read a book 📖':
        bot.set_state(user_id=message.from_user.id, state=SaveBookState.book_name, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text='Как называется книга?')

    elif message.text == "Books that I've read 📚":
        with open(DOC_NAME, 'r', encoding='utf-8') as read_books:
            bot.send_message(chat_id=message.chat.id, text=read_books.read())





