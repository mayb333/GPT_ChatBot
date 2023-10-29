import os
import src.handlers.start
import src.handlers.admin
import src.handlers.dialog
from aiogram import Bot, Dispatcher, executor, types
from config import OWNER_ID
from loguru import logger
from src.app.loader import bot, dp, db


class GptBotLaunching:
    def start(self):
        executor.start_polling(dispatcher=dp, 
                               on_startup=self._on_startup,
                               on_shutdown=self._on_shutdown, 
                               skip_updates=True)

    async def _on_startup(self, dp):
        logger.info("Bot started.")

        # Write to DB
        db.add_user_to_admins_table(user_id=OWNER_ID)

        logger.info("Initialized Main Admin")

    async def _on_shutdown(self, dp):
        logger.info("Bot stopped.")
