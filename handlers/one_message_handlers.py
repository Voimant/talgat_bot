from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup

from DB.db_func import conn
from DB.main_db import add_data, add_data_two
from config import TOKEN
from keyboards.keyboards import cancel_markup, send_canc_markup, main_menu_markup, podpiaki_markup
from keyboards.keyboards_lk import lk_main_markup

router = Router()
router.message.filter(
    F.chat.type == "private"
)
bot = Bot(token=TOKEN)





class Fsmone(StatesGroup):
    text = State()
    picture = State()
    check = State()
    go_one = State()


@router.callback_query(F.data == 'post_pablic_with_photo')
async def get_one_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Введите текст объявления', reply_markup=cancel_markup)
    await state.set_state(Fsmone.text)


@router.message(Fsmone.text)
async def get_text_1(mess: Message, state: FSMContext):
    try:
        await state.update_data(text=mess.text)
        await mess.answer('Отправте картинку', reply_markup=cancel_markup)
        await state.set_state(Fsmone.picture)
    except Exception as e:
        await mess.answer('Что то пошло не так, начните заново')
        await state.clear()


@router.message(Fsmone.picture)
async def get_picture_1(mess: Message, state: FSMContext):
    try:
        x = mess.photo[-1].file_id
    except Exception as e:
        await mess.answer('Нажмите на скрепку и прикрепите фото для объявления', reply_markup=cancel_markup)
        await state.set_state(Fsmone.picture)
    await state.update_data(picture=mess.photo[-1].file_id)
    await mess.answer(f'Проверьте правильность объявления и нажмите начать рассылку',
                      reply_markup=cancel_markup)
    # await state.set_state(Fsmone.check)
    data = await state.get_data()
    await mess.answer_photo(photo=data['picture'], caption=data['text'], reply_markup=send_canc_markup)
    await state.set_state(Fsmone.go_one)


@router.callback_query(Fsmone.go_one)
async def go_one(call: CallbackQuery, state: FSMContext):
    try:
        if call.data == 'send':
            data = await state.get_data()
            username = call.from_user.username
            photo = data['picture']
            text = data['text']
            chat_id = call.message.chat.id
            add_data(username, text, photo, 'no link', 0, chat_id)
            conn.commit()
            await call.message.answer('Объявление готово к старту,'
                                      ' на сколько дней хотите опубликовать объявление?', reply_markup=podpiaki_markup)
        else:
            await state.clear()
    except Exception as e:
        await call.message.answer('Внимательно заполните объявления следуя инструкциям. На '
                                  'место картинки нужно поместить графический файл, либо'
                                  'если вы уже создавали объявление но не оплатили, зайдите в личный кабинет и сделайте изменить объявление'
                                  , reply_markup=main_menu_markup)
        await state.clear()

# @router.message(Fsmone.check)
# async def get_check(mess: Message, state: FSMContext):

class Fsmtwo(StatesGroup):
    text = State()
    check = State()
    go_one = State()


@router.callback_query(F.data == 'post_pablic')
async def get_one_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Введите текст объявления', reply_markup=cancel_markup)
    await state.set_state(Fsmtwo.text)


@router.message(Fsmtwo.text)
async def get_text_1(mess: Message, state: FSMContext):
    try:
        await state.update_data(text=mess.text)
        await mess.answer('Проверьте правильность объявления', reply_markup=send_canc_markup)
        await state.set_state(Fsmtwo.go_one)
    except Exception as e:
        await mess.answer('Что то пошло не так, начните заново')
        await state.clear()


@router.callback_query(Fsmtwo.go_one)
async def go_one(call: CallbackQuery, state: FSMContext):
    try:
        if call.data == 'send':
            data = await state.get_data()
            username = call.from_user.username
            text = data['text']
            chat_id = call.message.chat.id
            print(chat_id)
            print(text)
            print(username)
            print(0)
            add_data_two(username, text, 0, chat_id)
            conn.commit()
            await call.message.answer('Объявление готово к старту,'
                                          ' на сколько дней хотите опубликовать объявление?', reply_markup=podpiaki_markup)
        else:
            await state.clear()
    except Exception as e:
        print(e)
        await call.message.answer('Возможно вы уже создали ообъявление, либо проверьте правильность заполнения'
                                  'если вы хотите продлить подписку или изменить объявление зайдите в личный кабинет'
                                  'через кнопку Menu/Меню', reply_markup=main_menu_markup)
        await state.clear()