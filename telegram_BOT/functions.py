from telegram.ext import *
from telegram import Update

# Passar todas as funções para cá.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Meu nome é abobra amigo do farpa!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Vou te ajudar no que for possível!")

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps=' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text[5::])

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text= 'Infelizmente não reconheci esse comando, por gentileza tente novamente.')




    