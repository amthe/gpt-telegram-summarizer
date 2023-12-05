# external libraries
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

# local functions
import chat_buffer

# Initialize Router
recap_router = Router()
stats_router = Router()

admin = (F.from_user.id == 145893019)
admin_list = (F.from_user.id.in_({455872887, 145893019}))

# Telegram bot command /recap that provides log of last 10 messages
@recap_router.message(Command("recap"), admin_list)
async def command_recap_handler(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Bot is typing
    await message.bot.send_chat_action(message.chat.id, 'typing')

    try:
        if chat_id == user_id:
            recap = chat_buffer.get_recap()
            msg = f"Last 10 messages are:\n\n{recap}\n\n"
            await message.answer(msg)
        elif chat_id in chat_buffer.buffer_dict:
            recap = chat_buffer.get_recap_chat(chat_id)
            msg = f"Last 10 messages are:\n\n{recap}\n\n"
            await message.answer(msg)
        else:
            raise KeyError(f"Chat ID {chat_id} not found in buffer_dict")
    except (TypeError, KeyError) as e:
        await message.answer(f"Error: {str(e)}")


@stats_router.message(Command("stats"))
async def command_stats_handler(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Bot is typing
    await message.bot.send_chat_action(message.chat.id, 'typing')

    try:
        if chat_id == user_id:
            recorded_chats = chat_buffer.get_num_chats()
            recorded_messages = chat_buffer.get_num_messages()

            msg = f"Amount of records:\nTotal Chats: {recorded_chats}\nTotal Messages: {recorded_messages}"
            await message.answer(msg)
        elif chat_id in chat_buffer.buffer_dict:
            recorded_messages_in_chat = chat_buffer.get_num_messages_in_chat(chat_id)
            msg = f"Amount of records:\nMessages: {recorded_messages_in_chat}"
            await message.answer(msg)
        else:
            raise KeyError(f"Chat ID {chat_id} not found in buffer_dict")
    except (TypeError, KeyError) as e:
        await message.answer(f"Error: {str(e)}")


    

    

    