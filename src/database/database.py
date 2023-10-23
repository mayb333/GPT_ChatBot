import os
import psycopg2
from loguru import logger
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


class DataBase:
    def __init__(self, database_url: str = DATABASE_URL):
        self.database_url = database_url

    def connect_to_db(self):
        connection = psycopg2.connect(self.database_url)

        logger.info("Connected to Database")

        return connection 
