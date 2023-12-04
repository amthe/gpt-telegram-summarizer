# external libraries
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

# local functions
import getenv
from handlers.summary import summary_router
from handlers.chat_grab import chat_grab_router
from handlers.start import start_router, delete_buffer_router
from handlers.recap import recap_router

# Telegram Bot API Key
TG_KEY = getenv.get_key('ENV_TELEGRAM_BOT_TOKEN')


# Main bot function
async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # Register all the routers from handlers package
    dp.include_routers(
        start_router,
        delete_buffer_router,
        recap_router,
        summary_router,
        chat_grab_router,
    )

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TG_KEY, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())