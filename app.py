import asyncio
import logging
from aiogram import Bot, Dispatcher
from bot.config import config
from bot import handlers


logging.basicConfig(level=config.LOG_LEVEL)
bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher()


async def main():
    handlers.register_common_handlers(dp)
    handlers.register_example_kbd_buttons(dp)
    handlers.register_example_messages_handlers(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
