from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.teleBot.aiogram._004_inLineKey.config import URL_PEAR, URL_APPLES
from src.teleBot.aiogram._004_inLineKey.keyboards.inline.callback_datas import buy_callback

# choice = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Купить грушу', callback_data=buy_callback.new(
#                 item_name='pear', quantity=1
#             )),
#             InlineKeyboardButton(text='Купить яблоки', callback_data='buy:apple:5'),
#         ],
#         [
#             InlineKeyboardButton(text='Отмена', callback_data='cancel')
#         ]
#     ]
# )

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text='Купить грушу', callback_data='buy:pear:1')
choice.insert(buy_pear)
buy_apple = InlineKeyboardButton(text='Купить яблоки', callback_data='buy:apple:5')
choice.insert(buy_apple)
cancel_button = InlineKeyboardButton(text='Отмена', callback_data='cancel')
choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup().insert(InlineKeyboardButton(text='Купи тут', url=URL_PEAR))
apples_keyboard = InlineKeyboardMarkup().insert(InlineKeyboardButton(text='Купи тут', url=URL_APPLES))

