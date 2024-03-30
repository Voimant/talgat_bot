from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



main_menu = [
    [InlineKeyboardButton(text='Подписки', callback_data='podpiski')],
    [InlineKeyboardButton(text='Наши группы', callback_data='groups')]
]

main_menu_markup = InlineKeyboardMarkup(inline_keyboard=main_menu)

groups_button = [
    [InlineKeyboardButton(text='ОБЩЕПИТ МОСКВА', url='https://t.me/moskvaopshepit')],
    [InlineKeyboardButton(text='РАБОТА МОСКВА', url='https://t.me/Rabotamoskva_work')],
    [InlineKeyboardButton(text='МОСКВА ОФИЦИАНТЫ', url='https://t.me/moskva_zherdesh')],
    [InlineKeyboardButton(text='БАР, ХОСТЕС, КАЛЬЯН', url='https://t.me/moskva_mekendew')],
    [InlineKeyboardButton(text='ОБЩЕПИТ', url='https://t.me/ObshepitMSK')],
    [InlineKeyboardButton(text='НАЗАД', callback_data='cancel')]
]

group_markup = InlineKeyboardMarkup(inline_keyboard=groups_button)

subs_form = [[InlineKeyboardButton(text='Опубликовать объявление c картинкой', callback_data='post_pablic_with_photo')],
            [InlineKeyboardButton(text='Опубликовать объявление без картинки', callback_data='post_pablic')],
             [InlineKeyboardButton(text='Информация о публикациях', callback_data='pablic_info')]]
subs_form_markup = InlineKeyboardMarkup(inline_keyboard=subs_form)


podpiski_button = [
    [InlineKeyboardButton(text='1 день ( за сутки обновляется 4-5 раза) 300 RUB', callback_data='pay_300')],
    [InlineKeyboardButton(text='7 дней ( за сутки обновляется 4-5 раза) 2000 RUB', callback_data='pay_2000')],
    [InlineKeyboardButton(text='30 дней ( за сутки обновляется 4-5 раза) 8000 RUB', callback_data='pay_8000')],
    [InlineKeyboardButton(text='Назад', callback_data='cancel')]
]

podpiaki_markup = InlineKeyboardMarkup(inline_keyboard=podpiski_button)

cancel_button = [[InlineKeyboardButton(text="Отмена", callback_data='cancel')]]
cancel_markup = InlineKeyboardMarkup(inline_keyboard=cancel_button)



send_canc_button = [
    [InlineKeyboardButton(text="Начать рассылку", callback_data='send')],
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]
]
send_canc_markup = InlineKeyboardMarkup(inline_keyboard=send_canc_button)
