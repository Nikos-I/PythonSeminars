from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters



async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    result = 0
    text = update.message.text  # Получили "12 + 15"
    text_1 = text.split()
    print(text_1)
    if len(text_1) != 3:
        return
    a = text_1[0]
    b = text_1[2]
    operator = text_1[1]
    if operator == '+':
        result = int(a) + int(b)
    elif operator == '-':
        result = int(a) - int(b)
    elif operator == '*':
        result = int(a) * int(b)
    elif operator == '/':
        result = int(a) / int(b)
    elif operator == '^':
        result = int(a) ** int(b)
    await update.message.re
От Карина Казаманова всем 12:50 PM
app = ApplicationBuilder().token("Ввести токен").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calc))
  # Прописать данную функцию


app.run_polling()
