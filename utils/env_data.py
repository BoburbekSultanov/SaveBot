from os import getenv
from os.path import join

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from utils.settings import BASE_DIR, ENV_PATH

load_dotenv(ENV_PATH)


class BotConfig:
    TOKEN = getenv("BOT_TOKEN")


# class DBConfig(BaseSettings):
#     DB_HOST: str
#     DB_PORT: int
#     DB_USER: str
#     DB_PASSWORD: str
#     DB_NAME: str
#     DB_URL : str

class DBConfig:
    DB_NAME  = getenv("DB_NAME")
    DB_USER = getenv("DB_USER")
    DB_PASSWORD = getenv("DB_PASSWORD")
    DB_HOST = getenv("DB_HOST")
    DB_PORT  = getenv("DB_PORT"),
    DB_URL = getenv("DB_ASYNC_URL")


class WebConfig:
    ADMIN_USERNAME = getenv("ADMIN_USERNAME")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD")


class Config:
    bot = BotConfig()
    db = DBConfig()
    web = WebConfig()
