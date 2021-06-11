from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from src.teleBot.aiogram._005_StateMashine.config import admin_id
from src.teleBot.aiogram._005_StateMashine.loader import dp, bot
from src.teleBot.aiogram._005_StateMashine.states.tests import Test



async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='Бот запущен')

@dp.message_handler(Command('test'), state=None)
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование.\n"
                         "Вопрос №1. \n\n"
                         "Вы часто занимаетесь бессмысленными делами "
                         "(бесцельно блуждаете по интернету, клацаете пультом телевизора, "
                         "просто смотрите в потолок)?")

    await Test.Q1.set()
#     OR
#     await Test.first()

@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)

    await message.answer("Вопрос №2. \n\n"
                         "Ваша память ухудшилась и вы помните то, что было давно, "
                         "но забываете недавние события?")

    await Test.Q2.set()

@dp.message_handler(state=Test.Q2)
async def answer_q1(message: types.Message, state: FSMContext):
    answer2 = message.text
    data = await state.get_data()
    answer1 = data.get('answer1')
    await message.answer(f'Спасибо за Ваши ответы.\n '
                         f'Ответ на первый вопрос - {answer1} \n'
                         f'Ответ на второй вопрос - {answer2}' )



