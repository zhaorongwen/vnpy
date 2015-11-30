from WindPy import w
import MyEventEngine

class MarketPriceEvent:
    EVENT_MARKET_PRICE = "eMaketPrice"




class MarketPrice(object):
    """
    Use this class to get market price.

    private member:
        __event_engine: a event engine to handle the callbackFunc event;

    """

    def __init__(self):
        self.__event_engine = MyEventEngine.EventEngine()
        w.start(waitTime=10)
        self.__event_engine.register(MarketPriceEvent.EVENT_MARKET_PRICE,self.On_subscribe_realtime_data)
        self.__event_engine.start()

    def Get_history_price(self):
        pass
    
    def Get_realtime_price(self):
        pass

    def Subscibe_realtime_data(self,stock,indicates):
        w.wsq(stock,indicates, func=lambda indata:self.__event_engine.put(MyEventEngine.Event(eventType=MarketPriceEvent.EVENT_MARKET_PRICE,eventData=indata)))

    def On_subscribe_realtime_data(self,eventData):
        print(eventData)

    def SimulateTrading(self):
        pass