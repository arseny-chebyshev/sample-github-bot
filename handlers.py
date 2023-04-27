from aiogram import types
from loader import dp


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Start')


@dp.message_handler(commands=['end'])
async def end(message: types.Message):
    await message.reply('end')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply('Вы обратились к справке бота')


@dp.message_handler(commands=['dice'])
async def dice(message: types.Message):
    await message.answer_dice(emoji="🎰")
