from aiogram.types import Message, CallbackQuery
from aiogram import F, Dispatcher
import bot.keyboards as kbd
from bot.keyboards.kbd_cbd_factory import ButtonsCallbackFactory


async def inline_kbd_call(message: Message):
    await message.answer("yababoba", reply_markup=kbd.inline_kbd)


async def cbd_factory_start(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=kbd.cbd_factory_kbd)


async def cancel(call: CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer("Операция отменена", reply_markup=kbd.main_keyboard)


async def callback_factory_handling(call: CallbackQuery, callback_data: ButtonsCallbackFactory):
    """ Соответственно, на каждый полученный параметр callback_data можно вешать любую логику"""
    await call.message.delete_reply_markup()
    await call.message.answer(f'Выбрано значение {callback_data.str_data} с параметром: {callback_data.int_data}', reply_markup=kbd.cbd_factory_kbd)


async def pass_the_flag(message: Message):
    await message.answer('Флаг передан в мидлу')


def register_example_kbd_buttons(dp: Dispatcher):
    """
        Для сообщений ждем text.
        Для колбеков ждем data.
    """
    dp.message.register(inline_kbd_call, F.text == 'Инлайн клавиатура')
    dp.message.register(pass_the_flag, F.text == 'Передать флаг через мидлу', flags={"flag_operation": "typing"})
    dp.callback_query.register(cancel, F.data.startswith('can'))
    dp.callback_query.register(cbd_factory_start, F.data == 'cbd_factory_dialog')
    dp.callback_query.register(callback_factory_handling, ButtonsCallbackFactory.filter())
