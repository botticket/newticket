def update1():
	try:
		from bs4 import BeautifulSoup as soup 
		from urllib.request import urlopen as req
		from pandas_datareader import data 
		from datetime import datetime
		import config_ticket as cty

		text_from_user = 'ADVANC'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'AMATA'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()
		
		text_from_user = 'AOT'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()
		
		text_from_user = 'AU'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'BAM'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'BCH'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'BCPG'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'BDMS'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'BEM'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'BGRIM'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'BJC'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'BTS'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'CPALL'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'CPF'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'COM7'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()
	except:
		print('Scan error')

def update2():
	try:
		text_from_user = 'DOHOME'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()
		
		text_from_user = 'DTAC'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'DIF'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'EA'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()
		
		text_from_user = 'ESSO'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()
	
		text_from_user = 'GFPT'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()
	
		text_from_user = 'GGC'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()
		
		text_from_user = 'GLOBAL'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()
		
		text_from_user = 'GPSC'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()
		
		text_from_user = 'GULF'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'HANA'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'HMPRO'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'INTUCH'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()
		
		text_from_user = 'IVL'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'KCE'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'KTC'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'MTC'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

	except:
		print('Scan error')

def update3():
	try:
		text_from_user = 'OSP'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'PRM'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'PTG'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'PTT'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'PTTEP'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'PTTGC'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'RATCH'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'SAWAD'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'SGP'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'RS'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'STEC'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'TASCO'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'TOP'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'TFG'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'TCAP'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'TKN'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()

		text_from_user = 'WHAUP'
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
				dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
				dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-20', end=end)

				#2020-01-01 = Y M D

				list = list.replace('.bk','')
							
				OpenY = dfY['Open'].iloc[0]
				OpenY  = '%.2f'%OpenY
				OpenY = str(OpenY)

				OpenM = dfM['Open'].iloc[0]
				OpenM  = '%.2f'%OpenM
				OpenM = str(OpenM)

				OpenW = dfW['Open'].iloc[0]
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

				Volume = dfM['Volume'].iloc[-1]
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

				text1 = text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text2 = text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM +'\n' + 'X ' + exitM1 + ' | ' + exitM2 + ' | ' + exitM3 
				text3 = 'รอซื้อ' + '\n'  + text_request +'\n' + 'Y ' + OpenY + ' ({} %)'.format(barY) +'\n' + 'B ' + stopY + ' ~ '+ buyY 
				text4 = 'อย่าเพิ่งเข้า' + '\n'  + text_request +'\n' + 'O ' + OpenM + ' ({} %)'.format(barM) +'\n' + 'B ' + stopM + ' ~ '+ buyM 
				text5 = text_request + '\n' + 'ซื้อขายน้อย' + '\n' + 'Val : ' + request_val 
				alert = '\n'  +'ชนแนวต้าน'

				if float(value) > 15000000:
					if barW >= 0:
						if barY >= 0:
							if barM > 6.00:
								word_to_reply2 = str(text1 + alert)
								cty.linechat(text1 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text1)
							else:
								word_to_reply2 = str(text3)
						elif barM >= 0.00:
							if barM > 6.00:
								cty.linechat(text2 + alert)
								word_to_reply2 = str(text2 + alert)
							elif 3.00 > barM >= 0.00:
								cty.linechat(text1)
								word_to_reply2 = str(text2)
							else:
								word_to_reply2 = str(text4)
						else:
							word_to_reply2 = str(text4)
					else:
						word_to_reply2 = str(text4)

				else:
					word_to_reply2 = str(text5)
				
				print(word_to_reply2)
				print('\n' + '------' + '\n')
				
		for symbol in symbols:
			stock(symbol).ticket()
	except:
		print('Scan error')
