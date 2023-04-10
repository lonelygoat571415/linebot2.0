import os
import json
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

{ "rewrites": [{ "source": "/(.*)", "destination": "/" }] }
linebot_api = LineBotApi(
    'T7SxI84IeUrDczb3GqWNiJ6uR9BYNqcYKDN4lXvysix1KKcGrvDj9WbzyE4dW8G6/oDPGkwlt81sX+eoMjGZFprmsr+Fc023Y5UvMa/MA5LJSuyhLK3doXLLqGda8PVFQNuerl9p6dMrRWaPOo9EmAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8934b15b8ceb5ce6236d72238f226ebf')

app = Flask(__name__)


@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
# mant list
def handle_message(event):
    mtext = event.message.text
# 1 個人專區
    if mtext == '個人專區':
        try:
            message = TemplateSendMessage(
                alt_text='個人專區',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/TGx1RuH.jpg',
                    tetle='個人專區',
                    text='請選擇您要搜尋之項目',
                    actions=[
                        MessageTemplateAction(
                            label='醫院繳費資訊',
                            text='醫院繳費資訊'
                        ),
                        URITemplateAction(
                            label='預約慢性病連續處方簽領藥',
                            uri='http://opdws.fjuh.fju.edu.tw/RegChronic/AP/Default.aspx'
                        )
                    ]
                )
            )
            linebot_api.reply_message(event.reply_token, message)

        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
    elif mtext == '醫院繳費資訊':
        try:
            message = TemplateSendMessage(
                alt_text='繳費資訊',
                template=ConfirmTemplate(
                    text='請選擇您要搜尋的費用項目',
                    actions=[
                        MessageTemplateAction(
                            label='掛號費',
                            text='掛號費'
                        ),
                        MessageTemplateAction(
                            label='全民健保',
                            text='全民健康保險部分負擔'
                        )
                    ]
                )
            )
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
    elif mtext == '掛號費':
        try:
            message = [
                TextSendMessage(text="依照圖表的時段與類別，對應掛號費用"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/rc9HaUE.png",
                    preview_image_url="https://i.imgur.com/rc9HaUE.png"
                ),
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
    elif mtext == "全民健康保險部分負擔":
        try:
            message = TemplateSendMessage(
                alt_text='全民健康保險部分負擔',
                template=ConfirmTemplate(
                    text='請選擇了解之負擔費用',
                    actions=[
                        MessageTemplateAction(
                            label='藥費',
                            text='藥費'
                        ),
                        MessageTemplateAction(
                            label='其他',
                            text='藥費以外之負擔費用',
                        )
                    ]
                )
            )
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
    elif mtext == '藥費':
        try:
            message = [
                TextSendMessage(text="依照圖表的時段與類別，對應掛號費用"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/pprjyvx.png",
                    preview_image_url="https://i.imgur.com/pprjyvx.png"
                ),
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
    elif mtext == '藥費以外之負擔費用':
        try:
            message = [
                TextSendMessage(text="依照圖表的時段與類別，對應掛號費用"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/J13pJbg.png",
                    preview_image_url="https://i.imgur.com/J13pJbg.png"
                ),
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
# 2 掛號
    elif mtext == '掛號':
        try:
            message = [
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/2476coB.jpg",
                    preview_image_url="https://i.imgur.com/2476coB.jpg"
                ),
                TextSendMessage(
                    text='選擇掛號科別',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="內科", text="內科")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="外科", text="外科")
                            ),
                            QuickReplyButton(
                                action=MessageAction(
                                    label="其他專科", text="其他專科")
                            ),
                            QuickReplyButton(
                                action=MessageAction(
                                    label="特色中心", text="特色中心")
                            ),
                            QuickReplyButton(
                                action=MessageAction(
                                    label="新冠肺炎專區", text="新冠肺炎專區")
                            ),

                        ]
                    )
                ),
            ]
            linebot_api.reply_message(event.reply_token, message)

        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
    elif mtext == '內科':
        file_path = os.path.join(os.path.abspath(
            '.'), '/a專題/下學期/coding/medical department.json')
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        linebot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='內科', contents=data)
        )
    elif mtext == '外科':
        file_path = os.path.join(os.path.abspath(
            '.'), '/a專題/下學期/coding/surgical department.json')
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        linebot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='外科', contents=data)
        )

    elif mtext == '其他專科':
        file_path = os.path.join(os.path.abspath(
            '.'), '/a專題/下學期/coding/professional subjects.json')
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        linebot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='其他專科', contents=data)
        )

    elif mtext == '特色中心':
        file_path = os.path.join(os.path.abspath(
            '.'), '/a專題/下學期/coding/feature center.json')
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        linebot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='特色中心', contents=data)
        )

    elif mtext == '新冠肺炎專區':
        file_path = os.path.join(os.path.abspath(
            '.'), '/a專題/下學期/coding/covid19.json')
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        linebot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='新冠肺炎專區', contents=data)
        )

