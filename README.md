# TELIGRAM-BOT-TRADINGVIEW-ALERTS


This Python script monitors Gmail for new emails, checks for specific content related to trading signals from TradingView, and sends alerts to a Telegram group or channel.

### How to Use:
1. Clone this repository.
2. Set up your Gmail account and Telegram bot (see instructions below).
3. Install required dependencies using `pip install -r requirements.txt`.
4. Run the script!

### Dependencies:
- `imaplib`
- `email`
- `python-telegram-bot`

### Setup Instructions:
1. Replace `GMAIL_USER`, `GMAIL_PASSWORD`, and `BOT_TOKEN` in the script with your own details.
2. Modify the `GROUP_CHAT_ID` to your group's or channel's Telegram chat ID.
3. Make sure you are subscribed to TradingView alerts. The script will trigger on emails received from TradingView with trading signals (e.g., BTC price crossing a threshold).

### TradingView Alerts:
This script is designed to work with TradingView email alerts. To use this bot, you'll need to create an account on [TradingView](https://www.tradingview.com/), set up email alerts for your desired trading conditions (e.g., when BTCUSD crosses a certain price), and link your Gmail account to this script. The bot will automatically check your inbox for new alerts and forward them to your Telegram group or channel.

### Setting Up Gmail with 2-Step Verification and App Password:
To securely use your Gmail account for this bot, you must enable two-factor authentication (2FA) and generate an App Password. Here's how:

1. **Enable 2-Step Verification (2FA):**
   - Go to your [Google Account](https://myaccount.google.com/).
   - In the left-hand menu, select **Security**.
   - Under **Signing in to Google**, click **2-Step Verification**.
   - Follow the steps to set up 2FA on your account.

2. **Generate an App Password:**
   - Once 2FA is enabled, return to the **Security** section of your Google Account.
   - Under **App passwords**, you may need to sign in again.
   - Select **Mail** as the app and **Other (Custom name)** as the device.
   - Name it something like **Telegram Bot** and click **Generate**.
   - Copy the generated 16-character App Password (it will look something like: `jcut qqkp lniu gqdz`).

3. **Update the Script:**
   - Replace `GMAIL_PASSWORD` in the script with the generated App Password (not your regular Gmail password).

   Example:
   ```python
   GMAIL_PASSWORD = "jcut qqkp lniu gqdz"  # Your Gmail App-specific password

