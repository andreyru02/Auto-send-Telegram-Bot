from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputFile
import glob
import config
import os
from time import sleep

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

user = config.USER_ID
channel = config.CHANNEL


@dp.message_handler(commands=['start'])
async def start_spam(message: types.Message):
    if message.from_user.id == int(user):
        await bot.send_message(str(user), 'Бот запущен!')
        count = 0
        files = os.listdir(f'{os.getcwd()}/content')

        for file in files:
            send_file = InputFile(glob.glob(f'{os.getcwd()}/content/{file}')[0])
            await bot.send_photo(channel, send_file)
            count += 1
            await bot.send_message(str(user), f'Пост отправлен.\n'
                                              f'{count} из {len(files)}.\n'
                                              f'Пауза на {config.WAIT} секунд.')
            sleep(int(config.WAIT))


if __name__ == '__main__':
    executor.start_polling(dp)
