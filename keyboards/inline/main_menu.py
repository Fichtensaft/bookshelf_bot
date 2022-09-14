from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def request_main_menu() -> ReplyKeyboardMarkup:
    """Func for making a main menu in BookShelf_Bot"""

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = KeyboardButton(text='Read a book 📖')
    btn_2 = KeyboardButton(text="Books that I've read 📚")
    # btn_3 = KeyboardButton(text='Clear my list 🪓')
    # btn_4 = KeyboardButton(text="Вернуться ↩️")
    markup.add(btn_1, btn_2)

    return markup
