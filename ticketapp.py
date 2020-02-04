import os
import sys

from config import line_secret, line_access_token
from flask import Flask, request, abort, send_from_directory, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,FollowEvent,QuickReply,QuickReplyButton,MessageAction
from line_notify import LineNotify

app = Flask(__name__)

channel_secret = line_secret
channel_access_token = line_access_token

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

def linechat(text):
    
    ACCESS_TOKEN = "oK2sk4w1eidfRyOVfgIcln38TBS8JmL0PgfbbQ8t0Zv"

    notify = LineNotify(ACCESS_TOKEN)

    notify.send(text)

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
    text_from_user = event.message.text
    Reply_token = event.reply_token

    userid = event.source.user_id
    disname = line_bot_api.get_profile(user_id=userid).display_name
    request_text= (' ticket'+'\n' + '>> {} : {}').format(disname,text_from_user)
    
    print(request_text)
    linechat(request_text)

    try:
        if 'IQXUSTB' in text_from_user:

            from urllib.request import Request, urlopen
            from bs4 import BeautifulSoup as soup 

            def usdcheck():
                IQXUSTHB = '31.21'
                #1.06 1.12 0.94 0.88

                req = Request('https://th.investing.com/currencies/usd-thb', headers={'User-Agent': 'Chrome/78.0'})
                webopen = urlopen(req).read()

                data = soup(webopen, 'html.parser')

                usthbrate = data.findAll('div',{'class':'top bold inlineblock'})
                usthbrate = usthbrate[0].text
                usthbrate = usthbrate.replace('\n',' ')
                usthbrate = usthbrate.replace(',','')
                usthbrate = usthbrate[1:]
                usthbrate = usthbrate[0:6]

                xusthbrate = data.findAll('div',{'class':'top bold inlineblock'})
                xusthbrate = xusthbrate[0].text
                xusthbrate = xusthbrate.replace('\n',' ')
                xusthbrate = xusthbrate.replace(',','')
                xusthbrate = xusthbrate[1:]
                xusthbrate = xusthbrate[7:13]

                usthbspot = float(usthbrate)
                usthbspot = '%.2f'%usthbspot

                buy = float(usthbspot) + 0.02 #dif rate buy
                buy = '%.2f'%buy
                sale = float(usthbspot) - 0.06 #dif rate sale
                sale = '%.2f'%sale

                text1 = 'IQXUSTB >> ' 
                text2 = '\n' + IQXUSTHB +' >> ' + usthbrate + ' (' + xusthbrate + ')' + '\n' + 'ซื้อ ' + sale + ' / ขาย '+ buy

                if float(usthbspot) >= float(IQXUSTHB):
                    word_to_reply2 = text1 + 'ค่าเงินอ่อน' + text2
                else:
                    word_to_reply2 = text1 + 'ค่าเงินแข็ง' + text2
                
                print(word_to_reply2)
                word_to_reply1 = '{} '.format(disname) + 'ค้นข้อมูล ' + text_from_user

                text_to_reply1 = TextSendMessage(text = word_to_reply1)
                text_to_reply2 = TextSendMessage(text = word_to_reply2)

                line_bot_api.reply_message(
                        event.reply_token,
                        messages=[text_to_reply2]
                    )

            usdcheck()

        elif 'IQXWTI' in text_from_user:

            from urllib.request import Request, urlopen
            from bs4 import BeautifulSoup as soup 


            def wticheck():
                IQXWTI = '51.55'

                #1.06 1.12 0.94 0.88

                targetUp_01 = float(IQXWTI) * 1.06
                targetUp_01 = '%.2f'%targetUp_01

                targetUp_02 = float(IQXWTI) * 1.12
                targetUp_02 = '%.2f'%targetUp_02
                
                targetDown_01 = float(IQXWTI) * 0.94
                targetDown_01 = '%.2f'%targetDown_01

                targetDown_02 = float(IQXWTI) * 0.88
                targetDown_02 = '%.2f'%targetDown_02

                req = Request('https://th.investing.com/commodities/crude-oil', headers={'User-Agent': 'Chrome/78.0'})
                webopen = urlopen(req).read()

                data = soup(webopen, 'html.parser')

                wtirate = data.findAll('div',{'class':'top bold inlineblock'})
                wtirate = wtirate[0].text
                wtirate = wtirate.replace('\n',' ')
                wtirate = wtirate.replace(',','')
                wtirate = wtirate[1:]
                wtirate = wtirate[0:6]

                xwtirate = data.findAll('div',{'class':'top bold inlineblock'})
                xwtirate = xwtirate[0].text
                xwtirate = xwtirate.replace('\n',' ')
                xwtirate = xwtirate.replace(',','')
                xwtirate = xwtirate[1:]
                xwtirate = xwtirate[6:11]

                wtispot = float(wtirate)
                wtispot = '%.2f'%wtispot

                text1 = 'IQXWTI >> Long' + '\n' + IQXWTI +' >> ' + wtispot + ' (' + xwtirate + ')' + '\n' + 'X : {} / {}'.format(targetUp_01,targetUp_02)
                text2 = 'IQXWTI >> Short' + '\n' + IQXWTI +' >> ' + wtispot + ' (' + xwtirate + ')' + '\n' + 'X : {} / {}'.format(targetDown_01,targetDown_02)

                if float(wtispot) >= float(IQXWTI):
                    word_to_reply3 = text1 
                else:
                    word_to_reply3 = text2
                
                print(word_to_reply3)
                word_to_reply1 = '{} '.format(disname) + 'ค้นข้อมูล ' + text_from_user

                text_to_reply1 = TextSendMessage(text = word_to_reply1)
                text_to_reply3 = TextSendMessage(text = word_to_reply3)

                line_bot_api.reply_message(
                        event.reply_token,
                        messages=[text_to_reply3]
                    )
            wticheck()

        elif 'IQXGL' in text_from_user:

            from urllib.request import Request, urlopen
            from bs4 import BeautifulSoup as soup 

            def goldcheck():
                IQXGL = '1589.69'
                #1.06 1.12 0.94 0.88

                targetUp_01 = float(IQXGL) * 1.06
                targetUp_01 = '%.2f'%targetUp_01

                targetUp_02 = float(IQXGL) * 1.12
                targetUp_02 = '%.2f'%targetUp_02
                
                targetDown_01 = float(IQXGL) * 0.94
                targetDown_01 = '%.2f'%targetDown_01

                targetDown_02 = float(IQXGL) * 0.88
                targetDown_02 = '%.2f'%targetDown_02

                req = Request('https://th.investing.com/currencies/xau-usd', headers={'User-Agent': 'Chrome/78.0'})
                webopen = urlopen(req).read()

                data = soup(webopen, 'html.parser')

                goldrate = data.findAll('div',{'class':'top bold inlineblock'})
                goldrate = goldrate[0].text
                goldrate = goldrate.replace('\n',' ')
                goldrate = goldrate.replace(',','')
                goldrate = goldrate[1:]
                goldrate = goldrate[0:8]

                xgoldrate = data.findAll('div',{'class':'top bold inlineblock'})
                xgoldrate = xgoldrate[0].text
                xgoldrate = xgoldrate.replace('\n',' ')
                xgoldrate = xgoldrate.replace(',','')
                xgoldrate = xgoldrate[9:]
                xgoldrate = xgoldrate[0:5]

                gspot = float(goldrate)
                gspot = '%.2f'%gspot
                gspot = str(gspot)

                text1 = 'IQXGL >> ' 
                text2 = '\n' + IQXGL +' >> ' + gspot + ' (' + xgoldrate + ')' + '\n' + 'X : {} / {}'.format(targetUp_01,targetUp_02)
                text3 = '\n' + IQXGL +' >> ' + gspot + ' (' + xgoldrate + ')' + '\n' + 'X : {} / {}'.format(targetDown_01,targetDown_02)

                if float(gspot) >= float(IQXGL):
                    word_to_reply4 = text1 + 'Long' + text2
                
                else:
                    word_to_reply4 = text1 + 'Short' + text3

                print(word_to_reply4)
                word_to_reply1 = '{} '.format(disname) + 'ค้นข้อมูล ' + text_from_user

                text_to_reply1 = TextSendMessage(text = word_to_reply1)
                text_to_reply4 = TextSendMessage(text = word_to_reply4)

                line_bot_api.reply_message(
                        event.reply_token,
                        messages=[text_to_reply4]
                    )
            goldcheck()

        elif 'TFEX' in text_from_user:
            from urllib.request import urlopen as req
            from bs4 import BeautifulSoup as soup 

            def tfexcheck():

                url = 'https://www.tfex.co.th/tfex/dailySeriesQuotation.html?locale=th_TH&symbol=S50H20'
                webopen = req(url)
                page_html = webopen.read()
                webopen.close()

                data = soup(page_html, 'html.parser')

                main = data.findAll('span',{'class':'h2'})

                tx = main[0].text
                tx = tx.replace('\n','')
                tx = tx.replace('\r','')
                tx = tx.replace(' ','')
                tx = tx.replace(',','')

                sub = data.findAll('span',{'class':'h3'})
                ux = sub[0].text
                ux = ux.replace('\n','')
                ux = ux.replace('\r','')
                ux = ux.replace(' ','')

                cx = sub[1].text
                cx = cx.replace('\n','')
                cx = cx.replace('\r','')
                cx = cx.replace(' ','')

                return[tx,ux,cx]

            def dailytfex():
                tfexx = '1013.20'
                #1.007 1.015 0.993 0.986
                tff = tfexcheck()
            
                targetUp_01 = float(tff[0]) * 1.007
                targetUp_01 = '%.2f'%targetUp_01

                targetUp_02 = float(tff[0]) * 1.015
                targetUp_02 = '%.2f'%targetUp_02
                
                targetDown_01 = float(tff[0]) * 0.993
                targetDown_01 = '%.2f'%targetDown_01

                targetDown_02 = float(tff[0]) * 0.986
                targetDown_02 = '%.2f'%targetDown_02

                text3 = 'S50H20 Today :' + '\n'+ tfexx +' > '+ tff[0] +' ('+ tff[1] +') ' + '\n'+'Status : Long' + '\n' + 'X : {} / {}'.format(targetUp_01,targetUp_02)
                text4 = 'S50H20 Today :' + '\n'+ tfexx +' > '+ tff[0] +' ('+ tff[1] +') ' + '\n'+ 'Status : Short' + '\n' + 'X : {} / {}'.format(targetDown_01,targetDown_02)
                
                float(tff[0])
                if float(tff[0]) >= float(tfexx): 
                    word_to_reply2 = text3 
                else:
                    word_to_reply2 = text4

                print(word_to_reply2)
                word_to_reply1 = '{} '.format(disname) + 'ค้นข้อมูล ' + text_from_user

                text_to_reply1 = TextSendMessage(text = word_to_reply1)
                text_to_reply2 = TextSendMessage(text = word_to_reply2)

                line_bot_api.reply_message(
                        event.reply_token,
                        messages=[text_to_reply2]
                    )
            dailytfex()

        elif 'SET' in text_from_user:

            from urllib.request import urlopen as req
            from bs4 import BeautifulSoup as soup 

            def setcheck():

                url = 'https://www.settrade.com/C13_MarketSummary.jsp?detail=SET'
                webopen = req(url)
                page_html = webopen.read()
                webopen.close()

                data = soup(page_html, 'html.parser')

                currency = data.findAll('div',{'class':'col-xs-12'})

                st = currency[0].text
                st = st.replace('\n',' ')
                st = st.replace('\r',' ')
                st = st.replace('\n',' ')
                st = st[3316:]
                st = st[0:9]
                st = st.replace(',','')

                chg = currency[0].text
                chg = chg.replace('\n',' ')
                chg = chg.replace('\r',' ')
                chg = chg.replace('\n',' ')
                chg = chg[3325:]
                chg = chg[0:5]

                return[st,chg]

            def dailyset():
                sett = '1514.14'
                #1.007 1.015 0.993 0.986
                st = setcheck()

                targetUp_01 = float(st[0]) * 1.007
                targetUp_01 = '%.2f'%targetUp_01

                targetUp_02 = float(st[0]) * 1.015
                targetUp_02 = '%.2f'%targetUp_02
                
                targetDown_01 = float(st[0]) * 0.993
                targetDown_01 = '%.2f'%targetDown_01

                targetDown_02 = float(st[0]) * 0.986
                targetDown_02 = '%.2f'%targetDown_02

                text1 = 'SET Today :' + '\n' + sett +' > '+ st[0] +' ('+st[1]+') ' + '\n' + 'Status : Buy' + '\n' + 'X : {} / {}'.format(targetUp_01,targetUp_02)
                text2 = 'SET Today :' + '\n' + sett +' > '+ st[0] +' ('+st[1]+') ' + '\n' + 'Status : Hold' + '\n' + 'X : {} / {}'.format(targetDown_01,targetDown_02)

                float(st[0])

                if float(st[0]) >= float(sett): 
                    word_to_reply2 = text1 

                else:
                    word_to_reply2 = text2


                print(word_to_reply2)
                word_to_reply1 = '{} '.format(disname) + 'ค้นข้อมูล ' + text_from_user

                text_to_reply1 = TextSendMessage(text = word_to_reply1)
                text_to_reply2 = TextSendMessage(text = word_to_reply2)

                line_bot_api.reply_message(
                        event.reply_token,
                        messages=[text_to_reply2]
                    )
            dailyset()

        else:
                    
            from bs4 import BeautifulSoup as soup 
            from urllib.request import urlopen as req
            from pandas_datareader import data 
            from datetime import datetime

            code = text_from_user
            ticket = [text_from_user]
            symbols = list(map(lambda e: e + '.bk', ticket))
            
            def request(code):
                url = 'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol={}&ssoPageId=10&selectPage=2'.format(code)
                webopen = req(url)
                page_html = webopen.read()
                webopen.close()

                data = soup(page_html, 'html.parser')

                price = data.findAll('div',{'class':'col-xs-6'})

                title = price[0].text
                stockprice = price[2].text

                change = price[3].text
                change = change.replace('\n','')
                change = change.replace('\r','')
                change = change.replace('\t','')
                change = change.replace(' ','')
                change = change[11:]

                pchange = price[4].text
                pchange = pchange.replace('\n','')
                pchange = pchange.replace('\r','')
                pchange = pchange.replace(' ','')
                pchange = pchange[12:]

                update = data.findAll('span',{'class':'stt-remark'})

                stockupdate = update[0].text
                stockupdate = stockupdate[13:]

                return [title,stockprice,change,pchange,stockupdate]

            r = request(code)

            text_request = '{} {} ({})'.format(r[0], r[1], r[2])

            class stock:
                def __init__(self,stock):
                    self.stock = stock

                def ticket(self):
                    end = datetime.now()
                    start = datetime(end.year,end.month,end.day)
                    list = self.stock

                    dfY = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
                    dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-02-01', end=end)
                    dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-02-01', end=end)

                    #2020-01-01 = Y M D

                    list = list.replace('.bk','')
                                
                    OpenY = dfY['Open'].iloc[0]
                    OpenY  = '%.2f'%OpenY
                    OpenY = str(OpenY)

                    OpenM = dfM['Open'].iloc[0]
                    OpenM  = '%.2f'%OpenM
                    OpenM = str(OpenM)

                    OpenW = dfM['Open'].iloc[0]
                    OpenW  = '%.2f'%OpenW
                    OpenW = str(OpenW)

                    Close = float(f'{r[1]}')
                    Close  = '%.2f'%Close
                    Close = str(Close)

                    endday = float(f'{r[2]}')
                    endday = '%.2f'%endday
                    endday = str(endday)

                    barY = ((float(Close) - float(OpenY)) / float(OpenY) )*100
                    barY = '%.2f'%barY
                    barY = float(barY)

                    barM = ((float(Close) - float(OpenM)) / float(OpenM) )*100
                    barM = '%.2f'%barM
                    barM = float(barM)

                    barW = ((float(Close) - float(OpenW)) / float(OpenW) )*100
                    barW = '%.2f'%barW
                    barW = float(barW)

                    Volume1 = dfM['Volume'].iloc[-1]
                    Volume2 = dfM['Volume'].iloc[-2]
                    Volume = (float(Volume1)+float(Volume2))/2
                    Volume  = '%.0f'%Volume
                    Volume = str(Volume)

                    value = float(Volume) * float(Close)
                    value  = '%.2f'%value
                    value = str(value)

                    request_val = float(value) 
                    request_val  = '{:,.0f}'.format(request_val)
                    request_val = str(request_val)
                    
                    exitM1 = float(OpenM) * 1.06
                    exitM1 = '%.2f'%exitM1
                    exitM1 = str(exitM1)

                    exitM2 = float(OpenM) * 1.16
                    exitM2 = '%.2f'%exitM2
                    exitM2 = str(exitM2)

                    exitM3 = float(OpenM) * 1.26
                    exitM3 = '%.2f'%exitM3
                    exitM3 = str(exitM3)

                    buyM = float(OpenM) * 1.01
                    buyM = '%.2f'%buyM
                    buyM = str(buyM) 

                    stopM = float(OpenM) * 0.985
                    stopM = '%.2f'%stopM
                    stopM = str(stopM) 

                    exitY1 = float(OpenY) * 1.06
                    exitY1 = '%.2f'%exitY1
                    exitY1 = str(exitY1)

                    exitY2 = float(OpenY) * 1.16
                    exitY2 = '%.2f'%exitY2
                    exitY2 = str(exitY2)

                    exitY3 = float(OpenY) * 1.26
                    exitY3 = '%.2f'%exitY3
                    exitY3 = str(exitY3)

                    buyY = float(OpenY) * 1.01
                    buyY = '%.2f'%buyY
                    buyY = str(buyY) 

                    stopY = float(OpenY) * 0.985
                    stopY = '%.2f'%stopY
                    stopY = str(stopY) 

                    text1 = '\n' + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
                    text2 = '\n' + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
                    text3 = 'กำลังย่อ'  + '\n' + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
                    text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
                    text5 = 'ซื้อขายน้อย' +'\n' +text_request + '\n' + 'Val : ' + request_val + '\n' + 'Vol : ' + Volume
                    alert = 'ชนแนวต้าน'
                    alert2 = 'ไปต่อ'
                    notice = 'ซื้อ'

                    if float(value) > 7500000:
                        if barY >= 0:
                            if barM > 6.00:
                                word_to_reply2 = str(alert + text1)
                            elif 6.00 >= barM >= 3.00:
                                if barW >= 0:
                                    word_to_reply2 = str(alert2 + text1)
                                else:
                                    word_to_reply2 = str(text3)
                            elif 3.00 > barM >= 0.00:
                                if barW >= 0:
                                    word_to_reply2 = str(notice + text1)
                                else:
                                    word_to_reply2 = str(text3)
                            else:
                                word_to_reply2 = str(text4)
                        elif barM >= 0:
                            if barM > 6.00:
                                word_to_reply2 = str(alert + text2)
                            elif 6.00 >= barM >= 3.00:
                                if barW >= 0:
                                    word_to_reply2 = str(alert2 + text2)
                                else:
                                    word_to_reply2 = str(text3)
                            elif 3.00 > barM >= 0.00:
                                if barW >= 0:
                                    word_to_reply2 = str(notice + text2)
                                else:
                                    word_to_reply2 = str(text3)
                            else:
                                word_to_reply2 = str(text4)                  
                        else:
                            word_to_reply2 = str(text4)
                    else:
                        word_to_reply2 = str(text5)

                    print(word_to_reply2)

                    text_to_reply2 = TextSendMessage(text = word_to_reply2)
                    line_bot_api.reply_message(
                            event.reply_token,
                            messages=[text_to_reply2]
                        )
                    
            for symbol in symbols:
                stock(symbol).ticket()
    except:
        text_list = [
            '{} พิมพ์ชื่อหุ้น {} ผิด ลองใหม่อีกครั้ง'.format(disname, text_from_user),
            '{} ไม่มีในฐานข้อมูล {} ลองใหม่อีกครั้ง'.format(text_from_user,disname),

        ]

        from random import choice
        word_to_reply = choice(text_list)
        
        text_to_reply = TextSendMessage(text = word_to_reply)

        line_bot_api.reply_message(
                event.reply_token,
                messages=[text_to_reply]
            )

@handler.add(FollowEvent)
def RegisRichmenu(event):
    userid = event.source.user_id
    disname = line_bot_api.get_profile(user_id=userid).display_name
    line_bot_api.link_rich_menu_to_user(userid,'richmenu-d0e50386b9bfe1a8621db0175920589e')

    button_1 = QuickReplyButton(action=MessageAction(lable='IQXUSTB',text='IQXUSTB'))
    button_2 = QuickReplyButton(action=MessageAction(lable='IQXGL',text='IQXGL'))
    button_3 = QuickReplyButton(action=MessageAction(lable='IQXWTI',text='IQXWTI'))
    button_4 = QuickReplyButton(action=MessageAction(lable='SET',text='SET'))
    button_5 = QuickReplyButton(action=MessageAction(lable='TFEX',text='TFEX'))

    answer_button = QuickReply(items=[button_1,button_2,button_3,button_4,button_5])

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    #print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)