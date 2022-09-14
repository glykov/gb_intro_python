import logging
import asyncio
import pathlib
from aiogram import Bot, Dispatcher, types, executor
from configparser import ConfigParser
import sqlite3

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_DIR = pathlib.Path(__file__).parent
config = ConfigParser()
config.read(BOT_DIR / 'bot.conf', encoding='utf-8')

BOT_TOKEN = config.get('bot', 'TOKEN')
BOT_LINK = config.get('bot', 'LINK')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

con = sqlite3.connect(BOT_DIR / "phonebook.db")
cursor = con.cursor()


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.get_mention(as_html=True)} 👋!\nВведи /help, чтобы увидеть доступные команды",
        parse_mode=types.ParseMode.HTML,
    )


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.answer("Ты можешь сделать следующее:\n"
                         "/create Фамилия, Имя, телефон, описание - создать новый контакт\n"
                         "/read Фамилия или телефон - найти контакт\n"
                         "/udpate маркер : старое значение : новое значение - обновить контакт\n"
                         "маркер может принимать следующие значения: Ф - поменять фамилию\n"
                         "И - поменять имя, Т - поменять телефон, О - поменять описание\n"
                         "/delete Фамилия - удалить контакт")


@dp.message_handler(commands=['create'])
async def create_handler(message: types.Message):
    idx = message.text.index(" ")
    data = [s.strip() for s in message.text[idx:].split(',')]
    cursor.execute("insert into people(last_name, first_name, phone, description) values(?, ?, ?, ?)",
                   (data[0], data[1], data[2], data[3]))
    con.commit()
    msg = "Добавлено: " + ', '.join(data)
    await bot.send_message(message.from_user.id, msg)


@dp.message_handler(commands=['read'])
async def read_handler(message: types.Message):
    idx = message.text.index(" ")
    target = message.text[idx:].strip()
    result = tuple()
    if target[0].isdigit():
        result = cursor.execute(
            "select * from people where phone like :phone", {"phone": target})
    else:
        result = cursor.execute(
            "select * from people where last_name like :name", {"name": target})
    msg = ""
    for row in result:
        msg += ', '.join(row[1:])
    await bot.send_message(message.from_user.id, msg)


@dp.message_handler(commands=['update'])
async def update_handler(message: types.Message):
    msg = ""
    idx = message.text.index(" ")
    target = message.text[idx:].strip().split(':')
    if target[0].upper() == "Ф":
        cursor.execute(
            "update people set last_name=? where last_name=?", (target[2], target[1]))
    elif target[0].upper() == "И":
        cursor.execute(
            "update people set first_name=? where first_name=?", (target[2], target[1]))
    elif target[0].upper() == "Т":
        cursor.execute("update people set phone=? where phone=?",
                       (target[2], target[1]))
    elif target[0].upper() == "О":
        cursor.execute(
            "update people set description=? where description=?", (target[2], target[1]))
    else:
        msg = "Ошибка ввода данных"

    con.commit()

    if (not msg):
        msg = f"Произведена замена {target[1]} на {target[2]}"

    await bot.send_message(message.from_user.id, msg)


@dp.message_handler(commands=['delete'])
async def delete_handler(message: types.Message):
    idx = message.text.find(" ")
    lname = message.text[idx:]
    cursor.execute("delete from people where last_name=?", (lname,))
    await bot.send_message(message.from_user.id, f"Запись об {lname} была удалена")


@dp.message_handler()
async def main(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(dp)
