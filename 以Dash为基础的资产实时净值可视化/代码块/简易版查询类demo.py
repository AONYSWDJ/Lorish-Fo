from XtTraderPyApi import *
import time
import math
from typing import List
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
    def __init__(self, address, username, password, accountID):
        super(CallBack, self).__init__()
        self.m_strAddress = address
        self.m_strUserName = username
        self.m_strPassword = password
        self.m_strFutureAccountKey = ''
        self.m_strAccountID = accountID
        self.m_strAccountKey = ''
        self.m_nRequestId = 1
        self.m_api = XtTraderApi.createXtTraderApi(self.m_strAddress)   #创建用户
        self.m_nUserLogined = 0
        self.m_brequest = 1
        self.m_dictAccountKeyStatus = {}
        self.m_dictAccountID2Key = {}
        self.m_dictAccountKey2type = {}
        self.m_bConnected = 0


    def init(self):
        if self.m_strAddress == None:
            return -1, u'server address is empty'
        if self.m_api == None:
            return -1, u'failed to create traderapi client'
        if isinstance(self,XtTraderApiCallback):                         #当前类是否为父类的实例
            self.m_api.setCallback(self)
            return self.m_api.init("../config")
        return 0, u''

    def join(self):
        # self.m_api.joinAll()
        self.m_api.join()

    def joinAsync(self):
        self.m_api.join_async()

    #连接服务器的回调函数，参数success标识服务器连接是否成功,参数errorMsg表示服务器连接失败的错误信息
    def onConnected(self, success, error_msg):
        print('[onConnected] connect to server: {}, success:{}, error_msg:{}'.format(self.m_strAddress, success, error_msg))
        if success:
            self.m_bConnected = 1
        else:
            self.m_bConnected = 0
    def doLogin(self):
        # machineInfo代表"IP地址|mac地址|磁盘序列号|cpu号|主机名|磁盘信息|CPUID指令的ecx参数|主板信息"，如果相关字段无关，那就直接给个空值，忽略相应字段就好，两个字段间用分隔符|隔开。
        # machineInfo = "192.168.1.172|5C-F9-DD-73-7C-83|0682056C|BFEBFBFF000206A7|DESKTOP-84OBV5E|C,NTFS,223|6VKJD3X"
        machineInfo = ""
        appid = "xt_api_2.0"
        authcode = "7f3c92e678f9ec77"
        # 异步登录
        # self.m_api.userLogin(self.m_strUserName, self.m_strPassword, self.m_nRequestId, machineInfo, appid, authcode)
        # 同步登录
        self.userLoginSync(self.m_strUserName, self.m_strPassword, machineInfo, appid, authcode)

    #同步登录
    def userLoginSync(self, username,password,machineInfo,appid,authcode):
        print("userLoginSync started")
        error = self.m_api.userLoginSync(username,password, machineInfo, appid, authcode)
        if error.isSuccess():
            self.m_nUserLogined = 1
            print('userLoginSync resilt:', error.isSuccess()) 
            # self.request()
        else:
            print(error.errorMsg())
    #同步请求账号key
    def reqAccountKeySync(self):
        print("reqAccountKeysSync started")
        error = XtError(0, "")
        print(self.m_api.reqAccountKeysSync(error))
        acckeyList = self.m_api.reqAccountKeysSync(error)
        if error.isSuccess():
            print("acckeyList size", len(acckeyList))
            for data in acckeyList:
                print("accountKey: ", data.m_strAccountKey)

    #同步查询产品信息
    def reqProductDataSync(self):
        error = XtError(0, "")
        productList = self.m_api.reqProductDataSync(error)
        if error.isSuccess():
            print("productList size", len(productList))
            for data in productList:
                print("m_nProductId: ", data.m_nProductId, "m_strProductName", data.m_strProductName, "m_strProductCode", data.m_strProductCode, "m_dTotalNetValue", data.m_dTotalNetValue, "m_dGGTStockValue", data.m_dGGTStockValue )
        else:
            print("reqProductDataSync errmsg:", error.errorMsg())
            for data in productList:
                print("m_nProductId: ", data.m_nProductId, "m_strProductName", data.m_strProductName, "m_strProductCode", data.m_strProductCode, "m_dTotalNetValue", data.m_dTotalNetValue, "m_dGGTStockValue", data.m_dGGTStockValue )


    #查询产品信息
    def reqProductData(self):
        self.m_api.reqProductData(self.m_nRequestId)
        self.m_nRequestId += 1
    def onReqProductData(self, nRequestId, data, isLast, error):
        #if error.isSuccess():
        print("m_nProductId: ", data.m_nProductId, "m_strProductName", data.m_strProductName)
        #else:
        #    print("查询产品信息失败， errmsg: ", error.errorMsg())

    # 账号登录之后做检查
    def request(self):
        # demo遍历所有账户测试查询，请根据实际情况修改代码
        if(self.m_dictAccountID2Key):
            for name in self.m_dictAccountID2Key:
                self.m_strAccountID = name
                self.m_strAccountKey = self.m_dictAccountID2Key[name]
                print("m_dictAccountID2Key accountID:",name, "accountkey", self.m_strAccountKey)
                if name and self.checkAccountStatus(self.m_strAccountKey):
                    self.doRequest()

    # 检查请求账号是否登录成功
    def checkAccountStatus(self, accountKey):
        if accountKey in self.m_dictAccountKeyStatus:
            print("userlogin status:", self.m_nUserLogined)
            status = self.m_dictAccountKeyStatus[accountKey]
            print("accountKey", accountKey, " status:", status)
            if self.m_nUserLogined:
                return 1
                # if status == EBrokerLoginStatus.BROKER_LOGIN_STATUS_OK or status == EBrokerLoginStatus.BROKER_LOGIN_STATUS_CLOSED:
                #     return 1
                # else:
                #     return 0
            else:
                return 0
        else:
            return 0

    #连接上之后的测试请求
    def doRequest(self):
        #同步请求测试demo
        print("start request")
        #查询用户对应的accountKey
        # self.reqAccountKeySync()
        #查询产品信息
        # self.reqProductDataSync()

        #查询账号资金信息
        # self.reqAccountDetailSync(self.m_strAccountID,self.m_strAccountKey)
        # 查询账号历史资金信息
        # self.reqHistoryAccountDetailSync(self.m_strAccountID,self.m_strAccountKey)

        #查询账号委托明细信息
        # self.reqOrderDetailSync(self.m_strAccountID,self.m_strAccountKey)
        #查询账号历史委托明细信息
        #self.reqHistoryOrderDetailSync(self.m_strAccountID,self.m_strAccountKey)

        #查询账号成交明细信息
        # self.reqDealDetailSync(self.m_strAccountID,self.m_strAccountKey)
        #查询账号成交统计信息
        # self.reqDealStaticsSync(self.m_strAccountID,self.m_strAccountKey)
        # 查询账号历史成交明细信息
        # self.reqHistoryDealDetailSync(self.m_strAccountID,self.m_strAccountKey)

        #查询账号持仓明细信息
        # self.reqPositionDetailSync(self.m_strAccountID,self.m_strAccountKey)
        #查询账号持仓统计信息
        # self.reqPositionStaticsSync(self.m_strAccountID,self.m_strAccountKey)
        #查询账号历史持仓统计信息
        #self.reqHistoryPositionStaticsSync(self.m_strAccountID,self.m_strAccountKey)
        # 查询日初持仓
        # self.reqInitialPositionStaticsSync(self.m_strAccountID,self.m_strAccountKey)
        #同步主动请求对应合约行情
        # self.reqPriceDataSync("SH", "600000")
        #查询用户所有指令信息
        # self.reqCommandsInfoSync()
        #查询账号委托明细信息
        # self.reqOrderDetailSyncByOrderID(self.m_strAccountID,self.m_strAccountKey)
        # 查询账号成交明细信息
        # self.reqDealDetailSyncByOrderID(self.m_strAccountID,self.m_strAccountKey)
        #查询可下单量
        # self.reqCanOrderVolumeSync(self.m_strAccountID, self.m_strAccountKey)
        #查询枚举名称
        # self.reqEnumItemName()
        # 查询未了结负债合约
        # self.reqStkUnCloseCompactsSync(self.m_strAccountID, self.m_strAccountKey)
        # 查询未了结负债合约
        # self.reqStkClosedCompactsSync(self.m_strAccountID, self.m_strAccountKey)
        # 请求信用账号资产数据
        # self.reqCreditDetailSync(self.m_strAccountID,self.m_strAccountKey)

        # 异步请求测试demo

        # 请求账号资产数据
        # self.reqAccountDetail(self.m_strAccountID,self.m_strAccountKey)
        # 请求信用账号资产数据
        # self.reqCreditDetail(self.m_strAccountID,self.m_strAccountKey)
        # 请求委托明细
        # self.reqOrderDetail(self.m_strAccountID,self.m_strAccountKey)
        # 请求成交明细
        self.reqDealDetail(self.m_strAccountID,self.m_strAccountKey)
        # self.reqHistoryDealDetail(self.m_strAccountID,self.m_strAccountKey)
        # 请求持仓明细
        # self.reqPositionDetail(self.m_strAccountID,self.m_strAccountKey)
        # 请求持仓统计
        # self.reqPositionStatics(self.m_strAccountID,self.m_strAccountKey)
        # 请求账号历史持仓统计
        # self.reqHistoryPositionStatics(self.m_strAccountID,self.m_strAccountKey)
        # 查询行情数据
        # self.reqPriceData(self.m_strAccountID,self.m_strAccountKey)
        # 查询产品信息
        # self.reqProductData()
        #查询用户所有指令信息
        # self.reqCommandsInfo()

        # 查询股东
        # self.reqSecuAccount(self.m_strAccountID, self.m_strAccountKey)

        # 查询可下单量
        # self.reqCanOrderVolume(self.m_strAccountID, self.m_strAccountKey)
        # 查询未了结负债合约
        # self.reqStkUnCloseCompacts(self.m_strAccountID, self.m_strAccountKey)
        # 查询市场状态
        # self.reqExchangeStatus(self.m_strAccountID, self.m_strAccountKey)
    #查询资金流水
    def reqFundFlowSync(self, accountID, accountKey):
        startdate = '20240101'
        enddate = '20240516'
        error = XtError(0, "")
        fundflowList = self.m_api.reqFundFlowSync(accountID, startdate, enddate, error, accountKey)
        if error.isSuccess():
            print("reqFundFlowSync success records:", len(fundflowList))

        else:
            print("reqFundFlowSync errmsg:", error.errorMsg())


    #查询市场状态
    def reqExchangeStatus(self, accountID, accountKey):
        print("reqExchangeStatus, accountID: ", accountID, "accountKey", accountKey)
        self.m_api.reqExchangeStatus(accountID, self.m_nRequestId, accountKey)
    def onReqExchangeStatus(self, accountID, nRequestId, accountKey,  datas, error):
        if(error.isSuccess):
            print("onReqExchangeStatus")
            if(datas):
                print("onReqExchangeStatus,records: ", len(datas))
            for marketdata in datas:
                print("reqExchangeStatus,records: ", len(datas))
                print("交易所代码", marketdata.m_strExchangeId, "市场状态", marketdata.m_eInstrumentStatus)
        else:
            print("onReqExchangeStatus errMsg: ", error.errorMsg())

    def refreshStkClosedCompacts(self, accountID, accountKey):
        self.m_api.refreshStkClosedCompacts(accountID, self.m_nRequestId, accountKey)
        self.m_nRequestId += 1
        print("refreshStkClosedCompacts")
    def refreshStkUnCloseCompacts(self, accountID, accountKey):
        self.m_api.refreshStkUnCloseCompacts(accountID, self.m_nRequestId, accountKey)
        self.m_nRequestId += 1
        print("refreshStkClosedCompacts")
    # 同步查询未了结合约
    def reqStkUnCloseCompactsSync(self, accountID, accountKey):
        error = XtError(0, "")
        dataList = self.m_api.reqStkUnCloseCompactsSync(accountID, error, accountKey)
        if(error.isSuccess()):
            print("reqStkUnCloseCompactsSync records: ", len(dataList))
            for data in dataList:
                print("账号ID: {}, 合约代码: {}, 合约编号: {}, 合约金额: {}, 未还合约金额: {}, 未还合约息费: {}" \
                      .format(data.m_strAccountID, data.m_strInstrumentID, data.m_strCompactId, data.m_dBusinessBalance,
                              data.m_dRealCompactBalance, data.m_dRealCompactFare))
        else:
            print("reqStkUnCloseCompactsSync failed, esrrmsg:", error.errorMsg())

    # 同步查询已了结合约
    def reqStkClosedCompactsSync(self, accountID, accountKey):
        error = XtError(0, "")
        dataList = self.m_api.reqStkClosedCompactsSync(accountID, error, accountKey)
        if (error.isSuccess()):
            print("reqStkClosedCompactsSync records: ", len(dataList))
            for data in dataList:
                print("账号ID: {}, 合约代码: {}, 合约编号: {}, 合约金额: {}, 已还金额: {}, 已还息费: {}" \
                      .format(data.m_strAccountID, data.m_strInstrumentID, data.m_strCompactId,
                              data.m_dBusinessBalance,
                              data.m_dRepaidBalance, data.m_dRepaidFare))
        else:
            print("reqStkClosedCompactsSync failed, esrrmsg:", error.errorMsg())
    # 查询未了结合约
    def reqStkUnCloseCompacts(self, accountID, accountKey):
        self.m_api.reqStkUnCloseCompacts(accountID, self.m_nRequestId, accountKey)
        self.m_nRequestId += 1
        print("reqStkUnCloseCompacts")

    def onReqStkUnCloseCompact(self, accountID: str, nRequestId: int, data: CStkUnClosedCompacts, isLast: bool, error: XtError) :
        if(error.isSuccess()):
            print("onReqStkUnCloseCompact success")
            if(data):
                print("账号ID: {}, 合约代码: {}, 合约编号: {}, 合约金额: {}, 未还合约金额: {}, 未还合约息费: {}"\
                      .format(data.m_strAccountID, data.m_strInstrumentID, data.m_strCompactId, data.m_dBusinessBalance,data.m_dRealCompactBalance,data.m_dRealCompactFare))
        else:
            print("onReqStkUnCloseCompact failed, errmsg:", error.errorMsg())

    def onReqStkUnCloseCompactWithAccKey(self, accountID: str, nRequestId: int, accountKey: str,
                                         data: CStkUnClosedCompacts, isLast: bool, error: XtError):
        pass
    def onBatchReqStkUnCloseCompact(self, accountID: str, nRequestId: int, data: List[CStkUnClosedCompacts], isLast: bool, error: XtError) :
        if(error.isSuccess()):
            print("onBatchReqStkUnCloseCompact success")
            if(data):
                print("CStkUnClosedCompacts records:", len(data))
                for unCloseCompace in data:
                    print("账号ID: {}, 合约代码: {}, 合约编号: {}, 合约金额: {}, 未还合约金额: {}, 未还合约息费: {}" \
                          .format(unCloseCompace.m_strAccountID, unCloseCompace.m_strInstrumentID, unCloseCompace.m_strCompactId,
                                  unCloseCompace.m_dBusinessBalance, unCloseCompace.m_dRealCompactBalance, unCloseCompace.m_dRealCompactFare))
        else:
            print("onBatchReqStkUnCloseCompact failed, errmsg:", error.errorMsg())
    # 查询枚举名称
    def reqEnumItemName(self):
        name = self.m_api.reqEnumItemName("EBrokerPriceType", EBrokerPriceType.BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_KKS)
        print(name)
        name = self.m_api.reqEnumItemName("EOperationType", EOperationType.OPT_CLOSE_LONG_TODAY_HISTORY_THEN_OPEN_SHORT)
        print(name)
        name = self.m_api.reqEnumItemName("ETimeCondition", ETimeCondition.TIME_CONDITION_GTD)
        print(name)
    # 查询可下单数量
    def reqCanOrderVolumeSync(self, account_id, account_key):
        error = XtError(0, "")
        reqParam = COpVolumeReq()
        reqParam.m_strAccountID = account_id
        reqParam.m_strMarket = "SH"
        reqParam.m_strInstrument = "601919"
        reqParam.m_dPrice = 9.88
        # reqParam.m_eOperationType = EOperationType.OPT_BUY
        reqParam.m_eOperationType = EOperationType.OPT_SELL
        reqParam.m_eHedgeFlag = EHedgeFlagType.HEDGE_FLAG_SPECULATION
        volume = self.m_api.reqCanOrderVolumeSync(reqParam, error, account_key)
        print("reqCanOrderVolumeSync market {}, code {}, volume {}".format(reqParam.m_strMarket, reqParam.m_strInstrument, volume))

    def reqCanOrderVolume(self, account_id, account_key):
        reqParam = COpVolumeReq()
        reqParam.m_strAccountID = account_id
        reqParam.m_strMarket = "SH"
        reqParam.m_strInstrument = "601919"
        reqParam.m_dPrice = 9.88
        # reqParam.m_eOperationType = EOperationType.OPT_BUY
        reqParam.m_eOperationType = EOperationType.OPT_SELL
        reqParam.m_eHedgeFlag = EHedgeFlagType.HEDGE_FLAG_SPECULATION
        print("reqCanOrderVolume makret {} code {}".format(reqParam.m_strMarket, reqParam.m_strInstrument))
        self.m_api.reqCanOrderVolume(reqParam, self.m_nRequestId, account_key)
        self.m_nRequestId +=1

    def onReqCanOrderVolume(self, accountID, nRequestId, accountKey, market, instrument, nVolume, error):
        if error.isSuccess():
            print("查询市场{} 代码 {}可下单量为：{}".format(market,instrument, nVolume))
        else:
            print("onReqCanOrderVolume failed, errmsg:", error.errorMsg())


    # 同步查询资金数据
    def reqAccountDetailSync(self, account_id, account_key):
        print("reqAccountDetailSync account_id:", account_id)
        errno = XtError(0, "")
        data = self.m_api.reqAccountDetailSync(account_id, errno, account_key)
        if errno.isSuccess():
            print("reqAccountDetailSync success")
            print(data.m_strAccountID)
            print(data.m_strStatus)
            print('总资产', data.m_dBalance)
            print('可用资金', data.m_dAvailable)
            print('股票总市值:', data.m_dStockValue)
            print('债券总市值', data.m_dLoanValue)
            print('基金总市值', data.m_dFundValue)
            print('m_dFrozenMargin', data.m_dFrozenMargin)
            print('m_dFrozenCash', data.m_dFrozenCash)
            print('m_dFrozenCommission', data.m_dFrozenCommission)
            print('m_dRisk', data.m_dRisk)
            print('m_dNav', data.m_dNav)
            print('持仓盈亏', data.m_dPositionProfit)
            print('平仓盈亏', data.m_dCloseProfit)
            print('当日盈亏', data.m_dDaysProfit)
            print('m_eDualStatus', data.m_eDualStatus)
            print('账号名称', data.m_strAccountName)
            print('经纪公司编号', data.m_strBrokerID)
            print('经纪公司名称', data.m_strBrokerName)
        else:
            print("reqAccountDetailSync failed, errmsg:", errno.errorMsg(), "account_id: ", account_id)
    # 查询账号历史资金信息
    def reqHistoryAccountDetailSync(self, account_id, account_key):
        print("reqHistoryAccountDetailSync started")
        errno = XtError(0, "")
        deallist = self.m_api.reqHistoryAccountDetailSync(account_id, '20230911', '20230911', errno, account_key)
        if errno.isSuccess:
            print("reqHistoryAccountDetailSync success, record:", len(deallist))
            for data in deallist:
                print('m_strAccountID', data.m_strAccountID, 'm_strTradingDate', data.m_strTradingDate,
                      'm_dAvailable', data.m_dAvailable)

    #同步查询委托数据
    def reqOrderDetailSync(self, account_id, account_key):
        print("reqOrderDetailSync started")
        errno = XtError(0, "")
        orderlist = self.m_api.reqOrderDetailSync(account_id, errno, account_key)
        if errno.isSuccess:
            print("reqOrderDetailSync success, record:", len(orderlist))
            # for data in orderlist:
            #     print("m_strOrderSysID:", data.m_strOrderSysID,
            #           "m_strSecuAccount:", data.m_strSecuAccount,
            #           "m_strInsertDate", data.m_strInsertDate,
            #           "m_dAveragePrice", data.m_dAveragePrice,
            #           "m_dTradeAmount", data.m_dTradeAmount,
            #           "m_strInsertTime", data.m_strInsertTime)
    #同步查询指令对应委托数据
    def reqOrderDetailSyncByOrderID(self, account_id, account_key):
        print("reqOrderDetailSyncByOrderID started")
        errno = XtError(0, "")
        orderId = 703377
        orderlist = self.m_api.reqOrderDetailSyncByOrderID(account_id, errno, orderId, account_key)
        if errno.isSuccess:
            print("reqOrderDetailSyncByOrderID success, record:", len(orderlist))
            for data in orderlist:
                print("m_strOrderSysID:", data.m_strOrderSysID,
                      "m_strSecuAccount:", data.m_strSecuAccount,
                      "m_strInsertDate", data.m_strInsertDate,
                      "m_dAveragePrice", data.m_dAveragePrice,
                      "m_dTradeAmount", data.m_dTradeAmount,
                      "m_nOrderID", data.m_nOrderID,
                      "m_nOrderPriceType", data.m_nOrderPriceType,
                      "m_nDirection", data.m_nDirection,
                      "m_eOffsetFlag", data.m_eOffsetFlag,
                      "m_strInsertTime", data.m_strInsertTime)
    #同步查询历史委托数据
    def reqHistoryOrderDetailSync(self, account_id, account_key):
        print("reqHistoryOrderDetailSync started")
        errno = XtError(0, "")
        orderlist = self.m_api.reqHistoryOrderDetailSync(account_id, '20240614', '20240614', errno, account_key)
        if errno.isSuccess:
            print("reqHistoryOrderDetailSync success, record:", len(orderlist))
            for data in orderlist:
                # print('m_strInstrumentID: ', data.m_strInstrumentID,  'm_strOrderSysID:', data.m_strOrderSysID)
                pass

    #同步查询历史委托数据
    def reqHistoryOrderDetail(self, account_id, account_key):
        print("reqHistoryOrderDetail started")
        self.m_nRequestId += 1
        self.m_api.reqHistoryOrderDetail(account_id, '20240614', '20240614', self.m_nRequestId, account_key)
    def onReqHistoryOrderDetail(self, accountID, nRequestId, data, isLast, error):
        print(data.m_strOrderSysID, "isLast:", isLast)
    #同步查询成交数据
    def reqDealDetailSync(self, account_id, account_key):
        print("reqDealDetailSync started, account_id:", account_id)
        errno = XtError(0, "")
        deallist = self.m_api.reqDealDetailSync(account_id, errno, account_key)
        if errno.isSuccess:
            print("reqDealDetailSync success, record:", len(deallist))
            # for data in deallist:
            #     print("reqDealDetailSync", data.m_nOrderID, "code:", data.m_strInstrumentID,"m_nOrderID", data.m_nOrderID, "m_strOrderSysID:", data.m_strOrderSysID, "volume:", data.m_nVolume, "m_nHedgeFlag", data.m_nHedgeFlag, "m_strTradeID", data.m_strTradeID)

    def reqDealStaticsSync(self, account_id, account_key):
        print("reqDealStaticsSync started, account_id:", account_id, 'account_key:', account_key)
        errno = XtError(0, "")
        dealStaticsList = self.m_api.reqDealStaticsSync(account_id, errno, account_key)
        if errno.isSuccess:
            print("reqDealStaticsSync success, record:", len(dealStaticsList))
            for data in dealStaticsList:
                print("m_strInstrumentID:", data.m_strInstrumentID, "m_nVolume:", data.m_nVolume)

    #同步查询指令对应成交数据
    def reqDealDetailSyncByOrderID(self, account_id, account_key):
        print("reqDealDetailSyncByOrderID started")
        errno = XtError(0, "")
        orderID = 703377
        deallist = self.m_api.reqDealDetailSyncByOrderID(account_id, errno, orderID,  account_key)
        if errno.isSuccess:
            print("reqDealDetailSyncByOrderID success, record:", len(deallist))
            for data in deallist:
                print("reqDealDetailSync", "code:", data.m_strInstrumentID,
                      "m_nOrderID", data.m_nOrderID,
                      "m_strOrderSysID:", data.m_strOrderSysID,
                      "volume:", data.m_nVolume,
                      "m_nHedgeFlag", data.m_nHedgeFlag,
                      "m_nDirection", data.m_nDirection,
                      "m_nOffsetFlag", data.m_nOffsetFlag,
                      "m_strTradeID", data.m_strTradeID)


    #同步查询历史成交数据
    def reqHistoryDealDetailSync(self, account_id, account_key):
        print("reqHistoryDealDetailSync started")
        errno = XtError(0, "")
        deallist = self.m_api.reqHistoryDealDetailSync(account_id, '20240614', '20240614', errno, account_key)
        if errno.isSuccess:
            print("reqHistoryDealDetailSync success, record:", len(deallist))
            for data in deallist:
                print('m_strInstrumentID', data.m_strInstrumentID, 'm_strOrderSysID', data.m_strOrderSysID)
                # print('m_strInstrumentID', data.m_strInstrumentID, 'm_strOrderSysID', data.m_strOrderSysID, 'm_strTradeDate', data.m_strTradeDate, "m_nHedgeFlag", data.m_nHedgeFlag)
    #同步查询持仓数据
    def reqPositionDetailSync(self, account_id, account_key):
        print("reqPositionDetailSync started")
        error = XtError(0, "")
        positionlist = self.m_api.reqPositionDetailSync(account_id, error, account_key)
        if error.isSuccess():
            print("reqPositionDetailSync success, record:", len(positionlist))
            for data in positionlist:
                print(data.m_strInstrumentID)
                print(data.m_dOpenPrice)
        else:
            print("reqPositionDetailSync failed, errmsg", error.errorMsg())
    # 同步查询持仓统计
    def reqPositionStaticsSync(self, account_id, account_key):
        print("reqPositionStaticsSync started, account_id",account_id)
        errno = XtError(0, "")
        positionlist = self.m_api.reqPositionStaticsSync(account_id, errno, account_key)
        if errno.isSuccess:
            print("reqPositionStaticsSync success, record:", len(positionlist))
            for data in positionlist:
                # print("data 属性 == {}：".format(dir(data)))
                # if data.m_strInstrumentID == "601318":
                print("accountId", data.m_strAccountID,
                      "m_strInstrumentID", data.m_strInstrumentID,
                      "m_strInstrumentName", data.m_strInstrumentName
                      # ,"m_nOpenVolume", data.m_nOpenVolume
                      # , "m_nPosition", data.m_nPosition
                      # , "m_nOnRoadVolume", data.m_nOnRoadVolume
                      # , "m_nYesterdayVolume", data.m_nYesterdayVolume
                      # , "m_dPositionProfit", data.m_dPositionProfit
                      # , "m_dFloatProfit", data.m_dFloatProfit
                      # , "m_nCoveredAmount", data.m_nCoveredAmount
                      # , "m_dUsedMargin", data.m_dUsedMargin
                      # , "m_nDirection", data.m_nDirection
                      # , "m_bIsToday", data.m_bIsToday
                      # , "m_strSecuAccount", data.m_strSecuAccount
                      # , "m_nCanCloseVol", data.m_nCanCloseVolume
                      # , "m_nCanUseVolume", data.m_nCanUseVolume
                 )

    #同步查询历史持仓统计
    def reqHistoryPositionStaticsSync(self, account_id, account_key):
        print("reqHistoryDealDetailSync started")
        errno = XtError(0, "")
        deallist = self.m_api.reqHistoryPositionStaticsSync(account_id, '20230913', '20230913', errno, account_key)
        if errno.isSuccess:
            print("reqHistoryPositionStaticsSync success, record:", len(deallist))
            for data in deallist:
                print('m_strInstrumentID', data.m_strInstrumentID, 'm_dInstrumentValue', data.m_dInstrumentValue, 'm_strAccountKey', data.m_strAccountKey)
    # 同步查询日初持仓统计
    def reqInitialPositionStaticsSync(self, account_id, account_key):
        print("reqInitialPositionStaticsSync started account_id： ", account_id)
        errno = XtError(0, "")
        positionlist = self.m_api.reqInitialPositionStaticsSync(account_id, errno, account_key)
        if errno.isSuccess:
            print("reqInitialPositionStaticsSync success, record:", len(positionlist))
            for data in positionlist:
                print(data.m_strInstrumentID)
    #同步查询行情数据
    def reqPriceDataSync(self,market,code):
        errno = XtError(0, "")
        pricelist = self.m_api.reqPriceDataSync(market, code, errno)
        if errno.isSuccess():
            for data in pricelist:
                print('合约代码', data.m_strInstrumentID)
                print('最新价', data.m_dLastPrice)
                print('m_dUpDown', data.m_dUpDown)
                print('m_dUpDownRate', data.m_dUpDownRate)

    #用户登录的回调函数
    def onUserLogin(self, username, password, nRequestId, error):
        if error.isSuccess():
            print('[onUserlogin] username:{},登录成功'.format(username))
            self.m_nUserLogined = 1
            # self.request()
        else:
            print('[onUserlogin] username:{},登录失败，失败原因{}'.format(username, error.errorMsg()))

    # 用户登出的回调函数 ,username用户名，password密码，error类
    def onUserLogout(self, username, password, nRequestId, error):
        print(u'[onUserLogout] success: ', error.isSuccess(), ', username: ', username)

    def onRtnLoginStatus(self, account_id, status, account_type, error_msg):
        # print("onRtnLoginStatus")
        pass

    # 账号key主推接口，账号登录成功后才可以执行下单等操作，可以根据这里的status字段做判断
    # 参数: status 主推资金账号的登录状态
    # 参数: account_type 主推资金账号的类型 1:期货账号, 2:股票账号, 3:信用账号
    def onRtnLoginStatusWithActKey(self, account_id, status, account_type, account_key, error_msg):
        # if account_id == self.m_strAccountID:
            self.m_dictAccountKeyStatus[account_key] = status
            self.m_dictAccountID2Key[account_id] = account_key
            self.m_dictAccountKey2type[account_key] = account_type
            print(u'[onRtnLoginStatusWithActKey] account_id：{}, account_id：{}, account_type: {}, status:{}, error_msg:{}'.format(account_id, account_key, account_type, status, error_msg))
            # if status == EBrokerLoginStatus.BROKER_LOGIN_STATUS_OK or status == EBrokerLoginStatus.BROKER_LOGIN_STATUS_CLOSED:
            #     self.request()
            # else:
            #     pass
    # 请求账号资产数据
    def reqAccountDetail(self, account_id, account_key):
        print(u'[reqAccountDetail]查询账号:', account_id, u"的资产数据")
        self.m_nRequestId += 1
        self.m_api.reqAccountDetail(account_id, self.m_nRequestId, account_key)

    #请求资金数据的回调函数，data对应CAccountDetail结构, error对应XtError结构
    def onReqAccountDetail(self,account_id, request_id, data, is_last, error):
        if error.isSuccess():
            print(u'[onReqAccountDetail] success, account_id:', account_id, ', m_dAvailable:', data.m_dAvailable, ', m_dPositionProfit:', data.m_dPositionProfit, ', m_dDaysProfit:', data.m_dDaysProfit, ', m_dStockValue:', data.m_dStockValue)
        else:
            print(u'[onReqAccountDetail] failed, account_id:', account_id, ', error_msg:',error.errorMsg())

    def onRtnAccountDetail(self, account_id,  data):
        # print(u'[onRtnAccountDetail] success, account_id:', account_id)
        pass
    # 请求两融账号综合资金信息
    def reqCreditDetailSync(self, accountID):
        error = XtError(0, "")
        creditData = self.m_api.reqCreditDetailSync(accountID, error)
        if error.isSuccess():
            pass
        else:
            print("reqCreditDetailSync failed, errmsg: ", error.errorMsg())

    # 请求信用账号资产数据
    def reqCreditDetail(self, account_id, account_key):
        print(u'[reqCreditAccountDetail]查询信用账号:', account_id, u"的资产数据")
        self.m_nRequestId += 1
        self.m_api.reqCreditDetail(account_id, self.m_nRequestId, account_key)

    #请求信用资产数据的回调函数，data对应CCreditDetail结构, error对应XtError结构
    def onReqCreditDetail(self,account_id, request_id, data, is_last, error):
        if error.isSuccess():
            print(u'[onReqCreditAccountDetail] success, account_id:', account_id, 'is_last:', is_last)
        else:
            print(u'[onReqCreditAccountDetail] failed, account_id:', account_id, ', error_msg:',error.errorMsg())

    # 请求委托明细
    def reqOrderDetail(self, account_id, account_key):
        print(u'[reqOrderDetail]查询账号:', account_id, u"的当日委托明细")
        self.m_nRequestId += 1
        self.m_api.reqOrderDetail(account_id, self.m_nRequestId, account_key)

    #委托明细查询的回调函数，data对应COrderDetail结构, error对应XtError结构
    def onReqOrderDetail(self,account_id, request_id, data, is_last, error):
        if error.isSuccess():
            print(u'[onReqOrderDetail] success, account_id: {}, InstrumentID: {}'.format(account_id, data.m_strInstrumentID))
        else:
            print(u'[onReqOrderDetail] failed, account_id:', account_id, ', error_msg:',error.errorMsg())

    # 请求成交明细
    def reqDealDetail(self, account_id, account_key):
        print(u'[reqDealDetail]查询账号:', account_id, u"的当日成交明细")
        self.m_nRequestId += 1
        self.m_api.reqDealDetail(account_id, self.m_nRequestId, account_key)

    #成交明细查询的回调函数，data对应CDetalDetail结构, error对应XtError结构
    def onReqDealDetail(self, account_id, request_id, data, is_last, error):
        if error.isSuccess():
            print(u'[onReqDealDetail] success, account_id:', account_id, ', is_last:', is_last)
        else:
            print(u'[onReqDealDetail] failed, account_id:', account_id, ', error_msg:',error.errorMsg())

    # 请求历史成交明细
    def reqHistoryDealDetail(self, account_id, account_key):
        print(u'[reqHistoryDealDetail]查询账号:', account_id, u"的当日成交明细", "account_key", account_key)
        self.m_nRequestId += 1
        self.m_api.reqHistoryDealDetail(account_id, "20231103","20231103", self.m_nRequestId, account_key)

    #历史成交明细查询的回调函数，data对应CDetalDetail结构, error对应XtError结构
    def onReqHistoryDealDetail(self, account_id, request_id, data, is_last, error):
        if error.isSuccess():
            print(u'[onReqHistoryDealDetail] success, account_id:', account_id, ', is_last:', is_last)
        else:
            print(u'[onReqHistoryDealDetail] failed, account_id:', account_id, ', error_msg:',error.errorMsg())

    # 请求持仓明细
    def reqPositionDetail(self, account_id, account_key):
        print(u'[reqPositionDetail]查询账号:', account_id, u"的持仓明细")
        self.m_nRequestId += 1
        self.m_api.reqPositionDetail(account_id, self.m_nRequestId, account_key)

    #请求持仓明细的回调函数，data对应CPositionDetail结构, error对应XtError结构
    def onReqPositionDetail(self, account_id, request_id, data, is_last, error):
        if error.isSuccess():
            print(u'[onReqPositionDetail] success, account_id:', account_id, ', is_last: ', is_last)
        else:
            print(u'[onReqPositionDetail] failed, account_id:', account_id, ', error_msg:',error.errorMsg())

    # 请求持仓统计
    def reqPositionStatics(self, account_id, account_key):
        print(u'[reqPositionStatics]查询账号:', account_id, u"的持仓明细")
        self.m_nRequestId += 1
        self.m_api.reqPositionStatics(account_id, self.m_nRequestId, account_key)

    #请求持仓统计的回调函数，data对应CPositionStatics结构, error对应XtError结构
    def onReqPositionStatics(self,account_id, request_id, data, is_last,error):
        if error.isSuccess():
            print(u'[onReqPositionStatics] success, account_id:', account_id, ', is_last:', is_last)
        else:
            print(u'[onReqPositionStatics] failed, account_id:', account_id, ', error_msg:',error.errorMsg())

    # 请求账号历史持仓统计
    def reqHistoryPositionStatics(self, account_id, account_key):
        print(u'[reqHistoryPositionStatics]查询账号:', account_id, u"的历史持仓统计", 'account_key: ', account_key)
        self.m_nRequestId += 1
        self.m_api.reqHistoryPositionStatics(account_id, '20230902', '20230902', self.m_nRequestId, account_key)

    # 账号历史持仓统计的回调函数，data对应CPositionStatics结构, error对应XtError结构
    def onReqHistoryPositionStatics(self, account_id, request_id, data, is_last, error):
        if error.isSuccess():
            print(u'[onReqHistoryPositionStatics] success, account_id:', account_id, ', is_last:', is_last,
                  'm_strInstrumentID', data.m_strInstrumentID)
        else:
            print(u'[onReqHistoryPositionStatics] failed, account_id:', account_id, ', error_msg:',
                  error.errorMsg())

    #请求负债合约的回调函数, error对应XtError结构
    def onReqStksubjects(self, account_id, request_id, data, is_last, error):
        if error.isSuccess():
            print(u'[onReqStksubjects] success, account_id:', account_id, ', is_last:', is_last)
        else:
            print('[onReqStksubjects] failed, account_id:', account_id, ', error_msg:',error.errorMsg())

    #请求融资融券标的接口后的回调函数, error对应XtError结构
    def onReqStkcompacts(self, account_id, request_id, data, is_last, error):
        if error.isSuccess():
            print(u'[onReqStkcompacts] success, account_id:', account_id, ', is_last:', is_last)
        else:
            print(u'[onReqStkcompacts] failed, account_id:', account_id, ', error_msg:',error.errorMsg())

    # 查询行情数据
    def reqPriceData(self, market, code):
        self.m_api.reqPriceData(market, code, self.m_nRequestId)
        self.m_nRequestId += 1
        print(u'[reqPriceData]查询合约:', code, u"的行情快照")

    # 请求行情数据的回调，data对应CPriceData结构, error对应XtError结构
    def onReqPriceData(self, request_id, data, error):
        if error.isSuccess():
            print(u'[onReqPriceData] success')
            print('合约代码', data.m_strInstrumentID)
            print('最新价', data.m_dLastPrice)

        else:
            print(u'[onReqPriceData] failed, error_msg:', error.errorMsg())

    def reqCommandsInfo(self):
        self.m_api.reqCommandsInfo(self.m_nRequestId)
        self.m_nRequestId +=1
        print(u'[reqCommandsInfo] 查询指令:')

    def onReqCommandsInfo(self, nRequestId, data, isLast, error):
        if error.isSuccess():
            print("指令详情 ={}".format(dir(data)))
            # print("orderid: ", data.m_nOrderID)
        else:
            print("errmsg: ", error.errorMsg())

    def reqCommandsInfoSync(self):
        print(u'[reqCommandsInfoSync] 查询指令:')
        errno = XtError(0, "")
        cmdList= self.m_api.reqCommandsInfoSync(errno)
        if errno.isSuccess():
            for data in cmdList:
                # if(data.m_nOrderID == 811340 ):
                print("查询指令成功,total:  ", len(cmdList))
                print("orderid: ", data.m_nOrderID)
                print("成交量: ", data.m_dTradedVolume)
                print("成交均价: ", data.m_dTradedPrice)
                print("成交金额: ", data.m_dTradedAmount)
                print("m_dPrice: ", data.m_dPrice)
                print("m_eOperationType: ", data.m_eOperationType)
                print("m_eStatus: ", data.m_eStatus)
                print("m_nCmdSource: ", data.m_nCmdSource)
        else:
            print("查询指令失败，：", errno.errorMsg())
    # 请求股东号
    def reqSecuAccount(self, account_id, account_key):
        print(u'[reqSecuAccount]查询账号:', account_id, u"的股东数据")
        self.m_nRequestId += 1
        self.m_api.reqSecuAccount(account_id, self.m_nRequestId, account_key)
    #请求资金数据的回调函数，data对应CAccountDetail结构, error对应XtError结构
    def onReqSecuAccount(self,account_id, request_id, accountkey, data, is_last, error):
        if error.isSuccess():
            print(u'[onReqSecuAccount] success, m_strSecuAccount:', data.m_strSecuAccount, "m_strExchangeID:", data.m_strExchangeID, "m_eMainFlag", data.m_eMainFlag,  ', is_last:', is_last)
        else:
            print(u'[onReqSecuAccount] failed, account_id:', account_id, ', error_msg:',error.errorMsg())
    def onRtnMarketAndTradeDay(self, market, tradeDay):
        print("onRtnMarketAndTradeDay market {}, tradeDay {}".format(market, tradeDay))
    def onNamedTimer(self, timerName):
        self.m_nRequestId += 1
        self.m_api.reqAccountDetail("2000154", self.m_nRequestId, "2____11194____11194____49____2000154____")

    def reqOrderDetailBySysIDSync(self, account_id, account_key):
        error = XtError(0, "")
        data = self.m_api.reqOrderDetailBySysIDSync(account_id, error, "2024061200002688", "SH", account_key)
        if error.isSuccess():
            print("reqOrderDetailBySysIDSync m_strAccountID: {}, m_strInstrumentID: {}".format(data.m_strAccountID, data.m_strInstrumentID))

    def reqOrderDetailBySysID(self, account_id, account_key):
        self.m_nRequestId += 1
        data = self.m_api.reqOrderDetailBySysID(account_id, self.m_nRequestId, "2024061200002688", "SH", account_key)
        print("reqOrderDetailBySysID started")
    def onReqOrderDetailBySysID(self, accountID, requestID, accountKey, orderSyeID, exchangeID, data, error):
        if error.isSuccess():
            print("reqOrderDetailBySysID m_strAccountID:", data.m_strAccountID)

