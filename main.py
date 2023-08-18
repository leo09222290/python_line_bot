#2023/06/09
#主1
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
# 載入 TextSendMessage 和 LocationSendMessage 模組
from linebot.models import TextSendMessage, LocationSendMessage
import json
import recommend

app = Flask(__name__)
flag_menu = 0
rest_dic = {}
@app.route("/", methods=['POST'])
def linebot():
    global flag_menu
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi('vQbpOEtMx3CFy6oEkr2VWqlBOinPP9mGXKyXRprGCjGAcYrmtdEYJFfTMNirTCd+JFvGjo5HozayUKYIX/PRdItUZ0IXjnQWFZzaLhXIbBda2m4Qt1bdw7m9QhXOYpVBbCgBMqMHdWNJ0yPy2vDdUgdB04t89/1O/w1cDnyilFU=')
        handler = WebhookHandler('d3e36ec9bd30b54f1d1240b3e5aecb6a')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']
        msg = json_data['events'][0]['message']['text']
        # 取得對應的地址，如果沒有取得，會是 False
        # send_msg(msg)
        print(type(msg))
        print(msg)
        if (flag_menu == 0):
            print("OK")
            if (msg == '1'):
                flag_menu = 1
                text_message = TextSendMessage(text='請輸入要搜尋的地標')
                line_bot_api.reply_message(tk,text_message)
                #print("into1")
            elif (msg == '2'):
                #print("into2")
                flag_menu = 2
                text_message = TextSendMessage(text='請輸入捷運站站名')
                line_bot_api.reply_message(tk,text_message)
            elif (msg == '3'):
                flag_menu = 3
            else:
                flag_menu = 0
        else:
            #print("FAIL")
            if (flag_menu == 1):
               #print("into1-1")
                location_dect = reply_location(msg)
                if location_dect:
                    location_message = LocationSendMessage(title=location_dect['title'],\
                                                         address=location_dect['address'],\
                                                          latitude=location_dect['latitude'],\
                                                          longitude=location_dect['longitude'])
                    line_bot_api.reply_message(tk,location_message)
                    flag_menu = 0
                else:
                    # 如果是 False，回傳文字
                    text_message = TextSendMessage(text='找不到相關地點')
                    line_bot_api.reply_message(tk,text_message)
                    flag_menu = 1
            elif (flag_menu == 2):
                rest_dic = recommend.recommend(msg)
                str_msg=""
                list1= ['餐廳名稱: ','地址: ','營業時間: ']
                for i in range(5):
                    for j in range(3):
                        str_msg += list1[j]
                        str_msg += rest_dic[i][j]
                        str_msg += '\n'
                    str_msg += '-------------------------------\n'
                text_message = TextSendMessage(text = str_msg)
                line_bot_api.reply_message(tk,text_message)
                flag_menu = 0
            elif (flag_menu == 3):
                print("do 3")
                flag_menu = 0
    except:
        print('error')
    return 'OK'

# def send_msg(msg):

# 建立回覆地點的函式
def reply_location(text):
    # 建立地點與文字對應的字典
    with open("Taipei.json","r", encoding='utf-8') as file:
        location = json.load(file)
    if text in location:
      return location[text]
    else:
      # 如果找不到對應的地點，回傳 False
      return False

if __name__ == "__main__":
    # Colab 才需要，本機環境請刪除
    #run_with_ngrok(app)
    app.run()