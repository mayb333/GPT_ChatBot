from aiogram import types
from loguru import logger
from config import ADMIN_IDS
from src.app.loader import dp, db
from src.utils.markups import no_markup
from src.utils.admin_service import AdminService


admin = AdminService()


@dp.message_handler(commands=["add_admin"])
async def process_adding_admin(message: types.Message):
    await admin.add_admin(message=message)


@dp.message_handler(commands=["remove_admin"])
async def process_removing_admin(message: types.Message):
    await admin.remove_admin(message=message)


@dp.message_handler(commands=["add_user"])
async def process_adding_user(message: types.Message):
    await admin.add_user(message=message)


@dp.message_handler(commands=["remove_user"])
async def process_removing_user(message: types.Message):
    await admin.remove_user(message=message)


@dp.message_handler(commands=["get_reg_users"])
async def process_getting_registered_users(message: types.Message):
    await admin.get_registered_users(message=message)


@dp.message_handler(commands=["get_allowed_users"])
async def process_getting_allowed_users(message: types.Message):
    await admin.get_allowed_users(message=message)


@dp.message_handler(commands=["get_admins"])
async def process_getting_admins(message: types.Message):
    await admin.get_admins(message=message)


@dp.message_handler(commands=["get_analytics"])
async def process_getting_admins(message: types.Message):
    await admin.get_analytics(message=message)
