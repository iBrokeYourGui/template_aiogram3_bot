from aiogram import F, types, Dispatcher, html, Bot
from aiogram.filters import Command, CommandObject

import bot.keyboards as kbd


async def cmd_start(message: types.Message):
    await message.answer('Ой кто пришёл!', reply_markup=kbd.main_keyboard)


async def cmd_help(message: types.Message):
    await message.answer("""
    /ыефке - начало работы с ботом
    /help - получить текущее сообщение
    /markup - покажет все возможные варианты форматирования текста
    /args <аргументы> - распарсит по пробелу, переданные после команды аргументы 
    """)


async def get_params_from_command(message: types.Message, command: CommandObject):
    """
    command.args вытащит все что было передано после команды (без самой команды)
    сплитим самостоятельно
    """
    if command.args:
        message_text = "Аргументы переданные с командой:\n"
        args = command.args.split(" ")
        for i, arg in enumerate(args, start=1):
            message_text += f'{i}) {arg} \n'
        await message.answer(message_text)
    else:
        await message.answer('Аргументы не были переданы. Передайте аргументы после команды /args')


async def reaction_on_word(message: types.Message):
    await message.answer('Я все слышу')


async def reaction_on_sticker(message: types.Message, bot: Bot):
    """ Скачает стикер в указанную папку и вернет его отправителю """
    await bot.download(
        message.sticker,
        destination=f"./tmp/{message.sticker.file_id}.webp"
    )
    await message.reply_sticker(message.sticker.file_id)


async def get_items_from_message(message: types.Message):
    """
        Извлечь сущности (url/email/code) сообщения
        Если будет передано несколько значений то вытащится только последнее
    """
    result = {
        'url': 'N/A',
        'email': 'N/A',
        'code': 'N/A'
    }
    entities = message.entities or []
    for item in entities:
        if item.type in result.keys():
            result[item.type] = item.extract_from(message.text)
    await message.answer(
        "Результат извлечения данных:\n"
        f"URL: {html.quote(result['url'])}\n"
        f"E-mail: {html.quote(result['email'])}\n"
        f"Пароль: {html.quote(result['code'])}"
    )


def register_common_handlers(dp: Dispatcher):
    dp.message.register(cmd_start, Command('start'))
    dp.message.register(cmd_help, Command('help'))
    dp.message.register(get_params_from_command, Command('args'))
    dp.message.register(reaction_on_word, F.text == 'pipi')
    dp.message.register(get_items_from_message, F.text)
    dp.message.register(reaction_on_sticker, F.content_type == 'sticker')  # .in_({'sticker', 'text', 'etc'})
