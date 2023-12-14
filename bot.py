import asyncio
import logging
from datetime import time
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
# Local
from keys.getenv import get_key
from handlers.chat_grab import chat_grab_router
from handlers.chat_buffer import (
    buffer_save_router,
    buffer_load_router,
    buffer_delete_router,
    buffer_stats_router,
)
from handlers.chat_schedule import schedule_msg

# Telegram Bot API Key
TG_BOT_TOKEN = get_key('ENV_TELEGRAM_BOT_TOKEN')
TG_USER_ID = get_key('ENV_TELEGRAM_USER_ID')
# Set Timer
TIMER = time(5, 0)


async def main() -> None:
    # Initialize Dispatcher as a root router
    dp = Dispatcher()

    # Register routers from handlers package
    dp.include_routers(
        buffer_save_router,
        buffer_load_router,
        buffer_delete_router,
        buffer_stats_router,
        chat_grab_router,
    )

    # Initialize Bot instance with a default parse mode
    bot = Bot(TG_BOT_TOKEN, parse_mode=ParseMode.HTML)


    # Run multiple tasks concurrently
    await asyncio.gather(
        dp.start_polling(bot),  # Run polling in one task
        schedule_msg(bot, TIMER, TG_USER_ID),  # Run schedule_msg in another task
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=logging.ERROR)
    asyncio.run(main())
