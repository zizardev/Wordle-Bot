from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Слово дня')],
                                     [KeyboardButton(text='Статистика'),
                                      KeyboardButton(text='Магазин')]])
