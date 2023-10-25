# GPT ChatBot 
![Static Badge](https://img.shields.io/badge/status-deployment-blue?style=fot-the-badge)

# About The Project
This repository represents GPT ChatBot in Telegram using OpenAI. With a focus on maintaining the context of dialog, this ChatBot offers intelligent responses and meaningful conversations. Alongside its conversational capabilities, the project incorporates advanced analytics and admin service. All the necessary data, including user conversations and statistics, are stored securely in a PostgreSQL Database.

# Capabilities

* ChatGPT-3.5-Turbo
* Keeping the context of the converstaion
* Solid User Experience
* Admin service: adding and removing users, admins with commands
* Collecting user statistics via PostgreSQL Database
* Analytics for admins

# Get Started
* Clone the repository:
```
git clone https://github.com/mayb333/GPT_ChatBot.git
```
* Install the required Python libraries:
```
pip install -r requirements.txt
```

* Specify the environment variables in `.env` file:
```
BOT_TOKEN = Bot Token
OPENAI_API_KEY = OpenAI API key
DATABASE_URL = PostgreSQL Database URL
CONTACT_ACCOUNT = Contact Account for getting access to the Bot
ADMIN_IDS_LIST = List of Adming IDs
ALLOWED_USERS_LIST = List of Allowed users IDs for using the Bot
```

* Start the Bot by running bash-script:
```
bash run_bot.sh
```


# Project Structure
1. `static/`: contains script to launch the Bot 
2. `src/`: contains application source folder
    * `app/`:
        - `bot.py`: source code for the Bot
        - `loader.py`: source code for initializating Bot, Dispatcher, Database
    * `handlers/`:
        - `start.py`: source code for start handler 
        - `dialog.py`: source code for dialog handlers
        - `admin.py`: source code for admin handlers
    * `database/`:
        - `database.py`: source code for interaction with database 
        - `queries`: sql queries for create tables in PostgreSQL
    * `utils/`:
        - `openai_service.py`: source code for OpenAI service
        - `admin_service.py`: source code for admin service
        - `messages.py`: source code for messages processing
        - `markups.py`: source code for keyboard markups


# The main tools used in the project
![Static Badge](https://img.shields.io/badge/-Python_3.10.8-090909?style=for-the-badge&logo=python&color=black)
![Static Badge](https://img.shields.io/badge/-aiogram_2.25.1-090909?style=for-the-badge&logo=aiogram&color=black)
![Static Badge](https://img.shields.io/badge/-openai_0.28.1-090909?style=for-the-badge&logo=openai&color=black)
![Static Badge](https://img.shields.io/badge/-psycopg2_2.9.9-090909?style=for-the-badge&logo=psycopg2&color=black)
![Static Badge](https://img.shields.io/badge/-loguru_0.7.2-090909?style=for-the-badge&logo=loguru&color=black)