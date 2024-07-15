from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# 以下請替換為您的 Channel Secret 和 Channel Access Token
line_bot_api = LineBotApi('m8deMq/iaZ56h+wbHflTmFIu5JXPu4hOi0Q2yKW5vwQy4W3RsL5K/I8nErk7Pb++nY2Ijl52FdCqMyZQuBNewok8Nv+Jy02FIeMZWtCR4zBWpzY88EKuEpOzNc7bY9kLmbPDmIW0DgCNYLLdmBDbCwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('58abdf1b41b1580ddd1b43e1f17cab96')


# 監聽所有來自 /callback 的 Post Request
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


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg=str(event.message.text)
    
    line_bot_api.reply_message(event.reply_token, TextSendMessage(msg))

@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    basicInfoExample = '建立資料\n[名稱]:栗子哥 \n[出生日期]:2024/07/01\n[出生體重]:2450\n[出生身長]:49.5\n[出生頭圍]:32.5'
    message = TextSendMessage(text=f'{name}歡迎加入，請初始化建立Baby基本資料。範例如下:\{basicInfoExample}')
    line_bot_api.reply_message(event.reply_token, message)       


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=10000)