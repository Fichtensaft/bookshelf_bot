from telebot.types import Message
from states.save_book_states import SaveBookState

from loader import bot
import sqlite3


path_db = 'C:\\Me\\Coding_Python\\Projects\\Bookshelf_Bot\\database\\bookshelf.db'
conn = sqlite3.connect(path_db, check_same_thread=False)
c = conn.cursor()


@bot.message_handler(content_types=['text'])
def write_book_catcher(message: Message) -> None:
    """Func for catching commands via text messages:
    1) to start 'Read a book 📖 ---scenario' and saving a read book in database
    2) to send to user all of his read books == 'Books that I've read 📚 ---scenario'

     """

    if message.text == 'Read a book 📖':
        bot.set_state(user_id=message.from_user.id, state=SaveBookState.book_name, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text='Как называется книга?')

    # Вывод файлов из SQLite базы данных
    elif message.text == "Books that I've read 📚":
        all_data = c.execute("SELECT * FROM read_books")
        all_beauty_books = []
        for i_book in all_data:
            beauty_book = f'{i_book[1]},  автор: {i_book[2]}\n'
            all_beauty_books.append(beauty_book)
        ready_beauty_books = '\n'.join(all_beauty_books)
        bot.send_message(chat_id=message.chat.id, text=ready_beauty_books)
        print(c.fetchall())

    # Очистка списка (из .txt-файла, сейчас бесполезна с SQL)
    # elif message.text == "Clear my list 🪓":
    #     with open(DOC_NAME, 'w', encoding='utf-8') as read_books:
    #         read_books.write('')
    #         bot.send_message(chat_id=message.chat.id, text='Список очищен')

    # elif message.text == "Find by ISBN 🔎":



