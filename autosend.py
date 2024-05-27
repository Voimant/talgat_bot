import asyncio
import logging
import os

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile, BufferedInputFile
import aiocron
from aiogram import Bot, Dispatcher
import time
import datetime
from aiogram.exceptions import TelegramForbiddenError, TelegramBadRequest, TelegramRetryAfter

from count_day import get_day
from db_func import conn
from main_db import list_chat_id, data_output_subs, list_username, update_subscription_days, list_group_id
from config import TOKEN

bot = Bot(token=TOKEN)


async def autos():
    while True:
        posts = data_output_subs()
        for post in posts:
            text = (f"{post['text']}\n"
                    f"<post_id : {post['chat_id']}>")
            picture = post['media']
            link = post['link']
            days = post['subscription_days']
            print(days)
            if days > 0:
                for group_id in list_group_id():
                    if post['type_file'] == 'photo':
                        if int(group_id) < 0:
                            try:
                                await bot.send_photo(group_id, photo=picture, caption=text)
                            except (TelegramForbiddenError, TelegramBadRequest):
                                pass
                            except TelegramRetryAfter as e:
                                await bot.send_message(423947942, str(e))
                        else:
                            pass
                    elif post['type_file'] == 'text':
                        if int(group_id) < 0:
                            try:
                                await bot.send_message(group_id, text)
                            except (TelegramForbiddenError, TelegramBadRequest):
                                pass
                            except TelegramRetryAfter as e:
                                await bot.send_message(423947942, f'{str(e)}  {group_id}')
                                os.system('systemctl stop autosend2.service')
                        else:
                            pass
                    elif post['type_file'] == 'video':
                        if int(group_id) < 0:
                            try:
                                await bot.send_video(group_id, video=picture, caption=text)
                            except (TelegramForbiddenError, TelegramBadRequest):
                                pass
                            except TelegramRetryAfter as e:
                                await bot.send_message(423947942, f'{str(e)}  {group_id}')
                                logging.info(f'Это пиздец товарищи: {e}')
                                os.system('systemctl stop autosend2.service')

                time.sleep(350)  # Интервал между объявлениями
            else:
                pass
        time.sleep(18000)  # рассылка объявления раз в 5 часов
        pass


async def main1():
    await autos()


if __name__ == "__main__":
    asyncio.run(main1())
