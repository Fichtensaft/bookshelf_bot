import sqlite3

from loader import bot
from states.save_book_states import SaveBookState
from telebot.types import Message
from keyboards.inline.save_add_info import req_yes_no


path_db = 'C:\\Me\\Coding_Python\\Projects\\Bookshelf_Bot\\database\\bookshelf.db'
conn = sqlite3.connect(path_db, check_same_thread=False)
c = conn.cursor()


@bot.message_handler(state=SaveBookState.book_name)
def book_name_next(message: Message) -> None:
    """Saving book name in database (SQLite) and asking - should we proceed with extra information to save"""

    last_id = c.execute("""SELECT * FROM read_books ORDER BY rowid DESC""")
    if not c.fetchall():
        book_title_insertion = "INSERT INTO read_books (title) VALUES (?)"
        title_name = (message.text, )
        c.execute(book_title_insertion, title_name)
        conn.commit()
    else:
        book_title_insertion = "INSERT INTO read_books (title) VALUES (?)"
        title_name = (message.text, )
        c.execute(book_title_insertion, title_name)
        conn.commit()

    author_question = 'Название получил. Кто же автор? '
    bot.send_message(chat_id=message.chat.id, text=author_question)
    bot.set_state(user_id=message.from_user.id, state=SaveBookState.book_author, chat_id=message.chat.id)


@bot.message_handler(state=SaveBookState.book_author)
def get_book_author(message: Message) -> None:
    """Getting and adding the author of the book into our database"""

    last_db_entry = c.execute("""SELECT * FROM read_books ORDER BY id DESC LIMIT 1""")
    last_title = last_db_entry.fetchall()[0][1]

    book_author_insertion = """UPDATE read_books SET author = ?
    WHERE title = ? AND author is 'кто-то'"""
    author_name = (message.text, last_title)
    c.execute(book_author_insertion, author_name)
    conn.commit()

    bot.delete_state(user_id=message.from_user.id, chat_id=message.chat.id)

    question = 'Saved! Add any commentaries?'
    bot.send_message(chat_id=message.chat.id, text=question, reply_markup=req_yes_no())


@bot.callback_query_handler(func=lambda call: True)
def call_worker(call):
    if call.data == 'yes':
        bot.send_message(chat_id=call.from_user.id, text='Bubba works!')
        bot.set_state(state=SaveBookState.add_commentary, user_id=call.from_user.id)
    elif call.data == 'no':
        bot.send_message(chat_id=call.from_user.id, text='На нет и суда нет! ')
        bot.delete_state(user_id=call.from_user.id)


@bot.message_handler(state=SaveBookState.add_commentary)
def add_commentary(message: Message) -> None:
    """Adding commentaries"""

    bot.send_message(chat_id=message.chat.id, text='HOMO')
    bot.delete_state(user_id=message.from_user.id, chat_id=message.chat.id)
