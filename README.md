# Telegram Bot

A simple Telegram bot built with aiogram 3.x.

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your bot token:
   ```
   BOT_TOKEN=your_bot_token_here
   ```
   You can get a bot token from [@BotFather](https://t.me/BotFather) on Telegram.

## Running the Bot

To run the bot, execute:
```bash
python bot.py
```

## Features

- `/start` command handler that greets users
- Echo handler that forwards received messages back to the sender
- HTML formatting support 