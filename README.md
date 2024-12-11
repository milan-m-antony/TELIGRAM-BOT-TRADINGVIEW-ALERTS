# TELIGRAM-BOT-TRADINGVIEW-ALERTS


This Python script monitors Gmail for new emails, checks for specific content related to trading signals from TradingView, and sends alerts to a Telegram group or channel.

### Features:
Monitors Gmail for unread emails.
Forwards email alerts to Telegram group.
Supports custom message formatting for better styling.
Deployed on Railway for continuous operation (cloud service with free credits).

### How to Use:
1. Clone this repository.
2. Set up your Gmail account and Telegram bot and group/channel for receiving alerts (see instructions below).
3. Clone the Repository: `git clone https://github.com/milan-m-antony/TELIGRAM-BOT-TRADINGVIEW-ALERTS.git`
4. Install required dependencies using `pip install -r requirements.txt`.
5. Run the script!

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

### Setting Up Gmail with 2-Step Verification for App Password:
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
   
4.**Telegram Bot and Channel Setup:**

You will need both a Telegram Bot and a Telegram Channel or Group to use this script. Follow these steps:

+. Create a Telegram Bot:
   
Open Telegram and search for BotFather.
Start a chat with BotFather and type /newbot to create a new bot.
Follow the prompts to name your bot and get your Bot Token. This token will be used to authenticate your bot with the Telegram API.

+. Create a Telegram Channel or Group:

Create a Channel (or Group) in Telegram where you want the alerts to be sent.
For a Channel, go to the Channel Settings and copy the Chat ID. The Chat ID usually starts with @ for public channels (e.g., @MyChannel) or a numeric ID for private channels.
For a Group, add your bot to the group and get the Group Chat ID (use tools like @userinfobot to get the Chat ID).

+. Update the Script with Bot Token and Chat ID: for app.py & test.py
Replace BOT_TOKEN with the token you received from BotFather.
Replace GROUP_CHAT_ID with the Chat ID of your Telegram Channel or Group.

`BOT_TOKEN = "YOUR_BOT_TOKEN"  # Replace with your bot token from BotFather
GROUP_CHAT_ID = "@your_channel_or_group_id"  # Replace with your channel or group chat ID`

### Deploy on Railway:

Sign Up/Log In to Railway: Visit Railway and sign up using your GitHub account.

Create a New Project:
    On the Railway dashboard, click New Project.
    Select Deploy from GitHub and link your repository.
    
Add Environment Variables in Railway: Go to the Settings tab of your Railway project and add the following environment variables:
   GMAIL_USER: Your Gmail address (e.g., your-email@gmail.com).
   GMAIL_PASSWORD: Your Gmail app-specific password.
   BOT_TOKEN: Your Telegram Bot API token.
   GROUP_CHAT_ID: Your Telegram group chat ID.
   
Deploy the Project: Railway will automatically deploy your project. You can view logs and manage the deployment from the Railway dashboard.




