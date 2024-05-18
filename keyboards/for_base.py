
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

weather = [[InlineKeyboardButton(text='Погода сегодня', callback_data='weather')]]



menu = InlineKeyboardMarkup(inline_keyboard=weather)


exit_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Выйти в меню')]], resize_keyboard=True)
iexit_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Выйти в меню', callback_data='menu')]])