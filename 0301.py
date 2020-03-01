import requests
import datetime
import sys

#market_code = "sh" #sz
print("input market code: ")
market_code = input()
#stock_code = "601318"
print("input stock code: ")
stock_code = input()
cur_time = datetime.datetime.now() + datetime.timedelta(days=-2)
print(cur_time)
#cur_date = cur_time.strftime('%Y%m%d')
print("input current date: ")
cur_date = input()
print(cur_date)
cur_date_6 = cur_date[2 : 8]
print(cur_date_6)

#url = "http://hq.sinajs.cn/list=sh601318"
url = "http://data.gtimg.cn/flashdata/hushen/latest/daily/" + market_code + stock_code + ".js"
print('visit url: ' + url)
res = requests.get(url)
#print(res.text)
#print(len(res.text))

price_start_index = res.text.find(cur_date_6) + 7
price_today = res.text[price_start_index : len(res.text)]
price_end_index = price_today.find("\\n\\")
price_today = price_today[0 : price_end_index]
price_list = price_today.split(' ')
print(price_list)
open = price_list[0]
close = price_list[1]
high = price_list[2]
low = price_list[3]
volumn = price_list[4]
print("open=" + open + " close=" + close + " high=" + high + " low=" + low + " volumn=" + volumn)

#pause
input()

