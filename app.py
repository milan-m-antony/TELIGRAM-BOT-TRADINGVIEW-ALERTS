import imaplib
import email
from email.header import decode_header
import time
import os
import asyncio
from telegram import Bot
from telegram.error import TelegramError

# Gmail configuration
GMAIL_USER = ""  # Your Gmail address
GMAIL_PASSWORD = ""  # Your Gmail app-specific password

# Telegram Bot configuration
BOT_TOKEN = ""
GROUP_CHAT_ID = ""  # Use your actual Telegram group chat ID

# Set up the Telegram bot
bot = Bot(token=BOT_TOKEN)

# Function to check Gmail for new emails
async def check_emails():
    try:
        print("Checking emails...")  # Debugging line
        # Connect to Gmail's IMAP server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(GMAIL_USER, GMAIL_PASSWORD)
        mail.select("inbox")

        # Search for all emails that are not seen
        status, messages = mail.search(None, 'UNSEEN')

        # If there are new messages
        if status == "OK":
            print("Found new emails!")  # Debugging line
            for num in messages[0].split():
                # Fetch the email by ID
                status, msg_data = mail.fetch(num, "(RFC822)")
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        # Parse the email
                        msg = email.message_from_bytes(response_part[1])

                        # Decode email subject
                        subject, encoding = decode_header(msg["Subject"])[0]
                        if isinstance(subject, bytes):
                            subject = subject.decode(encoding if encoding else "utf-8")

                        # Decode email sender
                        from_ = msg.get("From")
                        
                        # Get the email content (body)
                        body = ""
                        if msg.is_multipart():
                            for part in msg.walk():
                                content_type = part.get_content_type()
                                content_disposition = str(part.get("Content-Disposition"))

                                # Extract text/plain or text/html content
                                if "attachment" not in content_disposition:
                                    if content_type == "text/plain":
                                        body = part.get_payload(decode=True).decode()
                                        break
                        else:
                            body = msg.get_payload(decode=True).decode()

                        # Debugging line to check extracted subject, from, and body
                        print(f"Subject: {subject}\nFrom: {from_}\nBody: {body}")

                        if body is None:
                            body = "No content found."
                        
                        # Send email content to Telegram
                        formatted_message = format_message(subject, from_, body)
                        await send_to_telegram(formatted_message)
                
        mail.close()
        mail.logout()

    except Exception as e:
        print(f"Error checking emails: {e}")

# Function to format the message with Markdown styling
def format_message(subject, sender, body):
    message = f"""
  *                    🚨 NEW EMAIL ALERT 🚨*

*                             📬* {subject}

*✉️ From:* {sender}

*💬 MESSAGE:*

{body}
"""
    return message

# Function to send message to Telegram
async def send_to_telegram(message):
    try:
        print(f"Sending message to Telegram: {message}")  # Debugging line
        await bot.send_message(chat_id=GROUP_CHAT_ID, text=message, parse_mode='Markdown')
    except TelegramError as e:
        print(f"Error sending message to Telegram: {e}")

# Main loop to check emails every minute
async def main():
    while True:
        await check_emails()
        await asyncio.sleep(1)  # Check for new emails every 60 seconds

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
