from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram import types

def get_keyboard(buttons):
   
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


fq_menu = [
        [
            types.InlineKeyboardButton(text="Сан-Франциско", callback_data="san_fran"),
            types.InlineKeyboardButton(text="Вашингтон", callback_data="washington")
        ],
        [
            types.InlineKeyboardButton(text="Нью Йорк", callback_data="new_york"),
            types.InlineKeyboardButton(text="Санкт-Петербург", callback_data="spb")
        ],
]

sq_menu = [
        [
            types.InlineKeyboardButton(text="50", callback_data="50"),
            types.InlineKeyboardButton(text="49", callback_data="49")
        ],
        [
            types.InlineKeyboardButton(text="52", callback_data="52"),
            types.InlineKeyboardButton(text="6", callback_data="6")
        ],
]
fiq_menu = [
        [
            types.InlineKeyboardButton(text="Ford", callback_data="Ford"),
            types.InlineKeyboardButton(text="Nike", callback_data="Nike")
        ],
        [
            types.InlineKeyboardButton(text="Boeing", callback_data="Ford"),
            types.InlineKeyboardButton(text="Diesel", callback_data="Nike")
        ],
]
fou_menu = [
        [
            types.InlineKeyboardButton(text="9.8 млн км^2", callback_data="9.8"),
            types.InlineKeyboardButton(text="12.2 млн км^2", callback_data="12.2")
        ],
        [
            types.InlineKeyboardButton(text="4.9 млн км^2", callback_data="4.9"),
            types.InlineKeyboardButton(text="2.3 млн км^2", callback_data="2.3")
        ],
]

fifth_menu = [
        [
            types.InlineKeyboardButton(text="336 млн", callback_data="336"),
            types.InlineKeyboardButton(text="124 млн", callback_data="124")
        ],
        [
            types.InlineKeyboardButton(text="1000 млн", callback_data="1000"),
            types.InlineKeyboardButton(text="124 млн", callback_data="23.3")
        ],
]


start_btm = [
    [
        types.InlineKeyboardButton(text="К первому вопросу", callback_data="start_btm") #обратно в главное меню 
    ]
]


subback = [
    [
        types.InlineKeyboardButton(text="Subscribed", callback_data="subback") #обратно в главное меню 
    ]
] 