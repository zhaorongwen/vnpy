# -*- coding:utf-8 -*- 
import tushare as ts
import sys

class MyApp(object):
    """description of class"""
    
    def __init__(self):
        print('HI this is me')
        print('大家好这是我')
        df = ts.get_today_all()
        print(df)

def main():
    myapp = MyApp()

if __name__ == '__main__':
    main()