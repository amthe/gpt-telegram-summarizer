import csv
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# For each module with handlers we can create a separate router.
chat_grab_router = Router()


def writer(usrmsg,message_chat_id):
    filename = f'{message_chat_id}.csv'
    with open(filename, 'a+', newline='', encoding='utf-8') as file:
        fieldnames = ['time', 'from_user_username', 'message', 'link']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(usrmsg)


@chat_grab_router.message()
async def chat_grab_handler(message: Message) -> None:
    rawmsg = message
    # print(rawmsg)
    usrmsg = (f'time: {str(message.date)}\n\n'
              f'Chat: {str(message.chat.title)}\n'
              f'Chat ID: {str(message.chat.id)}\n\n'
              f'username: @{message.from_user.username}\n'
              f'nickname: {message.from_user.first_name}\n'
              f'id: {str(message.from_user.id)}\n\n'
              f'message: {message.text}')
    #print(usrmsg)
    try:
        # Trying to write message

        number = str(message.chat.id)
        prefix = "-100"

        if number.startswith(prefix):
            number = number[len(prefix):]

        

        usrmsg = {'time': str(message.date), 'from_user_username': '@' + str(message.from_user.username),  'message': message.text, 'link': 't.me/c/'+ str(number) + '/' + str(message.message_id)}
        writer(usrmsg,message.chat.id)
    except TypeError:
        # But not all the types is supported so need to handle it
        await message.answer("Error")