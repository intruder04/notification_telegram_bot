import telepot
import pymysql
import pymysql.cursors
import sys
import time
import threading
from telepot.loop import MessageLoop

token = 'tokenhere'
TelegramBot = telepot.Bot(token)
interval = 200

def handle(msg):
    print(msg)

MessageLoop(TelegramBot, handle).run_as_thread()
print ('Listening ...')

while 1:
    time.sleep(5)