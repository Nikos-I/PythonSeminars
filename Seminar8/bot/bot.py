from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5727450524:AAEvolPtaXrCtT_dzzUih0kgft_7IpfcSVY").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def remove_abc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    my_list = list(filter(lambda x: 'абв' not in x , msg.split()))
    await update.message.reply_text(' '.join(my_list))



# app = ApplicationBuilder().token("Напишите свой токен").build()

# app.add_handler(CommandHandler("hello", hello))
# app.add_handler(MessageHandler(filters.TEXT, remove_abc))

# app.run_polling()
# -
# свой токен").build()

# app.add_handler(CommandHandler("hello", hello))
# app.add_handler(MessageHandler(filters.TEXT, remove_abc))

# app.run_polling()

# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# async def remove_abc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     msg = update.message.text
#     my_list = list(filter(lambda x: 'абв' not in x , msg.split()))
#     await update.message.reply_text(' '.join(my_list))



# app = ApplicationBuilder().token("Напишите свой токен").build()

# app.add_handler(CommandHandler("hello", hello))
# app.add_handler(MessageHandler(filters.TEXT, remove_abc))

# app.run_polling()

from turtle import update
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, 
async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global candies
    msg = update.message.text
    candies -= int(msg)
    await update.message.reply_text(f'На столе {candies} конфет')
    if win_in_game():
        await update.message.reply_text(f'Выиграл {update.effective_user.first_name}')
        return
    await update.message.reply_text(f'Бот взял {bot_candy()} конфет, на столе {candies} конфет')
    if win_in_game():
        await update.message.reply_text('Выиграл БОТ')
        return


from turtle import 
async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global candies
    msg = update.message.text
    candies -= 
От Дмитрий Суродеев всем 01:27 PM
def bot_candy():
    global candies 
    if candies > 28:
        candy = candies % 29
    else:
        candy = candies
    candies -= candy
    return candy

def win_in_game():
    global candies
    return candies < 1
        
candies = 100

app = ApplicationBuilder().token(my_token).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", new_game))
app.add_handler(MessageHandler(filters.TEXT,game))

app.run_polling()
