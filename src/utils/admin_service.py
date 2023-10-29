import pandas as pd
from aiogram import types
from datetime import datetime, timedelta
from loguru import logger
from prettytable import PrettyTable
from config import ADMIN_IDS, ALLOWED_USERS, OWNER_ID
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

    async def remove_admin(self, message: types.Message, ADMIN_IDS=ADMIN_IDS, OWNER_ID=OWNER_ID):
        # Check if the message sender is an admin
        if message.from_user.id not in ADMIN_IDS:
            await message.answer("Access denied", reply_markup=no_markup)
            return

        del_id = message.get_args()

        if int(del_id) == OWNER_ID:
            await message.answer("Access denied. \nYou're trying to remove the Owner")
            return

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
        result = result[['user_id', 'username', 'first_name']]

        if len(result) == 0:
            await message.answer("No data found for <u>Registered users</u>")
            return 

        # Create pretty ouputs of the table in telegram
        table = self._pretty_table(result, columns=['user_id', 'username', 'first_name'])

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

        # Create pretty ouputs of the table in telegram
        table = self._pretty_table(result, columns=['user_id', 'username', 'first_name'])

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

        # Create pretty ouputs of the table in telegram
        table = self._pretty_table(result, columns=['user_id', 'username', 'first_name'])
        
        await message.answer(f"<b>Admins:</b> \n<pre>\n{table}\n</pre>", reply_markup=no_markup)

    async def get_analytics(self, message: types.Message, ADMIN_IDS=ADMIN_IDS):
        # Check if the message sender is an admin
        if message.from_user.id not in ADMIN_IDS:
            await message.answer("Access denied")
            return
        
        data = db.import_messages_table()
        data = pd.DataFrame(data, columns=['user_id', 'username', 'first_name', 'tokens', 'timestamp'])
    
        data['timestamp'] = pd.to_datetime(data.timestamp, dayfirst=True)
        data['tokens'] = data['tokens'].astype('int')

        tokens_spent_per_user = data.groupby('user_id', as_index=False).tokens.sum()
        tokens_spent_per_user_for_week = data[data.timestamp >= (datetime.now() - timedelta(days=7))]\
            .groupby('user_id', as_index=False).tokens.sum()
        tokens_spent_per_user_for_month = data[data.timestamp >= (datetime.now() - timedelta(days=7))]\
            .groupby('user_id', as_index=False).tokens.sum()

        # Create pretty ouputs of the table in telegram
        table_1 = self._pretty_table(tokens_spent_per_user, columns=['user_id', 'tokens'])
        table_2 = self._pretty_table(tokens_spent_per_user_for_week, columns=['user_id', 'tokens'])
        table_3 = self._pretty_table(tokens_spent_per_user_for_month, columns=['user_id', 'tokens'])

        await message.answer(f"<b>Tokens spent per user</b> \n<pre>\n{table_1}\n</pre>\n"
                             f"<b>Tokens spent per user for a <u>week</u></b> \n<pre>\n{table_2}\n</pre>\n"
                             f"<b>Tokens spent per user for a <u>month</u></b> \n<pre>\n{table_3}\n</pre>\n", 
                              reply_markup=no_markup)

    def _pretty_table(self, data, columns):
        table = PrettyTable()
        table.field_names = columns

        for index, row in data.iterrows():
            table.add_row(row)

        return table
