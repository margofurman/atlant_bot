from aiogram import Bot, Dispatcher, types, executor
from config import bot_token

bot = Bot(bot_token)
dp = Dispatcher(bot)

help_commands='''/start - начать работу с ботом 
/help - вывести список всех команд
/coaches - вывести список тренеров и информацию о них
/news - подписаться на рассылку новостей из группы Вконтакте
/free_class - записаться на первое бесплатное занятие 
'''

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    username = message.from_user.full_name
    answ1 = f'Здравствуйте, {username}!\n'
    answ2 = 'Это чат-бот детского спортивного клуба "Атлант" в Петергофе. Вы можете узнать все доступные команды в меню соощений или через команду \help.'
    answ1 += answ2
    await message.answer(answ1)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=help_commands)
    await message.delete()



if __name__ == '__main__':
    executor.start_polling(dp)

