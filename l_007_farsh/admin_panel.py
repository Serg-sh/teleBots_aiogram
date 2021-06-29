from asyncio import sleep
from aiogram import types
from aiogram.dispatcher import FSMContext
from config import admin_id
from load_all import dp, bot, _
from states import NewItem, Mailing
from database import Item, User


@dp.message_handler(user_id=admin_id, commands=['cancel'], state=NewItem)
async def cancel(message: types.Message, state: FSMContext):
    await message.answer(_('Вы отменили создание товара'))
    await state.reset_state()


@dp.message_handler(user_id=admin_id, commands=['add_item'])
async def add_item(message: types.Message):
    await message.answer(_('Введите название товара или нажмите /cancel'))
    await NewItem.Name.set()


@dp.message_handler(user_id=admin_id, state=NewItem.Name)
async def enter_name(message: types.Message, state: FSMContext):
    name = message.text
    item = Item()
    item.name = name
    await message.answer(_('Название: {name}'
                           '\nПришлите мне фотографию товара (не документ) или нажмите /cancel').format(
        name=name))
    await NewItem.Photo.set()
    await state.update_data(item=item)


@dp.message_handler(user_id=admin_id, state=NewItem.Photo, content_types=types.ContentTypes.PHOTO)
async def add_photo(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    data = await state.get_data()
    item: Item = data.get('item')
    item.photo = photo
    await message.answer_photo(
        photo=photo,
        caption=_('Название: {name}'
                  '\nПришлите цену товара в копейках или нажмите /cancel').format(
            name=item.name)
    )
    await NewItem.Price.set()
    await state.update_data(item=item)


@dp.message_handler(user_id=admin_id, state=NewItem.Price)
async def enter_price(message: types.Message, state: FSMContext):
    data = await state.get_data()
    item: Item = data.get('item')
    try:
        price = int(message.text)
    except ValueError:
        await message.answer(_('Неверное значение, введите число.'))
        return
    item.price = price

    markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                (types.InlineKeyboardButton(text=_('Да'), callback_data='confirm ')),
                (types.InlineKeyboardButton(text=_('Ввести заново'), callback_data='change'))
            ],
            [types.InlineKeyboardButton(text=_('Отменить'), callback_data='cancel')]
        ]

    )
    await message.answer(_('Цена: {price:,}\nПодтверждаете? Нажмите /cancel чтобы отменить.').format(
        price=price), reply_markup=markup)
    await NewItem.Confirm.set()
    await state.update_data(item=item)


@dp.callback_query_handler(user_id=admin_id, text_contains='change', state=NewItem.Confirm)
async def change_price(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(_('Введите заново цену товара в копейках.'))
    await NewItem.Price.set()


@dp.callback_query_handler(user_id=admin_id, text_contains='confirm', state=NewItem.Confirm)
async def confirm(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    data = await state.get_data()
    item: Item = data.get('item')
    await item.create()
    await call.message.answer(_('Товар удачно создан'))
    await state.reset_state()


@dp.message_handler(user_id=admin_id, commands=['tell_everyone'])
async def mailing(message: types.Message):
    await message.answer_photo(_('Пришли текст рассылки'))
    await Mailing.Text.set()


@dp.message_handler(user_id=admin_id, state=Mailing.Text)
async def enter_text(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                [types.InlineKeyboardButton(text='Українська', callback_data='uk')],
                [types.InlineKeyboardButton(text='Русский', callback_data='ru')],
                [types.InlineKeyboardButton(text='English', callback_data='eu')]
            ]
        ]
    )
    await message.answer(_('На каком языке разослать это сообщение?\n\n'
                           'Текст:\n'
                           '{text}').format(text=text), reply_markup=markup)
    await Mailing.Languarge.set()


@dp.callback_query_handler(user_id=admin_id, state=Mailing.Languarge)
async def enter_lang(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    await state.reset_state()
    await call.message.edit_reply_markup()
    users = await User.query.where(User.language == call.data).gino.all()
    for user in users:
        try:
            await bot.send_message(chat_id=user.user_id, text=text)
            await sleep(0.3)
        except Exception:
            pass
    await call.message.answer(_('Рассылка выполнена.'))
