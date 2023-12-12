import asyncio
from datetime import datetime, timedelta, timezone

from aiogram import Bot
from aiogram.types import Message
from aiogram.enums import ParseMode

#local
from systems.systems_buffer import save_buffer, delete_buffer
from summary import get_summary


async def schedule_msg(bot: Bot):
    try:
        franconian_timezone = timezone(timedelta(hours=1))  # UTC+1 for Franconia
        print(franconian_timezone)
        # msg = 'Test message'
        user_id = [145893019, 6829688825]

        print("schedule task started")

        while True:
            current_time = datetime.now(franconian_timezone)
            print(f"Current time: {current_time}")
            target_time = current_time.replace(hour=5, minute=0, second=0, microsecond=0)

            if current_time > target_time:
                target_time += timedelta(days=1)

            wait_time = (target_time - current_time).total_seconds()
            print(f"Waiting for {wait_time} seconds")
            await asyncio.sleep(wait_time)
            save_buffer()
            print(f"Buffer Saved in schedule process at: {current_time}")
            msg = get_summary()
            await bot.send_message(chat_id=user_id, text=msg, parse_mode="HTML")
            print(f'schedule message process completed at: {current_time}')
            delete_buffer()
            print(f"Buffer deleted after schedule process at: {current_time}")
    except Exception as e:
        print(f"Error in schedule_msg: {e}")

# Call the function to start the scheduled job
# asyncio.run(schedule_msg(Bot))