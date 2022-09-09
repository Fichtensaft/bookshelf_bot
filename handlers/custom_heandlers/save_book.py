import pathlib

from loader import bot
from states.save_book_states import SaveBookState
from telebot.types import Message


@bot.message_handler(commands=['bubba'])
def test_bubba(message: Message) -> None:
    bot.send_message(chat_id=message.chat.id, text='Bubba works!')


"""A .txt doc for saving (before learning SQL)"""
SAVE_DOC_NAME = 'C:\\Me\\Coding_Python\\Projects\\Bookshelf_Bot\\utils\\read_books.txt'


@bot.message_handler(state=SaveBookState.book_name)
def book_name_next(message: Message) -> None:
    """Saving book name in database (file) and asking - should we proceed with extra information to save"""

    # user_dict = {message.from_user.id: []}

    with open(SAVE_DOC_NAME, 'a+', encoding='utf-8') as book_data:
        # if user_dict in book_data:
        #     user_dict[message.from_user.id].append(message.text)
        # else:
        #     user_dict[message.from_user.id] = [message.text]

        book_data.write(f"{message.text}\n")

    bot.set_state(user_id=message.from_user.id, state=SaveBookState.is_commentary, chat_id=message.chat.id)
    bot.send_message(chat_id=message.chat.id, text='Saved! Add any commentaries? (Да/Нет)')


@bot.message_handler(state=SaveBookState.is_commentary)
def book_commentary(message: Message) -> None:
    """Some test commentary"""
    bot.send_message(chat_id=message.chat.id, text='SaveBookState.is_commentary - is active')
    if message.text.lower() == 'да':
        bot.set_state(user_id=message.from_user.id, state=SaveBookState.add_commentary, chat_id=message.chat.id)

    elif message.text.lower() == 'нет':
        bot.delete_state(user_id=message.from_user.id, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text='На нет и суда нет!')

    #bot.send_message(chat_id=message.chat.id, text='HOMO')
    #
    # with open(SAVE_DOC_NAME, 'a+', encoding='utf-8') as book_data:


@bot.message_handler(state=SaveBookState.add_commentary)
def add_commentary(message: Message) -> None:
    """Adding commentaries"""

    bot.send_message(chat_id=message.chat.id, text='HOMO')




