from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



admin_button = [
    [InlineKeyboardButton(text='Отправить объявление в группы', callback_data='admin_send')],
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]
]
admin_markup = InlineKeyboardMarkup(inline_keyboard=admin_button)


subs_form_2 = [[InlineKeyboardButton(text='Опубликовать объявление c картинкой', callback_data='admin_with_photo')],
            [InlineKeyboardButton(text='Опубликовать объявление без картинки', callback_data='admin_non_media_pablic')],
             [InlineKeyboardButton(text='Информация о публикациях', callback_data='pablic_info')],
        [InlineKeyboardButton(text='Опубликовать объявление c видео', callback_data='admin_with_video')],
]

subs_form_markup_2 = InlineKeyboardMarkup(inline_keyboard=subs_form_2)


subs_day_button = [
    [InlineKeyboardButton(text='1', callback_data='1')],
    [InlineKeyboardButton(text='7', callback_data='7')],
    [InlineKeyboardButton(text='14', callback_data='14')],
    [InlineKeyboardButton(text='30', callback_data='30')],
]
subs_day_markup = InlineKeyboardMarkup(inline_keyboard=subs_day_button)

send_canc_button_admin = [
    [InlineKeyboardButton(text="Начать рассылку", callback_data='send_1')],
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]
]
send_canc_markup_admin = InlineKeyboardMarkup(inline_keyboard=send_canc_button_admin)
