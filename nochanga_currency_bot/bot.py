# coding: utf-8

import logging
import requests

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType, KeyboardButton, \
    ReplyKeyboardMarkup, InlineKeyboardMarkup

from data.config import settings


# logging
logging.basicConfig(level=logging.INFO)

# initializate bot
bot = Bot(token=settings["token"])
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=["start"])
async def start(message: types.Message):
    currency_button = KeyboardButton("Курс валют 💸")

    panel = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    ).add(currency_button)

    await message.answer("Выберите одно из действий 🎛", reply_markup=panel)

@dispatcher.message_handler(content_types=[ContentType.TEXT])
async def catch_text_messages(message: types.Message):
    if message == "Курс валют 💸":
        # dollar
        dollar_button = KeyboardButton(
            "Доллар 💵",
            callback_query="dollar_cource"
        )

        # euro
        euro_button = KeyboardButton(
            "Евро 💶",
            callback_query="euro_cource"
        )

        # all cources
        dollar_euro_button = KeyboardButton(
            "Все вместе 💰",
            callback_query="dollar_euro_cource"
        )

        # currency keyboard
        currency_panel = InlineKeyboardMarkup(
            resize_keyboard=True,
        ).add(dollar_button, euro_button).add(dollar_euro_button)



@dispatcher.callback_query_handler(lambda callback_query: True)
async def cath_buttons(callback_query: types.CallbackQuery):
    try:
        if callback_query.data == "dollar_cource":
            pass
        elif callback_query.data == "euro_cource":
            pass
        else:
            pass
    except Exception as error:
        print(repr(error))


if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)