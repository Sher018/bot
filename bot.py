import asyncio
import logging
import sys
import os
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

# Load environment variables from .env file in development
if os.path.exists('.env'):
    load_dotenv()

from aiogram import Bot, Dispatcher, html
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# Bot token can be obtained via https://t.me/BotFather
# Get token from environment variable (Heroku Config Vars)
TOKEN = os.getenv("BOT_TOKEN")

# Log token status (but not the token itself for security)
logger.info("Token loaded: %s", "Yes" if TOKEN else "No")

if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set")

# Initialize bot instance
bot = Bot(token=TOKEN)

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender
    """
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")

async def main() -> None:
    logger.info("Starting bot...")
    # Skip pending updates
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error("Error occurred: %s", str(e)) 