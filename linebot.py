from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
linebot_api = LineBotApi(
    'T7SxI84IeUrDczb3GqWNiJ6uR9BYNqcYKDN4lXvysix1KKcGrvDj9WbzyE4dW8G6/oDPGkwlt81sX+eoMjGZFprmsr+Fc023Y5UvMa/MA5LJSuyhLK3doXLLqGda8PVFQNuerl9p6dMrRWaPOo9EmAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8934b15b8ceb5ce6236d72238f226ebf')

app = Flask(__name__)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
