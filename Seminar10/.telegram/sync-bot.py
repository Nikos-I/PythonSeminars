import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
# импортируем обработчик `MessageHandler` и класс с фильтрами
from telegram.ext import *  # MessageHandler, filters


# настроим модуль ведения журнала логов
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# определяем асинхронную функцию


async def start(update, context):
    # ожидание отправки сообщения по сети - нужен `await`
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="I'm a bot, please talk to me!")


async def echo(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def list(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Список сотрудников')
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def caps(update, context):
    # если аргументы присутствуют
    if context.args:
        # объединяем список в строку и
        # переводим ее в верхний регистр
        text_caps = ' '.join(context.args).upper()
        # `update.effective_chat.id` - определяем `id` чата,
        # откуда прилетело сообщение
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
    else:
        # если в команде не указан аргумент
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='No command argument')
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='send: /caps argument')

async def unknown(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="Извините, но эта команда неизвестна нашему боту.")

    

if __name__ == '__main__':
    TOKEN = '5632320403:AAHP0g8O1VtONC_h3kVmFQc57VMFpM79ahM'
    # создание экземпляра бота через `ApplicationBuilder`
    application = ApplicationBuilder().token(TOKEN).build()

    # создаем обработчик для команды '/start'
    start_handler = CommandHandler('start', start)
    # обработчик команды '/caps'
    caps_handler = CommandHandler('caps', caps)
    list_handler = CommandHandler('list', list)

    # говорим обработчику `MessageHandler`, если увидишь текстовое
    # сообщение (фильтр `Filters.text`)  и это будет не команда
    # (фильтр ~Filters.command), то вызови функцию `echo()`
    echo_handler = MessageHandler(filters.TEXT & (~(filters.COMMAND)), echo)
    
    # создаем обработчик для функции `unknown()`
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    
    # регистрируем обработчик для `start()`
    application.add_handler(start_handler)
    # регистрируем обработчик для `echo()`
    application.add_handler(echo_handler)
    # регистрируем обработчик в диспетчере
    application.add_handler(caps_handler)
    application.add_handler(list_handler)
    # регистрируем обработчик
    application.add_handler(unknown_handler)
    
    # запускаем приложение
    application.run_polling()
