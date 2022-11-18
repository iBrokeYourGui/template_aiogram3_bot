from aiogram import F, types, Dispatcher, html, Bot
from aiogram.filters import Command, CommandObject


async def dick_in_text(message: types.Message):
    await message.answer('Я все слышу')


async def get_params_from_command(message: types.Message, command: CommandObject):
    if command.args:
        await message.answer(f'Аргументы переданные с командой: {command.args}')
    else:
        await message.answer('Аргументы не были переданы. Передайте аргументы после команды /args')


async def reaction_on_sticker(message: types.Message, bot: Bot):
    """ Скачает стикер в указанную папку и вернет его отправителю """
    await bot.download(
        message.sticker,
        destination=f"./tmp/{message.sticker.file_id}.webp"
    )
    await message.reply_sticker(message.sticker.file_id)


async def get_items_from_message(message: types.Message):
    """ Извлечь сущности сообщения """
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


async def formatted_text(message: types.Message):
    await message.answer(f"""Parsed by HTML
{html.quote("<Обработка кавычек>")}
<b>bold</b>, <strong>bold</strong>, {html.bold('bold')}
<i>italic</i>, <em>italic</em>, {html.italic('italic')}
<u>underline</u>, <ins>underline</ins>, {html.underline('underline')}
<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>, {html.strikethrough('strikethrough')}
<span class="tg-spoiler">spoiler</span>, <tg-spoiler>spoiler</tg-spoiler>, {html.spoiler('spoiler')}
<b>bold <i>italic bold <s>italic bold strikethrough <span class="tg-spoiler">italic bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> bold</b>
<a href="http://www.example.com/">inline URL</a>, {html.link('inline URL', 'http://www.example.com/')}
<a href="tg://user?id=123456789">inline mention of a user</a>
<code>inline fixed-width code</code>, {html.code('inline fixed-width code')}
<pre>pre-formatted fixed-width code block</pre>, {html.pre('pre-formatted fixed-width code block')}
<pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>
    """, parse_mode="HTML")
    await message.answer("""Parsed by Markdown2
\<Обработка кавычек\>
*bold \*text*
_italic \*text_
__underline__
~strikethrough~
||spoiler||
*bold _italic bold ~italic bold strikethrough ||italic bold strikethrough spoiler||~ __underline italic bold___ bold*
[inline URL](http://www.example.com/)
[inline mention of a user](tg://user?id=123456789)
`inline fixed-width code`
```
pre-formatted fixed-width code block
```
```python
import os

os.path()
print('11')
```
""", parse_mode="MarkdownV2")


def register_example_messages_handlers(dp: Dispatcher):
    dp.message.register(dick_in_text, F.text == 'pipi')
    dp.message.register(formatted_text, Command('text'))
    dp.message.register(get_params_from_command, Command('args'))
    dp.message.register(get_items_from_message, F.text)
    dp.message.register(reaction_on_sticker, F.content_type == 'sticker')  # .in_({'sticker', 'text', 'etc'})
