import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from src.teleBot.aiogram._004_inLineKey.keyboards.inline.callback_datas import buy_callback
from src.teleBot.aiogram._004_inLineKey.keyboards.inline.chois_buttons import choice, pear_keyboard, apples_keyboard
from src.teleBot.aiogram._004_inLineKey.loader import dp


@dp.message_handler(Command('items'))
async def show_items(message: Message):
    await message.answer('На продажу у нас есть 2 товара: 5 Яблок и 1 Груша. \n '
                         'Если вам ничего не нужно - жмите отмену', reply_markup=choice)

@dp.callback_query_handler(buy_callback.filter(item_name='apple'))
async def buying_appls(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'call = {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'Вы выбрали Яюлоки. Яблок всего {quantity}. Спасибо',
                              reply_markup=apples_keyboard)

@dp.callback_query_handler(text_contains='pear')
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Вы выбрали грушу. Груша всего одна. Спасибо',
                              reply_markup=pear_keyboard)


@dp.callback_query_handler(text='cancel')
async def cancel_buyng(call: CallbackQuery):
    await call.answer('Вы отменили эту покупку!', show_alert=True)
    await call.message.edit_reply_markup()
