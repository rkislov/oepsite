from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot
from telebot import types

# Объявление переменной бота
bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)


# Название класса обязательно - "Command"
class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'Бот ГБУ СО "ОЭП" для ведения технической поддержки пользователей'
    def handle(self, *args, **kwargs):
        @bot.message_handler(commands=['start'])
        def start(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.InlineKeyboardButton("Проверить статус заявки",)
            markup.add(button1)
            bot.send_message(message.chat.id, "Привет, {0.first_name}! Введите номер заявки)".format(message.from_user), reply_markup=markup)
        @bot.message_handler(commands=['help'])
        def help(message):
            bot.reply_to(message, """\
            Привет, меня я бот ГБУ СО "ОЭП"\
            я умею уведомлять о всех технических работах, а так же проверять статус ваших заявок в системе технической поддержки\
            """)
        def send_welcome(message):
            bot.reply_to(message, """\
            Привет, я бот ГБУ СО "ОЭП" я умею уведомлять о всех технических работах, а также проверять статус ваших заявок в системе технической поддержки\
            """)

        # @bot.message_handler(content_types=['text'])
        # def func(message):
        #     if(message.text == "Проверить статус заявки"):

# https://sd.egov66.ru/get_status.php?IncidentNumber=221235011

        # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
        @bot.message_handler(func=lambda message: True)
        def echo_message(message):
            bot.reply_to(message, message.text)


        bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        bot.load_next_step_handlers()								# Загрузка обработчиков
        bot.infinity_polling()
    


