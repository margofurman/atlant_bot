from aiogram import Bot, Dispatcher, types, executor
from config import bot_token, help_commands, info_text, atlant_text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(bot_token)
dp = Dispatcher(bot)

keyboard_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_start.add(KeyboardButton('/start')).add(KeyboardButton('/commands')).add(KeyboardButton('/coaches'))   #coaches

keyboard_info = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_info.row(KeyboardButton('/contacts'), KeyboardButton('/atlant')).row(KeyboardButton('/location'))#, KeyboardButton('/back'))      #news, contacts

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    username = message.from_user.full_name
    answ1 = f'Здравствуйте, {username}!\nЭто чат-бот детского спортивного клуба "Атлант" в Петергофе. Вы можете узнать все доступные команды в меню соощений или через команду /commands.'
    await message.answer(answ1, reply_markup=keyboard_start)
    await message.delete()

@dp.message_handler(commands=['location'])
async def loc_command(message: types.Message):
    await message.answer_location(latitude=59.870235, longitude=29.846928)
    await message.answer('Мы находимся по адресу: Старый Петергоф, ул. Чичеринская, дом 2. Вход со стороны Гостилицкого шоссе, на цокольном этаже за подписью Amakids')

@dp.message_handler(commands=['commands'])
async def help_command(message: types.Message):
    await message.answer(text=help_commands, parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['info'])
async def help_command(message: types.Message):
    await message.answer(text=info_text, parse_mode='HTML', reply_markup=keyboard_info)
    await message.delete()


@dp.message_handler(commands=['atlant'])
async def help_command(message: types.Message):
    await message.answer(text=atlant_text, parse_mode='HTML', reply_markup=keyboard_info)
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)