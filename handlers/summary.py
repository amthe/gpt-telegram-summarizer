# external libraries
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

# Logging
import logging

# local functions
import gpt
import chat_buffer
import create_summary

# Initialize Router
summary_router = Router()

admin = (F.from_user.id == 145893019)
admin_list = (F.from_user.id.in_({6829688825, 145893019}))

# Telegram bot command /summary that provides summary for a chat history from multiple chats
@summary_router.message(Command("summary"), admin_list)
async def command_summary_handler(message: Message) -> None:

    try:
        logging.info("Trying to create summary with create_summary_now()")
        create_summary.create_summary_now(message)
    except Exception as e:
        # Handle the exception here
        await message.answer(f"Error :\n\n{e}")

    #This handler receives messages with /summary command
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Bot is typing
    await message.bot.send_chat_action(message.chat.id, 'typing')

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


# async def send_message_to_user(user_id: int, message: str):
#     # Ben
#     # user_id = 455872887
#     # Panda
#     # user_id = 145893019
#     await bot.send_message(chat_id=145893019, text='test DM')     