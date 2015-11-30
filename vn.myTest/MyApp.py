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
        self.mp = MarketPrice()
    

def main():
    myapp = MyApp()
    myapp.mp.Subscibe_realtime_data("002740.SZ","rt_time,rt_latest")

if __name__ == '__main__':
    main()