
# gpt-telegram-summarizer

A Telegram bot that summarizes chats with GPT. If this bot is nothing for you, go check out this one: 
https://github.com/yellalena/telegram-gpt-summarizer/tree/master

## todo
- Telegram server says - Bad Request: not enough rights to send text messages to the chat
- Telegram server says - Forbidden: bot was kicked from the supergroup chat
- sending a message to chats daily.
- admin list should be an environment variable.

## Available commands
- /stats - shows number of saved messages.
- /save - saves buffer.
- /load - loads buffer from previously saved.
- /delete - clears buffer.

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
    
