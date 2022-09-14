from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def request_contact() -> ReplyKeyboardMarkup:
    """ Keyboard added to a message to give information about a contact to the Bot"""

    keyboard = ReplyKeyboardMarkup(True, True)
    keyboard.add(KeyboardButton('Отправить контакт', request_contact=True))
    return keyboard
