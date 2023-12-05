# external libraries
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

# local functions
import chat_buffer
# Initialize Router
start_router = Router()
delete_buffer_router = Router()

admin = (F.from_user.id == 145893019)
admin_list = (F.from_user.id.in_({455872887, 145893019}))


# Telegram bot command /start that prints starting message with available commands
@delete_buffer_router.message(Command("start"), admin_list)
async def command_start_handler(message: Message) -> None:
    msg = (f"Available commands:\n\n"
          f"/stats - shows number of saved messages\n\n"
          f"/system - debug\n\n")
    await message.answer(msg)

# Telegram bot command /delete that clears bufer
@delete_buffer_router.message(Command("delete"), admin_list)
async def command_delete_buffer_handler(message: Message) -> None:
    try:
        chat_buffer.delete_buffer()
        msg = f"Buffer deleted"
    except TypeError:
        msg = f"Error deleting Buffer"
    await message.answer(msg)