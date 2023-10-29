import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
CONTACT_ACCOUNT = os.getenv("CONTACT_ACCOUNT")

OWNER_ID = int(os.getenv("OWNER_ID", 0))
OWNER_NICKNAME = os.getenv("OWNER_NICKNAME")
OWNER_FIRST_NAME = os.getenv("OWNER_FIRST_NAME")

ADMIN_IDS = [int(OWNER_ID)]
ALLOWED_USERS = [int(OWNER_ID)]
