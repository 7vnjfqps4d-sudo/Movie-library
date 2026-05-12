import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import WebAppInfo

# Данные авторизации и ссылка успешно обновлены
API_TOKEN = '8702561950:AAHE4kktONgbRzik8ayC7rUUONukkahhU3o'
WEB_APP_URL = 'github.io' 

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = WebAppInfo(url=WEB_APP_URL)
    keyboard.add(types.KeyboardButton(text="🎬 Open Movie Library", web_app=web_app))
    
    await message.answer(
        "Welcome! Click the button below to watch free English movies and TV Shows.",
        reply_markup=keyboard
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
