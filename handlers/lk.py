from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from DB.main_db import data_day_subs
from config import TOKEN
from keyboards.keyboards_lk import lk_main_markup

router = Router()
bot = Bot(token=TOKEN)
router.message.filter(
    F.chat.type == "private"
)

@router.message(Command('lk'))
async def get_lk(mess: Message):
    await mess.answer('Личный кабиент', reply_markup=lk_main_markup)


@router.callback_query(F.data == 'days_subs')
async def my_balans(call: CallbackQuery):
    days = data_day_subs(call.from_user.username)
    await call.message.answer(str(days))