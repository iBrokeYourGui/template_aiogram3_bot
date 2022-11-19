import logging
from environs import Env

env = Env()
env.read_env()


class Config:
    def __init__(self):
        self.LOG_LEVEL = env.str("LOG_LEVEL", "INFO")
        self.TELEGRAM_TOKEN = env.str("TELEGRAM_TOKEN", "")
        self.TELEGRAM_BOT_ADMIN = env.int("TELEGRAM_BOT_ADMIN", 0)
        self.TELEGRAM_BOT_USERS = env.list("TELEGRAM_BOT_USERS", [])


config = Config()
logging.basicConfig(format=u'#%(levelname)-8s %(filename)-17s [LINE:%(lineno)-4d] [%(asctime)s] %(message)s',
                    level=config.LOG_LEVEL,)
