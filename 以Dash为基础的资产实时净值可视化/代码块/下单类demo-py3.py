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

# XtApiCallBack类继承XtTraderApiCallback类，用于接收请求以及主推的回调, XtApiCallBack不处理返回数据，全都抛到client去处理
class XtApiCallBack(XtTraderApiCallback):
    def __init__(self, xtTraderApiClient):
        super(XtApiCallBack, self).__init__()
        self.m_apiClient = xtTraderApiClient
    def onConnected(self, success, error_msg):
        if success:
            self.m_apiClient.onConnected()
        else:
            self.m_apiClient.onConnectError(error_msg)
    def onUserLogin(self, username, password, nRequestId, error):
        self.m_apiClient.onUserLogin(username, password, nRequestId, error)
    def onRtnLoginStatus(self, account_id, status, account_type, error_msg):
        self.m_apiClient.onRtnLoginStatus(account_id, status, account_type, error_msg)
    def onRtnLoginStatusWithActKey(self, account_id, status, account_type, account_key, error_msg):
        self.m_apiClient.onRtnLoginStatusWithActKey(account_id, status, account_type, account_key, error_msg)
    def onOrder(self, request_id, order_id, remark, error):
        self.m_apiClient.onOrder(request_id, order_id, remark, error)
    def onRtnOrder(self, data):
        self.m_apiClient.onRtnOrder(data)
    def onRtnOrderDetail(self, data):
        self.m_apiClient.onRtnOrderDetail(data)
    def onRtnDealDetail(self, data):
        self.m_apiClient.onRtnDealDetail(data)
    def onRtnOrderError(self, data):
        self.m_apiClient.onRtnOrderError(data)
    def onCancel(self, request_id, error):
        self.m_apiClient.onCancel(request_id, error)
    def onCancelWithRemark(self, request_id, remark, error):
        self.m_apiClient.onCancelWithRemark(request_id, remark, error)
    def onCancelOrder(self, request_id, error):
        self.m_apiClient.onCancelOrder(request_id, error)
    def onRtnCancelError(self, data):
        self.m_apiClient.onRtnCancelError(data)

