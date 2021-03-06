# -*- coding:utf-8 -*- 

# 系统模块
import threading
from queue import Queue, Empty
from threading import Thread

# 自己开发的模块
from eventType import *


########################################################################
class EventEngine:
    """
    事件驱动引擎
    
    __queue：私有变量，事件队列
    __active：私有变量，事件引擎开关
    __thread：私有变量，事件处理线程
    __handlers：私有变量，事件处理函数字典
    
    方法说明
    __run: 私有方法，事件处理线程连续运行用
    __process: 私有方法，处理事件，调用注册在引擎中的监听函数
    __onTimer：私有方法，计时器固定事件间隔触发后，向事件队列中存入计时器事件
    start: 公共方法，启动引擎
    stop：公共方法，停止引擎
    register：公共方法，向引擎中注册监听函数
    unregister：公共方法，向引擎中注销监听函数
    put：公共方法，向事件队列中存入新的事件
    
    事件监听函数必须定义为输入参数仅为一个event对象，即：
    
    函数
    def func(event)
        ...
    
    对象方法
    def method(self, event)
        ...
        
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """初始化事件引擎"""
        # 事件队列
        self.__queue = Queue()
        
        # 事件引擎开关
        self.__active = False
        
        # 事件处理线程
        self.__thread = Thread(target = self.__run)
        
        # 这里的__handlers是一个字典，用来保存对应的事件调用关系
        # 其中每个键对应的值是一个列表，列表中保存了对该事件进行监听的函数功能
        self.__handlers = {}
        
    #----------------------------------------------------------------------
    def __run(self):
        """引擎运行"""
        while self.__active == True:
            try:
                print("now in thread now")
                print(threading.current_thread())
                event = self.__queue.get(block = True, timeout = 1)  # 获取事件的阻塞时间设为1秒
                self.__process(event)
            except Empty:
                pass
            
    #----------------------------------------------------------------------
    def __process(self, event):
        """处理事件"""
        # 检查是否存在对该事件进行监听的处理函数
        if event.eventType in self.__handlers:
            # 若存在，则按顺序将事件传递给处理函数执行
            for handler in self.__handlers[event.eventType]:
                handler(event)    

    #----------------------------------------------------------------------
    def __onTimer(self,tick):
        """向事件队列中存入计时器事件"""
        # 创建计时器事件
        event = Event(eventType=EVENT_TIMER)
        
        # 向队列中存入计时器事件
        self.put(event)

        # set a timer to add triggle the onTimer func again
        threading.Timer(tick,self.__onTimer,args =[tick]).start();

    #----------------------------------------------------------------------
    def start(self):
        """引擎启动"""
        # 将引擎设为启动
        self.__active = True
        
        # 启动事件处理线程
        self.__thread.start()
        
        # 启动计时器，计时器事件间隔默认设定为1秒
        tick = 1
        threading.Timer(tick,self.__onTimer,args=[tick]).start();
    
    #----------------------------------------------------------------------
    def stop(self):
        """停止引擎"""
        # 将引擎设为停止
        self.__active = False
        
        # 停止计时器
        self.__timer.stop()
        
        # 等待事件处理线程退出
        self.__thread.join()
            
    #----------------------------------------------------------------------
    def register(self, eventType, handler):
        """注册事件处理函数监听"""
        # 尝试获取该事件类型对应的处理函数列表，若无则创建
        try:
            handlerList = self.__handlers[eventType]
        except KeyError:
            handlerList = []
            self.__handlers[eventType] = handlerList
        
        # 若要注册的处理器不在该事件的处理器列表中，则注册该事件
        if handler not in handlerList:
            handlerList.append(handler)
            
    #----------------------------------------------------------------------
    def unregister(self, eventType, handler):
        """注销事件处理函数监听"""
        # 尝试获取该事件类型对应的处理函数列表，若无则忽略该次注销请求
        try:
            handlerList = self.__handlers[eventType]
            
            # 如果该函数存在于列表中，则移除
            if handler in handlerList:
                handlerList.remove(handler)

            # 如果函数列表为空，则从引擎中移除该事件类型
            if not handlerList:
                del self.handlers[eventType]
        except KeyError:
            pass     

    #----------------------------------------------------------------------
    def put(self, event):
        """向事件队列中存入事件"""
        self.__queue.put(event)

    #----------------------------------------------------------------------
    def List_all_register_events(self):
        """List all the register evnets"""
        return self.__handlers.keys()


########################################################################
class Event:
    """事件对象"""

    #----------------------------------------------------------------------
    def __init__(self, eventType=None,eventData=None):
        """Constructor"""
        self.eventType = eventType      # 事件类型
        self.data = {}         # 字典用于保存具体的事件数据

    def Add(key,value):
        self.data[key] = value;
#----------------------------------------------------------------------
def test():
    """测试函数"""
    import sys
    from datetime import datetime
    
    def simpletest(event):
        event1 = Event(eventType="EVENT_TEST")
        event1.data = {'data':100}
        ee.put(event1)
        print('处理每秒触发的计时器事件：%s' % str(datetime.now()))
    
    def simpleEEtest(event):
        print(event.data)
    
    ee = EventEngine()
    #ee.register(EVENT_TIMER, simpletest)
    #ee.register("EVENT_TEST",simpleEEtest)
    ee.start()

# 直接运行脚本可以进行测试
if __name__ == '__main__':
    test()
