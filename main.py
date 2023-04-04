from aiogram import Bot, Dispatcher, types, executor
from config import bot_token, help_commands, coaches
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


bot = Bot(bot_token)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Bot was lunched successfully')


@dp.message_handler(commands=['start', 'начать'])   #старт
async def start_command(message: types.Message):
    username = message.from_user.full_name
    answ1 = f'Здравствуйте, {username}!\n Это чат-бот детского спортивного клуба "Атлант" в Петергофе. Вы можете узнать все доступные команды в меню соощений или через команду \help.'
    await message.answer(answ1)
    await message.delete()

@dp.message_handler(commands=['location', 'местоположение', 'адрес', 'место', 'расположение'])
async def loc_command(message: types.Message):
    await message.answer_location(latitude=59.870235, longitude=29.846928)
    await message.answer('Мы находимся по адресу: Старый Петергоф, ул. Чичеринская, дом 2. Вход со стороны Гостилицкого шоссе, на цокольном этаже за подписью Amakids')

@dp.message_handler(commands=['help', 'команды'])   #help
async def help_command(message: types.Message):
    await message.answer(text=help_commands, parse_mode='HTML')
    await message.delete()

#список тренеров
# @dp.message_handler(commands=['coaches', 'тренеры'])
# async def help_command(message: types.Message):
#     await message.answer(text=coaches, parse_mode='HTML')
#     await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

