
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import *
import sympy


app = ApplicationBuilder().token("5632320403:AAHP0g8O1VtONC_h3kVmFQc57VMFpM79ahM").build()          #  введите сдесь свой токкен

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("formula", formula_command))

print('сервер запущен')
app.run_polling()

