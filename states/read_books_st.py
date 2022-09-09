from telebot.handler_backends import State, StatesGroup


class UserReadState(StatesGroup):
    book_name = State()
    book_author = State()
    book_rate = State()
