import json
import os
from io import BytesIO
import re

import qrcode
import telegram
import sentry_init

bot = telegram.Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])


def telegram_webhook_handler(event, context):
    upd = telegram.Update.de_json(json.loads(event['body']), bot)
    if upd.message and upd.message.text:
        urls = re.findall(r"https?://[^\s]*", upd.message.text)
        for url in urls:
            img = qrcode.make(url)
            buf = BytesIO()
            img.save(buf)
            buf.seek(0)
            upd.message.reply_photo(photo=buf, caption=url)
    return {
        "statusCode": 200,
        "body": json.dumps({})
    }
