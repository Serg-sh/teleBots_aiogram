import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
ADMINS = [os.getenv('ADMIN_ID')]
IP = os.getenv('IP')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')

POSTGRESURI = f'postgresql://{DB_USER}:{DB_PASS}@{IP}/{DB_NAME}'

