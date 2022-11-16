from aiogram.filters import BoundFilter
from aiogram.types import Message
from ..config import config


class IsAdmin(BoundFilter):

    async def check(self, message: Message) -> bool:
        return message.from_user.id == int(config.TELEGRAM_BOT_ADMIN.get('telegram_id'))
