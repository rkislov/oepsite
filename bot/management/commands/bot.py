from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot, Update
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater, CommandHandler, CallbackQueryHandler
from telegram.utils.request import Request
from bot.models import Profile, Message
from subprocess import PIPE, Popen


def log_errors(f):

    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:

            error_message = f'Произошла ошибка: {e}'
            print(error_message)
            raise e
    return inner


@log_errors
def do_start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    p, _ = Profile.objects.get_or_create(
        external_id = chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    reply_text = "Добро пожаловать в телеграм бот \nГБУ СО ОЭП \nдля более пожробного знакомства воспользуйтесь командой /help"
    update.message.reply_text(
        reply_text
    )
@log_errors
def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text

    p, _ = Profile.objects.get_or_create(
        external_id = chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
   
    reply_text = "Ваш ID = {}\n\n{}".format(chat_id, text)
    update.message.reply_text(
        reply_text
    )
    Message(
        profile=p,
        text=text
    ).save()


@log_errors
def do_count(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id = chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )

    count = Message.objects.filter(profile=p).count()

    update.message.reply_text(
        text=f'У вас {count} сообщений'
    )

@log_errors
def do_help(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id = chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
   
    reply_text = "данный бот поддерживает несколько команд \nСписок доступных команд есть в меню"
    update.message.reply_text(
        reply_text
    )

@log_errors
def do_time(update: Update, context: CallbackContext):
    """Узнать время на сервере"""

    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id = chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )

    process = Popen("date", stdout=PIPE)
    text, error = process.communicate()
    if error:
        text = "Произошла ошибка, время не доступно"
    else:
        text = text.decode("utf-8")

    reply_text = text
    update.message.reply_text(
        reply_text
    )

class Command(BaseCommand):
    help = "Телеграм-бот"

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
            con_pool_size=10
        )
        bot = Bot(
            request=request,
            token=settings.TELEGRAM_BOT_API_KEY
        )
        print(bot.get_me())

        updater = Updater(
            bot=bot,
            use_context=True
        )

        message_hadler = MessageHandler(Filters.text, do_echo)
        help_handler = CommandHandler("help", do_help)
        time_handler = CommandHandler("time", do_time)
        start_handler = CommandHandler("start", do_start) 

        message_hadler2 = CommandHandler("count", do_count)

        updater.dispatcher.add_handler(start_handler)
        updater.dispatcher.add_handler(time_handler)
        updater.dispatcher.add_handler(help_handler)
        updater.dispatcher.add_handler(message_hadler2)
        updater.dispatcher.add_handler(message_hadler)

        updater.start_polling()
        updater.idle()