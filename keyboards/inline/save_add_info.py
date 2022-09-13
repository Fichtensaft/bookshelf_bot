from telebot import types


def req_yes_no() -> types.InlineKeyboardMarkup:
    """Func for making an addition for a message with a choice of 'Yes or No' """

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)

    return keyboard

