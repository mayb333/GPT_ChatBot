from aiogram import Bot, Dispatcher
from config import BOT_TOKEN, DATABASE_URL
from src.database import DataBase


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
db = DataBase()