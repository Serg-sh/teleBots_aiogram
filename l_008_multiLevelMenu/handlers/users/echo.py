from aiogram import types

from l_008_multiLevelMenu.loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(message.text)