# 3 看診進度
    elif mtext == '看診進度':
        try:
            message = TemplateSendMessage(
                alt_text='看診進度查詢',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/oEmJG6R.jpg',
                    title='看診進度查詢',
                    text='點選網站了解更多',
                    actions=[

                        URITemplateAction(
                            label='今日看診進度查詢',
                            uri='https://www.hospital.fju.edu.tw/Process#gsc.tab=0'
                        ),

                    ]
                )
            )
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
# 4 就醫指南
    elif mtext == '就醫指南':
        try:
            message = TemplateSendMessage(
                alt_text='就醫指南',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/R3tTkcg.jpg',
                    title='就醫指南',
                    text='請選擇以下要了解的相關資訊',
                    actions=[
                        MessageTemplateAction(
                            label='門診科別位置',
                            text='門診科別位置'
                        ),
                        MessageTemplateAction(
                            label='醫師介紹',
                            text='醫師介紹'
                        ),
                        MessageTemplateAction(
                            label='醫院樓層介紹',
                            text='醫院樓層介紹'
                        ),
                        MessageTemplateAction(
                            label='探病時間/規定',
                            text='探病時間/規定'
                        )
                    ]
                )
            )
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '門診科別位置':
        try:
            message = [
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/nVq9uBC.png",
                    preview_image_url="https://i.imgur.com/nVq9uBC.png"
                ),
                TextSendMessage(
                    text='選擇科別',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="內科", text="內科.")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="外科", text="外科.")
                            ),
                            QuickReplyButton(
                                action=MessageAction(
                                    label="其他專科", text="其他專科.")
                            ),
                            QuickReplyButton(
                                action=MessageAction(
                                    label="特色中心", text="特色中心.")
                            ),
                            QuickReplyButton(
                                action=MessageAction(
                                    label="新冠肺炎專區", text="新冠肺炎專區.")
                            )
                        ]
                    )
                )]
            linebot_api.reply_message(event.reply_token, message)

        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '內科.':
        file_path = os.path.join(os.path.abspath(
            '.'), '/a專題/下學期/coding/internal medicine location.json')
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        linebot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='內科 位置', contents=data)
        )

    elif mtext == '外科.':
        file_path = os.path.join(os.path.abspath(
            '.'), '/a專題/下學期/coding/surgical department location.json')
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        linebot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='外科 位置', contents=data)
        )

    elif mtext == '其他專科.':
        file_path = os.path.join(os.path.abspath(
            '.'), '/a專題/下學期/coding/professional subjects location.json')
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        linebot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='其他專科 位置', contents=data)
        )

    elif mtext == '特色中心.':
        file_path = os.path.join(os.path.abspath(
            '.'), '/a專題/下學期/coding/feature center location.json')
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        linebot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='特色中心 位置', contents=data)
        )
    elif mtext == '新冠肺炎專區.':
        file_path = os.path.join(os.path.abspath(
            '.'), '/a專題/下學期/coding/covid19 location.json')
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        linebot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='新冠肺炎專區 位置', contents=data)
        )

    elif mtext == '內科部':
        try:
            message = [
                TextSendMessage(text="內科部位於2樓"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/o7zGrMk.png",
                    preview_image_url="https://i.imgur.com/o7zGrMk.png"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '心臟內科':
        try:
            message = [
                TextSendMessage(text="心臟內科位於2樓214、220、229、230、231、235診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/1LWIohD.jpg",
                    preview_image_url="https://i.imgur.com/1LWIohD.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '胃腸肝膽內科':
        try:
            message = [
                TextSendMessage(text="胃腸肝膽內科位於2樓214~217診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/JVHhNvi.jpg",
                    preview_image_url="https://i.imgur.com/JVHhNvi.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '新陳代謝科':
        try:
            message = [
                TextSendMessage(text="新陳代謝科位於2樓212、223、235診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/QuEUQj0.jpg",
                    preview_image_url="https://i.imgur.com/QuEUQj0.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '胸腔內科':
        try:
            message = [
                TextSendMessage(text="胸腔內科位於2樓205~206診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/pYxiffv.jpg",
                    preview_image_url="https://i.imgur.com/pYxiffv.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '腎臟內科':
        try:
            message = [
                TextSendMessage(text="腎臟內科位於2樓218、223~225診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/lCZtAvS.jpg",
                    preview_image_url="https://i.imgur.com/lCZtAvS.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '一般內科':
        try:
            message = [
                TextSendMessage(text="一般內科位於2樓220診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/jS71oh4.jpg",
                    preview_image_url="https://i.imgur.com/jS71oh4.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '血液腫瘤科':
        try:
            message = [
                TextSendMessage(text="血液腫瘤科位於2樓218、219及3樓312診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/8v33C6N.jpg",
                    preview_image_url="https://i.imgur.com/8v33C6N.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '風濕免疫科':
        try:
            message = [
                TextSendMessage(text="風濕免疫科位於2樓218、220診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/XRo6AOH.jpg",
                    preview_image_url="https://i.imgur.com/XRo6AOH.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '感染科':
        try:
            message = [
                TextSendMessage(text="感染科科位於2樓221診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/WyWEzxu.jpg",
                    preview_image_url="https://i.imgur.com/WyWEzxu.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '外科部':
        try:
            message = [
                TextSendMessage(text="外科部位於2、3樓診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/o7zGrMk.png",
                    preview_image_url="https://i.imgur.com/o7zGrMk.png"
                ),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/AtwEWe0.png",
                    preview_image_url="https://i.imgur.com/AtwEWe0.png"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '神經外科':
        try:
            message = [
                TextSendMessage(text="神經外科位於2樓208、251、252診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/BaN2ovQ.jpg",
                    preview_image_url="https://i.imgur.com/BaN2ovQ.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '大腸直腸外科':
        try:
            message = [
                TextSendMessage(text="大腸直腸外科位於2樓209診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/RvNuyPF.jpg",
                    preview_image_url="https://i.imgur.com/RvNuyPF.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '乳房外科':
        try:
            message = [
                TextSendMessage(text="乳房外科位於3樓312、313診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/EZF9YHT.jpg",
                    preview_image_url="https://i.imgur.com/EZF9YHT.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '泌尿科':
        try:
            message = [
                TextSendMessage(text="泌尿科位於2樓203、204及3樓314診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/SjIoL55.jpg",
                    preview_image_url="https://i.imgur.com/SjIoL55.jpg"
                ),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/7aQfTym.jpg",
                    preview_image_url="https://i.imgur.com/7aQfTym.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
    elif mtext == '一般外科':
        try:
            message = [
                TextSendMessage(text="一般外科位於2樓207、208診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/5Ia4swJ.jpg",
                    preview_image_url="https://i.imgur.com/5Ia4swJ.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
    elif mtext == '心臟血管外科':
        try:
            message = [
                TextSendMessage(text="心臟血管外科位於2樓232診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/W8nocrP.jpg",
                    preview_image_url="https://i.imgur.com/W8nocrP.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
    elif mtext == '整形外科':
        try:
            message = [
                TextSendMessage(text="整形外科位於2樓210、211診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/32rsAil.jpg",
                    preview_image_url="https://i.imgur.com/32rsAil.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '胸腔外科':
        try:
            message = [
                TextSendMessage(text="胸腔外科位於2樓211診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/e1JmO8B.jpg",
                    preview_image_url="https://i.imgur.com/e1JmO8B.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '兒童醫學部':
        try:
            message = [
                TextSendMessage(text="兒童醫學部位於2樓243、244、247診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/NB2e1yT.jpg",
                    preview_image_url="https://i.imgur.com/NB2e1yT.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '婦產部':
        try:
            message = [
                TextSendMessage(text="婦產部位於3樓307~310診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/ATK8eVF.jpg",
                    preview_image_url="https://i.imgur.com/ATK8eVF.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '智慧科學體重管理中心':
        try:
            message = [
                TextSendMessage(text="智慧科學體重管理中心位於3樓314診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/tszGPXD.jpg",
                    preview_image_url="https://i.imgur.com/tszGPXD.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '運動醫學中心(復健)':
        try:
            message = [
                TextSendMessage(text="運動醫學中心(復健)位於4樓401、402、405診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/i33IMPL.jpg",
                    preview_image_url="https://i.imgur.com/i33IMPL.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '骨科':
        try:
            message = [
                TextSendMessage(text="骨科位於2樓201、222及4樓405診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/2HftPWq.jpg",
                    preview_image_url="https://i.imgur.com/2HftPWq.jpg"
                ),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/i33IMPL.jpg",
                    preview_image_url="https://i.imgur.com/i33IMPL.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '口腔顎面科':
        try:
            message = [
                TextSendMessage(text="口腔顎面科位於B2"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/mEFBzKM.jpg",
                    preview_image_url="https://i.imgur.com/mEFBzKM.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '兒童牙科':
        try:
            message = [
                TextSendMessage(text="兒童牙科位於B2"), ImageSendMessage(
                    original_content_url="https://i.imgur.com/2EBugKs.jpg",
                    preview_image_url="https://i.imgur.com/2EBugKs.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '神經科':
        try:
            message = [
                TextSendMessage(text="神經科位於2樓249、250、252診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/J5aIQig.jpg",
                    preview_image_url="https://i.imgur.com/J5aIQig.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '牙科':
        try:
            message = [
                TextSendMessage(text="牙科位於B2樓層"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/2EBugKs.jpg",
                    preview_image_url="https://i.imgur.com/2EBugKs.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '運動醫學中心(骨科)':
        try:
            message = [
                TextSendMessage(text="運動醫學中心（骨科）位於4樓405診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/i33IMPL.jpg",
                    preview_image_url="https://i.imgur.com/i33IMPL.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '家庭醫學科':
        try:
            message = [
                TextSendMessage(text="家庭醫學科位於2樓214、254、255及3樓312診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/UXC6Q86.jpg",
                    preview_image_url="https://i.imgur.com/UXC6Q86.jpg"
                ),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/CDTRzCM.jpg",
                    preview_image_url="https://i.imgur.com/CDTRzCM.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '精神科':
        try:
            message = [
                TextSendMessage(text="精神科位於2樓265、266診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/wSDVY08.jpg",
                    preview_image_url="https://i.imgur.com/wSDVY08.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '眼科':
        try:
            message = [
                TextSendMessage(text="眼科位於3樓315~318診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/WPZaThO.jpg",
                    preview_image_url="https://i.imgur.com/WPZaThO.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '耳鼻喉科':
        try:
            message = [
                TextSendMessage(text="耳鼻喉科位於3樓301~303診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/oK5WFzS.jpg",
                    preview_image_url="https://i.imgur.com/oK5WFzS.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '皮膚科':
        try:
            message = [
                TextSendMessage(text="皮膚科位於3樓306診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/uYh5EUF.jpg",
                    preview_image_url="https://i.imgur.com/uYh5EUF.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '放射腫瘤科':
        try:
            message = [
                TextSendMessage(text="放射腫瘤科位於B2樓B205、B206診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/KiuhlfB.jpg",
                    preview_image_url="https://i.imgur.com/KiuhlfB.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '復健科':
        try:
            message = [
                TextSendMessage(text="復健科位於4樓401、402、405診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/i33IMPL.jpg",
                    preview_image_url="https://i.imgur.com/i33IMPL.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '營養諮詢':
        try:
            message = [
                TextSendMessage(text="營養諮詢位於2樓213及4樓406診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/e1JmO8B.jpg",
                    preview_image_url="https://i.imgur.com/e1JmO8B.jpg"
                ),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/i33IMPL.jpg",
                    preview_image_url="https://i.imgur.com/i33IMPL.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '腦血管介入治療':
        try:
            message = [
                TextSendMessage(text="腦血管介入治療門診位於2樓251診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/RwBzLT2.jpg",
                    preview_image_url="https://i.imgur.com/RwBzLT2.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '疼痛麻醉科':
        try:
            message = [
                TextSendMessage(text="疼痛麻醉科位於2樓235診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/4XKzsrD.jpg",
                    preview_image_url="https://i.imgur.com/4XKzsrD.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '職業醫學科':
        try:
            message = [
                TextSendMessage(text="職業醫學科位於B2樓B202診間")
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '影像醫學科門診':
        try:
            message = [
                TextSendMessage(text="影像醫學科位於2樓208診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/rzPBXLb.jpg",
                    preview_image_url="https://i.imgur.com/rzPBXLb.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '新冠肺炎康復後整合門診':
        try:
            message = [
                TextSendMessage(text="新冠肺炎康復後整合門診位於2樓205A診間"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/V4R3W5m.jpg",
                    preview_image_url="https://i.imgur.com/V4R3W5m.jpg"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '醫師介紹':
        try:
            message = TextSendMessage(
                text='選擇科別',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="內科醫師介紹", text="內科醫師介紹")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="外科醫師介紹", text="外科醫師介紹")
                        ),
                        QuickReplyButton(
                            action=MessageAction(
                                label="獨立部門醫師介紹", text="獨立部門醫師介紹")
                        ),
                    ]
                )
            )
            linebot_api.reply_message(event.reply_token, message)

        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '內科醫師介紹':

        try:
            message = TemplateSendMessage(
                alt_text='醫師介紹',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/9Axmlhw.jpg',
                    title='內科醫師介紹',
                    text='點選以下連結前往內科醫師介紹',
                    actions=[
                        URITemplateAction(
                            label='內科醫師介紹',
                            uri='https://webdept.fjuh.fju.edu.tw/FjuhDep/im/doctors/'
                        ),
                    ]
                ),
            )
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '外科醫師介紹':
        try:
            message = TemplateSendMessage(
                alt_text='醫師介紹',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/9Axmlhw.jpg',
                    title='外科醫師介紹',
                    text='點選以下連結前往外科醫師介紹',
                    actions=[
                        URITemplateAction(
                            label='外科醫師介紹',
                            uri='https://d02536.wixsite.com/mysite/blank-14'
                        ),
                    ]
                )

            )
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '獨立部門醫師介紹':
        try:
            message = TemplateSendMessage(
                alt_text='醫師介紹',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/9Axmlhw.jpg',
                    title='獨立部門醫師介紹',
                    text='點選以下連結前往獨立部門醫師介紹',
                    actions=[
                        URITemplateAction(
                            label='獨立部門醫師介紹',
                            uri='https://www.hospital.fju.edu.tw/Team/ShowTeamItem?SelectGroup=%E7%8D%A8%E7%AB%8B%E9%83%A8%E7%A7%91&SelectID=DERM#txtSectionName'
                        ),

                    ]
                )

            )
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '探病時間/規定':
        file_path = os.path.join(os.path.abspath(
            '.'), '/a專題/下學期/coding/visit patient.json')
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        linebot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='探病時間/規定', contents=data)
        )
    elif mtext == '探病時間':
        try:
            message = [
                TextSendMessage(text="點開以下照片，查看探病時間"),
                ImageSendMessage(
                    original_content_url="https://imgur.com/P0LoDW4.png",
                    preview_image_url="https://imgur.com/P0LoDW4.png"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '醫院樓層介紹':
        try:
            message = TextSendMessage(
                text='選擇樓層B1~4F (5F~13F樓層為病房及私人辦公空間)',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="B1", text="B1")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="1F", text="1F")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2F", text="2F")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="3F", text="3F")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="4F", text="4F")
                        ),
                    ]
                )
            )
            linebot_api.reply_message(event.reply_token, message)

        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
    elif mtext == 'B1':
        try:
            message = [
                TextSendMessage(text="B1為停車場、藥庫、美食街"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/HmqZh8u.png",
                    preview_image_url="https://i.imgur.com/HmqZh8u.png"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '1F':
        try:
            message = [
                TextSendMessage(text="1F為大廳、藥局、住出院中心、影像醫學科"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/qEay675.png",
                    preview_image_url="https://i.imgur.com/qEay675.png"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
    elif mtext == '2F':
        try:
            message = [
                TextSendMessage(text="2F為批價掛號櫃台、門診、心血管中心"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/o7zGrMk.png",
                    preview_image_url="https://i.imgur.com/o7zGrMk.png"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
    elif mtext == '3F':
        try:
            message = [
                TextSendMessage(text="3F為批價掛號櫃台、檢驗科、門診"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/AtwEWe0.png",
                    preview_image_url="https://i.imgur.com/AtwEWe0.png"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
    elif mtext == '4F':
        try:
            message = [
                TextSendMessage(text="4F為圖書室、復健中心、血液暨腹膜透析中心"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/R24xIGc.png",
                    preview_image_url="https://i.imgur.com/R24xIGc.png"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
# 5 交通
    elif mtext == '交通':
        try:
            message = TemplateSendMessage(
                alt_text='交通項目',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/w2RzFG9.jpg',
                    title='交通資訊',
                    text='請選擇以下要了解的相關資訊',
                    actions=[
                        MessageTemplateAction(
                            label='接駁車班次',
                            text='接駁車班次'
                        ),
                        MessageTemplateAction(
                            label='醫院附近汽機車停車位',
                            text='醫院附近汽機車停車位'
                        )
                    ]
                )
            )
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '接駁車班次':
        try:
            message = TextSendMessage(
                text='選擇班次路線',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="北新莊線", text="北新莊線")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="板橋線", text="板橋線")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="輔大捷運線", text="輔大捷運線")
                        ),

                    ]
                )
            )
            linebot_api.reply_message(event.reply_token, message)

        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
    elif mtext == '北新莊線':
        try:
            message = [
                TextSendMessage(text="下圖是北新莊線時刻表"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/lhSWFqJ.png",
                    preview_image_url="https://i.imgur.com/lhSWFqJ.png"
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '醫院附近汽機車停車位':
        try:
            message = TextSendMessage(
                text='選擇機車或汽車停車場',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="機車", text="機車")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="汽車", text="汽車")
                        ),
                    ]
                )
            )
            linebot_api.reply_message(event.reply_token, message)

        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
    elif mtext == '機車':
        try:
            message = [
                TextSendMessage(text="醫院B1機車收費:臨停30元/次"),
                LocationSendMessage(
                    title='商一臨時平面停車場',
                    address='242新北市泰山區貴子路198-3號',
                    latitude=25.039568545319042,
                    longitude=121.43015252549947
                )
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))

    elif mtext == '汽車':
        try:
            message = [
                TextSendMessage(text="醫院B1汽車及及重機 收費:30元/時"),
                TextSendMessage(text="三泰路 文中三臨時停車場或路邊停車格"),
                ImageSendMessage(
                    original_content_url="https://i.imgur.com/cVsItld.jpg",
                    preview_image_url="https://i.imgur.com/cVsItld.jpg"
                ),
                LocationSendMessage(
                    title='商一臨時平面停車場',
                    address='242新北市泰山區貴子路198-3號',
                    latitude=25.039568545319042,
                    longitude=121.43015252549947
                ),
                LocationSendMessage(
                    title='輔仁大學地下停車場',
                    address='242新北市新莊區中正路510號',
                    latitude=25.038431588064356,
                    longitude=121.43146305739474
                ),
            ]
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))
# 6 資源查詢&其他
    elif mtext == '資源查詢&其他':
        try:
            message = TemplateSendMessage(
                alt_text='資源項目',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/lVRiqTv.jpg',
                    title='資源項目',
                    text='請選擇以下要了解的相關資訊',
                    actions=[
                        MessageTemplateAction(
                            label='醫院聯絡電話查詢',
                            text='醫院聯絡電話'
                        ),
                        URITemplateAction(
                            label='衛教網站',
                            uri='https://www.hospital.fju.edu.tw/Health/Index?GID=4#gsc.tab=0'
                        ),
                        URITemplateAction(
                            label='輔醫防疫平台',
                            uri='https://www.hospital.fju.edu.tw/Health/Content?CID=20220517#gsc.tab=0'
                        ),
                        URITemplateAction(
                            label='民眾回饋表單',
                            uri='http://scm.fjuh.fju.edu.tw/SCM.NSF/FRSP01.xsp'
                        ),
                    ]
                )
            )
            linebot_api.reply_message(event.reply_token, message)
        except:
            linebot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤'))


{
    "builds": [
        {
            "src": "api/index.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "api/index.py"
        }
    ]
}

if __name__ == '__main__':
    app.run()
