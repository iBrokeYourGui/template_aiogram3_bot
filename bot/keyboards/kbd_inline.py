from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram import F

btn_url = InlineKeyboardButton(text='URL', url='https://example.com')
btn_channel = InlineKeyboardButton(text='Channel', url="tg://user?id=1234567890")
btn_close = InlineKeyboardButton(text='Cancel', callback_data='cancel_command')

inline_bkd = (
    InlineKeyboardBuilder()
    .add(btn_url)
    .add(btn_channel)
    .row(btn_close)
    .as_markup()
)