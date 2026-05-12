import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiohttp import web

API_TOKEN = '8702561950:AAELkJ_XXDQzlZet5Y2ESW7Zl_cO-YN-QOI'
WEB_APP_URL = 'github.io'

dp = Dispatcher()

# --- Логика Telegram-бота ---
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    web_app = WebAppInfo(url=WEB_APP_URL)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🎬 Open Movie Library", web_app=web_app)]],
        resize_keyboard=True
    )
    await message.answer(
        "Welcome! Click the button below to watch free English movies and TV Shows.",
        reply_markup=keyboard
    )

# --- Веб-сервер для обмана Render ---
async def handle_ping(request):
    return web.Response(text="Bot is alive!")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    # Бот будет слушать порт 10000, который Render проверяет по умолчанию
    site = web.TCPSite(runner, '0.0.0.0', 10000)
    await site.start()

async def main() -> None:
    bot = Bot(token=API_TOKEN)
    # Запускаем веб-сервер параллельно с ботом
    await start_web_server()
    print("Fake Web Server started on port 10000")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
