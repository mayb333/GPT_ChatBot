from aiogram import types
from loguru import logger
from config import CONTACT_ACCOUNT, ALLOWED_USERS, ADMIN_IDS
from src.app.loader import dp, db, bot
from src.utils import ask_openai
from src.utils.messages import reduce_context_window, send_in_parts
from src.utils.markups import end_dialog_markup, no_markup


USERS_HISTORY = {}


@dp.message_handler(lambda message: message.text != '❌ End Conversation' and message.from_user.id in ALLOWED_USERS)
async def process_asking_openai(message: types.Message):
    # Add typing action in bot
    await bot.send_chat_action(message.chat.id, types.ChatActions.TYPING)

    user_id = message.from_user.id

    if not USERS_HISTORY.get(user_id):
        USERS_HISTORY[user_id] = []

    # Add new prompt to context window (history)
    USERS_HISTORY[user_id].append({"role": "user", "content": message.text})

    # Reduce context window if it's greater than 4,000 tokens
    USERS_HISTORY[user_id] = reduce_context_window(USERS_HISTORY[user_id])
    messages_for_model = USERS_HISTORY[user_id]

    # Get openai answer
    model_answer, tokens = await ask_openai(messages_for_model)

    # Add answer from the OpenAI to history for future tracking context of the dialog
    USERS_HISTORY[user_id].append({"role": "assistant", "content": model_answer})

    # Send model answer. If len(model_answer) > 4096, then model answer is sended in parts
    await send_in_parts(message=model_answer, chat_id=message.chat.id, reply_markup=end_dialog_markup)
    logger.info(f"Successfully sent answer from GPT to user id={user_id}")

    # Add message to database (messages table)
    db.add_data_to_messages_table(user_id=user_id, message=message.text, tokens=tokens)


@dp.message_handler(lambda message: message.text == '❌ End Conversation' and message.from_user.id in ALLOWED_USERS)
async def process_ending_dialog(message: types.Message):
    user_id = message.from_user.id
    if user_id in USERS_HISTORY.keys():
        del USERS_HISTORY[user_id]
    
        await message.reply("The conversation is ended.\n"
                            "To start a new one, type your question.", reply_markup=no_markup)
    else:
        await message.answer(f"There was no active conversation.\n\n"\
                              "Start a conversation by typing your question.\n\n", reply_markup=no_markup)


@dp.message_handler(lambda message: message.from_user.id not in ALLOWED_USERS)
async def process_not_allowed_user(message: types.Message):
    await message.answer(f"You don't have access to the Bot.\n\n"\
                          "Contact {CONTACT_ACCOUNT} for getting access to the Bot.", reply_markup=no_markup)
