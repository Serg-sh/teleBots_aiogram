from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Котлетки')
        ],
        [
            KeyboardButton(text='Макарошки'),
            KeyboardButton(text='Пюрешка')
        ],
        [
            KeyboardButton(text='Борщик'),
            KeyboardButton(text='Супчик'),
            KeyboardButton(text='Солянка')
        ]
    ],
    resize_keyboard=True
)