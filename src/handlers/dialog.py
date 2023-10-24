from aiogram import types
from loguru import logger
from config import CONTACT_ACCOUNT, ALLOWED_USERS
from src.app.loader import dp, db
from src.utils import ask_openai
from src.utils.markups import end_dialog_markup, no_markup


USERS_HISTORY = {}


@dp.message_handler(lambda message: message.text != '❌ End Conversation' and message.from_user.id in ALLOWED_USERS)
async def process_asking_openai(message: types.Message):
    user_id = message.from_user.id

    if not USERS_HISTORY.get(user_id):
        USERS_HISTORY[user_id] = []

    # Build prompt
    USERS_HISTORY[user_id].append({"role": "user", "content": message.text})

    # !!! Need to dicrease history if it takes too much tokens

    prompt = USERS_HISTORY[user_id]

    # Get openai answer
    model_answer = await ask_openai(prompt)

    USERS_HISTORY[user_id].append({"role": "assistant", "content": model_answer})

    await message.answer(model_answer, reply_markup=end_dialog_markup)

    # Add message to database (messages table)
    db.add_data_to_messages_table(user_id=user_id, message=message.text)


@dp.message_handler(lambda message: message.text == '❌ End Conversation' and message.from_user.id in ALLOWED_USERS)
async def process_ending_dialog(message: types.Message):
    await message.reply("The conversation is ended.\n"
                        "To start a new one, type your question.", reply_markup=no_markup)
