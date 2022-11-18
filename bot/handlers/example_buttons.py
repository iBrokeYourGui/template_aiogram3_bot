from aiogram.types import Message, CallbackQuery
from aiogram import F, Dispatcher
import bot.keyboards as kbd


async def inline_kbd_call(message: Message):
    await message.answer("yababoba", reply_markup=kbd.inline_bkd)


async def cancel(call: CallbackQuery):
    await call.message.answer("Операция отменена", reply_markup=kbd.main_keyboard)


def register_example_kbd_buttons(dp: Dispatcher):
    dp.message.register(inline_kbd_call, F.text == 'Инлайн клавиатура')
    dp.callback_query.register(cancel, F.data.startswith('can'))
