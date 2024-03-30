from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


lk_main = [
    [InlineKeyboardButton(text='Изменить объявление', callback_data='change_post')],
    [InlineKeyboardButton(text='Продлить подписку на 1 день(300р)', callback_data='pay_300')],
    [InlineKeyboardButton(text='Продлить подписку на 7 дней(2000р)', callback_data='pay_2000')],
    [InlineKeyboardButton(text='Продлить подписку  на 30 дней(8000р)', callback_data='pay_8000')],
    [InlineKeyboardButton(text='Вернуться в главное меню', callback_data='cancel')],
    [InlineKeyboardButton(text='Сколько осталось дней подписки', callback_data='days_subs')]

]
lk_main_markup = InlineKeyboardMarkup(inline_keyboard=lk_main)

subs_form_1 = [[InlineKeyboardButton(text='Опубликовать объявление c картинкой', callback_data='update_with_photo')],
            [InlineKeyboardButton(text='Опубликовать объявление без картинки', callback_data='update_non_media_pablic')],
             [InlineKeyboardButton(text='Информация о публикациях', callback_data='pablic_info')],
]

subs_form_markup_1 = InlineKeyboardMarkup(inline_keyboard=subs_form_1)