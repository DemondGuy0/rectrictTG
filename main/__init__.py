#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("12569968", default=None, cast=int)
API_HASH = config("2d5b54d8745cab19f3bf12cfd77c4897", default=None)
BOT_TOKEN = config("5867281966:AAEfBMW4rj8J1g5e8AvqM2RVIVouHD0iYqU", default=None)
SESSION = config("killerj00", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("5360325865", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
