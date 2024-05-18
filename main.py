import asyncio
import logging
from handlers import base, no_handler
import datetime
from aiogram.types import Message

from aiogram.client.default import DefaultBotProperties

import config
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from parsing.parse import day


# async def qwe(message: Message):
#     await message.answer(f'Погода на сегодня:')
#     await message.answer(f'{day()[0]}°C - Минимальная температура')
#     await message.answer(f'{day()[1]}км/ч - Скорость ветра')
#     await message.answer(f'{day()[2]}°C - Максимальная температура')


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",)

    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()


    dp.include_router(base.router)
    dp.include_router(no_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(
        bot)



if __name__ == '__main__':
    asyncio.run(main())
