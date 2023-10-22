import os
from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv
from loguru import logger


# Load environment variables
load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


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
