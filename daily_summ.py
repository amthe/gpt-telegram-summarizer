import asyncio
from datetime import datetime, timedelta, timezone

async def job():
    print("Running job at 5 AM...")

async def schedule_job():
    franconian_timezone = timezone(timedelta(hours=1))  # UTC+2 for Franconia
    print(franconian_timezone)

    while True:
        current_time = datetime.now(franconian_timezone)
        print(current_time)
        target_time = current_time.replace(hour=5, minute=0, second=0, microsecond=0)

        if current_time > target_time:
            target_time += timedelta(days=1)

        wait_time = (target_time - current_time).total_seconds()
        await asyncio.sleep(wait_time)

        await job()

# Call the function to start the scheduled job
asyncio.run(schedule_job())