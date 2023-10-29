from aiogram import Bot, Dispatcher, types
from config import BOT_TOKEN, DATABASE_URL
from src.database import DataBase


bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
db = DataBase()