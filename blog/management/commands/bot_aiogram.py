from django.core.management.base import BaseCommand
from django.conf import settings
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, Dispatcher, types

logging.basicConfig(level=logging.INFO)

# Объявление переменной бота
bot = Bot(token=settings.TELEGRAM_BOT_API_KEY)
dp = Dispatcher(bot)

# Название класса обязательно - "Command"
class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'Бот ГБУ СО "ОЭП" для ведения технической поддержки пользователей'
    @dp.message(commands=["start"])
    async def cmd_start(message: types.Message):
        await message.answer("Hello!")


    dp.start_polling(bot)
    


