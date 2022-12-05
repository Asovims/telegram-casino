import logging

import config

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F

TOKEN = config.token
dp = Dispatcher()

logger = logging.getLogger(__name__)


@dp.message(Command(commands=["start"]))
async def cmd_start(msg: types.Message):
    kb = [
        [types.KeyboardButton(text="🎲")]
    ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                         input_field_placeholder='Ожидаем вашего выбора')

    await msg.answer("<b>Добро пожаловать!\nВыберите нужное действие:</b>", reply_markup=keyboard)


@dp.message(F.content_type.in_({'dice'}))
async def cmd_luck(msg: types.Message):
    bot_dice = await msg.answer_dice(emoji='🎲')

    await msg.answer(f"Ваш результат: {msg.dice.value}\nРезультат бота: {bot_dice.dice.value}")

    if msg.dice.value > bot_dice.dice.value:
        await msg.answer("Вы выиграли бота.")

    elif msg.dice.value < bot_dice.dice.value:
        await msg.answer("Вы проиграли боту.")

    elif msg.dice.value == bot_dice.dice.value:
        await msg.answer("Ничья.")

    return


def main() -> None:
    bot = Bot(TOKEN, parse_mode='html')

    dp.run_polling(bot)


if __name__ == "__main__":
    main()
