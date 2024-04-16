import os

from aiogram import Router, Bot, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, CallbackQuery

from DB.main_db import data_day_subs, db_del_post
from config import TOKEN
from keyboards.keyboards_lk import lk_main_markup
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup

router = Router()
bot = Bot(token=TOKEN)
router.message.filter(
    F.chat.type == "private"
)


@router.message(Command('lk'))
async def get_lk(mess: Message):
    await mess.answer('Личный кабиент', reply_markup=lk_main_markup)


@router.message(Command('del'))
async def get_del_post(mess: Message, command: CommandObject):
    if mess.from_user.id in [5805441535, 423947942]:
        try:
            result = int(command.args)
            db_del_post(result)
        except Exception as e:
            await mess.answer('что то пошло не так, обратитесь к Олегу...')
    else:
        await mess.answer('Команда /del, может использовать только администратор')


@router.callback_query(F.data == 'days_subs')
async def my_balans(call: CallbackQuery):
    days = data_day_subs(call.from_user.username)
    await call.message.answer(str(days))


@router.message(Command('restart'))
async def c_restart(mess:Message, state: FSMContext):
    if mess.from_user.id in [5805441535, 423947942]:
        os.system('systemctl restart bot.service')
    else:
        await mess.answer('Вы не являетесь Администратором')


@router.message(Command('stop'))
async def c_restart(mess:Message, state: FSMContext):
    if mess.from_user.id in [5805441535, 423947942]:
        os.system('systemctl stop autosend2.service')
        await mess.answer('бот перезапущен')
    else:
        await mess.answer('Вы не являетесь Администратором')
