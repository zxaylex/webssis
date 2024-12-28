from dotenv import load_dotenv 
from os import getenv 

load_dotenv()

class config:
    SECRET_KEY = getenv("SECRET_KEY")
    MYSQL_USERNAME = getenv("DB_USER")
    MYSQL_PORT = getenv("DB_PORT")
    MYSQL_PASSWORD = getenv("DB_PASS")
    MYSQL_HOST = getenv("DB_HOST")
    MYSQL_DB = getenv("DB_NAME")
    MYSQL_CURSORCLASS = 'DictCursor'

    CLOUD_NAME = getenv("CLOUD_NAME")
    CLOUD_KEY = getenv("CLOUD_KEY")
    CLOUD_SECRET = getenv("CLOUD_SECRET")
    CLOUD_URL = getenv("CLOUD_URL")