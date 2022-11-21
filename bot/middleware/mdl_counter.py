from typing import Callable, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message


class CounterMiddleware(BaseMiddleware):
    """
    Считает кол-во объектов типа "Message"
    Может быть вставлена как до обработчика так и после.
    Вставка задаётся при регистрации. Смотри файл app.py
    """
    def __init__(self) -> None:
        self.counter = 0

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any],
    ) -> Any:
        self.counter += 1
        print("Выполнить действие ДО хэндлера")
        data['counter'] = self.counter
        result = await handler(event, data)
        print("Выполнить действие ПОСЛЕ хэндлера")
        return result
