from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from DB.main_db import add_group_id

router = Router()


@router.message(F.text)
async def get_new_group(mess: Message):
    group_id = mess.chat.id
    add_group_id(group_id)
    print(group_id)
