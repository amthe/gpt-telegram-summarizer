# external libraries
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# Initialize Router
start_router = Router()

# Telegram bot command /start that prints starting message with available commands
@start_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    # create a message to send in chat
    msg = f"Hello, <b>{message.from_user.full_name}!</b>"
    # send a message
    await message.answer(msg)