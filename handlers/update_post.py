from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup

from DB.db_func import conn
from DB.main_db import add_data, add_data_two, update_post_1, update_post_two
from config import TOKEN
from keyboards.keyboards import cancel_markup, send_canc_markup, main_menu_markup, podpiaki_markup
from keyboards.keyboards_lk import lk_main_markup, subs_form_markup_1

router = Router()
router.message.filter(
    F.chat.type == "private"
)
bot = Bot(token=TOKEN)


@router.callback_query(F.data == 'change_post')
async def update_post_new(call: CallbackQuery):
    await call.message.answer('Как изменить ваше объявление?', reply_markup=subs_form_markup_1)

class Fsmpostupdate(StatesGroup):
    text = State()
    picture = State()
    check = State()
    go_one = State()


@router.callback_query(F.data == 'update_with_photo')
async def get_one_message_1(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Введите текст объявления', reply_markup=cancel_markup)
    await state.set_state(Fsmpostupdate.text)


@router.message(Fsmpostupdate.text)
async def get_text_1(mess: Message, state: FSMContext):
    try:
        await state.update_data(text=mess.text)
        await mess.answer('Отправте картинку', reply_markup=cancel_markup)
        await state.set_state(Fsmpostupdate.picture)
    except Exception as e:
        await mess.answer('Что то пошло не так, начните заново')
        await state.clear()


@router.message(Fsmpostupdate.picture)
async def get_picture_1(mess: Message, state: FSMContext):
    try:
        x = mess.photo[-1].file_id
    except Exception as e:
        await mess.answer('Нажмите на скрепку и прикрепите фото для объявления', reply_markup=cancel_markup)
        await state.set_state(Fsmpostupdate.picture)
    await state.update_data(picture=mess.photo[-1].file_id)
    await mess.answer(f'Проверьте правильность объявления и нажмите начать рассылку',
                      reply_markup=cancel_markup)
    # await state.set_state(Fsmone.check)
    data = await state.get_data()
    await mess.answer_photo(photo=data['picture'], caption=data['text'], reply_markup=send_canc_markup)
    await state.set_state(Fsmpostupdate.go_one)


@router.callback_query(Fsmpostupdate.go_one)
async def go_one(call: CallbackQuery, state: FSMContext):
    try:
        if call.data == 'send':
            data = await state.get_data()
            username = call.from_user.username
            chat_id = call.message.chat.id
            photo = data['picture']
            text = data['text']
            update_post_1(username, text, photo, 'no link', chat_id)
            conn.commit()
            await call.message.answer('Объявление изменено и запущено', reply_markup=main_menu_markup)
        else:
            await state.clear()
    except Exception as e:
        print(e)
        await call.message.answer('Внимательно заполните объявления следуя инструкциям. На '
                                  'место картинки нужно поместить графический файл', reply_markup=main_menu_markup)
        await state.clear()


# @router.message(Fsmone.check)
# async def get_check(mess: Message, state: FSMContext):

class Fsmupdatetwo(StatesGroup):
    text = State()
    check = State()
    go_one = State()


@router.callback_query(F.data == 'update_non_media_pablic')
async def get_one_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Введите текст объявления', reply_markup=cancel_markup)
    await state.set_state(Fsmupdatetwo.text)


@router.message(Fsmupdatetwo.text)
async def get_text_1(mess: Message, state: FSMContext):
    try:
        await state.update_data(text=mess.text)
        await mess.answer('Проверьте правильность объявления', reply_markup=send_canc_markup)
        await state.set_state(Fsmupdatetwo.go_one)
    except Exception as e:
        await mess.answer('Что то пошло не так, начните заново')
        await state.clear()


@router.callback_query(Fsmupdatetwo.go_one)
async def go_on(call: CallbackQuery, state: FSMContext):
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
            update_post_two(username, text, chat_id, media='0')
            conn.commit()
            await call.message.answer('Объявление изменено и запущено',
                                      reply_markup=main_menu_markup)
        else:
            await state.clear()
    except Exception as e:
        print(e)
        await call.message.answer('Возможно вы уже создали ообъявление, либо проверьте правильность заполнения'
                                  'если вы хотите продлить подписку или изменить объявление зайдите в личный кабинет'
                                  'через кнопку Menu/Меню', reply_markup=main_menu_markup)
        await state.clear()
