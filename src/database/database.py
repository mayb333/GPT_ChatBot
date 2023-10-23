import os
import psycopg2
from datetime import datetime
from loguru import logger
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


class DataBase:
    def __init__(self, database_url: str = DATABASE_URL):
        self.database_url = database_url

        logger.info("Initialized Database")

    def connect_to_db(self):
        connection = psycopg2.connect(self.database_url)

        logger.info("Connected to Database")

        return connection 
    
    def add_user(self, user_id, username, first_name, timestamp=datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        try:
            connection = self.connect_to_db()

            with connection.cursor() as cursor:
                query = f"""INSERT INTO users (user_id, username, first_name, first_message) 
                            VALUES('{user_id}', '{username}', '{first_name}', '{timestamp}')"""

                cursor.execute(query)
                connection.commit()
                connection.close()

                logger.info(f"User with id={user_id} has been added to users table")
                logger.info("Closed connection to Database")
        except Exception as exp:
            logger.info(f"Couldn't execute the function \"add_user\" \n {exp}")

    def user_not_in_users(self, user_id):
        try:
            connection = self.connect_to_db()
            flag = False

            with connection.cursor() as cursor:
                query = f"""SELECT user_id
                            FROM users
                            WHERE user_id = '{user_id}';"""
                cursor.execute(query)
                result = cursor.fetchone()

                connection.close()
                logger.info("Closed connection to Database")

                if result is None:
                    flag = True
                return flag

        except Exception as exp:
            logger.info(f"Couldn't execute the function \"user_not_in_users\" \n {exp}")
