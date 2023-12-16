# external libraries
import logging
from aiogram import Bot, Router, F, types
from aiogram.filters import Command
from aiogram.types import Message

# local
from summary import get_summary, get_chat_summary
from systems.systems_buffer import save_buffer, load_buffer, delete_buffer, get_num_chats, get_num_messages, get_num_messages_in_chat

# Initialize Router
buffer_router = Router()

admin_list = {145893019, 6829688825}

def admin_command(func):
    async def wrapper(message: Message):
        if F.from_user.id.in_(admin_list):
            try:
                await func(message)
            except Exception as e:
                logging.error(f"Error: {e}")
                await message.answer(f"Error: {e}")
        else:
            logging.warning(f"Unauthorized access: {message.from_user.id}")
            await message.answer("Unauthorized access")
    return wrapper

@buffer_router.message(Command("save"))
@admin_command
async def command_buffer_save_handler(message: Message) -> None:
    save_buffer()
    logging.info('Buffer saved')
    await message.answer('Buffer saved')

@buffer_router.message(Command("load"))
@admin_command
async def command_buffer_load_handler(message: Message) -> None:
    load_buffer()
    logging.info('Buffer loaded')
    await message.answer('Buffer loaded')

@buffer_router.message(Command("delete"))
@admin_command
async def command_buffer_delete_handler(message: Message) -> None:
    delete_buffer()
    logging.info('Buffer deleted')
    await message.answer('Buffer deleted')

@buffer_router.message(Command("stats"))
@admin_command
async def command_buffer_stats_handler(message: Message) -> None:
    try:
        chat_name = message.chat.title
        chat_id = message.chat.id
        user_id = message.from_user.id
        logging.info(f'\nChat ID:{chat_id}\nUser ID:{user_id}')
        if chat_id == user_id:
            msg = f'Number of stored chats: {get_num_chats()}\nNumber of stored messages: {get_num_messages()}\n'
            logging.info(msg)
            await message.answer(f'\nPrivate chat\nChat ID:{chat_id}\n{msg}')
        else:
            chat_id = str(chat_id)[4:]
            msg = f'Number of stored messages: {get_num_messages_in_chat(chat_id)}\n'
            logging.info(msg)
            await message.answer(f'\n{chat_name}\nChat ID:{chat_id}\n{msg}')
    except Exception as e:
        logging.error(f"Error: {e}")
        await message.answer(f"Error: {e}")

@buffer_router.message(Command("summary"))
@admin_command
async def command_buffer_summary_handler(message: Message) -> None:
    chat_name = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    try:
        logging.info('Getting summary, could take long.')
        await message.answer(f'Getting summary for {get_num_messages_in_chat(chat_id)} messages, could take long.')
        await message.bot.send_chat_action(message.chat.id, action='typing')
        if chat_id == user_id:
            msg = get_summary()
            logging.info('Sending full summary results')
        else:
            chat_id = str(chat_id)[4:]
            msg = get_chat_summary(chat_id)
            logging.info(f'Sending {chat_name} summary results')
        await message.answer(msg)
        logging.info('Summary results sent')
        await message.bot.send_chat_action(message.chat.id, action='typing')
    except Exception as e:
        logging.error(f"Error getting/sending summary: {e}")
        await message.answer(f"Error getting/sending summary: {e}")
