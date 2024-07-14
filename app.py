#app.py
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

# 以下請替換為您的 Channel Secret 和 Channel Access Token
line_bot_api = LineBotApi('m8deMq/iaZ56h+wbHflTmFIu5JXPu4hOi0Q2yKW5vwQy4W3RsL5K/I8nErk7Pb++nY2Ijl52FdCqMyZQuBNewok8Nv+Jy02FIeMZWtCR4zBWpzY88EKuEpOzNc7bY9kLmbPDmIW0DgCNYLLdmBDbCwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('58abdf1b41b1580ddd1b43e1f17cab96')


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=10000)