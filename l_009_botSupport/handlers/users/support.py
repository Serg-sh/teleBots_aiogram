from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from l_009_botSupport.keyboards.inline.support import support_keyboard, support_callback
from l_009_botSupport.loader import dp


@dp.message_handler(Command('support'))
async def ask_support(message: types.Message):
    text = 'Хотите написать сообщение техподдержке?\n' \
           'Нажмите на кнопку ниже.'
    keyboard = await support_keyboard(messages='one')
    await message.answer(text, reply_markup=keyboard)

@dp.callback_query_handler(support_callback.filter(message='one'))
async def send_to_support(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer()

