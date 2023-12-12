# external libraries
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

# local
from systems.systems_buffer import save_buffer, load_buffer, delete_buffer
from systems.systems_buffer import get_num_chats, get_num_messages

# Initialize Router
buffer_save_router = Router()
buffer_load_router = Router()
buffer_delete_router = Router()
buffer_stats_router = Router()

admin_list = (F.from_user.id.in_({145893019, 6829688825}))

# Telegram bot command /summary that provides summary for a chat history from multiple chats
@buffer_save_router.message(Command("save"), admin_list)
async def command_buffer_save_handler(message: Message) -> None:
    #This handler receives messages with /summary command
    try:
        # Trying to read buffer list of all messages
        save_buffer()
        msg = f'Buffer saved'

    except Exception as e:
        msg = f"Error saving buffer: {e}"

    print(msg)
    await message.answer(msg)


@buffer_load_router.message(Command("load"), admin_list)
async def command_buffer_load_handler(message: Message) -> None:
    #This handler receives messages with /summary command
    try:
        # Trying to read buffer list of all messages
        load_buffer()
        msg = f'Buffer loaded'

    except Exception as e:
        msg = f"Error loading buffer: {e}"
            
    print(msg)
    await message.answer(msg)


@buffer_delete_router.message(Command("delete"), admin_list)
async def command_buffer_delete_handler(message: Message) -> None:
    #This handler receives messages with /summary command
    try:
        # Trying to read buffer list of all messages
        delete_buffer()
        msg = f'Buffer deleted'

    except Exception as e:
        msg = f"Error deleting buffer: {e}"
            
    print(msg)
    await message.answer(msg)


@buffer_stats_router.message(Command("stats"), admin_list)
async def command_buffer_stats_handler(message: Message) -> None:
    #This handler receives messages with /summary command
    try:
        # Trying to read buffer list of all messages
        
        msg = f'Number of stored chats: {get_num_chats()}\n\nNumber of stored messages: {get_num_messages()}\n'

    except Exception as e:
        msg = f"Error deleting buffer: {e}"
            
    print(msg)
    await message.answer(msg)