import time

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboards import for_base
from parsing.parse import day
import datetime


router = Router()




@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(f"Приветствую тебя {message.from_user.username} \n"
                         f"Я погодный бот",
                         reply_markup=for_base.menu)

@router.callback_query(F.data == 'weather')
@router.message(Command('weather'))
async def cmd_weather(clb: CallbackQuery):
    await clb.message.answer(datetime.date.today().strftime("%d.%m"))
    await clb.message.answer(f'{day()[0]}°C - Минимальная температура')
    await clb.message.answer(f'{day()[1]}км/ч - Скорость ветра')
    await clb.message.answer(f'{day()[2]}°C - Максимальная температура')



