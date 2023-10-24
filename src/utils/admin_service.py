from aiogram import types
from loguru import logger
from config import ADMIN_IDS


class AdminService:
    async def add_admin(self, message: types.Message, ADMIN_IDS=ADMIN_IDS):
        # Check if message sender is an admin
        if message.from_user.id not in ADMIN_IDS:
            await message.answer("Access denied")
            return
        
        new_id = message.get_args()

        if new_id and new_id.isdigit() and int(new_id) not in ADMIN_IDS:
            ADMIN_IDS.append(int(new_id))
            with open(".env", "r") as f:
                lines = f.readlines()
            lines = self._add_admin_id_to_env(new_id, lines)
            with open(".env", "w") as f:
                f.writelines(lines)
            await message.answer("New admin added")

            logger.info(f"New admin id={new_id} added")
            logger.info(f"ADMIN_IDS_LIST: {ADMIN_IDS}")
        else:
            await message.answer("Invalid or duplicate ID")


    async def remove_admin(self, message: types.Message, ADMIN_IDS=ADMIN_IDS):
        # Check if message sender is an admin
        if message.from_user.id not in ADMIN_IDS:
            await message.answer("Access denied")
            return

        logger.info(f"ADMIN_IDS: {ADMIN_IDS}")

        del_id = message.get_args()

        if del_id and del_id.isdigit() and int(del_id) in ADMIN_IDS:
            ADMIN_IDS.remove(int(del_id))
            with open(".env", "r") as f:
                lines = f.readlines()
            lines = self._remove_admin_id_from_env(del_id, lines)
            with open(".env", "w") as f:
                f.writelines(lines)
            await message.answer("Admin ID removed")

            logger.info(f"Admin id={del_id} removed")
            logger.info(f"ADMIN_IDS_LIST: {ADMIN_IDS}")
        else:
            await message.answer("Invalid ID or ID not found")


    def _add_admin_id_to_env(self, user_id, lines):
        for i, line in enumerate(lines):
            if line.startswith("ADMIN_IDS_LIST"):
                current_ids = line.strip().split("=")[1].split(",")
                if str(user_id) not in current_ids:
                    current_ids.append(str(user_id))
                    lines[i] = f"ADMIN_IDS_LIST={','.join(current_ids)}\n"
        return lines
    
    def _remove_admin_id_from_env(self, user_id, lines):
        for i, line in enumerate(lines):
            if line.startswith("ADMIN_IDS_LIST"):
                current_ids = line.strip().split("=")[1].split(",")
                if str(user_id) in current_ids:
                    current_ids.remove(str(user_id))
                    lines[i] = f"ADMIN_IDS_LIST={','.join(current_ids)}\n"
        return lines
