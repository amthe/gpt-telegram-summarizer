
# gpt-telegram-summarizer

A Telegram bot that summarizes chats with GPT. 

## todo
- Telegram server says - Bad Request: not enough rights to send text messages to the chat
- Telegram server says - Forbidden: bot was kicked from the supergroup chat
- sending a message to chats daily.
- admin list should be an environment variable.

## Available commands
- /stats - shows number of saved messages.
- /recap - if send in chat, it makes a recap of messages of this chat. if send as pm, it makes a recap of all chats.
- /summary - if send in chat, it makes a summary of this chat. if send as pm, it makes a summary of all chats.
- /delete - delete all messages.

## Environment Variables
To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`

like this:

```dotenv .env
ENV_OPENAI_API_KEY=
ENV_TELEGRAM_BOT_TOKEN=
```

## Installation

Install docker

```
  docker-compose up --build
```
    
