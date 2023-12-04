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

    user_id = message.from_user.id
    chat_id = message.chat.id

    try:
        # Trying to get a list of recorded chats
        recorded_chats = chat_buffer.get_num_chats()
        # Trying to get amount of messages stored
        recorded_messages = chat_buffer.get_num_messages()
        # Trying to get amount of messages in specific chat
        recorded_messages_in_chat = chat_buffer.get_num_messages_in_chat(chat_id)

    except TypeError:
        # replying to chat with Error message
        await message.answer(f"Error reading buffer")

    if chat_id == user_id:
        try:
            # Trying to get a recap from all chats
            recap = chat_buffer.get_recap()
            # message processed from buffer
            msg = f"Amount of records:\nTotal Chats:{recorded_chats}\nTotal Messages:{recorded_messages}\nLast 10 messages are:\n\n{recap}\n\n"
            # replying to chat with processed message
            await message.answer(msg)
        except TypeError:
            # replying to chat with Error message
            await message.answer(f"Error getting recap from Chat ID:{chat_id}\n\n")


    elif chat_id in chat_buffer.buffer_dict:
        try:
            # Trying to get a recap from this chat
            recap = chat_buffer.get_recap_chat(chat_id)
            msg = f"Amount of records:\nMessages:{recorded_messages_in_chat}\nLast 10 messages are:\n\n{recap}\n\n"
            # replying to chat with processed message
            await message.answer(msg)
        except TypeError:
            # replying to chat with Error message
            await message.answer(f"Error getting recap from Chat ID:{chat_id}\n\n")





    

    

    