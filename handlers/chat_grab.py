import logging
from aiogram import Router, types
from aiogram.types import Message
from systems.systems_buffer import write_buffer

# Initialize Router
chat_grab_router = Router()

def get_user_info(user: types.User) -> str:
    return f'User [{user.full_name or "Anonymous"} - UserID:{user.id}]'

def get_content_type(message: types.Message) -> str:
    content_types = [
        f'[text message: "{message.text}"]' if message.text else '',
        ' [picture]' if message.photo else '',
        f' [caption "{message.caption}"]' if message.caption else '',
        f' [sticker "{message.sticker.emoji}"]' if message.sticker else '',
        ' [GIF]' if message.animation else '',
        ' [video]' if message.video else '',
        ' [audio]' if message.audio else '',
        ' [voice]' if message.voice else '',
        ' [video note]' if message.video_note else '',
        ' [document]' if message.document else ''
    ]
    return ''.join(content_types)

def get_replied_user_info(reply_user: types.User) -> str:
    return f'User [{reply_user.full_name or "Anonymous"} - UserID:{reply_user.id}]' if reply_user else '[Anonymous] user'

def get_chat_info(chat: types.Chat) -> str:
    return f'In Chat [{chat.title or "Private Chat"} - ChatID:{str(chat.id)[4:]}]'

def handle_chat_message(message: types.Message) -> None:
    chat_info = get_chat_info(message.chat)
    user_info = get_user_info(message.from_user)
    logmsg = f'\n{chat_info}\n{user_info}\nsend'

    if message.reply_to_message:
        replied_user_info = get_replied_user_info(message.reply_to_message.from_user)
        reply_content_type = get_content_type(message.reply_to_message)
        logmsg += f' reply to {reply_content_type}\nfrom {replied_user_info}\nwith'

    logmsg += get_content_type(message)
    logmsg += f'\n[MessageID:{message.message_id}]\n[Time:{message.date}]'

    if message.chat.id != message.from_user.id:
        try:
            # Trying to write message into memory
            write_buffer(str(message.chat.id)[4:], logmsg)
            logging.info(logmsg)

        except Exception as e:
            logging.error(f"Error writing to buffer: {e}")

# Register message handler
@chat_grab_router.message()
async def chat_grab_handler(message: Message) -> None:
    handle_chat_message(message)

