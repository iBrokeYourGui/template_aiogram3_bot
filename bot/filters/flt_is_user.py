from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsUser(BaseFilter):
    def __init__(self, admin: int, users: list):
        self.admin = admin
        self.users = users

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.users or message.from_user.id == self.admin
