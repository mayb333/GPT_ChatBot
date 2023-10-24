import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
CONTACT_ACCOUNT = os.getenv("CONTACT_ACCOUNT")
