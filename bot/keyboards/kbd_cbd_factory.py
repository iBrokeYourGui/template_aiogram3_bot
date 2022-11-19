"""
Пример реализации клавиатуры через фабрику колбеков
"""
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class ButtonsCallbackFactory(CallbackData, prefix="btn"):
    str_data: str
    int_data: int


# Keyboard
# Отдельное создание кнопок не работает из за несостыковки типов callback_data
cbd_factory_kbd = (
    InlineKeyboardBuilder()
    .button(text='Button 1', callback_data=ButtonsCallbackFactory(str_data="String1", int_data=1))
    .button(text='Button 2', callback_data=ButtonsCallbackFactory(str_data="String2", int_data=2))
    .button(text='Button 3', callback_data=ButtonsCallbackFactory(str_data="String3", int_data=3))
    .button(text='Cancel', callback_data="cancel")
    .adjust(3)
    .as_markup()
)


# Можно генерить клавиатуры с помощью функций,
# никакой разницы нет, просто в место объекта клавиатуры придется протащить функцию
# def get_cbd_factory_kbd():
#     cbd_factory_kbd = InlineKeyboardBuilder()
#     cbd_factory_kbd.buttonn(text='Button 1', callback_data=ButtonsCallbackFactory(str_data="String1", int_data=1))
#     cbd_factory_kbd.buttonn(text='Button 2', callback_data=ButtonsCallbackFactory(str_data="String2", int_data=2))
#     cbd_factory_kbd.buttonn(text='Button 3', callback_data=ButtonsCallbackFactory(str_data="String3", int_data=3))
#     cbd_factory_kbd.adjust(3)
#     return cbd_factory_kbd.as_markup()
