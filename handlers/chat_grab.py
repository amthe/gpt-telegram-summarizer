# external libraries
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message

#local functions
import chat_buffer

# Initialize Router
chat_grab_router = Router()

# Initialize logmsg as a string object
logmsg = ''

# Function that returns combined Chat info such as Chat ID and Chat Name
def chat_handler(message: types.Message) -> str:
    chat = message.chat

    # Access Chat ID
    chat_id = chat.id

    # Access Chat's name
    chat_name = chat.title

    # Create Chat info msg
    chat_info = f'In Chat [{chat_name} - ChatID:{chat_id}]'

    return chat_info


# Function that returns combined User info such as User ID and User Name
def user_handler(message: types.Message) -> str:
    user = message.from_user

    # Access user ID
    user_id = user.id

    # Access user's name
    user_name = user.full_name

    # Create User info msg
    user_info = f'User [{user_name} - UserID:{user_id}]'

    return user_info


# Function that returns combined replied to User info such as User ID and User Name
def reply_user_handler(message: types.Message) -> str:
    replied_user = message.reply_to_message.from_user if (message.reply_to_message and message.reply_to_message.from_user) else None

    if replied_user:
        # Access user ID
        replied_user_id = replied_user.id

        # Access user's first name
        replied_first_name = replied_user.first_name or ''

        # Access user's last name
        replied_last_name = replied_user.last_name or ''

        # Construct log message
        replied_user_info = f'User [{replied_first_name} {replied_last_name} - UserID:{replied_user_id}]'
    else:
        replied_user_info = '[Anonymous] user'

    return replied_user_info


# Function that returns combined reply content type
def reply_content_handler(message: types.Message) -> str:
    reply_msg = ""

    if message.reply_to_message:
        if message.reply_to_message.text:
            reply_msg += f'[text message: "{message.reply_to_message.text}"]'
        if message.reply_to_message.caption:
            reply_msg += f'[caption "{message.reply_to_message.caption}"]'
        if message.reply_to_message.sticker:
            reply_msg += f'[sticker {message.reply_to_message.sticker.emoji}]'
        if message.reply_to_message.animation:
            reply_msg += '[GIF]'
        if message.reply_to_message.photo:
            reply_msg += '[picture]'
        if message.reply_to_message.video:
            reply_msg += '[video]'
        if message.reply_to_message.audio:
            reply_msg += '[audio]'
        if message.reply_to_message.document:
            reply_msg += '[document]'

    return reply_msg


# Function that returns combined posted content type and partly assembles log message (need some clearing)
def content_handler(message: types.Message) -> str:
    chat_info = chat_handler(message)
    user_info = user_handler(message)
    logmsg =f'{chat_info} {user_info} send'

    if message.reply_to_message:
        logmsg+= f' reply to {reply_content_handler(message)} from {reply_user_handler(message)} with'

    if message.text:
        logmsg+= f' [text message: "{message.text}"]'

    if message.photo:
        logmsg+= f' [picture]'

    if message.caption:
        logmsg+= f' [caption "{message.caption}"]'

    if message.sticker:
        logmsg+= f' [sticker "{message.sticker.emoji}"]'

    if message.animation:
        logmsg+= f' [GIF]'

    if message.video:
        logmsg+= f' [video]'

    if message.audio:
        logmsg+= f' [audio]'

    if message.document:
        logmsg+= f' [document]'

    logmsg+= f' - [MessageID:{message.message_id}]'
    return logmsg


# Function that reads any message from a chat and trying to log it
@chat_grab_router.message()
async def chat_grab_handler(message: Message) -> None:
    chat_id = message.chat.id
    logmsg = content_handler(message)

    try:
        # Trying to write message into memory
        chat_buffer.buffer(chat_id, logmsg)

    except TypeError:
        # replying to chat with Error message
        await message.answer("Sneeed and feeed")