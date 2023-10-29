import pandas as pd
from aiogram import types
from loguru import logger
from prettytable import PrettyTable
from config import ADMIN_IDS, ALLOWED_USERS
from src.app.loader import db
from src.utils.markups import no_markup


class AdminService:
    async def add_admin(self, message: types.Message, ADMIN_IDS=ADMIN_IDS):
        # Check if the message sender is an admin
        if message.from_user.id not in ADMIN_IDS:
            await message.answer("Access denied", reply_markup=no_markup)
            return
        
        new_id = message.get_args()

        if new_id and new_id.isdigit() and int(new_id) not in ADMIN_IDS:
            ADMIN_IDS.append(int(new_id))

            # Add user to admins table in Database
            db.add_user_to_admins_table(user_id=new_id)

            await message.answer(f"New admin id={new_id} added", reply_markup=no_markup)

            logger.info(f"New admin id={new_id} added")
            logger.info(f"ADMIN_IDS_LIST: {ADMIN_IDS}")
        else:
            await message.answer("Invalid or duplicate ID", reply_markup=no_markup)

    async def remove_admin(self, message: types.Message, ADMIN_IDS=ADMIN_IDS):
        # Check if the message sender is an admin
        if message.from_user.id not in ADMIN_IDS:
            await message.answer("Access denied", reply_markup=no_markup)
            return

        del_id = message.get_args()

        if del_id and del_id.isdigit() and int(del_id) in ADMIN_IDS:
            ADMIN_IDS.remove(int(del_id))
            
            # Remove user from admins table in Database
            db.remove_user_from_admins_table(user_id=del_id)

            await message.answer(f"Admin ID={del_id} removed", reply_markup=no_markup)

            logger.info(f"Admin id={del_id} removed")
            logger.info(f"ADMIN_IDS_LIST: {ADMIN_IDS}")
        else:
            await message.answer("Invalid ID or ID not found", reply_markup=no_markup)
    
    async def add_user(self, message: types.Message, ADMIN_IDS=ADMIN_IDS, ALLOWED_USERS=ALLOWED_USERS):
        # Check if the message sender is an admin
        if message.from_user.id not in ADMIN_IDS:
            await message.answer("Access denied", reply_markup=no_markup)
            return
        
        new_id = message.get_args()

        if new_id and new_id.isdigit() and int(new_id) not in ALLOWED_USERS:
            ALLOWED_USERS.append(int(new_id))

            # Add user to allowed_users table in Database
            db.add_user_to_allowed_users_table(user_id=new_id)

            await message.answer(f"New user ID={new_id} added", reply_markup=no_markup)

            logger.info(f"New user id={new_id} added")
            logger.info(f"ALLOWED_USERS_LIST: {ALLOWED_USERS}")
        else:
            await message.answer("Invalid or duplicate ID", reply_markup=no_markup)

    async def remove_user(self, message: types.Message, ADMIN_IDS=ADMIN_IDS, ALLOWED_USERS=ALLOWED_USERS):
        # Check if the message sender is an admin
        if message.from_user.id not in ADMIN_IDS:
            await message.answer("Access denied", reply_markup=no_markup)
            return

        del_id = message.get_args()

        if del_id and del_id.isdigit() and int(del_id) in ALLOWED_USERS:
            ALLOWED_USERS.remove(int(del_id))
            
            # Remove user from allowed_users table in Database
            db.remove_user_from_allowed_users_table(user_id=del_id)

            await message.answer(f"User ID={del_id} removed", reply_markup=no_markup)

            logger.info(f"User id={del_id} removed")
            logger.info(f"ALLOWED_USERS_LIST: {ALLOWED_USERS}")
        else:
            await message.answer("Invalid ID or ID not found", reply_markup=no_markup)

    async def get_registered_users(self, message: types.Message, ADMIN_IDS=ADMIN_IDS):
        # Check if the message sender is an admin
        if message.from_user.id not in ADMIN_IDS:
            await message.answer("Access denied")
            return
        
        result = db.import_registered_users()
        result = pd.DataFrame(result, columns=['user_id', 'username', 'first_name', 'date'])

        if len(result) == 0:
            await message.answer("No data found for <u>Registered users</u>")
            return 

        # Create PrettyTable class for pretty ouputs of the table in telegram
        table = PrettyTable()
        table.field_names = ['user_id', 'username', 'first_name']

        for index, row in result.iterrows():
            user_id, username, first_name = row['user_id'], row['username'], row['first_name']
            table.add_row([user_id, username, first_name])

        await message.answer(f"<b>Registered users:</b> \n<pre>\n{table}\n</pre>", reply_markup=no_markup)

    async def get_allowed_users(self, message: types.Message, ADMIN_IDS=ADMIN_IDS):
        # Check if the message sender is an admin
        if message.from_user.id not in ADMIN_IDS:
            await message.answer("Access denied")
            return
        
        result = db.import_allowed_users()
        result = pd.DataFrame(result, columns=['user_id', 'username', 'first_name'])

        if len(result) == 0:
            await message.answer("No data found for <u>Allowed users</u>")
            return 

        # Create PrettyTable class for pretty ouputs of the table in telegram
        table = PrettyTable()
        table.field_names = ['user_id', 'username', 'first_name']

        for index, row in result.iterrows():
            user_id, username, first_name = row['user_id'], row['username'], row['first_name']
            table.add_row([user_id, username, first_name])

        await message.answer(f"<b>Allowed users:</b> \n<pre>\n{table}\n</pre>", reply_markup=no_markup)

    async def get_admins(self, message: types.Message, ADMIN_IDS=ADMIN_IDS):
        # Check if the message sender is an admin
        if message.from_user.id not in ADMIN_IDS:
            await message.answer("Access denied")
            return
        
        result = db.import_admins()
        result = pd.DataFrame(result, columns=['user_id', 'username', 'first_name'])

        if len(result) == 0:
            await message.answer("No data found for <u>Admins</u>")
            return 

        # Create PrettyTable class for pretty ouputs of the table in telegram
        table = PrettyTable()
        table.field_names = ['user_id', 'username', 'first_name']

        for index, row in result.iterrows():
            user_id, username, first_name = row['user_id'], row['username'], row['first_name']
            table.add_row([user_id, username, first_name])

        await message.answer(f"<b>Admins:</b> \n<pre>\n{table}\n</pre>", reply_markup=no_markup)
