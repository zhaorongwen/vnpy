# -*- coding:utf-8 -*- 
import tushare as ts
from MarketPrice import *
from MyEventEngine import *
from datetime import datetime

class MyApp(object):
    """description of class"""
    
    def __init__(self):
        print('HI this is me')
        print('大家好这是我')
        mp = MarketPrice()
        mp.Get_history_price()

def main():
    myapp = MyApp()

    def simpletest(event):
        print(u'处理每秒触发的计时器事件：%s' % str(datetime.now()))
    
    ee = EventEngine()
    ee.register(EVENT_TIMER, simpletest)
    ee.start()

if __name__ == '__main__':
    main()