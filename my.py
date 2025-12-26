import asyncio
import logging
import sys
import re

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        f"Salom, {html.bold(message.from_user.full_name)}!\n"
        "Savolingizni yozing ✍️"
    )

@dp.message()
async def chat_handler(message: Message):
    loading = await message.answer("⌛️ Javob tayyorlanmoqda...")
    try:
        await message.answer(message.text)
    except Exception as e:
        await message.answer("Xatolik yuz berdi 😕")
        print(e)
    finally:
        await loading.delete()

async def main():
    bot = Bot(
        token="8474965061:AAHfwl0NkfAkNVe2w9Zd0ne-sx1ct7f9kiA",
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
