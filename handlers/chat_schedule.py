import asyncio
import logging
from datetime import time, datetime, timedelta, timezone

from aiogram import Bot
from aiogram.types import Message
from aiogram.enums import ParseMode

#local
from systems.systems_buffer import save_buffer, delete_buffer
from summary import get_summary

async def schedule_msg(bot: Bot, target_time: time, user_id: int):
    try:
        franconian_timezone = timezone(timedelta(hours=1))  # UTC+1 for Franconia
        while True:
            current_time = datetime.now(franconian_timezone)
            logging.debug(f'*Sheldue task set: {current_time}')

            # Use the provided target_time parameter
            target_datetime = datetime.combine(current_time.date(), target_time)

            # Make target_datetime offset-aware
            target_datetime = target_datetime.replace(tzinfo=franconian_timezone)

            # Adjust target_datetime if it's in the past
            if current_time > target_datetime:
                target_datetime += timedelta(days=1)

            logging.info(f'\n\n*Timer set: {target_datetime}\n')

            wait_time = (target_datetime - current_time).total_seconds()
            logging.info(f"Waiting for {wait_time} seconds")
            await asyncio.sleep(wait_time)
            logging.info(f'\n\n+Sheldue task started: {current_time}\n')
            try:
                save_buffer()
                logging.debug(f"Buffer Saved in schedule process at: {current_time}")
            except Exception as e:
                logging.error(f"Error in saving buffer: {e}")
            try:

                msg = get_summary()
                logging.debug(f'getting summary results')
            except Exception as e:
                msg = f"Error in getting summary results: {e}"
                logging.error(msg)
            try:
                logging.debug(f'sending summary results to: {user_id}')
                await bot.send_message(chat_id=user_id, text=msg, parse_mode="HTML")
                logging.info(f'summary results sent to: {user_id}')
            except Exception as e:
                msg = f"Error sending summary to {user_id}: {e}"
                logging.error(msg)
                await bot.send_message(chat_id=user_id, text=msg, parse_mode="HTML")
            logging.debug(f'schedule message process completed at: {current_time}')
            try:
                delete_buffer()
                logging.debug(f"Buffer Deleted in schedule process at: {current_time}")
            except Exception as e:
                logging.error(f"Error in Deleting buffer: {e}")
            logging.info(f'\n\n-Sheldue task ended: {current_time}\n')

    except Exception as e:
        logging.error(f"Error in schedule_msg: {e}")