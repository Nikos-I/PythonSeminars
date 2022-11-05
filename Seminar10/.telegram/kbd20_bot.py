import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

TOKEN = '5632320403:AAHP0g8O1VtONC_h3kVmFQc57VMFpM79ahM'

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update, _):
    keyboard = [
        [
            InlineKeyboardButton("Привет", callback_data='1'),
            InlineKeyboardButton("Помощь", callback_data='2'),
        ],
        [InlineKeyboardButton("Высислить", callback_data='4')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Пожалуйста, выберите:', reply_markup=reply_markup)


async def button(update, _):
    query = update.callback_query
    variant = query.data

    # `CallbackQueries` требует ответа, даже если 
    # уведомление для пользователя не требуется, в противном
    #  случае у некоторых клиентов могут возникнуть проблемы. 
    # смотри https://core.telegram.org/bots/api#callbackquery.
    await query.answer()
    await query.edit_message_text(text=f"Выбранный вариант: {variant}")

async def help_command(update, _):
    await update.message.reply_text("Используйте `/start` для тестирования.")


if __name__ == '__main__':
    # приложение через `Application.builder()`
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(CommandHandler('help', help_command))

    # Запуск бота в версии 20.x 
    # start('','')
    app.run_polling()