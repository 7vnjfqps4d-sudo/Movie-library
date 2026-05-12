import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# Ваши данные уже встроены
API_TOKEN = '8702561950:AAHE4kktONgbRzik8ayC7rUUONukkahhU3o'
WEB_APP_URL = 'github.io'

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    web_app = WebAppInfo(url=WEB_APP_URL)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎬 Open Movie Library", web_app=web_app)]
        ],
        resize_keyboard=True
    )
    await message.answer(
        "Welcome! Click the button below to watch free English movies and TV Shows.",
        reply_markup=keyboard
    )

async def main() -> None:
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
