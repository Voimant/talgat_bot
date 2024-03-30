from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup

from DB.db_func import conn
from DB.main_db import add_data_two, add_data
from config import TOKEN
from keyboards.key_Admin import admin_markup, subs_form_markup_2, subs_day_markup, send_canc_markup_admin
from keyboards.keyboards import main_menu_markup, group_markup, podpiaki_markup, subs_form_markup, send_canc_markup, \
    cancel_markup
from aiogram.types import FSInputFile
import random


router = Router()
router.message.filter(
    F.chat.type == "private"
)
bot = Bot(token=TOKEN)


@router.message(F.text == 'talgat19911992')
async def get_admin (mess: Message):
    await mess.answer('Вы находитесь в административной панели, что будем делать хозяин?', reply_markup=admin_markup)

@router.callback_query(F.data == 'admin_send')
async def get_photo_unphoto(call: CallbackQuery):
    await call.message.answer('Какое объявление хозяин отправить, с фото или без фото?', reply_markup=subs_form_markup_2)


class Fadmin(StatesGroup):
    text = State()
    picture_admin = State()
    check = State()
    subs_day = State()
    sender_admin = State()


@router.callback_query(F.data == 'admin_with_photo')
async def get_one_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Введите текст объявления', reply_markup=cancel_markup)
    await state.set_state(Fadmin.text)


@router.message(Fadmin.text)
async def get_text_1(mess: Message, state: FSMContext):
    try:
        await state.update_data(text=mess.text)
        await mess.answer('Отправте картинку', reply_markup=cancel_markup)
        await state.set_state(Fadmin.picture_admin)
    except Exception as e:
        await mess.answer('Что то пошло не так, начните заново')
        await state.clear()


@router.message(Fadmin.picture_admin)
async def get_picture_1(mess: Message, state: FSMContext):
    try:
        x = mess.photo[-1].file_id
    except Exception as e:
        await mess.answer('Нажмите на скрепку и прикрепите фото для объявления', reply_markup=cancel_markup)
        await state.set_state(Fadmin.picture_admin)
    await state.update_data(picture_admin=mess.photo[-1].file_id)
    data = await state.get_data()
    await mess.answer_photo(photo=data['picture_admin'], caption=data['text'])
    await mess.answer(f'Проверьте правильность объявления и укажите на сколько дней делаем рассылку',
                      reply_markup=subs_day_markup)
    await state.set_state(Fadmin.subs_day)



@router.callback_query(Fadmin.subs_day)
async def get_subs_day(call: CallbackQuery, state: FSMContext):
    await state.update_data(subs_day=call.data)
    await call.message.answer('нажмите отправить если клиент оплатил и вы готовы начать рассылку', reply_markup=send_canc_markup_admin)
    await state.set_state(Fadmin.sender_admin)



@router.callback_query(Fadmin.sender_admin)
async def go_one(call: CallbackQuery, state: FSMContext):
    x = random.randint(1, 10000000000)
    try:
        if call.data == 'send_1':
            data = await state.get_data()
            username = call.from_user.username
            photo = data['picture_admin']
            text = data['text']
            subs_days= int(data['subs_day'])
            chat_id = call.message.chat.id
            add_data(username, text, photo, 'no link', subs_days, x)
            conn.commit()
            await call.message.answer('Объявление опубликованно', reply_markup=admin_markup)
        else:
            await state.clear()
    except Exception as e:
        print(e)
        await call.message.answer('Внимательно заполните объявления следуя инструкциям. На '
                                  'место картинки нужно поместить графический файл', reply_markup=admin_markup)
        await state.clear()

# @router.message(Fsmone.check)
# async def get_check(mess: Message, state: FSMContext):

class Fadmin_2(StatesGroup):
    text = State()
    check = State()
    subs_day = State()
    sender_admin = State()


@router.callback_query(F.data == 'admin_non_media_pablic')
async def get_one_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Введите текст объявления', reply_markup=cancel_markup)
    await state.set_state(Fadmin_2.text)


@router.message(Fadmin_2.text)
async def get_text_1(mess: Message, state: FSMContext):
    try:
        await state.update_data(text=mess.text)
        await mess.answer('Проверьте правильность объявления и укажите кол-во дней', reply_markup=subs_day_markup)
        await state.set_state(Fadmin_2.subs_day)
    except Exception as e:
        await mess.answer('Что то пошло не так, начните заново', reply_markup=admin_markup)
        await state.clear()


@router.callback_query(Fadmin_2.subs_day)
async def get_subs_day(call: CallbackQuery, state: FSMContext):
    await state.update_data(subs_day=call.data)
    await call.message.answer('нажмите отправить если клиент оплатил и вы готовы начать рассылку',reply_markup=send_canc_markup_admin)
    await state.set_state(Fadmin_2.sender_admin)


@router.callback_query(Fadmin_2.sender_admin)
async def go_one(call: CallbackQuery, state: FSMContext):
    x = random.randint(1, 10000000000)
    try:
        if call.data == 'send_1':
            data = await state.get_data()
            username = call.from_user.username
            subs_day = int(data['subs_day'])
            text = data['text']
            chat_id = call.message.chat.id
            print(chat_id)
            print(text)
            print(username)
            print(0)
            add_data_two(username, text, subs_day, x)
            conn.commit()
            await call.message.answer('Объявление опубликованно', reply_markup=admin_markup)
        else:
            await state.clear()
    except Exception as e:
        print(e)
        await call.message.answer('Возможно вы уже создали ообъявление, либо проверьте правильность заполнения'
                                  'если вы хотите продлить подписку или изменить объявление зайдите в личный кабинет'
                                  'через кнопку Menu/Меню', reply_markup=admin_markup)
        await state.clear()