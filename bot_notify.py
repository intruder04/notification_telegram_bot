import telepot
import pymysql
import pymysql.cursors
import sys
import time
import threading
from telepot.loop import MessageLoop

token = 'tokenhere'
TelegramBot = telepot.Bot(token)
# print (TelegramBot.getMe())
# response = TelegramBot.getUpdates()
# print(response)
interval = 60

def makeQuery(query):
    try:
        # Connect to the database
        connection = pymysql.connect(host='127.0.0.1',port=3306,user='',password='',db='',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = query
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
            return result
    finally:
        connection.close()

def getNewOrders():
    new_order_query = 'SELECT `sb_id`,`descr`, `company`.`companyname`,from_unixtime(`date_created`, \'%Y-%m-%d %H:%i\') from requests LEFT JOIN `company` on company.id = requests.company_id WHERE `date_created` >= unix_timestamp(CURRENT_TIMESTAMP - INTERVAL ' + str(interval) + ' MINUTE)'
    new_orders = makeQuery(new_order_query)
    new_orders_string = ''
    if new_orders:
        for order_dict in new_orders:
            # print(type(order_dict))
            new_orders_string = new_orders_string + order_dict['sb_id'] + '; Компания - ' + order_dict['companyname'] + '; ' + order_dict['descr'] + "\n"
        print(new_orders_string)
        TelegramBot.sendMessage('-1001107728433', 'Новые заявки на портале за ' + str(interval) + "минут:\n" + new_orders_string)
    # threading.Timer(interval, getNewOrders).start() # called every minute

getNewOrders()

