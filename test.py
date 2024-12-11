import asyncio
from telegram import Bot

BOT_TOKEN = "8148970327:AAEHknRF058G5CFKH2WlJXI4MMVMiApOD4U"
GROUP_CHAT_ID = "-1002369350392"  # Use your actual Telegram group chat ID

bot = Bot(token=BOT_TOKEN)

# Async function to send a message
async def send_message_to_telegram():
    await bot.send_message(chat_id=GROUP_CHAT_ID, text="Test message from the bot")
    print("Message sent successfully!")  # Confirming message sent

# Run the async function
if __name__ == "__main__":
    asyncio.run(send_message_to_telegram())
