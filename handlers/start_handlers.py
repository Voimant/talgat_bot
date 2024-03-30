from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from DB.main_db import add_user
from keyboards.keyboards import main_menu_markup
from aiogram.types import FSInputFile
from DB.db_func import conn

router = Router()
router.message.filter(
    F.chat.type == "private"
)

# @router.message(Command('start'))
# async def cmd_start(mess: Message):
#     chat_id = mess.chat.id
#     user_name = mess.from_user.username
#     print(chat_id)
#     print(user_name)
#     try:
#         add_user(user_name, chat_id)
#         conn.commit()
#         photo = FSInputFile('source/media/chippi.jpg')
#         await mess.answer_photo(photo=photo, caption=f"Вас приветствует бот Чиппи для рассылки объявлений\n"
#                                                      f"Для перехода в личный кабинет и других функций\n"
#                                                      f"нажмите кнопку МЕНЮ",
#                                 reply_markup=main_menu_markup)
#     except Exception as e:
#         photo = FSInputFile('source/media/chippi.jpg')
#         await mess.answer_photo(photo=photo, caption=f"Вас приветствует бот Чиппи для рассылки объявлений\n"
#                                                      f"Для перехода в личный кабинет и других функций\n"
#                                                      f"нажмите кнопку МЕНЮ",
#                                 reply_markup=main_menu_markup)


@router.message(Command('start'))
async def cmd_start(mess: Message):
    chat_id = mess.chat.id
    user_name = mess.from_user.username
    print(chat_id)
    print(user_name)
    if user_name is None:
        await mess.answer('Извините, что то пошло не так, скорее всего у вас нет username или он скрыт,  добавьте его и напишите /start')
    else:
        add_user(user_name, chat_id)
        conn.commit()
        photo = FSInputFile('source/media/chippi.jpg')
        await mess.answer_photo(photo=photo, caption=f"Вас приветствует бот Чиппи для рассылки объявлений\n"
                                                         f"Для перехода в личный кабинет и других функций\n"
                                                         f"нажмите кнопку МЕНЮ",
                                    reply_markup=main_menu_markup)
    # except Exception as e:
    #     photo = FSInputFile('source/media/chippi.jpg')
    #     await mess.answer_photo(photo=photo, caption=f"Вас приветствует бот Чиппи для рассылки объявлений\n"
    #                                                  f"Для перехода в личный кабинет и других функций\n"
    #                                                  f"нажмите кнопку МЕНЮ",
    #                             reply_markup=main_menu_markup)


@router.message(F.text == 'ид')
async def my_id(mess: Message):
    my_idd = mess.chat.id
    print(my_idd)