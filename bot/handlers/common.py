from aiogram import types, Dispatcher
from aiogram.filters import Command
import bot.keyboards as kbd


async def cmd_start(message: types.Message):
    await message.answer('Ой кто пришёл!', reply_markup=kbd.main_keyboard)


async def cmd_help(message: types.Message):
    await message.answer('Помоги себе сам')


def register_common_handlers(dp: Dispatcher):
    dp.message.register(cmd_start, Command('start'))
    dp.message.register(cmd_help, Command('help'))
