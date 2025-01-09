import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
from aiogram import Router
import asyncio
from dotenv import load_dotenv

load_dotenv()  # загрузит переменные из .env

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# Создадим роутер (в Aiogram 3 используется Router)
router = Router()
dp.include_router(router)

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.reply("Привет! Я тестовый бот. Пиши /help, чтобы узнать команды.")

# Запускаем бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

print("DEBUG TOKEN =", TELEGRAM_BOT_TOKEN)
bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode="HTML")
