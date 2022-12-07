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
    # Регистрация хэндлеров old school
    handlers.register_common_handlers(dp)
    handlers.register_example_kbd_buttons(dp)
    handlers.register_example_messages_handlers(dp)
    # Регистрация роутеров
    dp.include_router(handlers.privat_chat_router)
    dp.include_router(handlers.events_in_group_router)
    dp.include_router(handlers.changes_in_group_router)
    # outer_middleware - срабатывыет всегда
    # middleware - срабатывыет после фильтров
    dp.message.middleware.register(middleware.FlagsMiddleware())
    dp.message.middleware.register(middleware.CounterMiddleware())
    # resolve_used_update_types -  пройдёт по всем роутерам, узнает, хэндлеры на какие типы есть в коде,
    # и попросить Telegram присылать апдейты только про них.

    # Подгрузка списка админов
    # admins = await bot.get_chat_administrators(config.main_chat_id)
    # config.admins = {admin.user.id for admin in admins}
    # Можно передать список админов через диспетчер в виде доп параметра admins для каждого обработчика
    # await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), admins=config.admins)
    # А можно тупо через конфиг там где это нужно.

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped')
