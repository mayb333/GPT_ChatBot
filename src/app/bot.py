import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from loguru import logger
from src.database import DataBase


# Load environment variables
load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
db = DataBase()


class GptBotLaunching:
    def start(self):
        executor.start_polling(dispatcher=dp, 
                               on_startup=self._on_startup,
                               on_shutdown=self._on_shutdown, 
                               skip_updates=True)

    async def _on_startup(self, dp):
        logger.info("Bot started.")

    async def _on_shutdown(self, dp):
        logger.info("Bot stopped.")


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello! Ask me something")
    
    logger.info(f"User with id={message.from_id} started the bot!")

    user_info = message.from_user
    user_id, username, first_name = user_info.id, user_info.username, user_info.first_name

    # Add new user to users table
    if db.user_not_in_users(user_id=user_id):
        db.add_user(user_id=user_id, username=username, first_name=first_name)
    