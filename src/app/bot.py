import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from loguru import logger
from src.app.loader import bot, dp, db
from src.handlers.start import process_start_command
from src.handlers.dialog import process_asking_openai, process_ending_dialog


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
