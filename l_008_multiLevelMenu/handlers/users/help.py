from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp



from l_008_multiLevelMenu.loader import dp
from l_008_multiLevelMenu.utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку'
    ]
    await message.answer('\n'.join(text))
