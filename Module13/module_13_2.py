from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["start"])
async def start_message(message):
    text = "Привет! Я бот помогающий твоему здоровью."
    print(text)


@dp.message_handler()
async def all_message(message):
    text = "Ведите команду /start чтобы начать общение"
    print(text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
