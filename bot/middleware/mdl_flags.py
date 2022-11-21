from typing import Callable, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.dispatcher.flags import get_flag
from aiogram.utils.chat_action import ChatActionSender


class FlagsMiddleware(BaseMiddleware):
    """
    Пример мидлы с флагами.
    Обработка активируется если прилетел соотвествующий флаг из хэндлера.
    Соответственно такую мидру нужно регистрировать как inner middleware
    """
    async def __call__(self,
                 handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
                 event: Message,
                 data: dict[str, Any]
                 ) -> Any:
        flag = get_flag(data, "flag_operation")
        if not flag:
            return await handler(event, data)

        print(f'Флаг {flag} получен')
        async with ChatActionSender(action=flag, chat_id=event.chat.id):
            return await handler(event, data)
