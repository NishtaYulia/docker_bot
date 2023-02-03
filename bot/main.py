from aiogram import executor
from bot.src.echobot import dispatcher


executor.start_polling(dispatcher, skip_updates=True)