import asyncio
import logging
from datetime import datetime, timedelta, timezone
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
from handlers.chat_sheldue import sheldue_msg

# Telegram Bot API Key
TG_KEY = get_key('ENV_TELEGRAM_BOT_TOKEN')


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
    bot = Bot(TG_KEY, parse_mode=ParseMode.HTML)


    # Run multiple tasks concurrently
    await asyncio.gather(
        dp.start_polling(bot),  # Run polling in one task
        sheldue_msg(bot),  # Run sheldue_msg in another task
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
