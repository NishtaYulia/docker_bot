from aiogram import Bot, Dispatcher, types
from .settings import BOT_TOKEN
from bot.src.database.create_table import execute_query
from zoneinfo import ZoneInfo
from datetime import datetime

bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    timestamp_now = datetime.now(tz=ZoneInfo("UTC")).isoformat(" ")
    insert_query = (f"INSERT INTO message (message, userid, message_time) "
                    f"VALUES ({message.text}, {message.from_user['id']}, {timestamp_now})")
    execute_query(insert_query)
    await message.reply("Hi!\nI'm EchoBot!")


@dispatcher.message_handler()
async def echo(message: types.Message):
    """
    This handler accepts any message and sends it back unchanged.
    """
    timestamp_now = datetime.now(tz=ZoneInfo("UTC")).isoformat(" ")
    insert_query = (f"INSERT INTO message (message, userid, message_time) "
                    f"VALUES ('{message.text}', {message.from_user['id']}, '{timestamp_now}')")
    execute_query(insert_query)
    await message.answer(message.text)
