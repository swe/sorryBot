#!venv/bin/python
import logging
import asyncio
import aiogram.utils.markdown as fmt
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from ru_excuses import getRandomExcuse

bot = Bot(token="5110024379:AAHpD7BcLrb3MNNtcCPlQxZ0XDhwKZsY1Ko")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")

async def cmd_start(message: types.Message):
    await message.answer("👋🏻")
    await asyncio.sleep(1.0)
    await message.answer("Добро пожаловать!")
    await asyncio.sleep(0.5)
    await message.answer("Это — портативный генератор отмазок, позволяющий быстро придумать причину, по которой так или иначе не получилось закончить дела вовремя.")
    await asyncio.sleep(0.5)
    await message.answer("Для начала просто введите имя человека, от которого нужна отмазка:")

@dp.message_handler()
async def any_text_message1(message: types.Message):
    excuseTextFore = f'{fmt.quote_html(message.text)}{getRandomExcuse()}'
    excuseText = excuseTextFore
    
    await message.answer(f'Генерируем отмазку...')
    await asyncio.sleep(1)
    await message.answer(excuseText)

# async def cmd_start(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(*[types.KeyboardButton(word_but) for word_but in ['🇬🇧 English', '🇷🇺 Русский']])
#     await message.answer("👋🏻")
#     await asyncio.sleep(1.0)
#     await message.answer("Please, choose language you prefer:", reply_markup=keyboard)

# @dp.message_handler(Text(equals="🇬🇧 English"))
# async def with_puree(message: types.Message):
#     await message.answe("Great! Nice to meet you!")

# @dp.message_handler(Text(equals="🇷🇺 Русский"))
# async def with_puree(message: types.Message):
#     await message.answer("Отлично! Добро пожаловать!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)