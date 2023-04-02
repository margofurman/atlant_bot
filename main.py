from aiogram import Bot, Dispatcher, types, executor
from config import bot_token


bot = Bot(bot_token)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text = message.text)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text = message.text)


if __name__ == '__main__':
    executor.start_polling(dp)

