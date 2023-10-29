import os
import psycopg2
from datetime import datetime
from loguru import logger
from config import DATABASE_URL


class DataBase:
    def __init__(self, database_url: str = DATABASE_URL):
        self.database_url = database_url

        logger.info("Initialized Database")

    def connect_to_db(self):
        connection = psycopg2.connect(self.database_url)

        logger.info("Connected to Database")

        return connection 
    
    def register_user(self, user_id, username, first_name, timestamp=datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        try:
            connection = self.connect_to_db()

            with connection.cursor() as cursor:
                query = f"""INSERT INTO registered_users (user_id, username, first_name, timestamp) 
                            VALUES('{user_id}', '{username}', '{first_name}', '{timestamp}')"""

                cursor.execute(query)
                connection.commit()
                connection.close()

                logger.info(f"User with id={user_id} has been added to users table")
                logger.info("Closed connection to Database")
        except Exception as exp:
            logger.info(f"Couldn't execute the function \"register_user\" \n {exp}")

    def user_not_in_registered_users(self, user_id):
        try:
            connection = self.connect_to_db()
            flag = False

            with connection.cursor() as cursor:
                query = f"""SELECT user_id
                            FROM registered_users
                            WHERE user_id = '{user_id}';"""
                cursor.execute(query)
                result = cursor.fetchone()

                connection.close()
                logger.info("Closed connection to Database")

                if result is None:
                    flag = True
                return flag

        except Exception as exp:
            logger.info(f"Couldn't execute the function \"user_not_in_registered_users\" \n {exp}")

    def add_data_to_messages_table(self, user_id, message, tokens, timestamp=datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        try:
            connection = self.connect_to_db()

            with connection.cursor() as cursor:
                query = f"""INSERT INTO messages (user_id, message, tokens, timestamp) 
                            VALUES('{user_id}', '{message}', '{tokens}', '{timestamp}')"""

                cursor.execute(query)
                connection.commit()
                connection.close()

                logger.info(f"Added message from user with id={user_id} to messages_table")
                logger.info("Closed connection to Database")
        except Exception as exp:
            logger.info(f"Couldn't execute the function \"add_data_to_messages_table\" \n {exp}")

    def add_user_to_allowed_users_table(self, user_id, timestamp=datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        try:
            connection = self.connect_to_db()

            with connection.cursor() as cursor:
                query = f"""INSERT INTO allowed_users (user_id, date_added) 
                            VALUES('{user_id}', '{timestamp}')"""

                cursor.execute(query)
                connection.commit()
                connection.close()

                logger.info(f"User with id={user_id} has been added to allowed_users table")
                logger.info("Closed connection to Database")
        except Exception as exp:
            logger.info(f"Couldn't execute the function \"add_user_to_allowed_users_table\" \n {exp}")

    def add_user_to_admins_table(self, user_id, timestamp=datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        try:
            connection = self.connect_to_db()

            with connection.cursor() as cursor:
                query = f"""INSERT INTO admins (user_id, date_added) 
                            VALUES('{user_id}', '{timestamp}')"""

                cursor.execute(query)
                connection.commit()
                connection.close()

                logger.info(f"User with id={user_id} has been added to admins table")
                logger.info("Closed connection to Database")
        except Exception as exp:
            logger.info(f"Couldn't execute the function \"add_user_to_admins_table\" \n {exp}")

    def remove_user_from_allowed_users_table(self, user_id):
        try:
            connection = self.connect_to_db()

            with connection.cursor() as cursor:
                query = f"""DELETE FROM allowed_users 
                            WHERE user_id = '{user_id}';"""

                cursor.execute(query)
                connection.commit()
                connection.close()

                logger.info(f"User with id={user_id} has been remove from allowed_users table")
                logger.info("Closed connection to Database")
        except Exception as exp:
            logger.info(f"Couldn't execute the function \"remove_user_from_allowed_users_table\" \n {exp}")

    def remove_user_from_admins_table(self, user_id):
        try:
            connection = self.connect_to_db()

            with connection.cursor() as cursor:
                query = f"""DELETE FROM admins 
                            WHERE user_id = '{user_id}';"""

                cursor.execute(query)
                connection.commit()
                connection.close()

                logger.info(f"User with id={user_id} has been removed from admins table")
                logger.info("Closed connection to Database")
        except Exception as exp:
            logger.info(f"Couldn't execute the function \"remove_user_from_admins_table\" \n {exp}")

    def import_registered_users(self):
        try:
            connection = self.connect_to_db()

            with connection.cursor() as cursor:
                query = f"""SELECT *
                            FROM registered_users"""
                cursor.execute(query)
                result = cursor.fetchall()

                connection.close()
                logger.info("Closed connection to Database")

                return result

        except Exception as exp:
            logger.info(f"Couldn't execute the function \"import_registered_users\" \n {exp}")

    def import_allowed_users(self):
        try:
            connection = self.connect_to_db()

            with connection.cursor() as cursor:
                query = f"""SELECT registered_users.user_id, registered_users.username, registered_users.first_name
                            FROM registered_users
                            INNER JOIN allowed_users 
                                ON allowed_users.user_id = registered_users.user_id"""
                cursor.execute(query)
                result = cursor.fetchall()

                connection.close()
                logger.info("Closed connection to Database")

                return result

        except Exception as exp:
            logger.info(f"Couldn't execute the function \"import_allowed_users\" \n {exp}")

    def import_admins(self):
        try:
            connection = self.connect_to_db()

            with connection.cursor() as cursor:
                query = f"""SELECT registered_users.user_id, registered_users.username, registered_users.first_name
                            FROM registered_users
                            INNER JOIN admins 
                                ON admins.user_id = registered_users.user_id"""
                cursor.execute(query)
                result = cursor.fetchall()

                connection.close()
                logger.info("Closed connection to Database")

                return result

        except Exception as exp:
            logger.info(f"Couldn't execute the function \"import_admins\" \n {exp}")
