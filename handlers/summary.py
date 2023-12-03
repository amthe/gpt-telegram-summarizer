# external libraries
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# local functions
import gpt
import chat_buffer

# Initialize Router
summary_router = Router()

# Telegram bot command /summary that provides summary for a chat history from multiple chats
@summary_router.message(Command("summary"))
async def command_summary_handler(message: Message) -> None:
    #This handler receives messages with /summary command
    try:
        # Trying to read buffer list of messages
        buffer_list = chat_buffer.buffer_list

        # buffer_list = chat_buffer.buffer_list[-20:]
        
        # Converting buffer list into a string
        buffer_list = ''.join(buffer_list)

        try:
            # Trying to pass string messages from buffer into summary function for processing
            msg = gpt.summary(buffer_list)
            # replying to chat with processed message
            await message.answer(f'{msg}')
        except TypeError:
            # replying to chat with Error message
            await message.answer(f"Error summarizing:\n\n{buffer_list}")

    except TypeError:
        # replying to chat with Error message
        await message.answer(f"Error reading buffer")