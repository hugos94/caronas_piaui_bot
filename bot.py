import asyncio
import sys
import telepot
import telepot.async
import settings
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardHide


if __name__ == '__main__':
    BOT_ID = settings.BOT_ID
    TOKEN = settings.TELEGRAM_API_KEY
