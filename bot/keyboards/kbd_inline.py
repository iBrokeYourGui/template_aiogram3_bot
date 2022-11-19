from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

btn_url = InlineKeyboardButton(text='URL', url='https://example.com')
btn_channel = InlineKeyboardButton(text='Channel', url="tg://user?id=1234567890")
btn_close = InlineKeyboardButton(text='Cancel', callback_data='cancel_command')
btn_cbd_factory = InlineKeyboardButton(text='CBD_factory', callback_data='cbd_factory_dialog')

inline_kbd = (
    InlineKeyboardBuilder()
    .add(btn_url)
    .add(btn_channel)
    .add(btn_cbd_factory)
    .row(btn_close)
    .as_markup()
)
