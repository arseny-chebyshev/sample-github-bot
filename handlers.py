from aiogram import types
from loader import dp


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.reply('Start')


@dp.message_handler(commands=['end'])
async def echo(message: types.Message):
    await message.reply('end')


@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
    await message.reply('Вы обратились к справке бота')
