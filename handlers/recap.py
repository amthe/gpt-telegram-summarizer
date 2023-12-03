# external libraries
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# local functions
import chat_buffer

# Initialize Router
recap_router = Router()

# Telegram bot command /recap that provides log of last 10 messages
@recap_router.message(Command("recap"))
async def command_recap_handler(message: Message) -> None:

    try:
        # Trying to read buffer list of messages
        buffer_list = chat_buffer.buffer_list[-10:]
        # message processed from buffer
        msg = "Last 10 messages are: \n\n"
        for item in buffer_list:
            msg += f'{item}\n\n'
        # replying to chat with processed message
        await message.answer(msg)

    except TypeError:
        # replying to chat with Error message
        await message.answer(f"Error readin buffer")