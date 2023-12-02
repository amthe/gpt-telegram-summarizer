import asyncio
import logging
import os
import time #sleep


from openai import OpenAI
from os import getenv

from handlers.chat_grab import chat_grab_router
from handlers.start import start_router

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

# Bot token can be obtained via https://t.me/BotFather
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')




async def summarize_chats(bot):
    # Get the current directory
    folder_path = os.getcwd()

    # Loop over files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file has a .csv extension
        if file_name.endswith('.csv'):
            # Extract chat ID from file name
            chat_id_from_csv = file_name.split('.')[0]

            # Read file contents
            with open(file_name, 'r', encoding='utf-8') as file:
                payload = file.read()

                client = OpenAI(
                    api_key=os.getenv('OPENAI_API_KEY'),
                )

                chat_completion = client.chat.completions.create(
                    messages=[
                        {'role':'system', 'content': """
You summarize a chatlog in english in 500-1000 charachters.
You will be told by the user inside <csv></csv> tags, the content is in CSV Format.
You don't tell Dates and times.
Empty Messages is information you do not know and can only speculate.
@None are several users, which didnt create a name.                     
You add links to important messages that define or start a topic like shown in the example.
                                                                           
Example: 
@iamamt was talking about cars <a href="t.me/c/2101673397/41/">[1]</a> when @cat mentioned airplanes <a href="t.me/c/2101673397/49/">[2]</a>, then the conversation continued with airplanes for a while.                         

                        """}, 
                        {'role':'user', 'content':'<csv>' + 'time,from_user_username,message,link\n' + payload + '</csv>'}
                    ],
                    model="gpt-4-1106-preview"
                )

                print(chat_completion.choices[0].message.content.strip())

                answer = chat_completion.choices[0].message.content.strip()
                escaped_message = '''⚡️ {}'''.format(answer)

                escaped_string = escaped_message

                await bot.send_message(chat_id=455872887, text=escaped_string, parse_mode="HTML") 
            
            # Delete file
            #os.remove(file_name)

async def main() -> None:

    dp = Dispatcher()

    dp.include_routers(
        start_router,
        chat_grab_router,
    )

    bot = Bot(TOKEN)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(summarize_chats, 'interval', seconds=60, args=[bot])
    #scheduler.add_job(summarize_chats, CronTrigger(hour=22, minute=26), args=[bot])

    scheduler.start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())