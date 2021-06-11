from aiogram.dispatcher.filters import Command, Text

from main import bot, dp
from aiogram.types import Message, ReplyKeyboardRemove
from config import admin_id
from keybordsMenu import menu

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='Бот запущен')







# @dp.message_handler()
# async def echo(message: Message):
#     text = f'Привет, ты написал: {message.text}'
#     # await bot.send_message(chat_id=message.from_user.id, text=text)
#     await message.answer(text=text)

@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer('Выберите товар из меню', reply_markup=menu)

@dp.message_handler(Text(equals=['Котлетки', 'Макарошки', 'Пюрешка']))
async def get_food(message: Message):
    await message.answer(f'Вы выбрали {message.text}. Спасибо.', reply_markup=ReplyKeyboardRemove())