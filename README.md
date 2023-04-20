# Clone & run your own bot

Requirements:

- Telegram account (Create a new one here https://telegram.org/)
- AWS account (Create a new one here https://aws.amazon.com/) and [awscli](https://github.com/aws/aws-cli) ideally configured with your profile credentials (API key)
- Serverless Framework (Install it from here https://www.serverless.com/framework/docs/getting-started/)
- Python 3.9+ (Install it from here https://www.python.org/downloads/)
- Node.js 14+ (Install it from here https://nodejs.org/en/download/)

1. Clone the repo
2. Create a new bot in Telegram (https://core.telegram.org/bots#how-do-i-create-a-bot)
3. Create a new `.env` file in the root of the project and fill it:
   ```ini
   SERVICE_NAME=... (if you plan to monitor the service on serverless platform)
   TELEGRAM_BOT_NAME=... (from @BotFather)
   TELEGRAM_BOT_TOKEN=... (from @BotFather)
   SENTRY_DSN=... (if you plan to use Sentry.io)
   ```
   if you didn't configure `aws-cli` with your AWS credentials, then include your `AWS_ACCESS_KEY_ID` & `AWS_SECRET_ACCESS_KEY` in `.env` as well.
4. install requirements & sls plugins
   ```bash
   npm install
   sls plugin install -n serverless-python-requirements
   ```
5. Build & deploy the bot
   ```bash
   sls deploy
   ```
   this will build and deploy your AWS lambda and will give you the endpoint- **copy it**
6. Set webhook for the bot (this must be done only once after the first deployment)
   ```bash
   curl -F "url=https://<your-endpoint>" https://api.telegram.org/bot<your-token>/setWebhook
   ```
   You can use `telegram` lib and python console as an alternative, basically you need to call
   ```python
   import telegram
   telegram.Bot(token='..<your token>..').set_webhook('<..your endpoint..>')
   ```
7. Go to your Telegram bot and send it a message.


PS:
- Sentry.io is a great tool for monitoring your bot, you can use it for free with a limited number of events.
- Hint: Serverless.com gives you a great dashboard for monitoring your lambda executions, errors, logs, etc.
