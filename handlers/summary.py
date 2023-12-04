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
    user_id = message.from_user.id
    chat_id = message.chat.id

    if chat_id == user_id:
        try:
            # Trying to read buffer list of all messages
            buffer_full = chat_buffer.convert_buffer_to_string()
            try:
                # Trying to pass string messages from buffer into summary function for processing
                msg = gpt.summary(buffer_full)
                # replying to chat with processed message
                await message.answer(f'{msg}')
            except TypeError:
                # replying to chat with Error message
                await message.answer(f"Error summarizing:\n\n{buffer_full}")

        except TypeError:
            # replying to chat with Error message
            await message.answer(f"Error reading buffer")

    elif chat_id in chat_buffer.buffer_dict:
        try:
            # Trying to read buffer list of specific chat messages
            buffer_chat = chat_buffer.convert_chat_to_string(chat_id)
            try:
                # Trying to pass string messages from buffer into summary function for processing
                msg = gpt.summary(buffer_chat)
                # replying to chat with processed message
                await message.answer(f'{msg}')
            except TypeError:
                # replying to chat with Error message
                await message.answer(f"Error summarizing:\n\n{buffer_chat}")

        except TypeError:
            # replying to chat with Error message
            await message.answer(f"Error reading buffer")             