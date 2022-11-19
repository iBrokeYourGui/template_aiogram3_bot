from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    def __init__(self, admin: int):
        self.admin = admin

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == self.admin

