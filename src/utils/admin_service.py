from aiogram import types
from loguru import logger
from config import ADMIN_IDS, ALLOWED_USERS
from src.app.loader import db


class AdminService:
    async def add_admin(self, message: types.Message, ADMIN_IDS=ADMIN_IDS):
        # Check if the message sender is an admin
        if message.from_user.id not in ADMIN_IDS:
            await message.answer("Access denied")
            return
        
        new_id = message.get_args()

        if new_id and new_id.isdigit() and int(new_id) not in ADMIN_IDS:
            ADMIN_IDS.append(int(new_id))

            # Add user to admins table in Database
            db.add_user_to_admins_table(user_id=new_id)

            await message.answer(f"New admin id={new_id} added")

            logger.info(f"New admin id={new_id} added")
            logger.info(f"ADMIN_IDS_LIST: {ADMIN_IDS}")
        else:
            await message.answer("Invalid or duplicate ID")

    async def remove_admin(self, message: types.Message, ADMIN_IDS=ADMIN_IDS):
        # Check if the message sender is an admin
        if message.from_user.id not in ADMIN_IDS:
            await message.answer("Access denied")
            return

        del_id = message.get_args()

        if del_id and del_id.isdigit() and int(del_id) in ADMIN_IDS:
            ADMIN_IDS.remove(int(del_id))
            
            # Remove user from admins table in Database
            db.remove_user_from_admins_table(user_id=del_id)

            await message.answer(f"Admin ID={del_id} removed")

            logger.info(f"Admin id={del_id} removed")
            logger.info(f"ADMIN_IDS_LIST: {ADMIN_IDS}")
        else:
            await message.answer("Invalid ID or ID not found")
    
    async def add_user(self, message: types.Message, ADMIN_IDS=ADMIN_IDS, ALLOWED_USERS=ALLOWED_USERS):
        # Check if the message sender is an admin
        if message.from_user.id not in ADMIN_IDS:
            await message.answer("Access denied")
            return
        
        new_id = message.get_args()

        if new_id and new_id.isdigit() and int(new_id) not in ALLOWED_USERS:
            ALLOWED_USERS.append(int(new_id))

            # Add user to allowed_users table in Database
            db.add_user_to_allowed_users_table(user_id=new_id)

            await message.answer(f"New user ID={new_id} added")

            logger.info(f"New user id={new_id} added")
            logger.info(f"ALLOWED_USERS_LIST: {ALLOWED_USERS}")
        else:
            await message.answer("Invalid or duplicate ID")

    async def remove_user(self, message: types.Message, ADMIN_IDS=ADMIN_IDS, ALLOWED_USERS=ALLOWED_USERS):
        # Check if the message sender is an admin
        if message.from_user.id not in ADMIN_IDS:
            await message.answer("Access denied")
            return

        del_id = message.get_args()

        if del_id and del_id.isdigit() and int(del_id) in ALLOWED_USERS:
            ALLOWED_USERS.remove(int(del_id))
            
            # Remove user from allowed_users table in Database
            db.remove_user_from_allowed_users_table(user_id=del_id)

            await message.answer(f"User ID={del_id} removed")

            logger.info(f"User id={del_id} removed")
            logger.info(f"ALLOWED_USERS_LIST: {ALLOWED_USERS}")
        else:
            await message.answer("Invalid ID or ID not found")
