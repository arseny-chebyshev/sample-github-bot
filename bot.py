import logging
from aiogram import executor, types
from loader import dp
import handlers


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    executor.start_polling(dp, skip_updates=True)
