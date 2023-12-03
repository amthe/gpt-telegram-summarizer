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
        # Trying to get a list of records
        buffer_list = chat_buffer.buffer_list
        # Trying to get amount of records in a list
        records = len(buffer_list)
        # Trying to read buffer list of messages
        last_records = buffer_list[-10:]
        # message processed from buffer
        msg = f"Amount of records:{records} messages.\n\nLast 10 messages are: \n\n"
        for item in last_records:
            msg += f'{item}\n\n'
        # replying to chat with processed message
        await message.answer(msg)

    except TypeError:
        # replying to chat with Error message
        await message.answer(f"Error readin buffer")