from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def request_main_menu() -> ReplyKeyboardMarkup:
    """Func for making a main menu in BookShelf_Bot"""

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = KeyboardButton(text='Read a book ๐')
    btn_2 = KeyboardButton(text="Books that I've read ๐")
    # btn_3 = KeyboardButton(text='Clear my list ๐ช')
    # btn_4 = KeyboardButton(text="ะะตัะฝััััั โฉ๏ธ")
    markup.add(btn_1, btn_2)

    return markup
