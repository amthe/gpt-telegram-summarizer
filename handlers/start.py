# external libraries
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# local functions
import chat_buffer
# Initialize Router
start_router = Router()
delete_buffer_router = Router()

# Telegram bot command /start that prints starting message with available commands
@start_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    # create a message to send in chat
    msg = (f"Available commands:\n\n"
          f"/recap - recap last 10 messages\n\n"
          f"/summary - summarize chat\n\n"
          f"/delete - clear buffer")
    # send a message
    await message.answer(msg)

@delete_buffer_router.message(Command("delete"))
async def command_delete_buffer_handler(message: Message) -> None:

    try:
        chat_buffer.delete_buffer()
        msg = f"Buffer deleted"
    except TypeError:
        # create a message to send in chat
        msg = f"Error deleting Buffer"
    # send a message
    await message.answer(msg)