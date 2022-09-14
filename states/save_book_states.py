from telebot.handler_backends import State, StatesGroup


class SaveBookState(StatesGroup):
    book_name = State()
    book_author = State()
    is_commentary = State()
    add_commentary = State()