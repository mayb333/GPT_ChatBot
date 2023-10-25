from aiogram import types
from loguru import logger
from config import CONTACT_ACCOUNT
from src.app.loader import dp, db
from src.utils.markups import no_markup


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer(f"Hello! Contact {CONTACT_ACCOUNT} for access to the bot.\n\n" \
                          "If you already have an access, start a conversation by typing your question.", 
                          reply_markup=no_markup)
    
    logger.info(f"User with id={message.from_id} started the bot!")

    user_info = message.from_user
    user_id, username, first_name = user_info.id, user_info.username, user_info.first_name

    # Add new user to users table
    if db.user_not_in_registered_users(user_id=user_id):
        db.register_user(user_id=user_id, username=username, first_name=first_name)
    