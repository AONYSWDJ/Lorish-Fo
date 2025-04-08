from XtTraderPyApi import *
import time
import math

'''
本demo用于展示python traderapi的工作机制，该demo提供普通委托和各种算法委托下单以及撤单接口，分别展示了同步和异步接口的使用方式，供您选择
同步异步区别：
定义：同步和异步关注的是消息通信机制 (synchronous communication/ asynchronous communication)。
同步，就是调用某个东西是，调用方得等待这个调用返回结果才能继续往后执行。
异步，和同步相反  调用方不会理解得到结果，而是在调用发出后调用者可用继续执行后续操作，被调用者通过状体来通知调用者，或者通过回掉函数来处理这个调用
具体可以参考 https://www.cnblogs.com/IT-CPC/p/10898871.html
'''

# CallBack类继承XtTraderApiCallback类，用于接收请求以及主推的回调
class CallBack(XtTraderApiCallback):
    def __init__(self, address, username, password):
        super(CallBack, self).__init__()
        self.m_strAddress = address
        self.m_strUserName = username
        self.m_strPassword = password
        self.m_strFutureAccountKey = ''
        self.m_strFutureAccountID = ''
        self.m_strStkAccountID = ''
        self.m_strStkAccountKey = ''
        self.m_nRequestId = 1
        self.m_client = None
        self.m_nLogined = 0
        self.m_codeList = [
                #市场， 代码, 平台号(平台号期货填20001，其他可以默认0)
                ("SH","600000", 0),
                ("SH","600004", 0),
                ("SZ","000001", 0 ),
                ("SH","000001", 0 ),
                ("CFFEX","IF2311", 20001),
            ]

    def init(self):
        if self.m_strAddress == None:
            return -1, u'server address is empty'
        self.m_client = XtTraderApi.createXtTraderApi(self.m_strAddress)   #创建用户
        if self.m_client == None:
            return -1, u'failed to create traderapi client'
        if isinstance(self,XtTraderApiCallback):                         #当前类是否为父类的实例
            self.m_client.setCallback(self)
            return self.m_client.init("../config")
        return 0, u''

    def join(self):
        self.m_client.joinAll()
        #self.m_client.join_async()

    #连接服务器的回调函数，参数success标识服务器连接是否成功,参数errorMsg表示服务器连接失败的错误信息
    def onConnected(self, success, error_msg):
        print('[onConnected] connect to server: {}, success:{}, error_msg:{}'.format(self.m_strAddress, success, error_msg))
        if success:
            #machineInfo代表"IP地址|mac地址|磁盘序列号|cpu号|主机名|磁盘信息|CPUID指令的ecx参数|主板信息"，如果相关字段无关，那就直接给个空值，忽略相应字段就好，两个字段间用分隔符|隔开。
            #machineInfo = "192.168.1.172|5C-F9-DD-73-7C-83|0682056C|BFEBFBFF000206A7|DESKTOP-84OBV5E|C,NTFS,223|6VKJD3X"
            machineInfo = ""
            appid = "xt_api_2.0"
            authcode = "7f3c92e678f9ec77"
            time.sleep(1)
            # 异步登录
            # self.m_client.userLogin(self.m_strUserName, self.m_strPassword, self.m_nRequestId, machineInfo, appid, authcode)
            # 同步登录
            self.testUserLoginSync(self.m_strUserName, self.m_strPassword, machineInfo, appid, authcode)

    #同步登录
    def testUserLoginSync(self, username,password,machineInfo,appid,authcode):
        print("userLoginSync started")
        #self.m_client.userLogin(username, password, self.m_nRequestId ,machineInfo, appid, authcode)
        error = self.m_client.userLoginSync(username,password, machineInfo, appid, authcode)
        if error.isSuccess():
            self.m_nLogined = 1
            print('userLoginSync resilt:', error.isSuccess())
            self.doRequest()
        else:
            print("userLoginSync failed, errMsg: ", error.errorMsg() )


    #连接上之后的测试请求
    def doRequest(self):
        print("doRequest", "m_nLogined", self.m_nLogined)
        if  self.m_nLogined:
            #同步请求测试demo
            #行情订阅示例
            # self.testsubscribQuote("CFFEX", "IC2309")
            #批量订阅行情示例
            self.testBatchSubscribQuote()
            #主动请求对应合约行情
            # self.reqPriceDataSync("SHFE", "ni2405")
            # self.reqSingleInstrumentInfo()
            # self.reqPriceData()
    def reqPriceData(self):
        for market, stockcode, platformId in self.m_codeList:
            print("开始查询 市场：{}， 合约：{}的行情数据".format(market, stockcode))
            self.m_client.reqPriceData(market, stockcode, self.m_nRequestId)
            self.m_nRequestId += 1
    def onReqPriceData(self, requestId, data, error):
        if error.isSuccess():
            print("查询行情数据成功")
            if data:
                prcieData = []
                prcieData.append({
                    "交易日": data.m_strTradingDay,
                    "市场代码": data.m_strExchangeID,
                    "合约代码": data.m_strInstrumentID,
                    "合约名称": data.m_strInstrumentName,
                    "合约在交易所的代码": data.m_strExchangeInstID,
                    "最新价": data.m_dLastPrice,
                    "涨跌": data.m_dUpDown,
                    "涨跌幅": data.m_dUpDownRate,
                    "当日均价": data.m_dAveragePrice,
                    "数量": data.m_nVolume,
                    "成交金额": data.m_dTurnover,
                    "昨收盘": data.m_dPreClosePrice,
                    "上次结算价": data.m_dPreSettlementPrice,
                    "昨持仓量": data.m_dPreOpenInterest,
                    "持仓量": data.m_dOpenInterest,
                    "本次结算价": data.m_dSettlementPrice,
                    "今开盘": data.m_dOpenPrice,
                    "最高价": data.m_dHighestPrice,
                    "最低价": data.m_dLowestPrice,
                    "今收盘": data.m_dClosePrice,
                    "涨停板价": data.m_dUpperLimitPrice,
                    "跌停板价": data.m_dLowerLimitPrice,
                    "昨虚实度": data.m_dPreDelta,
                    "今虚实度": data.m_dCurrDelta,
                    "最后修改时间": data.m_strUpdateTime,
                    "最后修改毫秒": data.m_nUpdateMillisec,
                    "申买价一": data.m_dBidPrice1,
                    "申买量一": data.m_nBidVolume1,
                    "申卖价一": data.m_dAskPrice1,
                    "申卖量一": data.m_nAskVolume1,
                    "申买价二": data.m_dBidPrice2,
                    "申买量二": data.m_nBidVolume2,
                    "申卖价二": data.m_dAskPrice2,
                    "申卖量二": data.m_nAskVolume2,
                    "申买价三": data.m_dBidPrice3,
                    "申买量三": data.m_nBidVolume3,
                    "申卖价三": data.m_dAskPrice3,
                    "申卖量三": data.m_nAskVolume3,
                    "申买价四": data.m_dBidPrice4,
                    "申买量四": data.m_nBidVolume4,
                    "申卖价四": data.m_dAskPrice4,
                    "申卖量四": data.m_nAskVolume4,
                    "申买价五": data.m_dBidPrice5,
                    "申买量五": data.m_nBidVolume5,
                    "申卖价五": data.m_dAskPrice5,
                    "申卖量五": data.m_nAskVolume5,
                    "前一次的价格": data.m_dPrePrice,
                    "股票状态": data.m_nStockStatus
                })
                if prcieData:
                    print(prcieData)
        else:
            print("查询行情数据失败， errmsg：", error.errorMsg())

    def reqSingleInstrumentInfo(self):
        errno = XtError(0, "")
        self.m_client.reqSingleInstrumentInfo('SZO', '90002423', self.m_nRequestId)
        self.m_nRequestId += 1
    def onReqSingleInstrumentInfo(self, nRequestId, data, error):
        print("onReqSingleInstrumentInfo")
        if error.isSuccess():
            print("data:",data.m_strInstrumentID)
        else:
            print("error: ",error.errorMsg())

    #同步查询行情数据
    def reqPriceDataSync(self,market,code):
        errno = XtError(0, "")
        pricelist = self.m_client.reqPriceDataSync(market, code, errno)
        if errno.isSuccess():
            for data in pricelist:
                print('合约代码', data.m_strInstrumentID)
                print('最新价', data.m_dLastPrice)
                print('当日均价', data.m_dAveragePrice)
        else:
            print("msg:", errno.errorMsg())
    #行情订阅函数
    def testsubscribQuote(self,market,code):
        subscribdata = CSubscribData()  # 初始化数据，行情订阅结构体
        subscribdata.m_nPlatformID = 20001
        subscribdata.m_strExchangeID = market
        subscribdata.m_strInstrumentID = code
        subscribdata.m_eOfferStatus = EXTOfferStatus.XT_OFFER_STATUS_SP
        self.m_nRequestId += 1
        self.m_client.subscribQuote(subscribdata, self.m_nRequestId)
        print("订阅行情：代码：", code)

    #批量行情订阅函数
    def testBatchSubscribQuote(self):
        subdata = []
        print("开始组装订阅包体")
        for market, stockcode, platformId in self.m_codeList:
            print("添加订阅参数 市场：{}， 合约：{}， 平台：{}".format(market, stockcode, platformId))
            subscribdata = CSubscribData()  # 初始化数据，行情订阅结构体
            subscribdata.m_strExchangeID = market
            subscribdata.m_strInstrumentID = stockcode
            subscribdata.m_nPlatformID = platformId
            subdata.append(subscribdata)
        self.m_nRequestId += 1
        self.m_client.batchSubscribQuote(subdata, self.m_nRequestId)

    #用户登录的回调函数
    def onUserLogin(self, username, password, nRequestId, error):
        if error.isSuccess():
            print('[onUserlogin] username:{},登录成功'.format(username))
            self.m_nLogined = 1
            self.doRequest()
        else:
            print('[onUserlogin] username:{},登录失败，失败原因{}'.format(username, error.errorMsg()))

    # 用户登出的回调函数 ,username用户名，password密码，error类
    def onUserLogout(self, username, password, nRequestId, error):
        print(u'[onUserLogout] success: ', error.isSuccess(), ', username: ', username)


    #订阅行情后的订阅回调，data对应CSubscribData结构, error对应XtError结构
    def onSubscribQuote(self, request_id, data, error):
        print(u'[onSubscribQuote] m_strInstrumentID:', data.m_strInstrumentID)

    #行情订阅成功后的行情主推，data对应CPriceData结构
    def onRtnPriceData(self, data):
        if data:
            prcieData = []
            prcieData.append({
                "交易日": data.m_strTradingDay,
                "市场代码": data.m_strExchangeID,
                "合约代码": data.m_strInstrumentID,
                "合约名称": data.m_strInstrumentName,
                "合约在交易所的代码": data.m_strExchangeInstID,
                "最新价": data.m_dLastPrice,
                "涨跌": data.m_dUpDown,
                "涨跌幅": data.m_dUpDownRate,
                "当日均价": data.m_dAveragePrice,
                "数量": data.m_nVolume,
                "成交金额": data.m_dTurnover,
                "昨收盘": data.m_dPreClosePrice,
                "上次结算价": data.m_dPreSettlementPrice,
                "昨持仓量": data.m_dPreOpenInterest,
                "持仓量": data.m_dOpenInterest,
                "本次结算价": data.m_dSettlementPrice,
                "今开盘": data.m_dOpenPrice,
                "最高价": data.m_dHighestPrice,
                "最低价": data.m_dLowestPrice,
                "今收盘": data.m_dClosePrice,
                "涨停板价": data.m_dUpperLimitPrice,
                "跌停板价": data.m_dLowerLimitPrice,
                "昨虚实度": data.m_dPreDelta,
                "今虚实度": data.m_dCurrDelta,
                "最后修改时间": data.m_strUpdateTime,
                "最后修改毫秒": data.m_nUpdateMillisec,
                "申买价一": data.m_dBidPrice1,
                "申买量一": data.m_nBidVolume1,
                "申卖价一": data.m_dAskPrice1,
                "申卖量一": data.m_nAskVolume1,
                "申买价二": data.m_dBidPrice2,
                "申买量二": data.m_nBidVolume2,
                "申卖价二": data.m_dAskPrice2,
                "申卖量二": data.m_nAskVolume2,
                "申买价三": data.m_dBidPrice3,
                "申买量三": data.m_nBidVolume3,
                "申卖价三": data.m_dAskPrice3,
                "申卖量三": data.m_nAskVolume3,
                "申买价四": data.m_dBidPrice4,
                "申买量四": data.m_nBidVolume4,
                "申卖价四": data.m_dAskPrice4,
                "申卖量四": data.m_nAskVolume4,
                "申买价五": data.m_dBidPrice5,
                "申买量五": data.m_nBidVolume5,
                "申卖价五": data.m_dAskPrice5,
                "申卖量五": data.m_nAskVolume5,
                "前一次的价格": data.m_dPrePrice,
                "股票状态": data.m_nStockStatus
            })
            if prcieData:
                print("行情推送:",prcieData)

if __name__ == '__main__':
    server_addr = "175.25.41.247:65300" # 统一交易服务器的地址
    username = "api3"
    password = "@a1234567"
    cb = CallBack(server_addr, username, password)
    cb.init()
    cb.join()