class xtTraderApiClient:
    def __init__(self, serverAddr, pserName, password):
        super(xtTraderApiClient, self).__init__()
        self.m_strAddress = serverAddr
        self.m_strUserName = pserName
        self.m_strPassword = password
        self.m_strFutureAccountKey = ''
        self.m_strFutureAccountID = ''
        self.m_strStkAccountID = ''
        self.m_strStkAccountKey = ''
        self.m_nRequestId = 1
        self.m_api = XtTraderApi.createXtTraderApi(self.m_strAddress)   #创建用户api实例
        self.m_bTraderApiConnected = 0
        self.m_nUserLogined = 0
        self.m_bDoRequest = 1
        self.callback = XtApiCallBack(self)
        self.m_dictAccountKeyStatus = {}
        self.m_dictAccountID2Key = {}
        self.m_dictAccountKey2type = {}
    def init(self):
        if self.m_strAddress == None:
            return -1, u'server address is empty'
        if self.m_api == None:
            return -1, u'failed to create traderapi client'
        if isinstance(self.callback, XtTraderApiCallback):                         #当前类是否为父类的实例
            self.m_api.setCallback(self.callback)
            return self.m_api.init("../config")
        return 0, u''
    def join(self):
        #调用下面两个函数都行，一个是同步，一个是异步，如果需要创建多个api对象，必须调用joinAll
        #self.m_api.joinAll()
        self.m_api.join()
        # self.m_api.join_async()
    #连接服务器的回调函数，参数success标识服务器连接是否成功,参数errorMsg表示服务器连接失败的错误信息
    def onConnected(self):
        print('[onConnected] connect to server: {} success'.format(self.m_strAddress))
        #machineInfo代表"IP地址|mac地址|磁盘序列号|cpu号|主机名|磁盘信息|CPUID指令的ecx参数|主板信息"，如果相关字段无关，那就直接给个空值，忽略相应字段就好，两个字段间用分隔符|隔开。
        machineInfo = "192.168.1.172|5C-F9-DD-73-7C-83|0682056C|BFEBFBFF000206A7|DESKTOP-84OBV5E|C,NTFS,223|6VKJD3X"
        appid = "xt_api_2.0"
        authcode = "7f3c92e678f9ec77"
        #异步登录
        #self.m_api.userLogin(self.m_strUserName, self.m_strPassword, self.m_nRequestId, machineInfo, appid, authcode)
        #同步登录
        self.testUserLoginSync(self.m_strUserName, self.m_strPassword, machineInfo, appid, authcode)
    def onConnectError(self, error_msg):
        print('[onConnectError] connect to server: {} failed, error_msg:{}'.format(self.m_strAddress, error_msg))
    #同步登录
    def testUserLoginSync(self, username,password,machineInfo,appid,authcode):
        print("userLoginSync started")
        error = self.m_api.userLoginSync(username,password, machineInfo, appid, authcode)
        if error.isSuccess():
            self.m_nUserLogined = 1
            print('userLoginSync resilt:', error.isSuccess())
            self.request()
        else:
            print("登录失败，错误信息：", error.errorMsg())
    #用户登录的回调函数
    def onUserLogin(self, username, password, nRequestId, error):
        if error.isSuccess():
            print('[onUserlogin] username:{},登录成功'.format(username))
            self.m_nUserLogined = 1
            self.request()
        else:
            print('[onUserlogin] username:{},登录失败，失败原因{}'.format(username, error.errorMsg()))
    def onRtnLoginStatus(self, account_id, status, account_type, error_msg):
        # print("onRtnLoginStatus")
        pass
    # 账号key主推接口，账号登录成功后才可以执行下单等操作，可以根据这里的status字段做判断
    # 参数: status 主推资金账号的登录状态
    # 参数: account_type 主推资金账号的类型 1:期货账号, 2:股票账号, 3:信用账号
    def onRtnLoginStatusWithActKey(self, account_id, status, account_type, account_key, error_msg):
        self.m_dictAccountKeyStatus[account_key] = status
        self.m_dictAccountID2Key[account_id] = account_key
        self.m_dictAccountKey2type[account_key] = account_type
        if status == EBrokerLoginStatus.BROKER_LOGIN_STATUS_OK:
            print(u'[onRtnLoginStatusWithActKey] account_id：{}, account_type: {}, 账号登录成功，初始化完成，可以交易'.format(account_id,account_type))
            self.request()
        else:
            pass
    #账号登录之后做检查
    def request(self):
        # demo遍历所有账户测试查询，请根据实际情况修改代码
        if(self.m_dictAccountID2Key):
            for name in self.m_dictAccountID2Key:
                self.m_strAccountID = name
                self.m_strAccountKey = self.m_dictAccountID2Key[name]
                print("m_dictAccountID2Key accountID:",name, "accountkey", self.m_strAccountKey)
                if name and self.checkAccountStatus(self.m_strAccountKey):
                    self.doRequest(self.m_strAccountID, self.m_strAccountKey)
    #检查请求账号是否登录成功
    def checkAccountStatus(self, accountKey):
        print("userlogin status:", self.m_nUserLogined)
        print("account size:", len(self.m_dictAccountKeyStatus))
        status = self.m_dictAccountKeyStatus[accountKey]
        print("accountKey", accountKey, " status:", status)
        if self.m_nUserLogined:
            if status == EBrokerLoginStatus.BROKER_LOGIN_STATUS_OK or status == EBrokerLoginStatus.BROKER_LOGIN_STATUS_CLOSED:
                return 1
            else:
                return 0
        else:
            return 0

    #连接上之后的测试请求
    def doRequest(self, accountId, accountKey):
        print("doRequest", "accountId", accountId, "accountKey", accountKey)
        #同步请求测试demo
        # 股票普通单委托 同步接口，  demo下单会自动撤单，如不需要撤单，请将下单最后的撤单代码逻辑注释掉
        self.stockOrdinaryOrderSync(accountId,accountKey)
        # 股票普通单委托 异步接口
        # self.stockOrdinaryOrder(accountId,accountKey)
        # 股票普通组合单委托 异步接口
        # self.stockOrdinaryGroupOrder(accountId, accountKey)

        # 期货普通单 异步接口
        #self.futureOrdinaryOrder(accountId, accountKey)

        # 普通算法委托 异步接口
        #self.algorithmOrder(accountId, accountKey)

        # 智能算法委托（被动算法） 异步接口
        # self.intelligentAlgorithmOrder(accountId, accountKey)
        # 智能算法委托（被动算法） 同步接口
        # self.intelligentAlgorithmOrderSync(accountId, accountKey)

        # 智能算法组合单委托（被动算法） 异步接口
        # self.AlgGroupOrder(accountId, accountKey)

        # 主动算法组合单委托 同步接口
        # self.externAlgGroupOrderSync(accountId, accountKey)
        # 主动算法组合单委托 异步接口
        # self.externAlgGroupOrder(accountId, accountKey)

        # 主动算法单下单 同步接口
        # self.externAlgorithmOrderSync(accountId, accountKey)
        # 主动算法单下单 异步接口
        # self.externAlgorithmOrder(accountId, accountKey)

        #撤销指令 同步接口，请在""内填写下单返回的指令号,注意类型是int，删掉""
        # self.cancelSync(723455, accountKey)
        #暂停指令
        # self.pauseSync(463819)
        #恢复指令
        # self.resumeSync(463819)

        #撤销指令 异步接口，请在""内填写下单返回的指令号,注意类型是int，删掉""
        #self.cancel("", accountKey)

        #撤销委托 同步接口，请在""内填写下单返回的委托号，市场，合约
        #self.cancelOrderSync(accountId, "", "", "", accountKey)

        #撤销委托 异步接口，请在""内填写下单返回的委托号，市场，合约
        #self.cancelOrder(accountId, "", "", "", accountKey)
    # 股票普通单 同步接口
    def stockOrdinaryOrderSync(self, account_id, account_key):
        print("stockOrdinaryOrderSync")
        orderInfo = COrdinaryOrder()  # 初始化数据，普通单结构体
        orderInfo.m_strAccountID = account_id  # 资金账号，必填参数。不填会被api打回，并且通过onOrder反馈失败
        orderInfo.m_dPrice = 10.58  # 报单价格
        orderInfo.m_dSuperPriceRate = 0  # 单笔超价百分比，选填字段。默认为0
        orderInfo.m_nVolume = 100  # 报单委托量，必填字段。默认int最大值，填0或不填会被api打回
        orderInfo.m_strMarket = "SZ"  # 报单市场。必填字段。股票市场有"SH"/"SZ"，如果填空或填错都会被api直接打回
        orderInfo.m_strInstrument = "000001"  # 报单合约代码，必填字段
        orderInfo.m_ePriceType = EPriceType.PRTP_MARKET	  # 枚举类型，报单价格类型，必填字段
        orderInfo.m_eOperationType = EOperationType.OPT_BUY  # 报单委托类型。必填字段
        orderInfo.m_strRemark = "api 下单"
        error = XtError(0, "")
        orderid  = self.m_api.orderSync(orderInfo, error, account_key)
        if error.isSuccess():
            print(u'[orderSync]股票普通单, accountId:', account_id, "orderID: ", orderid)
            #发起撤单
            # self.cancelSync(orderid, account_key)
        else:
            print("orderSync 股票普通单下单失败，废单原因： ", error.errorMsg())

    # 股票普通单 异步接口
    def stockOrdinaryOrder(self, account_id, account_key):
        print(u'[stockOrdinaryOrder]股票普通单, accountId:', account_id)
        orderInfo = COrdinaryOrder()  # 初始化数据，普通单结构体
        orderInfo.m_strAccountID = account_id  # 资金账号，必填参数。不填会被api打回，并且通过onOrder反馈失败
        orderInfo.m_dPrice = 14.5  # 报单价格
        orderInfo.m_dSuperPriceRate = 0  # 单笔超价百分比，选填字段。默认为0
        orderInfo.m_nVolume = 400  # 报单委托量，必填字段。默认int最大值，填0或不填会被api打回
        orderInfo.m_strMarket = "SH"  # 报单市场。必填字段。股票市场有"SH"/"SZ"，如果填空或填错都会被api直接打回
        orderInfo.m_strInstrument = "600004"  # 报单合约代码，必填字段
        orderInfo.m_ePriceType = EPriceType.PRTP_FIX	  # 枚举类型，报单价格类型，必填字段
        orderInfo.m_eOperationType = EOperationType.OPT_BUY  # 报单委托类型。必填字段
        orderInfo.m_strRemark = "alpha"
        orderInfo.m_strStrategyID = "8184499999898044228";
        self.m_nRequestId += 1
        orderInfo.m_strStrategyID = "-72692859861132081";
        self.m_nRequestId += 1
        self.m_api.order(orderInfo, self.m_nRequestId, account_key)
        print(u'[stockOrdinaryOrder]股票普通单, accountId:', account_id)
    #期货普通单
    def futureOrdinaryOrder(self, account_id, account_key):
        orderInfo = COrdinaryOrder()  # 初始化COrdinaryOrder数据 ，普通单结构体
        orderInfo.m_strAccountID = account_id  # 资金账号，必填参数。不填会被api打回，并且通过onOrder反馈失败
        orderInfo.m_dPrice = 15705  # 报单价格，默认为double最大值
        orderInfo.m_dSuperPriceRate = 0  # 单笔超价百分比，选填字段。默认为0
        orderInfo.m_nVolume = 1  # 报单委托量，必填字段。默认int最大值，填0或不填会被api打回
        orderInfo.m_strMarket = "CZCE"  # 报单市场。必填字段
        orderInfo.m_strInstrument = "CF107"  # 报单合约代码，必填字段。
        orderInfo.m_ePriceType = EPriceType.PRTP_FIX	  # 报单价格类型，必填字段
        orderInfo.m_eOperationType = EOperationType.OPT_OPEN_LONG  # 报单委托类型。必填字段
        orderInfo.m_strRemark = "cta"
        self.m_nRequestId += 1
        self.m_api.order(orderInfo, self.m_nRequestId, account_key)  # 下单
        print(u'[futureOrdinaryOrder]期货普通单, accountId:', account_id, ', requestId:', self.m_nRequestId)
    # 普通算法委托
    def algorithmOrder(self, account_id, account_key):
        #股票为例
        orderInfo = CAlgorithmOrder()   # 算法单实例
        orderInfo.m_strAccountID = account_id    #资金账号
        orderInfo.m_strMarket = "SH"  # 市场
        orderInfo.m_strInstrument = "600000"  # 合约代码
        orderInfo.m_eOperationType = EOperationType.OPT_BUY  # 委托类型
        orderInfo.m_ePriceType = EPriceType.PRTP_FIX  # 报价类型
        orderInfo.m_dPrice = 12.3  # 委托价格
        orderInfo.m_nVolume = 1000  # 委托数量
        orderInfo.m_eSingleVolumeType = EVolumeType.VOLUME_FIX  # 单笔基准量，默认为目标量
        orderInfo.m_dSingleVolumeRate = 0.1 # 基准量比例
        orderInfo.m_dPlaceOrderInterval = 10 # 下单间隔
        orderInfo.m_dWithdrawOrderInterval = 10 #撤单间隔
        orderInfo.m_dPriceRangeRate = 0.1   # 价格波动区间，必填字段 0 <= orderInfo.m_dPriceRangeRate <= 1
        orderInfo.m_nSingleNumMin = 100  # 单笔最小量，股票最小为100，期货最小为1
        orderInfo.m_nSingleNumMax = 1000 # 单笔最大量
        # 指令有效时间
        orderInfo.m_nValidTimeStart = 0
        orderInfo.m_nValidTimeEnd = orderInfo.m_nValidTimeStart + 1800
        orderInfo.m_nMaxOrderCount = 100  # 最大下单笔数
        orderInfo.m_strRemark = 'algorithm' # 投资备注
        self.m_nRequestId += 1
        self.m_api.order(orderInfo,self.m_nRequestId, account_key)    #开始下单
        print(u'[algorithmOrder]普通算法委托下单, account_id:', account_id, ', request_id:', self.m_nRequestId)
    # 智能算法委托（被动算法）
    def intelligentAlgorithmOrder(self, account_id, account_key):
        #股票为例
        orderInfo = CIntelligentAlgorithmOrder()   # 算法单实例
        orderInfo.m_strAccountID = account_id    #资金账号
        orderInfo.m_strMarket = "SH"  # 市场
        orderInfo.m_strInstrument = "600000"  # 合约代码
        orderInfo.m_eOperationType = EOperationType.OPT_BUY  # 委托类型
        orderInfo.m_ePriceType = EPriceType.PRTP_FIX  # 报价类型
        orderInfo.m_dPrice = 12.3  # 委托价格
        orderInfo.m_nVolume = 1000  # 委托数量
        orderInfo.m_strOrderType = "VWAP"
        # 指令有效时间
        orderInfo.m_nValidTimeStart = int(time.time())
        orderInfo.m_nValidTimeEnd = orderInfo.m_nValidTimeStart + 1800
        orderInfo.m_dMaxPartRate = 1  # 量比比例
        orderInfo.m_dMinAmountPerOrder = 100  # 委托最小金额
        orderInfo.m_strRemark = 'intelligent' # 投资备注
        orderInfo.m_strStrategyID = '123321' # m_strStrategyID
        self.m_nRequestId += 1
        self.m_api.order(orderInfo,self.m_nRequestId, account_key)    #开始下单
        print(u'[intelligentAlgorithmOrder]智能算法委托下单, account_id:', account_id, ', request_id:', self.m_nRequestId)
    # 智能算法委托（被动算法）
    def intelligentAlgorithmOrderSync(self, account_id, account_key):
        #股票为例
        orderInfo = CIntelligentAlgorithmOrder()   # 算法单实例
        orderInfo.m_strAccountID = account_id    #资金账号
        orderInfo.m_strMarket = "SH"  # 市场
        orderInfo.m_strInstrument = "600000"  # 合约代码
        orderInfo.m_eOperationType = EOperationType.OPT_BUY  # 委托类型
        orderInfo.m_ePriceType = EPriceType.PRTP_FIX  # 报价类型
        orderInfo.m_dPrice = 12.3  # 委托价格
        orderInfo.m_nVolume = 1000  # 委托数量
        orderInfo.m_strOrderType = "VWAP"
        # 指令有效时间
        orderInfo.m_nValidTimeStart = int(time.time())
        orderInfo.m_nValidTimeEnd = orderInfo.m_nValidTimeStart + 1800
        orderInfo.m_dMaxPartRate = 1  # 量比比例
        orderInfo.m_dMinAmountPerOrder = 100  # 委托最小金额
        orderInfo.m_strRemark = 'intelligent' # 投资备注
        orderInfo.m_strStrategyID = '123321' # m_strStrategyID
        error = XtError(0, "")
        orderid = self.m_api.orderSync(orderInfo, error, account_key)
        if error.isSuccess():
            print(u'[orderSync]智能算法委托, accountId:', account_id, "orderID: ", orderid)
        else:
            print("orderSync 智能算法下单失败，废单原因： ", error.errorMsg())
    # 主动算法组合单委托（被动算法） 同一种算法，可传入不同市场 合约 每只股票的下单类型， 每只股票的下单量，其余参数相同
    def externAlgGroupOrder(self, account_id, account_key):
        #股票为例
        orderInfo = CExternAlgGroupOrder()   # 组合智能算法单实例

        orderInfo.m_orderParam = CExternAlgorithmOrder()   # 智能算法单实例
        orderInfo.m_orderParam.m_strAccountID = account_id    #资金账号
        # orderInfo.m_orderParam.m_eOperationType = EOperationType.OPT_BUY  # 委托类型
        orderInfo.m_orderParam.m_strMarket = "" # 委托价格
        orderInfo.m_orderParam.m_strInstrument = "" # 委托价格
        orderInfo.m_orderParam.m_dPrice = 0 # 委托价格
        orderInfo.m_orderParam.m_strOrderType = "FTAIWAP"
        # 指令有效时间
        orderInfo.m_orderParam.m_nValidTimeStart = int(time.time())
        orderInfo.m_orderParam.m_nValidTimeEnd = orderInfo.m_orderParam.m_nValidTimeStart + 1800

        orderInfo.m_strMarket = ["SZ", "SH"]  # 市场
        orderInfo.m_strInstrument = ["300356", "600004"]  # 合约代码
        orderInfo.m_nVolume = [1000, 1000]  # 委托数量
        orderInfo.m_eOperationType = [EOperationType.OPT_BUY, EOperationType.OPT_BUY]  # 每只股票的下单类型
        # orderInfo.m_eOperationType = [EOperationType.OPT_SELL, EOperationType.OPT_BUY]  # 每只股票的下单类型
        orderInfo.m_nOrderNum = 2
        orderInfo.m_strRemark = 'CExternAlgGroupOrder test' # 投资备注

        self.m_nRequestId += 1
        self.m_api.order(orderInfo, self.m_nRequestId, account_key)    #开始下单
        print(u'[externAlgGroupOrder]主动算法组合单委托下单, account_id:', account_id, ', request_id:', self.m_nRequestId)

    # 主动算法组合单委托（被动算法） 同一种算法，可传入不同市场 合约 每只股票的下单类型， 每只股票的下单量，其余参数相同
    def externAlgGroupOrderSync(self, account_id, account_key):
        # 股票为例
        orderInfo = CExternAlgGroupOrder()  # 组合主动算法单实例

        orderInfo.m_orderParam = CExternAlgorithmOrder()  # 主动算法单实例
        orderInfo.m_orderParam.m_strAccountID = account_id  # 资金账号
        # orderInfo.m_orderParam.m_eOperationType = EOperationType.OPT_BUY  # 委托类型
        orderInfo.m_orderParam.m_strMarket = ""  # 委托价格
        orderInfo.m_orderParam.m_strInstrument = ""  # 委托价格
        orderInfo.m_orderParam.m_dPrice = 0  # 委托价格
        orderInfo.m_orderParam.m_strOrderType = "FTAIWAP"
        # 指令有效时间
        orderInfo.m_orderParam.m_nValidTimeStart = int(time.time())
        orderInfo.m_orderParam.m_nValidTimeEnd = orderInfo.m_orderParam.m_nValidTimeStart + 1800

        orderInfo.m_strMarket = ["SZ", "SH"]  # 市场
        orderInfo.m_strInstrument = ["300356", "600004"]  # 合约代码
        orderInfo.m_nVolume = [1000, 1000]  # 委托数量
        orderInfo.m_eOperationType = [EOperationType.OPT_BUY, EOperationType.OPT_BUY]  # 每只股票的下单类型
        # orderInfo.m_eOperationType = [EOperationType.OPT_SELL, EOperationType.OPT_BUY]  # 每只股票的下单类型
        orderInfo.m_nOrderNum = 2
        orderInfo.m_strRemark = 'CExternAlgGroupOrder test'  # 投资备注
        error = XtError(0, "")
        orderid = self.m_api.orderSync(orderInfo, error, account_key)
        if error.isSuccess():
            print(u'[CExternAlgGroupOrder]主动算法组合单委托下单, accountId:', account_id, "orderID: ", orderid)
        else:
            print("[CExternAlgGroupOrder]主动算法组合单下单失败，废单原因： ", error.errorMsg())

    # 智能算法组合单委托（被动算法） 同一种算法，可传入不同市场 合约 每只股票的下单类型， 每只股票的下单量，其余参数相同
    def AlgGroupOrder(self, account_id, account_key):
        #组合单兼容多资金账号组合下单功能，如果是单账号组合单，m_strAccountKey可不填，如果是多账号下单，m_strAccountKey必填，否则会导致下单异常（m_strAccountKey指CIntelligentAlgorithmOrder里面的入参，非函数入参accountKey，m_strAccountKey填写之后，函数入参accountKey填写无意义）。
        #  使用多资金账户下单，必须保证每个合约的买卖方向一致性。
        #  每个账户对应的每个合约必须保证唯一性。
        #  单账号多合约可以选择买入卖出双方向。
        #  单账号多合约是组合单，多账号多合约也是组合单，多账号单合约只是批量单，在对应业务界面展示。
        #股票为例
        orderInfo = CAlgGroupOrder()   # 组合智能算法单实例
        # #换仓算法示例
        # orderInfo.m_orderParam = XtTraderPyApi.CIntelligentAlgorithmOrder()   # 智能算法单实例
        # orderInfo.m_orderParam.m_strAccountID = account_id    #资金账号
        # orderInfo.m_orderParam.m_ePriceType = XtTraderPyApi.EPriceType.PRTP_MARKET  # 报价类型
        # orderInfo.m_orderParam.m_dPrice = 12.3  # 委托价格
        # orderInfo.m_orderParam.m_strOrderType = "SWITCH"
        # # 换仓算法示例结束
        orderInfo.m_orderParam =CIntelligentAlgorithmOrder()   # 智能算法单实例
        orderInfo.m_orderParam.m_strAccountID = account_id    #资金账号 采用多账号下单时，m_strAccountID可不填写
        orderInfo.m_orderParam.m_eOperationType = EOperationType.OPT_BUY  # 委托类型
        orderInfo.m_orderParam.m_ePriceType = EPriceType.PRTP_MARKET  # 报价类型
        orderInfo.m_orderParam.m_dPrice = 12.3  # 委托价格
        orderInfo.m_orderParam.m_strOrderType = "TWAP"
        orderInfo.m_orderParam.m_nValidTimeStart = int(time.time())
        orderInfo.m_orderParam.m_nValidTimeEnd = orderInfo.m_orderParam.m_nValidTimeStart + 1800
        orderInfo.m_orderParam.m_dMaxPartRate = 1  # 量比比例
        orderInfo.m_orderParam.m_dMinAmountPerOrder = 100  # 委托最小金额
        orderInfo.m_orderParam.m_dOrderRateInOpenAcution = 0.4
        orderInfo.m_orderParam.m_dPriceOffsetBpsForAuction = 400
        orderInfo.m_orderParam.m_nStopTradeForOwnHiLow = EStopTradeForOwnHiLow.STOPTRADE_NONE
        orderInfo.m_orderParam.m_bOnlySellAmountUsed = True
        orderInfo.m_orderParam.m_dBuySellAmountDeltaPct = 3.0
        # orderInfo.m_orderParam.m_strStrategyID = '123569' # 收益互换策略ID
        orderInfo.m_strMarket = ["SH", "SH", "SH", "SZ", "SZ", "SZ"]  # 市场
        orderInfo.m_strInstrument = ["600000", "600000", "600000", "000001", "000001", "000001"]  # 合约代码
        #组合单兼容多资金账号组合下单功能，如果是单账号组合单，m_strAccountKey可不填，如果是多账号下单，m_strAccountKey必填，否则会导致下单异常（m_strAccountKey指CIntelligentAlgorithmOrder里面的入参，非函数入参accountKey，m_strAccountKey填写之后，函数入参accountKey填写无意义）。
        orderInfo.m_strAccountKey = ["2____11172____60889____49____2000462____",
                                     "2____11172____60889____49____2000463____",
                                     "2____11172____60889____49____2000464____",
                                     "2____11172____60889____49____2000462____",
                                     "2____11172____60889____49____2000463____",
                                     "2____11172____60889____49____2000464____"]  # 合约代码
        orderInfo.m_nVolume = [200, 300, 400, 500, 400, 300]  # 委托数量
        orderInfo.m_eOperationType = [EOperationType.OPT_BUY]*6  # 每只股票的下单类型
        orderInfo.m_dMaxPartRate = [0.2, 0.3, 0.4, 0.5, 0.5, 0.3]  # 委托量比
        orderInfo.m_nOrderNum = 6
        orderInfo.m_strRemark = 'CAlgGroupOrder' # 投资备注

        self.m_nRequestId += 1
        self.m_api.order(orderInfo, self.m_nRequestId, account_key)    #开始下单
        print(u'[AlgGroupOrder]智能算法组合单委托下单, account_id:', account_id, ', request_id:', self.m_nRequestId)
    #普通单组合下单
    def stockOrdinaryGroupOrder(self, account_id, account_key):
        #组合单兼容多资金账号组合下单功能，如果是单账号组合单，m_strAccountKey可不填，如果是多账号下单，m_strAccountKey必填，否则会导致下单异常（m_strAccountKey指COrdinaryGroupOrder里面的入参，非函数入参accountKey，m_strAccountKey填写之后，函数入参accountKey填写无意义）。
        #  使用多资金账户下单，必须保证每个合约的买卖方向一致性。
        #  每个账户对应的每个合约必须保证唯一性。
        #  单账号多合约可以选择买入卖出双方向。
        #  单账号多合约是组合单，多账号多合约也是组合单，多账号单合约只是批量单，在对应业务界面展示。
        #股票为例
        orderInfo = COrdinaryGroupOrder()   # 普通单实例
        orderInfo.m_strAccountID = account_id    #资金账号
        orderInfo.m_dSuperPriceRate = 0  # 单笔超价百分比，选填字段。默认为0
        orderInfo.m_nOrderNum = 3  # 股票只数
        orderInfo.m_strMarket = ["SZ", "SH", "SH"]  # 市场
        orderInfo.m_strInstrument = ["000002", "600004", "600006"]  # 合约代码
        orderInfo.m_nVolume = [100, 200, 300]  # 委托数量
        orderInfo.m_eOperationType = [EOperationType.OPT_BUY, EOperationType.OPT_BUY, EOperationType.OPT_BUY]  # 报单委托类型
        orderInfo.m_ePriceType = EPriceType.PRTP_LATEST  # 报价类型
        orderInfo.m_eHedgeFlag = EHedgeFlagType.HEDGE_FLAG_SPECULATION  # 报价类型
        orderInfo.m_strRemark = 'COrdinaryGroupOrder test' # 投资备注
        self.m_nRequestId += 1
        self.m_api.order(orderInfo, self.m_nRequestId, account_key)    #开始下单
        print(u'[COrdinaryGroupOrder]普通组合下单, account_id:', account_id, ', request_id:', self.m_nRequestId)
    # 主动算法单下单
    def externAlgorithmOrder(self, account_id, account_key):
        #股票为例
        orderInfo = CExternAlgorithmOrder()   # 主动算法单实例
        orderInfo.m_strAccountID = account_id   #资金账号
        orderInfo.m_strMarket = "SH"  # 市场
        orderInfo.m_strInstrument = "600000"  # 合约代码
        orderInfo.m_strOrderType = "FTAIWAP" # 主动算法名称
        orderInfo.m_dPrice = 12.3  # 基准价
        orderInfo.m_nVolume = 1000  # 委托数量
        orderInfo.m_eOperationType = EOperationType.OPT_BUY  # 委托类型
        # 指令有效时间
        orderInfo.m_nValidTimeStart = int(time.time())
        orderInfo.m_nValidTimeEnd = orderInfo.m_nValidTimeStart + 1800
        orderInfo.m_strRemark = 'CExternAlgorithmOrder' # 投资备注
        self.m_nRequestId += 1
        self.m_api.order(orderInfo,self.m_nRequestId, account_key)    #开始下单
        print(u'[externAlgorithmOrder]主动算法单下单, account_id:', account_id, ', request_id:', self.m_nRequestId)

    # 主动算法单下单
    def externAlgorithmOrderSync(self, account_id, account_key):
        #股票为例
        orderInfo = CExternAlgorithmOrder()   # 主动算法单实例
        orderInfo.m_strAccountID = account_id   #资金账号
        orderInfo.m_strMarket = "SH"  # 市场
        orderInfo.m_strInstrument = "600000"  # 合约代码
        orderInfo.m_strOrderType = "FTAIWAP" # 主动算法名称
        orderInfo.m_dPrice = 12.3  # 基准价
        orderInfo.m_nVolume = 1000  # 委托数量
        orderInfo.m_eOperationType = EOperationType.OPT_BUY  # 委托类型
        # 指令有效时间
        orderInfo.m_nValidTimeStart = int(time.time())
        orderInfo.m_nValidTimeEnd = orderInfo.m_nValidTimeStart + 1800
        orderInfo.m_strRemark = 'CExternAlgorithmOrder' # 投资备注
        error = XtError(0, "")
        orderid = self.m_api.orderSync(orderInfo, error, account_key)
        if error.isSuccess():
            print(u'[CExternAlgorithmOrder]主动算法单委托下单, accountId:', account_id, "orderID: ", orderid)
        else:
            print("[CExternAlgorithmOrder]主动算法单下单失败，废单原因： ", error.errorMsg())

    #下达指令后的回调, error对应XtError结构
    def onOrder(self, request_id, order_id, remark, error):
        if error.isSuccess():
            print(u'[onOrder] success:True',u', order_id:',order_id, u', request_id: ',request_id, u', error_msg: ',error.errorMsg())
            #self.cancel_cmd(orderId)
        else:
            print(u'[onOrder] failed',u', order_id:',order_id, u', request_id: ',request_id, u', error_msg: ',error.errorMsg())
    # 获取主推的指令状态, data对应COrderInfo结构
    def onRtnOrder(self, data):
        if data.m_eStatus == EOrderCommandStatus.OCS_CHECKING:
            orderStatus = u'风控检查中'
        elif data.m_eStatus == EOrderCommandStatus.OCS_RUNNING:
            orderStatus = u'运行中'
        elif data.m_eStatus == EOrderCommandStatus.OCS_APPROVING:
            orderStatus = u'审批中'
        elif data.m_eStatus == EOrderCommandStatus.OCS_REJECTED:
            orderStatus = u'已驳回'
        elif data.m_eStatus == EOrderCommandStatus.OCS_RUNNING:
            orderStatus = u'运行中'
        elif data.m_eStatus == EOrderCommandStatus.OCS_CANCELING:
            orderStatus = u'撤销中'
        elif data.m_eStatus == EOrderCommandStatus.OCS_FINISHED:
            orderStatus = u'已完成'
        elif data.m_eStatus == EOrderCommandStatus.OCS_STOPPED:
            orderStatus = u'已撤销'
        else:
            orderStatus = u'默认状态:', data.m_eStatus
        print(u'[onRtnOrder] 指令编号:', data.m_nOrderID, ', account_id:', data.m_strAccountID, ', start_time:', data.m_startTime, \
        ', end_time:', data.m_endTime, ', status:', data.m_eStatus, ', traded_volume:', data.m_dTradedVolume, ', canceler:', data.m_canceler, \
        ', broker_type:', data.m_eBrokerType, ', remark:', data.m_strRemark, 'msg:', data.m_strMsg)

    # 获得主推的委托明细, data对应COrderDetail结构
    def onRtnOrderDetail(self, data):
        if data.m_eOrderStatus == EEntrustStatus.ENTRUST_STATUS_UNREPORTED:
            entrust_status = u'未报'
        elif data.m_eOrderStatus == EEntrustStatus.ENTRUST_STATUS_WAIT_REPORTING:
            entrust_status = u'待报'
        elif data.m_eOrderStatus == EEntrustStatus.ENTRUST_STATUS_REPORTED:
            entrust_status = u'已报'
        elif data.m_eOrderStatus == EEntrustStatus.ENTRUST_STATUS_REPORTED_CANCEL:
            entrust_status = u'已报待撤'
        elif data.m_eOrderStatus == EEntrustStatus.ENTRUST_STATUS_PARTSUCC_CANCEL:
            entrust_status = u'部成待撤'
        elif data.m_eOrderStatus == EEntrustStatus.ENTRUST_STATUS_PART_CANCEL:
            entrust_status = u'部撤'
        elif data.m_eOrderStatus == EEntrustStatus.ENTRUST_STATUS_CANCELED:
            entrust_status = u'已撤'
        elif data.m_eOrderStatus == EEntrustStatus.ENTRUST_STATUS_PART_SUCC:
            entrust_status = u'部成'
        elif data.m_eOrderStatus == EEntrustStatus.ENTRUST_STATUS_SUCCEEDED:
            entrust_status = u'已成'
        elif data.m_eOrderStatus == EEntrustStatus.ENTRUST_STATUS_JUNK:
            entrust_status = u'废单'
        else:
            entrust_status = u'默认状态->', data.m_eOrderStatus
        print(u'[onRtnOrderDetail] 指令编号:', data.m_nOrderID, u'，投资备注:', data.m_strRemark, u', 合同编号:', data.m_strOrderSysID, \
            u'，委托状态:', entrust_status, u'，已成量:',data.m_nTradedVolume,  u'，成交均价:', data.m_dAveragePrice, \
            u'，代码:', data.m_strInstrumentID, u'，ErrorID:', data.m_nErrorID, u'，ErrorMsg:', data.m_strErrorMsg, u', direction:', data.m_nDirection, \
            u', offset:', data.m_eOffsetFlag, u', hedge:', data.m_eHedgeFlag, u', m_eEntrustType:', data.m_eEntrustType)
        #self.cancel_order(data.m_strAccountID, data.m_strOrderSysID, data.m_strExchangeID, data.m_strInstrumentID, self.m_strAccountKey)

    # 获得主推的成交明细, data对应CDealDetail
    def onRtnDealDetail(self, data):
        print(u'[onRtnDealDetail] 指令编号:', data.m_nOrderID,  u'，投资备注:', data.m_strRemark, data.m_nOrderID, u'，成交量:', data.m_nVolume, u'，成交均价:', data.m_dAveragePrice)

    # 获得主推的委托错误信息，data对应COrderError结构，在委托被迅投风控或者柜台驳回都会产生这个回调
    def onRtnOrderError(self, data):
        if data == None:
            print(u'[onRtnOrderError], data is None')
        else:
            print(u'[onRtnOrderError] orderId: ', data.m_nOrderID, u'm_nErrorID: ', data.m_nErrorID, u'm_strErrorMsg: ', data.m_strErrorMsg, u'm_nRequestID:', data.m_nRequestID, u'm_nOrderID:', data.m_nOrderID)

    #同步撤单（根据指令号）
    def cancelSync(self,order_id, account_key):
        print(u'[cancel] 撤委托，指令编号:', order_id, 'account_key',account_key)
        errno = XtError(0,"")
        self.m_api.cancelSync(order_id, errno, account_key)
        if errno.isSuccess():
            print(u'[cancel] 撤委托成功，指令编号:', order_id, 'account_key',account_key)

    #同步暂停指令（根据指令号）
    def pauseSync(self,order_id):
        errno = XtError(0, "")
        print(u'[pauseSync] 暂停指令，指令编号:', order_id)
        self.m_api.pauseSync(order_id, errno)
        if errno.isSuccess():
            print(u'[pauseSync] 暂停指令成功，指令编号:', order_id)
    #同步恢复指令（根据指令号）
    def resumeSync(self,order_id):
        print(u'[resumeSync] 恢复指令，指令编号:', order_id)
        errno = XtError(0,"")
        self.m_api.resumeSync(order_id, errno)
        if errno.isSuccess():
            print(u'[resumeSync] 恢复指令成功，指令编号:', order_id)

    #同步撤单（根据委托号）
    def cancelOrderSync(self,account_id, order_sysid, market, code, account_key):
        print(u'[cancel_order] 撤委托，合同编号:', order_sysid, 'account_key',account_key)
        errno = XtError(0, "")
        self.m_api.cancelOrderSync(account_id, order_sysid, '', '', errno, account_key)
        if errno.isSuccess():
            print(u'[cancel] 撤委托成功，合同编号:', order_sysid, 'account_key',account_key)

    #撤销指令 异步
    def cancel(self, order_id,account_key):
        print(u'[cancel_cmd] 撤指令，指令编号:', order_id)
        self.m_nRequestId += 1
        self.m_api.cancel(order_id,self.m_nRequestId)

    #撤销指令回调, error对应XtError结构
    def onCancel(self, request_id, error):
        if error.isSuccess():
            print(u'[onCancel] success')
        else:
            print(u'[onCancel] failed, error_msg: ', error.errorMsg())

    # 撤销指令回调
    def onCancelWithRemark(self, request_id, remark, error):
        if error.isSuccess():
            print(u'[onCancelWithRemark] success, remark: ', remark)
        else:
            print(u'[onCancelWithRemark] failed', u', remark:', remark, u', error_msg: ', error.errorMsg())

    #撤销委托 异步
    def cancelOrder(self, account_id, order_sysid, market, code, account_key):
        print(u'[cancel_order] 撤委托，合同编号:', account_id, ', ', order_sysid,  ', ', market,  ', ', code,  ', ', account_key,  ', ', order_sysid)
        self.m_nRequestId += 1
        self.m_api.cancelOrder(account_id, order_sysid, market, '', self.m_nRequestId, account_key)

    #撤销委托回调, error对应XtError结构
    def onCancelOrder(self, request_id, error):
        if error.isSuccess():
            print(u'[onCancelOrder] success')
        else:
            print(u'[onCancelOrder] failed, error_msg: ', error.errorMsg())

    # 获得主推的撤单错误信息，data对应CCancelError结构
    # 撤委托请求被迅投系统风控打回，或者撤销请求被柜台打回，均通过这个接口推送
    def onRtnCancelError(self, data):
        print(u'[onRtnCancelError]orderId:', data.m_nOrderID, u'm_nErrorID:', data.m_nErrorID, u'm_strErrorMsg:', data.m_strErrorMsg)
if __name__ == '__main__':
    serverAddr = "175.25.41.247:65300" # 统一交易服务器的地址
    username = "api3"
    password = "@a1234567"
    apiclient = xtTraderApiClient(serverAddr, username, password)
    apiclient.init()
    apiclient.join()
    time.sleep(100000)

