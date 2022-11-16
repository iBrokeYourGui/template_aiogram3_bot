from aiogram.filters import BoundFilter
from aiogram.types import Message
from ..config import config


class IsUser(BoundFilter):

    async def check(self, message: Message) -> bool:
        result = (message.from_user.id in config.TELEGRAM_BOT_USERS
                  or message.from_user.id == int(config.TELEGRAM_BOT_ADMIN.get('telegram_id')))
        return result
