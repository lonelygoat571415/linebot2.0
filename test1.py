from flask import Flask, request, abort
import os
import json

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)

app = Flask(__name__)

linebot_api = LineBotApi(
    'jL+O8taDPaqts2KXANc/d34yfBiecg2sUzUevfaycS99ZZ+VHBSUGNtyCUouF2HaQf1uXsYMdn4K5nBv6vQK7f2b++XTUC9XJ0dR0RnghxDkyLP32+1ZcJCUw0g/3/9Knt1eLklVRZGGGtFLOZHZbQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('abb220892ec47ed303ead5bafb2ad99b')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == '交通':
        file_path = os.path.abspath('/a專題/下學期/coding/test.json')
        with open(file_path, 'r') as f:
            data = json.load(f)
        linebot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='hello', contents=data)
        )


if __name__ == "__main__":
    app.run()
