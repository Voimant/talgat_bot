import asyncio
from aiogram import Bot, Dispatcher
import aiocron
from config import TOKEN
import logging
from handlers import start_handlers, main_handlers, pay, lk, one_message_handlers, seven_day_message, month_day_message, \
    update_post, admin, new_group


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(start_handlers.router, main_handlers.router, pay.router, lk.router,
                       one_message_handlers.router, seven_day_message.router, month_day_message.router,
                       update_post.router, admin.router,new_group.router)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
#ff

if __name__ == "__main__":
    asyncio.run(main())
