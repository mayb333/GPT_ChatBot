from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


end_dialog_markup = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(KeyboardButton('❌ End Conversation'))

no_markup = ReplyKeyboardRemove()