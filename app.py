import asyncio
import logging
from aiogram import Bot, Dispatcher
from bot.config import config
from bot import handlers, middleware


logging.basicConfig(level=config.LOG_LEVEL)
bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher()


async def main():
    """
       Не забываем про порядок регистрации обработчиков.
       Все обрабатывается строго в заданном порядке
    """
    handlers.register_common_handlers(dp)
    handlers.register_example_kbd_buttons(dp)
    handlers.register_example_messages_handlers(dp)
    # outer_middleware - срабатывыет всегда
    # middleware - срабатывыет после фильтров
    dp.message.middleware.register(middleware.FlagsMiddleware())
    dp.message.middleware.register(middleware.CounterMiddleware())
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
