from telebot.handler_backends import State, StatesGroup


class SaveBookState(StatesGroup):
    book_name = State()
    is_commentary = State()
    add_commentary = State()