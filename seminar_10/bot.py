import logging
from pathlib import Path
from configparser import ConfigParser
from aiogram import executor, types, Bot, Dispatcher
from logic import run_calc

BASE_DIR = Path(__file__).parent

logging.basicConfig(
    filename=BASE_DIR / 'bot.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

config = ConfigParser()
config.read(BASE_DIR / 'bot.conf', encoding='utf-8')
TOKEN = config.get('bot', 'TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Привет!\nВведи выражение для вычисления')


@dp.message_handler(commands=['help'])
async def help_handler(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Чем тут можно помочь,\n'
                           'если ты не можешь ввести простое\n'
                           'арифметическое выражение?')


@dp.message_handler()
async def calc_handler(msg: types.Message):
    result = run_calc(msg.text)
    logging.info(f'calculated: {msg.text} = {result}')
    await bot.send_message(msg.from_user.id, f'Резульат вычислений = {result}')


if __name__ == "__main__":
    executor.start_polling(dp)