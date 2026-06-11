from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import asyncio
import random
import requests
import logging

TOKEN = "8946750900:AAEzoiJOioKwsh2ozoQmqR4H7kZzeejVV1s"

# Логирование
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

bot = Bot(token=TOKEN)

storage = MemoryStorage()
dp = Dispatcher(storage=storage)


# Кнопки меню
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/start")],
        [KeyboardButton(text="/help")],
        [KeyboardButton(text="/random")],
        [KeyboardButton(text="/weather")],
        [KeyboardButton(text="/fact")]
    ],
    resize_keyboard=True
)


# FSM состояния
class NumberState(StatesGroup):
    waiting_for_number = State()


# Игра
secret_number = random.randint(1, 10)


# Команда /start
@dp.message(Command("start"))
async def start_command(message: Message):

    logging.info(f"Пользователь {message.from_user.id} нажал /start")

    await message.answer(
        "Привет! Я Telegram бот-помощник.",
        reply_markup=keyboard
    )


# Команда /help
@dp.message(Command("help"))
async def help_command(message: Message):

    logging.info(f"Пользователь {message.from_user.id} нажал /help")

    await message.answer(
        "Мои команды:\n"
        "/start - запуск\n"
        "/help - список команд\n"
        "/about - информация\n"
        "/random - случайное число\n"
        "/calc - калькулятор\n"
        "/number - FSM число\n"
        "/weather - погода\n"
        "/fact - случайный факт\n"
        "/game - игра"
    )


# Команда /about
@dp.message(Command("about"))
async def about_command(message: Message):

    logging.info(f"Пользователь {message.from_user.id} нажал /about")

    await message.answer(
        "Бот создан на Python и aiogram."
    )


# Команда /random
@dp.message(Command("random"))
async def random_command(message: Message):

    logging.info(f"Пользователь {message.from_user.id} нажал /random")

    number = random.randint(1, 100)

    await message.answer(f"Случайное число: {number}")


# Команда /calc
@dp.message(Command("calc"))
async def calc_command(message: Message):

    logging.info(f"Пользователь {message.from_user.id} нажал /calc")

    await message.answer(
        "Отправь пример:\n"
        "Например: 2+2"
    )


# FSM команда
@dp.message(Command("number"))
async def number_command(message: Message, state: FSMContext):

    logging.info(f"Пользователь {message.from_user.id} нажал /number")

    await message.answer("Введите число:")

    await state.set_state(NumberState.waiting_for_number)


# FSM обработка
@dp.message(NumberState.waiting_for_number)
async def process_number(message: Message, state: FSMContext):

    text = message.text

    if text.lstrip("-").isdigit():

        number = int(text)

        if number % 2 == 0:
            even = "четное"
        else:
            even = "нечетное"

        if number > 0:
            sign = "положительное"
        elif number < 0:
            sign = "отрицательное"
        else:
            sign = "ноль"

        await message.answer(
            f"Число {number}:\n"
            f"- {even}\n"
            f"- {sign}"
        )

    else:
        await message.answer("Это не число.")

    await state.clear()


# Команда /weather
@dp.message(Command("weather"))
async def weather_command(message: Message):

    logging.info(f"Пользователь {message.from_user.id} нажал /weather")

    url = "https://wttr.in/Astana?format=3"

    weather = requests.get(url).text

    await message.answer(weather)


# Команда /fact
@dp.message(Command("fact"))
async def fact_command(message: Message):

    logging.info(f"Пользователь {message.from_user.id} нажал /fact")

    facts = [
        "У осьминога три сердца.",
        "Самая высокая гора — Эверест.",
        "Python создан Гвидо ван Россумом.",
        "Telegram был создан Павлом Дуровым."
    ]

    fact = random.choice(facts)

    await message.answer(fact)


# Команда /game
@dp.message(Command("game"))
async def game_command(message: Message):

    logging.info(f"Пользователь {message.from_user.id} начал игру")

    await message.answer(
        "Я загадал число от 1 до 10.\n"
        "Попробуй угадать!"
    )


# Обработка текстовых сообщений
@dp.message()
async def message_handler(message: Message):

    global secret_number

    text = message.text.lower()

    # Приветствие
    if text == "привет":

        await message.answer("Привет! Как дела?")

    # Игра
    elif text.isdigit():

        user_number = int(text)

        if user_number == secret_number:

            await message.answer("Ты угадал число!")

            secret_number = random.randint(1, 10)

        else:

            await message.answer("Не угадал.")

    # Калькулятор
    elif "+" in text or "-" in text or "*" in text or "/" in text:

        try:

            result = eval(text)

            await message.answer(f"Результат: {result}")

        except:

            await message.answer("Ошибка в примере.")

    # Неизвестная команда
    else:

        await message.answer("Я пока не знаю такую команду.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())