from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from config import TOKEN
from keyboards.keyboards import main_menu_markup, group_markup, podpiaki_markup, subs_form_markup
from aiogram.types import FSInputFile


router = Router()
router.message.filter(
    F.chat.type == "private"
)
bot = Bot(token=TOKEN)


@router.callback_query(F.data == 'groups')
async def get_groups(call: CallbackQuery):
    photo = FSInputFile('source/media/chippi.jpg')
    await call.message.answer_photo(photo=photo, caption="наши группы", reply_markup=group_markup)


@router.callback_query(F.data == 'cancel')
async def get_start(call: CallbackQuery, state: FSMContext):
    photo = FSInputFile('source/media/chippi.jpg')
    await call.message.answer_photo(photo=photo, caption="Вас приветствует бот Чиппи для рассылки объявлений",
                            reply_markup=main_menu_markup)
    await state.clear()


@router.callback_query(F.data == 'podpiski')
async def get_podpiski(call: CallbackQuery):
    photo = FSInputFile('source/media/chippi.jpg')
    await call.message.answer_photo(photo=photo, caption="Оформите подписку и публикуйте объявления!",
                                    reply_markup=subs_form_markup)


@router.callback_query(F.data == 'pablic_info')
async def subs_info(call: CallbackQuery):
    photo = FSInputFile('source/media/chippi.jpg')
    text = (f'В чатах есть бот который публикует заданный текст и медиа 24/7 .\n' 
            f'Ваш пост публикуется 3-4 раза в течении дня.\n' 
            f'Посмотреть и подписаться на чаты связанные с общепитом можете  нажав на кнопку Наши Чаты\n'
            f'7 дней поста -2000\n'
            f'30 дней роста -8000')
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=main_menu_markup)