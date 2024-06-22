import os

from dotenv import load_dotenv


class Settings:
    """Класс с настройками для проекта."""

    def __init__(self) -> None:
        load_dotenv()
        self.tg_bot_token = os.getenv('TELEGRAM_TOKEN')
        self.tg_user_id = os.getenv('TELEGRAM_USER_ID')
        self.hh_url = os.getenv('HH_URL')
