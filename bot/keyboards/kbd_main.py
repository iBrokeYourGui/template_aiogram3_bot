from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton


btn_search = KeyboardButton(text="🔎 Найти")
btn_settings = KeyboardButton(text="🛠 Настройки")

main_keyboard = (
  ReplyKeyboardBuilder()
  .row(btn_search, btn_settings)
  .button(text='Инлайн клавиатура')
  .button(text='Кнопка 4')
  .adjust(2)
  .as_markup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Текст плейсхолдера",
  )
)
