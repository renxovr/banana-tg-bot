from telegram.ext import Updater
from telegram.ext import CommandHandler
import random
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("BOT_TOKEN")

updater = Updater(token = token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    first_name = update.message.from_user.first_name
    username = update.message.from_user.username
    msg = f'Hola {first_name} (@{username}) bienvenido al bot'
    context.bot.send_message(chat_id = update.message.chat_id, text = msg)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def banana(update, context):
    rd = random.randint(8, 25)
    first_name = update.message.from_user.first_name
    username = update.message.from_user.username
    sticker = 'https://i.postimg.cc/GmMwLs0z/banana.webp'
    context.bot.send_message(chat_id = update.message.chat_id, text = f'La banana de {first_name} (@{username}) mide {rd} cm.')
    context.bot.send_sticker(chat_id = update.message.chat_id, sticker = sticker)
banana_handler = CommandHandler('banana', banana)
dispatcher.add_handler(banana_handler)

updater.start_polling()