if __name__ == '__main__':
    server_addr = "175.25.41.247:65300" # 统一交易服务器的地址
    username = "安值_独立交易员"
    password = "az913702"     #用户密码，客户端登录密码，非资金密码
    accountID = "2000463"       #测试账号，券商柜台的资金账号
    accountKey = "2____11172____60889____49____2000463____" #账号对应的账号key
    cb = CallBack(server_addr, username, password, accountID)#创建一个CallBack对象，后续操作基于该对象
    cb.init()
    cb.joinAsync()
    time.sleep(10)
    # while not cb.m_bConnected:
    #     pass
    # print("连接成功")
    # cb.doLogin()
    # while not cb.checkAccountStatus(accountKey):
    #     pass
    # print("账号登录成功，账号key：", accountKey)
    # #
    # cb.reqOrderDetailBySysIDSync(accountID, accountKey)
    # cb.reqOrderDetailBySysID(accountID, accountKey)
    #定时器测试
    # cb.m_api.startNamedTimer("test", 10, -1,False)
    # 查询用户对应的accountKey
    # cb.reqAccountKeySync()
    # 查询产品信息
    # cb.reqProductDataSync()

    # 查询账号资金流水
    # cb.reqFundFlowSync(accountID, accountKey)
    # 查询账号资金信息
    # cb.reqAccountDetailSync(accountID,accountKey)
    # 查询账号历史资金信息
    # cb.reqHistoryAccountDetailSync(accountID,accountKey)

    # 查询账号委托明细信息
    # cb.reqOrderDetailSync(accountID,accountKey)
    # 查询账号历史委托明细信息
    # cb.reqHistoryOrderDetailSync(accountID,accountKey)
    # cb.reqHistoryOrderDetail(accountID,accountKey)

    # 查询账号成交明细信息
    # cb.reqDealDetailSync(accountID,accountKey)
    # 查询账号成交统计信息
    # cb.reqDealStaticsSync(accountID,accountKey)
    # 查询账号历史成交明细信息
    # cb.reqHistoryDealDetailSync(accountID,accountKey)

    # 查询账号持仓明细信息
    # cb.reqPositionDetailSync(accountID,accountKey)
    # 查询账号持仓统计信息
    # cb.reqPositionStaticsSync(accountID,accountKey)
    # 查询账号历史持仓统计信息
    # cb.reqHistoryPositionStaticsSync(accountID,accountKey)
    # 查询日初持仓
    # cb.reqInitialPositionStaticsSync(accountID,accountKey)
    # 同步主动请求对应合约行情
    # cb.reqPriceDataSync("SH", "600000")
    # 查询用户所有指令信息
    # cb.reqCommandsInfoSync()
    # 查询账号委托明细信息
    # cb.reqOrderDetailSyncByOrderID(accountID,accountKey)
    # 查询账号成交明细信息
    # cb.reqDealDetailSyncByOrderID(accountID,accountKey)
    # 查询可下单量
    # cb.reqCanOrderVolumeSync(accountID, accountKey)
    # 查询枚举名称
    # cb.reqEnumItemName()
    # 查询未了结负债合约
    # cb.reqStkUnCloseCompactsSync(accountID, accountKey)
    # 查询未了结负债合约
    # cb.reqStkClosedCompactsSync(accountID, accountKey)
    # 请求信用账号资产数据
    # cb.reqCreditDetailSync(accountID,accountKey)

    # 异步请求测试demo

    # 请求账号资产数据
    # cb.reqAccountDetail(accountID, accountKey)
    # 请求信用账号资产数据
    # cb.reqCreditDetail(accountID,accountKey)
    # 请求委托明细
    # cb.reqOrderDetail(accountID,accountKey)
    # 请求成交明细
    # cb.reqDealDetail(accountID,accountKey)
    # cb.reqHistoryDealDetail(accountID,accountKey)
    # 请求持仓明细
    # cb.reqPositionDetail(accountID,accountKey)
    # 请求持仓统计
    # cb.reqPositionStatics(accountID,accountKey)
    # 请求账号历史持仓统计
    # cb.reqHistoryPositionStatics(accountID,accountKey)
    # 查询行情数据
    # cb.reqPriceData(accountID,accountKey)
    # 查询产品信息
    # cb.reqProductData()
    # 查询用户所有指令信息
    # cb.reqCommandsInfo()

    # 查询股东
    # cb.reqSecuAccount(accountID, accountKey)

    # 查询可下单量
    # cb.reqCanOrderVolume(accountID, accountKey)
    # 查询未了结负债合约
    # cb.reqStkUnCloseCompacts(accountID, accountKey)
    # 查询市场状态
    # cb.reqExchangeStatus(accountID, accountKey)
    #刷新未了结负债合约
    # cb.refreshStkUnCloseCompacts(accountID, accountKey)
    #刷新已了结负债合约
    # cb.refreshStkClosedCompacts(accountID, accountKey)


