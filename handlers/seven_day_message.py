from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup

from DB.db_func import conn
from DB.main_db import add_data
from config import TOKEN
from keyboards.keyboards import cancel_markup, send_canc_markup, main_menu_markup
from keyboards.keyboards_lk import lk_main_markup

router = Router()
bot = Bot(token=TOKEN)


class Fsm_7(StatesGroup):
    text = State()
    picture = State()
    check = State()
    go_one = State()


@router.callback_query(F.data == '7_day')
async def get_one_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Введите текст объявления', reply_markup=cancel_markup)
    await state.set_state(Fsm_7.text)


@router.message(Fsm_7.text)
async def get_text_1(mess: Message, state: FSMContext):
    try:
        await state.update_data(text=mess.text)
        await mess.answer('Прикрепите картинку к вашему объявлению', reply_markup=cancel_markup)
        await state.set_state(Fsm_7.picture)
    except Exception as e:
        await mess.answer('Что то пошло не так, начните заново')
        await state.clear()


@router.message(Fsm_7.picture)
async def get_picture_1(mess: Message, state: FSMContext):
    try:
        x = mess.photo[-1].file_id
    except Exception as e:
        await mess.answer('Нажмите на скрепку и прикрепите фото для объявления', reply_markup=cancel_markup)
        await state.set_state(Fsm_7.picture)
    await state.update_data(picture=mess.photo[-1].file_id)
    await mess.answer(f'Проверьте правильность объявления и нажмите начать рассылку',
                      reply_markup=cancel_markup)
    # await state.set_state(Fsmone.check)
    data = await state.get_data()
    await mess.answer_photo(photo=data['picture'], caption=data['text'], reply_markup=send_canc_markup)
    await state.set_state(Fsm_7.go_one)


@router.callback_query(Fsm_7.go_one)
async def go_one(call: CallbackQuery, state: FSMContext):
    try:
        if call.data == 'send':
            data = await state.get_data()
            username = call.from_user.username
            photo = data['picture']
            text = data['text']
            file_type = 'photo'
            add_data(username, text, photo, 'no link', 7, file_type)
            conn.commit()
            await call.message.answer('Объявление запущено')
        else:
            await state.clear()
    except Exception as e:
        print(e)
        await call.message.answer('Внимательно заполняйте анкету, на '
                                  'место картинки нужно поместить графический файл', reply_markup=main_menu_markup)
        await state.clear()