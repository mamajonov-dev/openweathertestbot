from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
import os
from dotenv import load_dotenv
from openweather import openweatherinfo

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    chat_id = message.chat.id
    fullname = message.from_user.full_name
    text = f'Xush kelibsiz {fullname}\nBotga shahar nomini yozing'
    await bot.send_message(chat_id, text)

@dp.message_handler()
async def sendweatherinfo(message: Message):
    city = message.text
    try:
        text = openweatherinfo(city)
        await message.reply(text)
    except:
        await message.reply('Bunday shaxar topilmadi')

executor.start_polling(dp, skip_updates=True)


