from __future__ import annotations
import typing
__all__ = ['CAccountDetail', 'CAccountKey', 'CAlgGroupOrder', 'CAlgorithmOrder', 'CCancelError', 'CCheckData', 'CCommissionRateDetail', 'CCoveredStockPosition', 'CCreditAccountDetail', 'CCreditAssure', 'CCreditDetail', 'CCreditSloCode', 'CCreditSubjects', 'CDealDetail', 'CDealStatics', 'CDeliveryDetail', 'CETFComponentStockInfo', 'CETFPCFDetail', 'CExchangeStatus', 'CExternAlgGroupOrder', 'CExternAlgorithmOrder', 'CFundFlow', 'CFuturePositionStatics', 'CGroupOrder', 'CHuaChuangAlgoGroupOrder', 'CHuaChuangAlgorithmOrder', 'CInstrumentDetail', 'CInstrumentInfo', 'CIntelligentAlgorithmOrder', 'CMarginRateDetail', 'CNetValue', 'CNewPortfolioReq', 'COpVolumeReq', 'COrderDetail', 'COrderError', 'COrderInfo', 'COrderStat', 'COrdinaryGroupOrder', 'COrdinaryOrder', 'CPortfolioInfo', 'CPortfolioStat', 'CPositionDetail', 'CPositionStatics', 'CPriceData', 'CProductData', 'CQueryBankAmount', 'CQueryBankInfo', 'CRandomOrder', 'CReferenceRate', 'CSecuAccount', 'CSecuFundTransferReq', 'CStkClosedCompacts', 'CStkCompacts', 'CStkUnClosedCompacts', 'CStockComFund', 'CStockComPosition', 'CStockOptionCombPositionDetail', 'CStrategyInfo', 'CSubscribData', 'CSubscribeInfo', 'CTaskOpRecord', 'CTransferReq', 'CTransferSerial', 'CUserConfig', 'EAbroadDurationType', 'EAdjustOrderNum', 'EAlgoPriceType', 'EBrokerLoginStatus', 'EBrokerPriceType', 'ECoveredFlag', 'EDualStatus', 'EEntrustBS', 'EEntrustStatus', 'EEntrustSubmitStatus', 'EEntrustTypes', 'EErrorType', 'EFutureTradeType', 'EHedgeFlagType', 'EMainFlag', 'EMoneyType', 'EOffsetFlagType', 'EOpTriggerType', 'EOperationType', 'EOptionType', 'EOrderCommandStatus', 'EOrderStrategyType', 'EPortfolioType', 'EPriceType', 'EProductClass', 'EReplaceFlag', 'ESecuFundTransDirection', 'ESideFlag', 'EStockType', 'EStopTradeForOwnHiLow', 'ETaskFlowOperation', 'ETimeCondition', 'ETransDirection', 'ETransTypeCreditFlag', 'EVolumeCondition', 'EVolumeType', 'EXTBrokerType', 'EXTCommandDateLimit', 'EXTCompactBrushSource', 'EXTCompactStatus', 'EXTCompactType', 'EXTExchangeStatus', 'EXTOfferStatus', 'EXTSubjectsStatus', 'EXtExDivdendType', 'EXtMaxMarginSideAlgorithmType', 'EXtOverFreqOrderMode', 'EXtSuspendedType', 'PortfolioDealType', 'PortfolioPositionType', 'XtError', 'XtTraderApi', 'XtTraderApiCallback']
class CAccountDetail:
    """
    账号详细信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dAssetBalance(self) -> float:
        """
        动态权益含期权
        """
    @m_dAssetBalance.setter
    def m_dAssetBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dAssureAsset(self) -> float:
        """
        净资产
        """
    @m_dAssureAsset.setter
    def m_dAssureAsset(self, arg0: float) -> None:
        ...
    @property
    def m_dAvailable(self) -> float:
        """
        可用资金
        """
    @m_dAvailable.setter
    def m_dAvailable(self, arg0: float) -> None:
        ...
    @property
    def m_dAvailableSH(self) -> float:
        """
        双中心上海可用
        """
    @m_dAvailableSH.setter
    def m_dAvailableSH(self, arg0: float) -> None:
        ...
    @property
    def m_dAvailableSZ(self) -> float:
        """
        双中心深圳可用
        """
    @m_dAvailableSZ.setter
    def m_dAvailableSZ(self, arg0: float) -> None:
        ...
    @property
    def m_dBalance(self) -> float:
        """
        动态权益, 总资产
        """
    @m_dBalance.setter
    def m_dBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dCashIn(self) -> float:
        """
        出入金净值
        """
    @m_dCashIn.setter
    def m_dCashIn(self, arg0: float) -> None:
        ...
    @property
    def m_dCloseProfit(self) -> float:
        """
        平仓盈亏
        """
    @m_dCloseProfit.setter
    def m_dCloseProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dCommission(self) -> float:
        """
        已用手续费
        """
    @m_dCommission.setter
    def m_dCommission(self, arg0: float) -> None:
        ...
    @property
    def m_dCredit(self) -> float:
        """
        信用额度
        """
    @m_dCredit.setter
    def m_dCredit(self, arg0: float) -> None:
        ...
    @property
    def m_dCurrMargin(self) -> float:
        """
        当前占用保证金
        """
    @m_dCurrMargin.setter
    def m_dCurrMargin(self, arg0: float) -> None:
        ...
    @property
    def m_dDaysProfit(self) -> float:
        """
        当日盈亏
        """
    @m_dDaysProfit.setter
    def m_dDaysProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dDeposit(self) -> float:
        """
        入金
        """
    @m_dDeposit.setter
    def m_dDeposit(self, arg0: float) -> None:
        ...
    @property
    def m_dEnableMargin(self) -> float:
        """
        可用保证金 用于股票期权
        """
    @m_dEnableMargin.setter
    def m_dEnableMargin(self, arg0: float) -> None:
        ...
    @property
    def m_dFetchBalance(self) -> float:
        """
        可取金额
        """
    @m_dFetchBalance.setter
    def m_dFetchBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dFrozenCash(self) -> float:
        """
        内外源冻结保证金和手续费四个的和
        """
    @m_dFrozenCash.setter
    def m_dFrozenCash(self, arg0: float) -> None:
        ...
    @property
    def m_dFrozenCommission(self) -> float:
        """
        外源性冻结资金源
        """
    @m_dFrozenCommission.setter
    def m_dFrozenCommission(self, arg0: float) -> None:
        ...
    @property
    def m_dFrozenMargin(self) -> float:
        """
        外源性 股票的保证金就是冻结资金 股票不需要
        """
    @m_dFrozenMargin.setter
    def m_dFrozenMargin(self, arg0: float) -> None:
        ...
    @property
    def m_dFundValue(self) -> float:
        """
        基金总市值，包括ETF和封闭式基金，期货没有
        """
    @m_dFundValue.setter
    def m_dFundValue(self, arg0: float) -> None:
        ...
    @property
    def m_dInitCloseMoney(self) -> float:
        """
        初始平仓盈亏
        """
    @m_dInitCloseMoney.setter
    def m_dInitCloseMoney(self, arg0: float) -> None:
        ...
    @property
    def m_dInstrumentValue(self) -> float:
        """
        合约价值
        """
    @m_dInstrumentValue.setter
    def m_dInstrumentValue(self, arg0: float) -> None:
        ...
    @property
    def m_dLoanValue(self) -> float:
        """
        债券总市值，期货没有
        """
    @m_dLoanValue.setter
    def m_dLoanValue(self, arg0: float) -> None:
        ...
    @property
    def m_dLongValue(self) -> float:
        """
        多单总市值，现货没有
        """
    @m_dLongValue.setter
    def m_dLongValue(self, arg0: float) -> None:
        ...
    @property
    def m_dMortgage(self) -> float:
        """
        质押
        """
    @m_dMortgage.setter
    def m_dMortgage(self, arg0: float) -> None:
        ...
    @property
    def m_dNav(self) -> float:
        """
        单位净值
        """
    @m_dNav.setter
    def m_dNav(self, arg0: float) -> None:
        ...
    @property
    def m_dNetValue(self) -> float:
        """
        净持仓总市值，净持仓市值=多-空
        """
    @m_dNetValue.setter
    def m_dNetValue(self, arg0: float) -> None:
        ...
    @property
    def m_dPositionProfit(self) -> float:
        """
        持仓盈亏
        """
    @m_dPositionProfit.setter
    def m_dPositionProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dPreBalance(self) -> float:
        """
        期初权益
        """
    @m_dPreBalance.setter
    def m_dPreBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dPremiumNetExpense(self) -> float:
        """
        权利金净支出 用于股票期权
        """
    @m_dPremiumNetExpense.setter
    def m_dPremiumNetExpense(self, arg0: float) -> None:
        ...
    @property
    def m_dRepurchaseValue(self) -> float:
        """
        回购总市值，所有回购，期货没有
        """
    @m_dRepurchaseValue.setter
    def m_dRepurchaseValue(self, arg0: float) -> None:
        ...
    @property
    def m_dRisk(self) -> float:
        """
        风险度
        """
    @m_dRisk.setter
    def m_dRisk(self, arg0: float) -> None:
        ...
    @property
    def m_dRiskDegree(self) -> float:
        """
        风险度含期权
        """
    @m_dRiskDegree.setter
    def m_dRiskDegree(self, arg0: float) -> None:
        ...
    @property
    def m_dRoyalty(self) -> float:
        """
        权利金支出 用于股票期权
        """
    @m_dRoyalty.setter
    def m_dRoyalty(self, arg0: float) -> None:
        ...
    @property
    def m_dShortValue(self) -> float:
        """
        空单总市值，现货没有
        """
    @m_dShortValue.setter
    def m_dShortValue(self, arg0: float) -> None:
        ...
    @property
    def m_dStockValue(self) -> float:
        """
        股票总市值，期货没有
        """
    @m_dStockValue.setter
    def m_dStockValue(self, arg0: float) -> None:
        ...
    @property
    def m_dTotalDebit(self) -> float:
        """
        总负债
        """
    @m_dTotalDebit.setter
    def m_dTotalDebit(self, arg0: float) -> None:
        ...
    @property
    def m_dUsedMargin(self) -> float:
        """
        占用保证金 用于股票期权
        """
    @m_dUsedMargin.setter
    def m_dUsedMargin(self, arg0: float) -> None:
        ...
    @property
    def m_dWithdraw(self) -> float:
        """
        出金
        """
    @m_dWithdraw.setter
    def m_dWithdraw(self, arg0: float) -> None:
        ...
    @property
    def m_eDualStatus(self) -> EDualStatus:
        """
        双中心状态
        """
    @m_eDualStatus.setter
    def m_eDualStatus(self, arg0: EDualStatus) -> None:
        ...
    @property
    def m_nAccountType(self) -> int:
        """
        账号类型
        """
    @m_nAccountType.setter
    def m_nAccountType(self, arg0: int) -> None:
        ...
    @property
    def m_nProductId(self) -> int:
        """
        迅投产品ID
        """
    @m_nProductId.setter
    def m_nProductId(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        资金账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountName(self) -> str:
        """
        账号名称
        """
    @m_strAccountName.setter
    def m_strAccountName(self, arg1: str) -> None:
        ...
    @property
    def m_strBrokerID(self) -> str:
        """
        经纪公司编号
        """
    @m_strBrokerID.setter
    def m_strBrokerID(self, arg1: str) -> None:
        ...
    @property
    def m_strBrokerName(self) -> str:
        """
        经纪公司名称
        """
    @m_strBrokerName.setter
    def m_strBrokerName(self, arg1: str) -> None:
        ...
    @property
    def m_strProductName(self) -> str:
        """
        迅投产品名称
        """
    @m_strProductName.setter
    def m_strProductName(self, arg1: str) -> None:
        ...
    @property
    def m_strStatus(self) -> str:
        """
        状态
        """
    @m_strStatus.setter
    def m_strStatus(self, arg1: str) -> None:
        ...
    @property
    def m_strTradingDate(self) -> str:
        """
        交易日
        """
    @m_strTradingDate.setter
    def m_strTradingDate(self, arg1: str) -> None:
        ...
class CAccountKey:
    """
    账号主键
    """
    def __init__(self) -> None:
        ...
    @property
    def m_eBrokerType(self) -> EXTBrokerType:
        """
        经纪公司类别
        """
    @m_eBrokerType.setter
    def m_eBrokerType(self, arg0: EXTBrokerType) -> None:
        ...
    @property
    def m_nAccountType(self) -> int:
        """
        账号类型编号
        """
    @m_nAccountType.setter
    def m_nAccountType(self, arg0: int) -> None:
        ...
    @property
    def m_nPlatformID(self) -> int:
        """
        经纪公司编号
        """
    @m_nPlatformID.setter
    def m_nPlatformID(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        资金账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        资金账号对应唯一主键
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountName(self) -> str:
        """
        账号名称
        """
    @m_strAccountName.setter
    def m_strAccountName(self, arg1: str) -> None:
        ...
    @property
    def m_strBrokerName(self) -> str:
        """
        经纪公司名称
        """
    @m_strBrokerName.setter
    def m_strBrokerName(self, arg1: str) -> None:
        ...
    @property
    def m_strSubAccount(self) -> str:
        """
        账号类型
        """
    @m_strSubAccount.setter
    def m_strSubAccount(self, arg1: str) -> None:
        ...
class CAlgGroupOrder:
    """
    算法组合单下单参数
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dMaxPartRate(self) -> list:
        """
        量比比例
        """
    @m_dMaxPartRate.setter
    def m_dMaxPartRate(self, arg1: list) -> None:
        ...
    @property
    def m_eOperationType(self) -> list:
        """
        每只股票的下单类型
        """
    @m_eOperationType.setter
    def m_eOperationType(self, arg1: list) -> None:
        ...
    @property
    def m_nOrderNum(self) -> int:
        """
        股票只数
        """
    @m_nOrderNum.setter
    def m_nOrderNum(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> list:
        """
        每只股票的下单量
        """
    @m_nVolume.setter
    def m_nVolume(self, arg1: list) -> None:
        ...
    @property
    def m_orderParam(self) -> CIntelligentAlgorithmOrder:
        """
        下单配置
        """
    @m_orderParam.setter
    def m_orderParam(self, arg0: CIntelligentAlgorithmOrder) -> None:
        ...
    @property
    def m_strAccountKey(self) -> list:
        """
        每个合约的下单资金账号Key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: list) -> None:
        ...
    @property
    def m_strInstrument(self) -> list:
        """
        证券代码
        """
    @m_strInstrument.setter
    def m_strInstrument(self, arg1: list) -> None:
        ...
    @property
    def m_strMarket(self) -> list:
        """
        市场列表
        """
    @m_strMarket.setter
    def m_strMarket(self, arg1: list) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
class CAlgorithmOrder:
    """
    算法单下单参数
    """
    m_dPrice: float
    def __init__(self) -> None:
        ...
    @property
    def m_dExtraLimitValue(self) -> float:
        """
        扩展限价
        """
    @m_dExtraLimitValue.setter
    def m_dExtraLimitValue(self, arg0: float) -> None:
        ...
    @property
    def m_dPlaceOrderInterval(self) -> float:
        """
        下单间隔
        """
    @m_dPlaceOrderInterval.setter
    def m_dPlaceOrderInterval(self, arg0: float) -> None:
        ...
    @property
    def m_dPriceRangeMax(self) -> float:
        """
        波动区间上限
        """
    @m_dPriceRangeMax.setter
    def m_dPriceRangeMax(self, arg0: float) -> None:
        ...
    @property
    def m_dPriceRangeMin(self) -> float:
        """
        波动区间下限
        """
    @m_dPriceRangeMin.setter
    def m_dPriceRangeMin(self, arg0: float) -> None:
        ...
    @property
    def m_dSingleVolumeRate(self) -> float:
        """
        单比下单比率
        """
    @m_dSingleVolumeRate.setter
    def m_dSingleVolumeRate(self, arg0: float) -> None:
        ...
    @property
    def m_dSuperPrice(self) -> float:
        """
        单笔超价,和m_dSuperPriceRate只用设置一个，优先使用m_dSuperPriceRate
        """
    @m_dSuperPrice.setter
    def m_dSuperPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dSuperPriceRate(self) -> float:
        """
        单笔超价比率
        """
    @m_dSuperPriceRate.setter
    def m_dSuperPriceRate(self, arg0: float) -> None:
        ...
    @property
    def m_dTriggerPrice(self) -> float:
        """
        触价价格
        """
    @m_dTriggerPrice.setter
    def m_dTriggerPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dWithdrawOrderInterval(self) -> float:
        """
        撤单间隔
        """
    @m_dWithdrawOrderInterval.setter
    def m_dWithdrawOrderInterval(self, arg0: float) -> None:
        ...
    @property
    def m_eAlgoPriceType(self) -> EAlgoPriceType:
        """
        订单类型
        """
    @m_eAlgoPriceType.setter
    def m_eAlgoPriceType(self, arg0: EAlgoPriceType) -> None:
        ...
    @property
    def m_eCmdDateLimit(self) -> EXTCommandDateLimit:
        """
        指令跨日开关
        """
    @m_eCmdDateLimit.setter
    def m_eCmdDateLimit(self, arg0: EXTCommandDateLimit) -> None:
        ...
    @property
    def m_eHedgeFlag(self) -> EHedgeFlagType:
        """
        套利标志
        """
    @m_eHedgeFlag.setter
    def m_eHedgeFlag(self, arg0: EHedgeFlagType) -> None:
        ...
    @property
    def m_eOperationType(self) -> EOperationType:
        """
        下单操作：开平、多空……
        """
    @m_eOperationType.setter
    def m_eOperationType(self, arg0: EOperationType) -> None:
        ...
    @property
    def m_eOverFreqOrderMode(self) -> EXtOverFreqOrderMode:
        """
        委托频率过快时的处理方式
        """
    @m_eOverFreqOrderMode.setter
    def m_eOverFreqOrderMode(self, arg0: EXtOverFreqOrderMode) -> None:
        ...
    @property
    def m_ePriceType(self) -> EPriceType:
        """
        报价方式：对手、最新……
        """
    @m_ePriceType.setter
    def m_ePriceType(self, arg0: EPriceType) -> None:
        ...
    @property
    def m_eSingleVolumeType(self) -> EVolumeType:
        """
        单笔下单基准
        """
    @m_eSingleVolumeType.setter
    def m_eSingleVolumeType(self, arg0: EVolumeType) -> None:
        ...
    @property
    def m_eTimeCondition(self) -> ETimeCondition:
        """
        期货条件单时间条件
        """
    @m_eTimeCondition.setter
    def m_eTimeCondition(self, arg0: ETimeCondition) -> None:
        ...
    @property
    def m_eTriggerType(self) -> EOpTriggerType:
        """
        触价类型
        """
    @m_eTriggerType.setter
    def m_eTriggerType(self, arg0: EOpTriggerType) -> None:
        ...
    @property
    def m_eUndealtEntrustRule(self) -> EPriceType:
        """
        未成委托处理
        """
    @m_eUndealtEntrustRule.setter
    def m_eUndealtEntrustRule(self, arg0: EPriceType) -> None:
        ...
    @property
    def m_eVolumeCondition(self) -> EVolumeCondition:
        """
        期货条件单数量条件
        """
    @m_eVolumeCondition.setter
    def m_eVolumeCondition(self, arg0: EVolumeCondition) -> None:
        ...
    @property
    def m_nExtraLimitType(self) -> int:
        """
        扩展限价类型
        """
    @m_nExtraLimitType.setter
    def m_nExtraLimitType(self, arg0: int) -> None:
        ...
    @property
    def m_nLastVolumeMin(self) -> int:
        """
        尾单最小量
        """
    @m_nLastVolumeMin.setter
    def m_nLastVolumeMin(self, arg0: int) -> None:
        ...
    @property
    def m_nLimitedPriceType(self) -> int:
        """
        价格限制类型
        """
    @m_nLimitedPriceType.setter
    def m_nLimitedPriceType(self, arg0: int) -> None:
        ...
    @property
    def m_nMaxOrderCount(self) -> int:
        """
        最大下单次数，与下单间隔相对应
        """
    @m_nMaxOrderCount.setter
    def m_nMaxOrderCount(self, arg0: int) -> None:
        ...
    @property
    def m_nSingleNumMax(self) -> int:
        """
        单比下单量最大值
        """
    @m_nSingleNumMax.setter
    def m_nSingleNumMax(self, arg0: int) -> None:
        ...
    @property
    def m_nSingleNumMin(self) -> int:
        """
        单比下单量最小值
        """
    @m_nSingleNumMin.setter
    def m_nSingleNumMin(self, arg0: int) -> None:
        ...
    @property
    def m_nStopTradeForOwnHiLow(self) -> EStopTradeForOwnHiLow:
        """
        涨跌停控制
        """
    @m_nStopTradeForOwnHiLow.setter
    def m_nStopTradeForOwnHiLow(self, arg0: EStopTradeForOwnHiLow) -> None:
        ...
    @property
    def m_nSuperPriceStart(self) -> int:
        """
        超价起始笔数
        """
    @m_nSuperPriceStart.setter
    def m_nSuperPriceStart(self, arg0: int) -> None:
        ...
    @property
    def m_nValidTimeEnd(self) -> int:
        """
        有效结束时间 来自股票，待定
        """
    @m_nValidTimeEnd.setter
    def m_nValidTimeEnd(self, arg0: int) -> None:
        ...
    @property
    def m_nValidTimeStart(self) -> int:
        """
        有效开始时间 来自股票，待定
        """
    @m_nValidTimeStart.setter
    def m_nValidTimeStart(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> int:
        """
        量
        """
    @m_nVolume.setter
    def m_nVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrument(self) -> str:
        """
        合约
        """
    @m_strInstrument.setter
    def m_strInstrument(self, arg1: str) -> None:
        ...
    @property
    def m_strMarket(self) -> str:
        """
        市场
        """
    @m_strMarket.setter
    def m_strMarket(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
    @property
    def m_strStrategyID(self) -> str:
        """
        收益互换策略ID
        """
    @m_strStrategyID.setter
    def m_strStrategyID(self, arg1: str) -> None:
        ...
class CCancelError:
    """
    撤单错误
    """
    def __init__(self) -> None:
        ...
    @property
    def m_nErrorID(self) -> int:
        """
        错误号
        """
    @m_nErrorID.setter
    def m_nErrorID(self, arg0: int) -> None:
        ...
    @property
    def m_nOrderID(self) -> int:
        """
        指令ID
        """
    @m_nOrderID.setter
    def m_nOrderID(self, arg0: int) -> None:
        ...
    @property
    def m_nRequestID(self) -> int:
        """
        请求ID
        """
    @m_nRequestID.setter
    def m_nRequestID(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strErrorMsg(self) -> str:
        """
        错误描述
        """
    @m_strErrorMsg.setter
    def m_strErrorMsg(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
class CCheckData:
    """
    风险试算信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_allResult(self) -> XtError:
        """
        全局风险试算结果
        """
    @m_allResult.setter
    def m_allResult(self, arg0: XtError) -> None:
        ...
    @property
    def m_singleResult(self) -> XtError:
        """
        单只风险试算结果
        """
    @m_singleResult.setter
    def m_singleResult(self, arg0: XtError) -> None:
        ...
class CCommissionRateDetail:
    """
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dCloseRatioByMoney(self) -> float:
        """
        平仓手续费率(按金额)
        """
    @m_dCloseRatioByMoney.setter
    def m_dCloseRatioByMoney(self, arg0: float) -> None:
        ...
    @property
    def m_dCloseRatioByVolume(self) -> float:
        """
        平仓手续费率(按手)
        """
    @m_dCloseRatioByVolume.setter
    def m_dCloseRatioByVolume(self, arg0: float) -> None:
        ...
    @property
    def m_dCloseTodayRatioByMoney(self) -> float:
        """
        平今手续费率(按金额)
        """
    @m_dCloseTodayRatioByMoney.setter
    def m_dCloseTodayRatioByMoney(self, arg0: float) -> None:
        ...
    @property
    def m_dCloseTodayRatioByVolume(self) -> float:
        """
        平今手续费率(按手)
        """
    @m_dCloseTodayRatioByVolume.setter
    def m_dCloseTodayRatioByVolume(self, arg0: float) -> None:
        ...
    @property
    def m_dOpenRatioByMoney(self) -> float:
        """
        开仓手续费率(按金额)
        """
    @m_dOpenRatioByMoney.setter
    def m_dOpenRatioByMoney(self, arg0: float) -> None:
        ...
    @property
    def m_dOpenRatioByVolume(self) -> float:
        """
        开仓手续费率(按手)
        """
    @m_dOpenRatioByVolume.setter
    def m_dOpenRatioByVolume(self, arg0: float) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        市场代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strTradeDate(self) -> str:
        """
        交易日
        """
    @m_strTradeDate.setter
    def m_strTradeDate(self, arg1: str) -> None:
        ...
class CCoveredStockPosition:
    """
    个股期权备兑持仓信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_nCoveredAmount(self) -> int:
        """
        备兑数量
        """
    @m_nCoveredAmount.setter
    def m_nCoveredAmount(self, arg0: int) -> None:
        ...
    @property
    def m_nLockAmount(self) -> int:
        """
        锁定量
        """
    @m_nLockAmount.setter
    def m_nLockAmount(self, arg0: int) -> None:
        ...
    @property
    def m_nTotalAmount(self) -> int:
        """
        总持仓量
        """
    @m_nTotalAmount.setter
    def m_nTotalAmount(self, arg0: int) -> None:
        ...
    @property
    def m_nUnlockAmount(self) -> int:
        """
        未锁定量
        """
    @m_nUnlockAmount.setter
    def m_nUnlockAmount(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易类别
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeName(self) -> str:
        """
        市场名字
        """
    @m_strExchangeName.setter
    def m_strExchangeName(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentName(self) -> str:
        """
        合约名称
        """
    @m_strInstrumentName.setter
    def m_strInstrumentName(self, arg1: str) -> None:
        ...
class CCreditAccountDetail:
    """
    信用账号详细信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dAssureEnbuyBalance(self) -> float:
        """
        可买担保品资金
        """
    @m_dAssureEnbuyBalance.setter
    def m_dAssureEnbuyBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dBuySecuRepayFrozenCommission(self) -> float:
        """
        买券还券冻结手续费
        """
    @m_dBuySecuRepayFrozenCommission.setter
    def m_dBuySecuRepayFrozenCommission(self, arg0: float) -> None:
        ...
    @property
    def m_dBuySecuRepayFrozenMargin(self) -> float:
        """
        买券还券冻结资金
        """
    @m_dBuySecuRepayFrozenMargin.setter
    def m_dBuySecuRepayFrozenMargin(self, arg0: float) -> None:
        ...
    @property
    def m_dDiffEnableBailBalance(self) -> float:
        """
        可用保证金调整值
        """
    @m_dDiffEnableBailBalance.setter
    def m_dDiffEnableBailBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dEnableBailBalance(self) -> float:
        """
        可用保证金
        """
    @m_dEnableBailBalance.setter
    def m_dEnableBailBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dFinCompactBalance(self) -> float:
        """
        融资合约金额
        """
    @m_dFinCompactBalance.setter
    def m_dFinCompactBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dFinCompactFare(self) -> float:
        """
        融资合约费用
        """
    @m_dFinCompactFare.setter
    def m_dFinCompactFare(self, arg0: float) -> None:
        ...
    @property
    def m_dFinCompactInterest(self) -> float:
        """
        融资合约利息
        """
    @m_dFinCompactInterest.setter
    def m_dFinCompactInterest(self, arg0: float) -> None:
        ...
    @property
    def m_dFinEnableBalance(self) -> float:
        """
        可融资金额
        """
    @m_dFinEnableBalance.setter
    def m_dFinEnableBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dFinEnableQuota(self) -> float:
        """
        融资可用额度
        """
    @m_dFinEnableQuota.setter
    def m_dFinEnableQuota(self, arg0: float) -> None:
        ...
    @property
    def m_dFinEnbuyBalance(self) -> float:
        """
        可买标的券资金
        """
    @m_dFinEnbuyBalance.setter
    def m_dFinEnbuyBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dFinEnrepaidBalance(self) -> float:
        """
        可还款资金
        """
    @m_dFinEnrepaidBalance.setter
    def m_dFinEnrepaidBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dFinIncome(self) -> float:
        """
        融资合约盈亏
        """
    @m_dFinIncome.setter
    def m_dFinIncome(self, arg0: float) -> None:
        ...
    @property
    def m_dFinMarketValue(self) -> float:
        """
        融资市值
        """
    @m_dFinMarketValue.setter
    def m_dFinMarketValue(self, arg0: float) -> None:
        ...
    @property
    def m_dFinMaxQuota(self) -> float:
        """
        融资授信额度
        """
    @m_dFinMaxQuota.setter
    def m_dFinMaxQuota(self, arg0: float) -> None:
        ...
    @property
    def m_dFinUsedBail(self) -> float:
        """
        融资已用保证金额
        """
    @m_dFinUsedBail.setter
    def m_dFinUsedBail(self, arg0: float) -> None:
        ...
    @property
    def m_dFinUsedQuota(self) -> float:
        """
        融资已用额度
        """
    @m_dFinUsedQuota.setter
    def m_dFinUsedQuota(self, arg0: float) -> None:
        ...
    @property
    def m_dOtherFare(self) -> float:
        """
        其它费用
        """
    @m_dOtherFare.setter
    def m_dOtherFare(self, arg0: float) -> None:
        ...
    @property
    def m_dPerAssurescaleValue(self) -> float:
        """
        个人维持担保比例
        """
    @m_dPerAssurescaleValue.setter
    def m_dPerAssurescaleValue(self, arg0: float) -> None:
        ...
    @property
    def m_dSloCompactBalance(self) -> float:
        """
        融券合约金额
        """
    @m_dSloCompactBalance.setter
    def m_dSloCompactBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dSloCompactFare(self) -> float:
        """
        融券合约费用
        """
    @m_dSloCompactFare.setter
    def m_dSloCompactFare(self, arg0: float) -> None:
        ...
    @property
    def m_dSloCompactInterest(self) -> float:
        """
        融券合约利息
        """
    @m_dSloCompactInterest.setter
    def m_dSloCompactInterest(self, arg0: float) -> None:
        ...
    @property
    def m_dSloEnableQuota(self) -> float:
        """
        融券可用额度
        """
    @m_dSloEnableQuota.setter
    def m_dSloEnableQuota(self, arg0: float) -> None:
        ...
    @property
    def m_dSloEnrepaidBalance(self) -> float:
        """
        可还券资金
        """
    @m_dSloEnrepaidBalance.setter
    def m_dSloEnrepaidBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dSloIncome(self) -> float:
        """
        融券合约盈亏
        """
    @m_dSloIncome.setter
    def m_dSloIncome(self, arg0: float) -> None:
        ...
    @property
    def m_dSloMarketValue(self) -> float:
        """
        融券市值
        """
    @m_dSloMarketValue.setter
    def m_dSloMarketValue(self, arg0: float) -> None:
        ...
    @property
    def m_dSloMaxQuota(self) -> float:
        """
        融券授信额度
        """
    @m_dSloMaxQuota.setter
    def m_dSloMaxQuota(self, arg0: float) -> None:
        ...
    @property
    def m_dSloUsedBail(self) -> float:
        """
        融券已用保证金额
        """
    @m_dSloUsedBail.setter
    def m_dSloUsedBail(self, arg0: float) -> None:
        ...
    @property
    def m_dSloUsedQuota(self) -> float:
        """
        融券已用额度
        """
    @m_dSloUsedQuota.setter
    def m_dSloUsedQuota(self, arg0: float) -> None:
        ...
    @property
    def m_dUnderlyMarketValue(self) -> float:
        """
        标的证券市值
        """
    @m_dUnderlyMarketValue.setter
    def m_dUnderlyMarketValue(self, arg0: float) -> None:
        ...
    @property
    def m_dUsedBailBalance(self) -> float:
        """
        已用保证金
        """
    @m_dUsedBailBalance.setter
    def m_dUsedBailBalance(self, arg0: float) -> None:
        ...
class CCreditAssure:
    """
    两融担保品
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dAssureRatio(self) -> float:
        """
        担保品折算比例
        """
    @m_dAssureRatio.setter
    def m_dAssureRatio(self, arg0: float) -> None:
        ...
    @property
    def m_eAssureStatus(self) -> EXTSubjectsStatus:
        """
        是否可做担保
        """
    @m_eAssureStatus.setter
    def m_eAssureStatus(self, arg0: EXTSubjectsStatus) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        市场
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
class CCreditDetail:
    """
    信用账号信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dAssureAsset(self) -> float:
        """
        净资产
        """
    @m_dAssureAsset.setter
    def m_dAssureAsset(self, arg0: float) -> None:
        ...
    @property
    def m_dAssureEnbuyBalance(self) -> float:
        """
        可买担保品资金
        """
    @m_dAssureEnbuyBalance.setter
    def m_dAssureEnbuyBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dAvailable(self) -> float:
        """
        可用资金
        """
    @m_dAvailable.setter
    def m_dAvailable(self, arg0: float) -> None:
        ...
    @property
    def m_dBalance(self) -> float:
        """
        动态权益
        """
    @m_dBalance.setter
    def m_dBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dEnableBailBalance(self) -> float:
        """
        可用保证金
        """
    @m_dEnableBailBalance.setter
    def m_dEnableBailBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dEnableQuota(self) -> float:
        """
        可用授信额度
        """
    @m_dEnableQuota.setter
    def m_dEnableQuota(self, arg0: float) -> None:
        ...
    @property
    def m_dEquityCompensation(self) -> float:
        """
        权益补偿资金
        """
    @m_dEquityCompensation.setter
    def m_dEquityCompensation(self, arg0: float) -> None:
        ...
    @property
    def m_dFetchBalance(self) -> float:
        """
        可取资金
        """
    @m_dFetchBalance.setter
    def m_dFetchBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dFinDealAvl(self) -> float:
        """
        融资本金
        """
    @m_dFinDealAvl.setter
    def m_dFinDealAvl(self, arg0: float) -> None:
        ...
    @property
    def m_dFinDebt(self) -> float:
        """
        融资负债
        """
    @m_dFinDebt.setter
    def m_dFinDebt(self, arg0: float) -> None:
        ...
    @property
    def m_dFinEnableQuota(self) -> float:
        """
        融资可用额度
        """
    @m_dFinEnableQuota.setter
    def m_dFinEnableQuota(self, arg0: float) -> None:
        ...
    @property
    def m_dFinFee(self) -> float:
        """
        融资息费
        """
    @m_dFinFee.setter
    def m_dFinFee(self, arg0: float) -> None:
        ...
    @property
    def m_dFinMaxQuota(self) -> float:
        """
        融资授信额度
        """
    @m_dFinMaxQuota.setter
    def m_dFinMaxQuota(self, arg0: float) -> None:
        ...
    @property
    def m_dFinUsedQuota(self) -> float:
        """
        融资冻结额度
        """
    @m_dFinUsedQuota.setter
    def m_dFinUsedQuota(self, arg0: float) -> None:
        ...
    @property
    def m_dFundValue(self) -> float:
        """
        基金总市值，包括ETF和封闭式基金，期货没有
        """
    @m_dFundValue.setter
    def m_dFundValue(self, arg0: float) -> None:
        ...
    @property
    def m_dMarketValue(self) -> float:
        """
        合约价值
        """
    @m_dMarketValue.setter
    def m_dMarketValue(self, arg0: float) -> None:
        ...
    @property
    def m_dMaxQuota(self) -> float:
        """
        总授信额度
        """
    @m_dMaxQuota.setter
    def m_dMaxQuota(self, arg0: float) -> None:
        ...
    @property
    def m_dOtherFare(self) -> float:
        """
        其它费用
        """
    @m_dOtherFare.setter
    def m_dOtherFare(self, arg0: float) -> None:
        ...
    @property
    def m_dPerAssurescaleValue(self) -> float:
        """
        维持担保比例
        """
    @m_dPerAssurescaleValue.setter
    def m_dPerAssurescaleValue(self, arg0: float) -> None:
        ...
    @property
    def m_dSloDebt(self) -> float:
        """
        融券负债
        """
    @m_dSloDebt.setter
    def m_dSloDebt(self, arg0: float) -> None:
        ...
    @property
    def m_dSloEnableQuota(self) -> float:
        """
        融券可用额度
        """
    @m_dSloEnableQuota.setter
    def m_dSloEnableQuota(self, arg0: float) -> None:
        ...
    @property
    def m_dSloFee(self) -> float:
        """
        融券息费
        """
    @m_dSloFee.setter
    def m_dSloFee(self, arg0: float) -> None:
        ...
    @property
    def m_dSloMarketValue(self) -> float:
        """
        融券市值
        """
    @m_dSloMarketValue.setter
    def m_dSloMarketValue(self, arg0: float) -> None:
        ...
    @property
    def m_dSloMaxQuota(self) -> float:
        """
        融券授信额度
        """
    @m_dSloMaxQuota.setter
    def m_dSloMaxQuota(self, arg0: float) -> None:
        ...
    @property
    def m_dSloSellBalance(self) -> float:
        """
        融券卖出资金
        """
    @m_dSloSellBalance.setter
    def m_dSloSellBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dSloUsedQuota(self) -> float:
        """
        融券冻结额度
        """
    @m_dSloUsedQuota.setter
    def m_dSloUsedQuota(self, arg0: float) -> None:
        ...
    @property
    def m_dSpecialNetRatio(self) -> float:
        """
        D与E类证券净持仓集中度
        """
    @m_dSpecialNetRatio.setter
    def m_dSpecialNetRatio(self, arg0: float) -> None:
        ...
    @property
    def m_dStibGemNetRatio(self) -> float:
        """
        双创板净持仓集中度
        """
    @m_dStibGemNetRatio.setter
    def m_dStibGemNetRatio(self, arg0: float) -> None:
        ...
    @property
    def m_dStockValue(self) -> float:
        """
        股票总市值，期货没有
        """
    @m_dStockValue.setter
    def m_dStockValue(self, arg0: float) -> None:
        ...
    @property
    def m_dSurplusSloSellBalance(self) -> float:
        """
        剩余融券卖出资金
        """
    @m_dSurplusSloSellBalance.setter
    def m_dSurplusSloSellBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dTotalDebt(self) -> float:
        """
        总负债
        """
    @m_dTotalDebt.setter
    def m_dTotalDebt(self, arg0: float) -> None:
        ...
    @property
    def m_dUsedSloSellBalance(self) -> float:
        """
        已用融券卖出资金
        """
    @m_dUsedSloSellBalance.setter
    def m_dUsedSloSellBalance(self, arg0: float) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
class CCreditSloCode:
    """
    可融券数量
    """
    def __init__(self) -> None:
        ...
    @property
    def m_eCashgroupProp(self) -> EXTCompactBrushSource:
        """
        头寸来源
        """
    @m_eCashgroupProp.setter
    def m_eCashgroupProp(self, arg0: EXTCompactBrushSource) -> None:
        ...
    @property
    def m_nEnableAmount(self) -> int:
        """
        融券可融数量
        """
    @m_nEnableAmount.setter
    def m_nEnableAmount(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        市场
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
class CCreditSubjects:
    """
    两融融资融券标的
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dFinRatio(self) -> float:
        """
        融资保证金比例
        """
    @m_dFinRatio.setter
    def m_dFinRatio(self, arg0: float) -> None:
        ...
    @property
    def m_dSloRatio(self) -> float:
        """
        融券保证金比例
        """
    @m_dSloRatio.setter
    def m_dSloRatio(self, arg0: float) -> None:
        ...
    @property
    def m_eFinStatus(self) -> EXTSubjectsStatus:
        """
        融资状态
        """
    @m_eFinStatus.setter
    def m_eFinStatus(self, arg0: EXTSubjectsStatus) -> None:
        ...
    @property
    def m_eSloStatus(self) -> EXTSubjectsStatus:
        """
        融券状态
        """
    @m_eSloStatus.setter
    def m_eSloStatus(self, arg0: EXTSubjectsStatus) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        市场
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
class CDealDetail:
    """
    成交信息
    """
    m_strAccountID: str
    def __init__(self) -> None:
        ...
    @property
    def m_dAmount(self) -> float:
        """
        成交额 期货=均价*量*合约乘数
        """
    @m_dAmount.setter
    def m_dAmount(self, arg0: float) -> None:
        ...
    @property
    def m_dAveragePrice(self) -> float:
        """
        成交均价
        """
    @m_dAveragePrice.setter
    def m_dAveragePrice(self, arg0: float) -> None:
        ...
    @property
    def m_dComssion(self) -> float:
        """
        手续费
        """
    @m_dComssion.setter
    def m_dComssion(self, arg0: float) -> None:
        ...
    @property
    def m_dOccupedMargin(self) -> float:
        """
        占用保证金
        """
    @m_dOccupedMargin.setter
    def m_dOccupedMargin(self, arg0: float) -> None:
        ...
    @property
    def m_dReferenceRate(self) -> float:
        """
        汇率
        """
    @m_dReferenceRate.setter
    def m_dReferenceRate(self, arg0: float) -> None:
        ...
    @property
    def m_eCoveredFlag(self) -> ECoveredFlag:
        """
        备兑标记 '0' - 非备兑，'1' - 备兑
        """
    @m_eCoveredFlag.setter
    def m_eCoveredFlag(self, arg0: ECoveredFlag) -> None:
        ...
    @property
    def m_eEntrustType(self) -> EEntrustTypes:
        """
        委托类别
        """
    @m_eEntrustType.setter
    def m_eEntrustType(self, arg0: EEntrustTypes) -> None:
        ...
    @property
    def m_nAccountType(self) -> int:
        """
        账号类型
        """
    @m_nAccountType.setter
    def m_nAccountType(self, arg0: int) -> None:
        ...
    @property
    def m_nDirection(self) -> EEntrustBS:
        """
        期货多空，该字段与m_eOffsetFlag一起判断期货的报单类型。股票无用
        """
    @m_nDirection.setter
    def m_nDirection(self, arg0: EEntrustBS) -> None:
        ...
    @property
    def m_nHedgeFlag(self) -> EHedgeFlagType:
        """
        投机 套利 套保
        """
    @m_nHedgeFlag.setter
    def m_nHedgeFlag(self, arg0: EHedgeFlagType) -> None:
        ...
    @property
    def m_nOffsetFlag(self) -> EOffsetFlagType:
        """
        期货开平 股票买卖
        """
    @m_nOffsetFlag.setter
    def m_nOffsetFlag(self, arg0: EOffsetFlagType) -> None:
        ...
    @property
    def m_nOrderID(self) -> int:
        """
        指令ID
        """
    @m_nOrderID.setter
    def m_nOrderID(self, arg0: int) -> None:
        ...
    @property
    def m_nOrderPriceType(self) -> EBrokerPriceType:
        """
        类型，例如市价单 限价单
        """
    @m_nOrderPriceType.setter
    def m_nOrderPriceType(self, arg0: EBrokerPriceType) -> None:
        ...
    @property
    def m_nPortfolioDealType(self) -> PortfolioDealType:
        """
        投资组合成交类型
        """
    @m_nPortfolioDealType.setter
    def m_nPortfolioDealType(self, arg0: PortfolioDealType) -> None:
        ...
    @property
    def m_nProductId(self) -> int:
        """
        迅投产品ID
        """
    @m_nProductId.setter
    def m_nProductId(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> int:
        """
        成交量 期货单位手 股票做到股
        """
    @m_nVolume.setter
    def m_nVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strCombID(self) -> str:
        """
        组合持仓编号，用于解除组合策略
        """
    @m_strCombID.setter
    def m_strCombID(self, arg1: str) -> None:
        ...
    @property
    def m_strEntryDate(self) -> str:
        """
        投资组合-录入日期
        """
    @m_strEntryDate.setter
    def m_strEntryDate(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易所代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strExpireDate(self) -> str:
        """
        投资组合-解禁日志
        """
    @m_strExpireDate.setter
    def m_strExpireDate(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentName(self) -> str:
        """
        合约名称
        """
    @m_strInstrumentName.setter
    def m_strInstrumentName(self, arg1: str) -> None:
        ...
    @property
    def m_strOrderSysID(self) -> str:
        """
        委托
        """
    @m_strOrderSysID.setter
    def m_strOrderSysID(self, arg1: str) -> None:
        ...
    @property
    def m_strProductID(self) -> str:
        """
        合约品种
        """
    @m_strProductID.setter
    def m_strProductID(self, arg1: str) -> None:
        ...
    @property
    def m_strProductName(self) -> str:
        """
        迅投产品名称
        """
    @m_strProductName.setter
    def m_strProductName(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
    @property
    def m_strSecuAccount(self) -> str:
        """
        股东号
        """
    @m_strSecuAccount.setter
    def m_strSecuAccount(self, arg1: str) -> None:
        ...
    @property
    def m_strStrategyID(self) -> str:
        """
        收益互换策略ID
        """
    @m_strStrategyID.setter
    def m_strStrategyID(self, arg1: str) -> None:
        ...
    @property
    def m_strTradeDate(self) -> str:
        """
        成交日期
        """
    @m_strTradeDate.setter
    def m_strTradeDate(self, arg1: str) -> None:
        ...
    @property
    def m_strTradeID(self) -> str:
        """
        成交编号
        """
    @m_strTradeID.setter
    def m_strTradeID(self, arg1: str) -> None:
        ...
    @property
    def m_strTradeTime(self) -> str:
        """
        成交时间
        """
    @m_strTradeTime.setter
    def m_strTradeTime(self, arg1: str) -> None:
        ...
class CDealStatics:
    """
    成交统计
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dAmount(self) -> float:
        """
        成交额 期货=均价*量*合约乘数
        """
    @m_dAmount.setter
    def m_dAmount(self, arg0: float) -> None:
        ...
    @property
    def m_dAveragePrice(self) -> float:
        """
        成交均价
        """
    @m_dAveragePrice.setter
    def m_dAveragePrice(self, arg0: float) -> None:
        ...
    @property
    def m_dComssion(self) -> float:
        """
        手续费
        """
    @m_dComssion.setter
    def m_dComssion(self, arg0: float) -> None:
        ...
    @property
    def m_nCount(self) -> int:
        """
        相同合约相同方向条数
        """
    @m_nCount.setter
    def m_nCount(self, arg0: int) -> None:
        ...
    @property
    def m_nDirection(self) -> EEntrustBS:
        """
        期货多空，该字段与m_eOffsetFlag一起判断期货的报单类型。股票无用
        """
    @m_nDirection.setter
    def m_nDirection(self, arg0: EEntrustBS) -> None:
        ...
    @property
    def m_nHedgeFlag(self) -> EHedgeFlagType:
        """
        投机 套利 套保
        """
    @m_nHedgeFlag.setter
    def m_nHedgeFlag(self, arg0: EHedgeFlagType) -> None:
        ...
    @property
    def m_nOffsetFlag(self) -> EOffsetFlagType:
        """
        期货开平 股票买卖
        """
    @m_nOffsetFlag.setter
    def m_nOffsetFlag(self, arg0: EOffsetFlagType) -> None:
        ...
    @property
    def m_nProductId(self) -> int:
        """
        迅投产品ID
        """
    @m_nProductId.setter
    def m_nProductId(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> int:
        """
        成交量 期货单位手 股票做到股
        """
    @m_nVolume.setter
    def m_nVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易所代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentName(self) -> str:
        """
        合约名称
        """
    @m_strInstrumentName.setter
    def m_strInstrumentName(self, arg1: str) -> None:
        ...
    @property
    def m_strProductID(self) -> str:
        """
        合约品种
        """
    @m_strProductID.setter
    def m_strProductID(self, arg1: str) -> None:
        ...
    @property
    def m_strProductName(self) -> str:
        """
        迅投产品名称
        """
    @m_strProductName.setter
    def m_strProductName(self, arg1: str) -> None:
        ...
class CDeliveryDetail:
    """
    结算单信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_StrSettlementInfo(self) -> str:
        """
        结算单表  期货和期货期权特有
        """
    @m_StrSettlementInfo.setter
    def m_StrSettlementInfo(self, arg1: str) -> None:
        ...
    @property
    def m_dBizAmount(self) -> float:
        """
        成交数量
        """
    @m_dBizAmount.setter
    def m_dBizAmount(self, arg0: float) -> None:
        ...
    @property
    def m_dBizBalance(self) -> float:
        """
        成交金额
        """
    @m_dBizBalance.setter
    def m_dBizBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dBizPrice(self) -> float:
        """
        成交价格
        """
    @m_dBizPrice.setter
    def m_dBizPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dCommission(self) -> float:
        """
        手续费
        """
    @m_dCommission.setter
    def m_dCommission(self, arg0: float) -> None:
        ...
    @property
    def m_dEntrustPrice(self) -> float:
        """
        委托价格  港股特有
        """
    @m_dEntrustPrice.setter
    def m_dEntrustPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dFrontFee(self) -> float:
        """
        前台费用  港股特有
        """
    @m_dFrontFee.setter
    def m_dFrontFee(self, arg0: float) -> None:
        ...
    @property
    def m_dFundEffect(self) -> float:
        """
        清算金额  港股特有
        """
    @m_dFundEffect.setter
    def m_dFundEffect(self, arg0: float) -> None:
        ...
    @property
    def m_dLevyFee(self) -> float:
        """
        交易征费  港股特有
        """
    @m_dLevyFee.setter
    def m_dLevyFee(self, arg0: float) -> None:
        ...
    @property
    def m_dPostAmount(self) -> float:
        """
        股份余额  股票和港股特有
        """
    @m_dPostAmount.setter
    def m_dPostAmount(self, arg0: float) -> None:
        ...
    @property
    def m_dPostBalance(self) -> float:
        """
        资金余额  股票和港股特有
        """
    @m_dPostBalance.setter
    def m_dPostBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dSettRate(self) -> float:
        """
        结算汇率  港股特有
        """
    @m_dSettRate.setter
    def m_dSettRate(self, arg0: float) -> None:
        ...
    @property
    def m_dShareFee(self) -> float:
        """
        股份交收费  港股特有
        """
    @m_dShareFee.setter
    def m_dShareFee(self, arg0: float) -> None:
        ...
    @property
    def m_dStampTax(self) -> float:
        """
        印花税
        """
    @m_dStampTax.setter
    def m_dStampTax(self, arg0: float) -> None:
        ...
    @property
    def m_dStandardCommission(self) -> float:
        """
        标准手续费  港股特有
        """
    @m_dStandardCommission.setter
    def m_dStandardCommission(self, arg0: float) -> None:
        ...
    @property
    def m_dSysUsageFee(self) -> float:
        """
        交易系统使用费用  港股特有
        """
    @m_dSysUsageFee.setter
    def m_dSysUsageFee(self, arg0: float) -> None:
        ...
    @property
    def m_dTradeFee(self) -> float:
        """
        交易费  港股特有
        """
    @m_dTradeFee.setter
    def m_dTradeFee(self, arg0: float) -> None:
        ...
    @property
    def m_dTransFee(self) -> float:
        """
        其他杂费  股票期权和股票特有
        """
    @m_dTransFee.setter
    def m_dTransFee(self, arg0: float) -> None:
        ...
    @property
    def m_nAccountType(self) -> int:
        """
        账号类型
        """
    @m_nAccountType.setter
    def m_nAccountType(self, arg0: int) -> None:
        ...
    @property
    def m_nBizDate(self) -> int:
        """
        成交日期
        """
    @m_nBizDate.setter
    def m_nBizDate(self, arg0: int) -> None:
        ...
    @property
    def m_nBizFlag(self) -> int:
        """
        业务代码  港股特有
        """
    @m_nBizFlag.setter
    def m_nBizFlag(self, arg0: int) -> None:
        ...
    @property
    def m_nBizTime(self) -> int:
        """
        成交时间
        """
    @m_nBizTime.setter
    def m_nBizTime(self, arg0: int) -> None:
        ...
    @property
    def m_nClearDate(self) -> int:
        """
        清算日期  港股特有
        """
    @m_nClearDate.setter
    def m_nClearDate(self, arg0: int) -> None:
        ...
    @property
    def m_nEntrustAmount(self) -> int:
        """
        委托数量  港股特有
        """
    @m_nEntrustAmount.setter
    def m_nEntrustAmount(self, arg0: int) -> None:
        ...
    @property
    def m_nEntrustDate(self) -> int:
        """
        委托日期  股票期权和港股特有
        """
    @m_nEntrustDate.setter
    def m_nEntrustDate(self, arg0: int) -> None:
        ...
    @property
    def m_nEntrustTime(self) -> int:
        """
        委托时间  股票期权和港股特有
        """
    @m_nEntrustTime.setter
    def m_nEntrustTime(self, arg0: int) -> None:
        ...
    @property
    def m_nbizTimes(self) -> int:
        """
        成交笔数  港股特有
        """
    @m_nbizTimes.setter
    def m_nbizTimes(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号ID
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strBizName(self) -> str:
        """
        业务类型  股票期权和港股特有
        """
    @m_strBizName.setter
    def m_strBizName(self, arg1: str) -> None:
        ...
    @property
    def m_strBizNo(self) -> str:
        """
        成交序号
        """
    @m_strBizNo.setter
    def m_strBizNo(self, arg1: str) -> None:
        ...
    @property
    def m_strBizStatus(self) -> str:
        """
        成交状态  港股特有
        """
    @m_strBizStatus.setter
    def m_strBizStatus(self, arg1: str) -> None:
        ...
    @property
    def m_strBizType(self) -> str:
        """
        成交类型  股票期权特有
        """
    @m_strBizType.setter
    def m_strBizType(self, arg1: str) -> None:
        ...
    @property
    def m_strContractAccount(self) -> str:
        """
        合约账号  股票期权特有
        """
    @m_strContractAccount.setter
    def m_strContractAccount(self, arg1: str) -> None:
        ...
    @property
    def m_strCoveredFlag(self) -> str:
        """
        备兑标记  股票期权特有
        """
    @m_strCoveredFlag.setter
    def m_strCoveredFlag(self, arg1: str) -> None:
        ...
    @property
    def m_strCoveredFlagName(self) -> str:
        """
        备兑标记名称  股票期权特有
        """
    @m_strCoveredFlagName.setter
    def m_strCoveredFlagName(self, arg1: str) -> None:
        ...
    @property
    def m_strCustName(self) -> str:
        """
        客户姓名  港股特有
        """
    @m_strCustName.setter
    def m_strCustName(self, arg1: str) -> None:
        ...
    @property
    def m_strDate(self) -> str:
        """
        结算单日期  期货和期货期权特有
        """
    @m_strDate.setter
    def m_strDate(self, arg1: str) -> None:
        ...
    @property
    def m_strEntrustBS(self) -> str:
        """
        操作
        """
    @m_strEntrustBS.setter
    def m_strEntrustBS(self, arg1: str) -> None:
        ...
    @property
    def m_strEntrustBSName(self) -> str:
        """
        操作名称
        """
    @m_strEntrustBSName.setter
    def m_strEntrustBSName(self, arg1: str) -> None:
        ...
    @property
    def m_strEntrustNo(self) -> str:
        """
        委托号
        """
    @m_strEntrustNo.setter
    def m_strEntrustNo(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易所代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeName(self) -> str:
        """
        交易所名称
        """
    @m_strExchangeName.setter
    def m_strExchangeName(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentName(self) -> str:
        """
        合约名称
        """
    @m_strInstrumentName.setter
    def m_strInstrumentName(self, arg1: str) -> None:
        ...
    @property
    def m_strMoneyName(self) -> str:
        """
        币种  股票期权特有
        """
    @m_strMoneyName.setter
    def m_strMoneyName(self, arg1: str) -> None:
        ...
    @property
    def m_strMoneyType(self) -> str:
        """
        币种类型  股票期权和港股特有
        """
    @m_strMoneyType.setter
    def m_strMoneyType(self, arg1: str) -> None:
        ...
    @property
    def m_strOpenFlag(self) -> str:
        """
        开平标识  股票期权特有
        """
    @m_strOpenFlag.setter
    def m_strOpenFlag(self, arg1: str) -> None:
        ...
    @property
    def m_strOpenFlagName(self) -> str:
        """
        开平标识名称  股票期权特有
        """
    @m_strOpenFlagName.setter
    def m_strOpenFlagName(self, arg1: str) -> None:
        ...
    @property
    def m_strOrderId(self) -> str:
        """
        合同序号  港股特有
        """
    @m_strOrderId.setter
    def m_strOrderId(self, arg1: str) -> None:
        ...
    @property
    def m_strPositionStr(self) -> str:
        """
        记录序列号  股票期权和港股特有
        """
    @m_strPositionStr.setter
    def m_strPositionStr(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        备注  股票期权特有
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
    @property
    def m_strStockAccount(self) -> str:
        """
        股东账号  股票和港股特有
        """
    @m_strStockAccount.setter
    def m_strStockAccount(self, arg1: str) -> None:
        ...
class CETFComponentStockInfo:
    """
    ETF成分股信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dDiscountRatio(self) -> float:
        """
        赎回折价比率
        """
    @m_dDiscountRatio.setter
    def m_dDiscountRatio(self, arg0: float) -> None:
        ...
    @property
    def m_dRedeemReplaceBalance(self) -> float:
        """
        赎回替代金额
        """
    @m_dRedeemReplaceBalance.setter
    def m_dRedeemReplaceBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dReplaceBalance(self) -> float:
        """
        替代金额
        """
    @m_dReplaceBalance.setter
    def m_dReplaceBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dReplaceRatio(self) -> float:
        """
        溢价比率
        """
    @m_dReplaceRatio.setter
    def m_dReplaceRatio(self, arg0: float) -> None:
        ...
    @property
    def m_eReplaceFlag(self) -> EReplaceFlag:
        """
         下单类型，开、平、买、卖…
        """
    @m_eReplaceFlag.setter
    def m_eReplaceFlag(self, arg0: EReplaceFlag) -> None:
        ...
    @property
    def m_nComponentVolume(self) -> int:
        """
        成份股数量
        """
    @m_nComponentVolume.setter
    def m_nComponentVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strComponentCode(self) -> str:
        """
        成份股代码
        """
    @m_strComponentCode.setter
    def m_strComponentCode(self, arg1: str) -> None:
        ...
    @property
    def m_strComponentExchID(self) -> str:
        """
        成份股名称
        """
    @m_strComponentExchID.setter
    def m_strComponentExchID(self, arg1: str) -> None:
        ...
    @property
    def m_strComponentName(self) -> str:
        """
        成份股市场
        """
    @m_strComponentName.setter
    def m_strComponentName(self, arg1: str) -> None:
        ...
    @property
    def m_strEtfCode(self) -> str:
        """
        ETF代码
        """
    @m_strEtfCode.setter
    def m_strEtfCode(self, arg1: str) -> None:
        ...
    @property
    def m_strEtfName(self) -> str:
        """
        ETF基金名称
        """
    @m_strEtfName.setter
    def m_strEtfName(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        ETF市场
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
class CETFPCFDetail:
    """
    ETF申赎清单
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dCashBalance(self) -> float:
        """
        现金差额
        """
    @m_dCashBalance.setter
    def m_dCashBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dEcc(self) -> float:
        """
        预估现金差额 单位:元
        """
    @m_dEcc.setter
    def m_dEcc(self, arg0: float) -> None:
        ...
    @property
    def m_dMaxCashRatio(self) -> float:
        """
        现金替代比例上限
        """
    @m_dMaxCashRatio.setter
    def m_dMaxCashRatio(self, arg0: float) -> None:
        ...
    @property
    def m_dNav(self) -> float:
        """
        基金份额净值 单位:元
        """
    @m_dNav.setter
    def m_dNav(self, arg0: float) -> None:
        ...
    @property
    def m_dNavPerCU(self) -> float:
        """
        最小申购,赎回单位净值 单位:元
        """
    @m_dNavPerCU.setter
    def m_dNavPerCU(self, arg0: float) -> None:
        ...
    @property
    def m_nCreationLimit(self) -> int:
        """
        申购上限 单位:份,0 表示不限制
        """
    @m_nCreationLimit.setter
    def m_nCreationLimit(self, arg0: int) -> None:
        ...
    @property
    def m_nEnableCreation(self) -> int:
        """
        是否允许申购 1,是,0,否
        """
    @m_nEnableCreation.setter
    def m_nEnableCreation(self, arg0: int) -> None:
        ...
    @property
    def m_nEnableRedemption(self) -> int:
        """
        是否允许赎回 1,是,0,否
        """
    @m_nEnableRedemption.setter
    def m_nEnableRedemption(self, arg0: int) -> None:
        ...
    @property
    def m_nNeedPublish(self) -> int:
        """
        是否需要公布IOPV 1,是,0,否
        """
    @m_nNeedPublish.setter
    def m_nNeedPublish(self, arg0: int) -> None:
        ...
    @property
    def m_nRedemptionLimit(self) -> int:
        """
        赎回上限 单位:份,0 表示不限制
        """
    @m_nRedemptionLimit.setter
    def m_nRedemptionLimit(self, arg0: int) -> None:
        ...
    @property
    def m_nReportUnit(self) -> int:
        """
        最小申购,赎回单位 单位:份
        """
    @m_nReportUnit.setter
    def m_nReportUnit(self, arg0: int) -> None:
        ...
    @property
    def m_nType(self) -> int:
        """
        基金类型
        """
    @m_nType.setter
    def m_nType(self, arg0: int) -> None:
        ...
    @property
    def m_strEtfCode(self) -> str:
        """
        ETF代码
        """
    @m_strEtfCode.setter
    def m_strEtfCode(self, arg1: str) -> None:
        ...
    @property
    def m_strEtfExchID(self) -> str:
        """
        ETF市场
        """
    @m_strEtfExchID.setter
    def m_strEtfExchID(self, arg1: str) -> None:
        ...
    @property
    def m_strName(self) -> str:
        """
        基金名称
        """
    @m_strName.setter
    def m_strName(self, arg1: str) -> None:
        ...
    @property
    def m_strPrCode(self) -> str:
        """
        基金申赎代码
        """
    @m_strPrCode.setter
    def m_strPrCode(self, arg1: str) -> None:
        ...
    @property
    def m_strPreTradingDay(self) -> str:
        """
        ETF前交易日期 格式 YYYYMMDD
        """
    @m_strPreTradingDay.setter
    def m_strPreTradingDay(self, arg1: str) -> None:
        ...
    @property
    def m_strTradingDay(self) -> str:
        """
        ETF交易日期 格式 YYYYMMDD
        """
    @m_strTradingDay.setter
    def m_strTradingDay(self, arg1: str) -> None:
        ...
class CExchangeStatus:
    """
    市场状态信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_eInstrumentStatus(self) -> EXTExchangeStatus:
        """
        市场状态
        """
    @m_eInstrumentStatus.setter
    def m_eInstrumentStatus(self, arg0: EXTExchangeStatus) -> None:
        ...
    @property
    def m_nExchangeTimeDelta(self) -> int:
        """
        交易所时间相对于服务器时间的时间差
        """
    @m_nExchangeTimeDelta.setter
    def m_nExchangeTimeDelta(self, arg0: int) -> None:
        ...
    @property
    def m_strEnterReason(self) -> str:
        """
        进入本状态原因
        """
    @m_strEnterReason.setter
    def m_strEnterReason(self, arg1: str) -> None:
        ...
    @property
    def m_strEnterTime(self) -> str:
        """
        进入本状态时间
        """
    @m_strEnterTime.setter
    def m_strEnterTime(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeId(self) -> str:
        """
        交易所代码
        """
    @m_strExchangeId.setter
    def m_strExchangeId(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentId(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentId.setter
    def m_strInstrumentId(self, arg1: str) -> None:
        ...
    @property
    def m_strProductId(self) -> str:
        """
        合约品种
        """
    @m_strProductId.setter
    def m_strProductId(self, arg1: str) -> None:
        ...
class CExternAlgGroupOrder:
    """
    外部算法组合单下单参数
    """
    def __init__(self) -> None:
        ...
    @property
    def m_eOperationType(self) -> list:
        """
        每只股票的下单类型
        """
    @m_eOperationType.setter
    def m_eOperationType(self, arg1: list) -> None:
        ...
    @property
    def m_nOrderNum(self) -> int:
        """
        股票只数
        """
    @m_nOrderNum.setter
    def m_nOrderNum(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> list:
        """
        每只股票的下单量
        """
    @m_nVolume.setter
    def m_nVolume(self, arg1: list) -> None:
        ...
    @property
    def m_orderParam(self) -> CExternAlgorithmOrder:
        """
        下单配置
        """
    @m_orderParam.setter
    def m_orderParam(self, arg0: CExternAlgorithmOrder) -> None:
        ...
    @property
    def m_strInstrument(self) -> list:
        """
        证券代码
        """
    @m_strInstrument.setter
    def m_strInstrument(self, arg1: list) -> None:
        ...
    @property
    def m_strMarket(self) -> list:
        """
        市场列表
        """
    @m_strMarket.setter
    def m_strMarket(self, arg1: list) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
class CExternAlgorithmOrder:
    """
    外部算法单下单参数
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dAvailable(self) -> float:
        """
        t0策略最大可用资金
        """
    @m_dAvailable.setter
    def m_dAvailable(self, arg0: float) -> None:
        ...
    @property
    def m_dMaxPartRate(self) -> float:
        """
        量比比例, 用户设定, 当MaxPartRate==100%, 表示没有限制
        """
    @m_dMaxPartRate.setter
    def m_dMaxPartRate(self, arg0: float) -> None:
        ...
    @property
    def m_dMinAmountPerOrder(self) -> float:
        """
        委托最小金额
        """
    @m_dMinAmountPerOrder.setter
    def m_dMinAmountPerOrder(self, arg0: float) -> None:
        ...
    @property
    def m_dPrice(self) -> float:
        """
        基准价
        """
    @m_dPrice.setter
    def m_dPrice(self, arg0: float) -> None:
        ...
    @property
    def m_eCmdDateLimit(self) -> EXTCommandDateLimit:
        """
        指令跨日开关
        """
    @m_eCmdDateLimit.setter
    def m_eCmdDateLimit(self, arg0: EXTCommandDateLimit) -> None:
        ...
    @property
    def m_eOperationType(self) -> EOperationType:
        """
        下单操作：买入卖出
        """
    @m_eOperationType.setter
    def m_eOperationType(self, arg0: EOperationType) -> None:
        ...
    @property
    def m_eOrderStrategyType(self) -> EOrderStrategyType:
        """
        算法下单方式
        """
    @m_eOrderStrategyType.setter
    def m_eOrderStrategyType(self, arg0: EOrderStrategyType) -> None:
        ...
    @property
    def m_nLimitedPriceType(self) -> int:
        """
        条件单价格限制类型
        """
    @m_nLimitedPriceType.setter
    def m_nLimitedPriceType(self, arg0: int) -> None:
        ...
    @property
    def m_nMaxTradeDurationAfterET(self) -> int:
        """
        收盘后是否继续执行， 0不继续，非0继续
        """
    @m_nMaxTradeDurationAfterET.setter
    def m_nMaxTradeDurationAfterET(self, arg0: int) -> None:
        ...
    @property
    def m_nStopTradeForOwnHiLow(self) -> EStopTradeForOwnHiLow:
        """
        涨跌停控制
        """
    @m_nStopTradeForOwnHiLow.setter
    def m_nStopTradeForOwnHiLow(self, arg0: EStopTradeForOwnHiLow) -> None:
        ...
    @property
    def m_nTimeType(self) -> int:
        """
        时间类型，0，按区间，1，按执行时间， 默认0
        """
    @m_nTimeType.setter
    def m_nTimeType(self, arg0: int) -> None:
        ...
    @property
    def m_nTimeValue(self) -> int:
        """
        执行时间
        """
    @m_nTimeValue.setter
    def m_nTimeValue(self, arg0: int) -> None:
        ...
    @property
    def m_nValidTimeEnd(self) -> int:
        """
        有效结束时间 
        """
    @m_nValidTimeEnd.setter
    def m_nValidTimeEnd(self, arg0: int) -> None:
        ...
    @property
    def m_nValidTimeStart(self) -> int:
        """
        有效开始时间 
        """
    @m_nValidTimeStart.setter
    def m_nValidTimeStart(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> int:
        """
        下单总量
        """
    @m_nVolume.setter
    def m_nVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrument(self) -> str:
        """
        合约
        """
    @m_strInstrument.setter
    def m_strInstrument(self, arg1: str) -> None:
        ...
    @property
    def m_strMarket(self) -> str:
        """
        市场
        """
    @m_strMarket.setter
    def m_strMarket(self, arg1: str) -> None:
        ...
    @property
    def m_strOrderType(self) -> str:
        """
        算法名称，FTAIWAP，ALGOINTERFACE, ZEUS....
        """
    @m_strOrderType.setter
    def m_strOrderType(self, arg1: str) -> None:
        ...
    @property
    def m_strOtherParam(self) -> str:
        """
        条件单其他参数
        """
    @m_strOtherParam.setter
    def m_strOtherParam(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark1(self) -> str:
        """
        投资备注1
        """
    @m_strRemark1.setter
    def m_strRemark1(self, arg1: str) -> None:
        ...
    @property
    def m_strStrategyID(self) -> str:
        """
        收益互换策略ID
        """
    @m_strStrategyID.setter
    def m_strStrategyID(self, arg1: str) -> None:
        ...
class CFundFlow:
    """
    资金流水信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dBalance(self) -> float:
        """
        剩余金额，股票，两融，深港通，沪港通，个股期权
        """
    @m_dBalance.setter
    def m_dBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dBizBalance(self) -> float:
        """
        发生金额，股票，两融，深港通，沪港通，个股期权
        """
    @m_dBizBalance.setter
    def m_dBizBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dBizOrderAmount(self) -> float:
        """
        委托数量，股票，两融
        """
    @m_dBizOrderAmount.setter
    def m_dBizOrderAmount(self, arg0: float) -> None:
        ...
    @property
    def m_dBizOrderPrice(self) -> float:
        """
        委托价格，股票，两融
        """
    @m_dBizOrderPrice.setter
    def m_dBizOrderPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dBizPrice(self) -> float:
        """
        成交价格，股票，两融
        """
    @m_dBizPrice.setter
    def m_dBizPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dBizPriceBalance(self) -> float:
        """
        成交金额，股票，两融
        """
    @m_dBizPriceBalance.setter
    def m_dBizPriceBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dChangeAmount(self) -> float:
        """
        发生数量/金额，股票，两融
        """
    @m_dChangeAmount.setter
    def m_dChangeAmount(self, arg0: float) -> None:
        ...
    @property
    def m_dCommission(self) -> float:
        """
        手续费，股票，两融
        """
    @m_dCommission.setter
    def m_dCommission(self, arg0: float) -> None:
        ...
    @property
    def m_dOtherFee(self) -> float:
        """
        其他费用，股票，两融
        """
    @m_dOtherFee.setter
    def m_dOtherFee(self, arg0: float) -> None:
        ...
    @property
    def m_dPostAmount(self) -> float:
        """
        剩余数量/金额，股票，两融
        """
    @m_dPostAmount.setter
    def m_dPostAmount(self, arg0: float) -> None:
        ...
    @property
    def m_dStampTax(self) -> float:
        """
        印花税，股票，两融
        """
    @m_dStampTax.setter
    def m_dStampTax(self, arg0: float) -> None:
        ...
    @property
    def m_dTransFee(self) -> float:
        """
        过户费，股票，两融
        """
    @m_dTransFee.setter
    def m_dTransFee(self, arg0: float) -> None:
        ...
    @property
    def m_eMoneyType(self) -> EMoneyType:
        """
        币种，股票，两融，深港通，沪港通，个股期权
        """
    @m_eMoneyType.setter
    def m_eMoneyType(self, arg0: EMoneyType) -> None:
        ...
    @property
    def m_nBizDate(self) -> int:
        """
        发生日期，股票，两融，深港通，沪港通，个股期权
        """
    @m_nBizDate.setter
    def m_nBizDate(self, arg0: int) -> None:
        ...
    @property
    def m_nBizTime(self) -> int:
        """
        发生时间，股票，两融，深港通，沪港通，个股期权
        """
    @m_nBizTime.setter
    def m_nBizTime(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        资金账户ID，股票，两融，深港通，沪港通，个股期权
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strBizName(self) -> str:
        """
        业务名称，股票，两融，深港通，沪港通，个股期权
        """
    @m_strBizName.setter
    def m_strBizName(self, arg1: str) -> None:
        ...
    @property
    def m_strBizNo(self) -> str:
        """
        成交序列号，股票，两融 
        """
    @m_strBizNo.setter
    def m_strBizNo(self, arg1: str) -> None:
        ...
    @property
    def m_strBizType(self) -> str:
        """
        业务名称，股票，两融
        """
    @m_strBizType.setter
    def m_strBizType(self, arg1: str) -> None:
        ...
    @property
    def m_strEntrustBS(self) -> str:
        """
        买卖方向，股票，两融 
        """
    @m_strEntrustBS.setter
    def m_strEntrustBS(self, arg1: str) -> None:
        ...
    @property
    def m_strEntrustNo(self) -> str:
        """
        委托号，股票，两融 
        """
    @m_strEntrustNo.setter
    def m_strEntrustNo(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrument(self) -> str:
        """
        合约，股票，两融，深港通，沪港通，个股期权
        """
    @m_strInstrument.setter
    def m_strInstrument(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentName(self) -> str:
        """
        合约名称，股票，两融
        """
    @m_strInstrumentName.setter
    def m_strInstrumentName(self, arg1: str) -> None:
        ...
    @property
    def m_strMarket(self) -> str:
        """
        市场，股票，两融，深港通，沪港通，个股期权
        """
    @m_strMarket.setter
    def m_strMarket(self, arg1: str) -> None:
        ...
    @property
    def m_strNotes(self) -> str:
        """
        备注，股票，两融 
        """
    @m_strNotes.setter
    def m_strNotes(self, arg1: str) -> None:
        ...
    @property
    def m_strSerialNo(self) -> str:
        """
        流水序号，股票，两融，深港通，沪港通，个股期权
        """
    @m_strSerialNo.setter
    def m_strSerialNo(self, arg1: str) -> None:
        ...
    @property
    def m_strStockAccount(self) -> str:
        """
        股东账号，股票，两融 
        """
    @m_strStockAccount.setter
    def m_strStockAccount(self, arg1: str) -> None:
        ...
class CFuturePositionStatics:
    """
    期货持仓统计
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dAssestWeight(self) -> float:
        """
        资产占比
        """
    @m_dAssestWeight.setter
    def m_dAssestWeight(self, arg0: float) -> None:
        ...
    @property
    def m_dAvgPrice(self) -> float:
        """
        持仓均价
        """
    @m_dAvgPrice.setter
    def m_dAvgPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dCloseProfit(self) -> float:
        """
        平仓盈亏
        """
    @m_dCloseProfit.setter
    def m_dCloseProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dEstimateSettleMargin(self) -> float:
        """
         当日盈亏（预结）
        """
    @m_dEstimateSettleMargin.setter
    def m_dEstimateSettleMargin(self, arg0: float) -> None:
        ...
    @property
    def m_dEstimateSettleProfitLoss(self) -> float:
        """
         保证金（预结）
        """
    @m_dEstimateSettleProfitLoss.setter
    def m_dEstimateSettleProfitLoss(self, arg0: float) -> None:
        ...
    @property
    def m_dFloatProfit(self) -> float:
        """
        浮动盈亏 detail的汇总
        """
    @m_dFloatProfit.setter
    def m_dFloatProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dFloatProfitDivideByBalance(self) -> float:
        """
         浮盈比例（动态权益）
        """
    @m_dFloatProfitDivideByBalance.setter
    def m_dFloatProfitDivideByBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dFloatProfitDivideByUsedMargin(self) -> float:
        """
         浮盈比例（保证金）
        """
    @m_dFloatProfitDivideByUsedMargin.setter
    def m_dFloatProfitDivideByUsedMargin(self, arg0: float) -> None:
        ...
    @property
    def m_dFrozenCommission(self) -> float:
        """
        冻结手续费
        """
    @m_dFrozenCommission.setter
    def m_dFrozenCommission(self, arg0: float) -> None:
        ...
    @property
    def m_dFrozenMargin(self) -> float:
        """
        冻结保证金
        """
    @m_dFrozenMargin.setter
    def m_dFrozenMargin(self, arg0: float) -> None:
        ...
    @property
    def m_dFrozenRoyalty(self) -> float:
        """
        冻结权利金
        """
    @m_dFrozenRoyalty.setter
    def m_dFrozenRoyalty(self, arg0: float) -> None:
        ...
    @property
    def m_dIncreaseBySettlement(self) -> float:
        """
        当日涨幅（结）
        """
    @m_dIncreaseBySettlement.setter
    def m_dIncreaseBySettlement(self, arg0: float) -> None:
        ...
    @property
    def m_dInstrumentValue(self) -> float:
        """
        合约价值
        """
    @m_dInstrumentValue.setter
    def m_dInstrumentValue(self, arg0: float) -> None:
        ...
    @property
    def m_dLastPrice(self) -> float:
        """
        最新价
        """
    @m_dLastPrice.setter
    def m_dLastPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dMarginRatio(self) -> float:
        """
        保证金占比
        """
    @m_dMarginRatio.setter
    def m_dMarginRatio(self, arg0: float) -> None:
        ...
    @property
    def m_dOpenCost(self) -> float:
        """
        开仓成本
        """
    @m_dOpenCost.setter
    def m_dOpenCost(self, arg0: float) -> None:
        ...
    @property
    def m_dOpenPrice(self) -> float:
        """
        开仓均价
        """
    @m_dOpenPrice.setter
    def m_dOpenPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dPositionCost(self) -> float:
        """
        持仓成本 detail的汇总
        """
    @m_dPositionCost.setter
    def m_dPositionCost(self, arg0: float) -> None:
        ...
    @property
    def m_dPositionProfit(self) -> float:
        """
        持仓盈亏 detail的汇总
        """
    @m_dPositionProfit.setter
    def m_dPositionProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dRiseRatio(self) -> float:
        """
        当日涨幅
        """
    @m_dRiseRatio.setter
    def m_dRiseRatio(self, arg0: float) -> None:
        ...
    @property
    def m_dRoyalty(self) -> float:
        """
        权利金市值
        """
    @m_dRoyalty.setter
    def m_dRoyalty(self, arg0: float) -> None:
        ...
    @property
    def m_dSettlementPrice(self) -> float:
        """
         结算价
        """
    @m_dSettlementPrice.setter
    def m_dSettlementPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dTodayCloseProfitLoss(self) -> float:
        """
        当日盈亏（收） 
        """
    @m_dTodayCloseProfitLoss.setter
    def m_dTodayCloseProfitLoss(self, arg0: float) -> None:
        ...
    @property
    def m_dTodayProfitLoss(self) -> float:
        """
        当日盈亏（结）
        """
    @m_dTodayProfitLoss.setter
    def m_dTodayProfitLoss(self, arg0: float) -> None:
        ...
    @property
    def m_dUsedCommission(self) -> float:
        """
        已使用的手续费
        """
    @m_dUsedCommission.setter
    def m_dUsedCommission(self, arg0: float) -> None:
        ...
    @property
    def m_dUsedMargin(self) -> float:
        """
        已使用保证金
        """
    @m_dUsedMargin.setter
    def m_dUsedMargin(self, arg0: float) -> None:
        ...
    @property
    def m_nCanCloseVol(self) -> int:
        """
        可平量
        """
    @m_nCanCloseVol.setter
    def m_nCanCloseVol(self, arg0: int) -> None:
        ...
    @property
    def m_nCancelTimes(self) -> int:
        """
        撤单次数
        """
    @m_nCancelTimes.setter
    def m_nCancelTimes(self, arg0: int) -> None:
        ...
    @property
    def m_nDirection(self) -> EEntrustBS:
        """
        期货多空，该字段与m_eOffsetFlag一起判断期货的报单类型。
        """
    @m_nDirection.setter
    def m_nDirection(self, arg0: EEntrustBS) -> None:
        ...
    @property
    def m_nHedgeFlag(self) -> EHedgeFlagType:
        """
        投机 套利 套保
        """
    @m_nHedgeFlag.setter
    def m_nHedgeFlag(self, arg0: EHedgeFlagType) -> None:
        ...
    @property
    def m_nOpenTimes(self) -> int:
        """
        开仓次数
        """
    @m_nOpenTimes.setter
    def m_nOpenTimes(self, arg0: int) -> None:
        ...
    @property
    def m_nOpenVolume(self) -> int:
        """
        总开仓量
        """
    @m_nOpenVolume.setter
    def m_nOpenVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nPosition(self) -> int:
        """
        总持仓
        """
    @m_nPosition.setter
    def m_nPosition(self, arg0: int) -> None:
        ...
    @property
    def m_nTodayPosition(self) -> int:
        """
        今仓
        """
    @m_nTodayPosition.setter
    def m_nTodayPosition(self, arg0: int) -> None:
        ...
    @property
    def m_nYestodayInitPosition(self) -> int:
        """
        昨日持仓
        """
    @m_nYestodayInitPosition.setter
    def m_nYestodayInitPosition(self, arg0: int) -> None:
        ...
    @property
    def m_nYestodayPosition(self) -> int:
        """
        昨仓
        """
    @m_nYestodayPosition.setter
    def m_nYestodayPosition(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        资金账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易所
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeName(self) -> str:
        """
        市场名称
        """
    @m_strExchangeName.setter
    def m_strExchangeName(self, arg1: str) -> None:
        ...
    @property
    def m_strExpireDate(self) -> str:
        """
        到期日
        """
    @m_strExpireDate.setter
    def m_strExpireDate(self, arg1: str) -> None:
        ...
    @property
    def m_strFtProductName(self) -> str:
        """
        品种名称
        """
    @m_strFtProductName.setter
    def m_strFtProductName(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentName(self) -> str:
        """
        合约名称
        """
    @m_strInstrumentName.setter
    def m_strInstrumentName(self, arg1: str) -> None:
        ...
    @property
    def m_strProductID(self) -> str:
        """
        品种代码
        """
    @m_strProductID.setter
    def m_strProductID(self, arg1: str) -> None:
        ...
    @property
    def m_strProductName(self) -> str:
        """
        产品名称
        """
    @m_strProductName.setter
    def m_strProductName(self, arg1: str) -> None:
        ...
class CGroupOrder:
    """
    组合单下单参数
    """
    def __init__(self) -> None:
        ...
    @property
    def m_eOperationType(self) -> list:
        """
        每只股票的下单类型
        """
    @m_eOperationType.setter
    def m_eOperationType(self, arg1: list) -> None:
        ...
    @property
    def m_nOrderNum(self) -> int:
        """
        股票只数
        """
    @m_nOrderNum.setter
    def m_nOrderNum(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> list:
        """
        每只股票的下单量
        """
    @m_nVolume.setter
    def m_nVolume(self, arg1: list) -> None:
        ...
    @property
    def m_orderParam(self) -> CAlgorithmOrder:
        """
        下单配置
        """
    @m_orderParam.setter
    def m_orderParam(self, arg0: CAlgorithmOrder) -> None:
        ...
    @property
    def m_strInstrument(self) -> list:
        """
        证券代码
        """
    @m_strInstrument.setter
    def m_strInstrument(self, arg1: list) -> None:
        ...
    @property
    def m_strMarket(self) -> list:
        """
        市场列表
        """
    @m_strMarket.setter
    def m_strMarket(self, arg1: list) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
class CHuaChuangAlgoGroupOrder:
    """
    华创算法组合单下单参数
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dPrice(self) -> list:
        """
        每只股票的下单价格
        """
    @m_dPrice.setter
    def m_dPrice(self, arg1: list) -> None:
        ...
    @property
    def m_eOperationType(self) -> list:
        """
        每只股票的下单类型
        """
    @m_eOperationType.setter
    def m_eOperationType(self, arg1: list) -> None:
        ...
    @property
    def m_nOrderNum(self) -> int:
        """
        股票只数
        """
    @m_nOrderNum.setter
    def m_nOrderNum(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> list:
        """
        每只股票的下单量
        """
    @m_nVolume.setter
    def m_nVolume(self, arg1: list) -> None:
        ...
    @property
    def m_orderParam(self) -> CHuaChuangAlgorithmOrder:
        """
        下单配置
        """
    @m_orderParam.setter
    def m_orderParam(self, arg0: CHuaChuangAlgorithmOrder) -> None:
        ...
    @property
    def m_strInstrument(self) -> list:
        """
        证券代码
        """
    @m_strInstrument.setter
    def m_strInstrument(self, arg1: list) -> None:
        ...
    @property
    def m_strMarket(self) -> list:
        """
        市场列表
        """
    @m_strMarket.setter
    def m_strMarket(self, arg1: list) -> None:
        ...
class CHuaChuangAlgorithmOrder:
    """
    华创算法单下单参数
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dInCloseAcution(self) -> int:
        """
        参与收盘竞价 1 是， 0 否，默认0
        """
    @m_dInCloseAcution.setter
    def m_dInCloseAcution(self, arg0: int) -> None:
        ...
    @property
    def m_dMaxMarketRate(self) -> float:
        """
        最大市场占比  0.00-100.00
        """
    @m_dMaxMarketRate.setter
    def m_dMaxMarketRate(self, arg0: float) -> None:
        ...
    @property
    def m_dMaxPartRate(self) -> float:
        """
        量比比例  仅三方算法指令有值
        """
    @m_dMaxPartRate.setter
    def m_dMaxPartRate(self, arg0: float) -> None:
        ...
    @property
    def m_dMinAmountPerOrder(self) -> float:
        """
        委托最小金额
        """
    @m_dMinAmountPerOrder.setter
    def m_dMinAmountPerOrder(self, arg0: float) -> None:
        ...
    @property
    def m_dMinQuantityRate(self) -> float:
        """
        最小跟量比例 ，默认0
        """
    @m_dMinQuantityRate.setter
    def m_dMinQuantityRate(self, arg0: float) -> None:
        ...
    @property
    def m_dPrice(self) -> float:
        """
        基准价
        """
    @m_dPrice.setter
    def m_dPrice(self, arg0: float) -> None:
        ...
    @property
    def m_eOperationType(self) -> EOperationType:
        """
        下单操作：买入卖出
        """
    @m_eOperationType.setter
    def m_eOperationType(self, arg0: EOperationType) -> None:
        ...
    @property
    def m_eOrderStrategyType(self) -> EOrderStrategyType:
        """
        算法下单方式
        """
    @m_eOrderStrategyType.setter
    def m_eOrderStrategyType(self, arg0: EOrderStrategyType) -> None:
        ...
    @property
    def m_ePriceType(self) -> EPriceType:
        """
        报价方式：市价和指定价
        """
    @m_ePriceType.setter
    def m_ePriceType(self, arg0: EPriceType) -> None:
        ...
    @property
    def m_nExecuteOffset(self) -> int:
        """
        执行偏移量  1 低,2 中,3 高，默认2
        """
    @m_nExecuteOffset.setter
    def m_nExecuteOffset(self, arg0: int) -> None:
        ...
    @property
    def m_nFixRate(self) -> int:
        """
        限价内占比  1 是， 0 否，默认0
        """
    @m_nFixRate.setter
    def m_nFixRate(self, arg0: int) -> None:
        ...
    @property
    def m_nInOpenAcution(self) -> int:
        """
        参与开盘竞价 1 是， 0 否，默认0
        """
    @m_nInOpenAcution.setter
    def m_nInOpenAcution(self, arg0: int) -> None:
        ...
    @property
    def m_nLimitedPriceType(self) -> int:
        """
        条件单价格限制类型
        """
    @m_nLimitedPriceType.setter
    def m_nLimitedPriceType(self, arg0: int) -> None:
        ...
    @property
    def m_nReferencePrice(self) -> int:
        """
        参考价格 1日内均价,2交易时段均价,3最新价,4开盘价,5昨日收盘价，默认1
        """
    @m_nReferencePrice.setter
    def m_nReferencePrice(self, arg0: int) -> None:
        ...
    @property
    def m_nSingleVolume(self) -> int:
        """
        单次委托量 0-1000000，默认0
        """
    @m_nSingleVolume.setter
    def m_nSingleVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> int:
        """
        下单总量
        """
    @m_nVolume.setter
    def m_nVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrument(self) -> str:
        """
        合约
        """
    @m_strInstrument.setter
    def m_strInstrument(self, arg1: str) -> None:
        ...
    @property
    def m_strMarket(self) -> str:
        """
        市场
        """
    @m_strMarket.setter
    def m_strMarket(self, arg1: str) -> None:
        ...
    @property
    def m_strOrderType(self) -> str:
        """
        算法名称，FTAIWAP，ALGOINTERFACE, ZEUS....
        """
    @m_strOrderType.setter
    def m_strOrderType(self, arg1: str) -> None:
        ...
    @property
    def m_strOtherParam(self) -> str:
        """
        华创算法额外扩展参数
        """
    @m_strOtherParam.setter
    def m_strOtherParam(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark1(self) -> str:
        """
        投资备注1
        """
    @m_strRemark1.setter
    def m_strRemark1(self, arg1: str) -> None:
        ...
    @property
    def m_strTimeEnd(self) -> str:
        """
        结束时间，格式yyyyMMdd-HH:mm:ss.fff  默认当日收盘时间
        """
    @m_strTimeEnd.setter
    def m_strTimeEnd(self, arg1: str) -> None:
        ...
    @property
    def m_strTimeStart(self) -> str:
        """
        开始时间，格式yyyyMMdd-HH:mm:ss.fff  默认当日开盘时间
        """
    @m_strTimeStart.setter
    def m_strTimeStart(self, arg1: str) -> None:
        ...
class CInstrumentDetail:
    """
    股票（合约）信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dDownStopPrice(self) -> float:
        """
        跌停价
        """
    @m_dDownStopPrice.setter
    def m_dDownStopPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dMarginUnit(self) -> float:
        """
        保证金单位
        """
    @m_dMarginUnit.setter
    def m_dMarginUnit(self, arg0: float) -> None:
        ...
    @property
    def m_dOptExercisePrice(self) -> float:
        """
        期权行权价格
        """
    @m_dOptExercisePrice.setter
    def m_dOptExercisePrice(self, arg0: float) -> None:
        ...
    @property
    def m_dPriceTick(self) -> float:
        """
        价格波动
        """
    @m_dPriceTick.setter
    def m_dPriceTick(self, arg0: float) -> None:
        ...
    @property
    def m_dSettlementPrice(self) -> float:
        """
        前结算
        """
    @m_dSettlementPrice.setter
    def m_dSettlementPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dUpStopPrice(self) -> float:
        """
        涨停价
        """
    @m_dUpStopPrice.setter
    def m_dUpStopPrice(self, arg0: float) -> None:
        ...
    @property
    def m_eSuspendedType(self) -> EXtSuspendedType:
        """
        停牌状态
        """
    @m_eSuspendedType.setter
    def m_eSuspendedType(self, arg0: EXtSuspendedType) -> None:
        ...
    @property
    def m_nCallOrPut(self) -> int:
        """
        合约种类(个股期权：0认购，1认沽)
        """
    @m_nCallOrPut.setter
    def m_nCallOrPut(self, arg0: int) -> None:
        ...
    @property
    def m_nOptUnit(self) -> int:
        """
        期权合约单位
        """
    @m_nOptUnit.setter
    def m_nOptUnit(self, arg0: int) -> None:
        ...
    @property
    def m_nVolumeMultiple(self) -> int:
        """
        合约乘数
        """
    @m_nVolumeMultiple.setter
    def m_nVolumeMultiple(self, arg0: int) -> None:
        ...
    @property
    def m_strEndDelivDate(self) -> str:
        """
        最后日期
        """
    @m_strEndDelivDate.setter
    def m_strEndDelivDate(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易所代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentName(self) -> str:
        """
        合约名称
        """
    @m_strInstrumentName.setter
    def m_strInstrumentName(self, arg1: str) -> None:
        ...
    @property
    def m_strOptUndlCode(self) -> str:
        """
        期权标的代码
        """
    @m_strOptUndlCode.setter
    def m_strOptUndlCode(self, arg1: str) -> None:
        ...
    @property
    def m_strOptUndlName(self) -> str:
        """
        期权标的证券名称
        """
    @m_strOptUndlName.setter
    def m_strOptUndlName(self, arg1: str) -> None:
        ...
    @property
    def m_strProductID(self) -> str:
        """
        品种代码
        """
    @m_strProductID.setter
    def m_strProductID(self, arg1: str) -> None:
        ...
class CInstrumentInfo:
    """
    合约信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dDownStopPrice(self) -> float:
        """
        跌停价
        """
    @m_dDownStopPrice.setter
    def m_dDownStopPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dLongMarginRatio(self) -> float:
        """
        多头保证金率
        """
    @m_dLongMarginRatio.setter
    def m_dLongMarginRatio(self, arg0: float) -> None:
        ...
    @property
    def m_dMarginUnit(self) -> float:
        """
        保证金单位
        """
    @m_dMarginUnit.setter
    def m_dMarginUnit(self, arg0: float) -> None:
        ...
    @property
    def m_dOptExercisePrice(self) -> float:
        """
        期权行权价
        """
    @m_dOptExercisePrice.setter
    def m_dOptExercisePrice(self, arg0: float) -> None:
        ...
    @property
    def m_dPriceTick(self) -> float:
        """
        最小变动价位
        """
    @m_dPriceTick.setter
    def m_dPriceTick(self, arg0: float) -> None:
        ...
    @property
    def m_dSettlementPrice(self) -> float:
        """
        前结算
        """
    @m_dSettlementPrice.setter
    def m_dSettlementPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dShortMarginRatio(self) -> float:
        """
        空头保证金率
        """
    @m_dShortMarginRatio.setter
    def m_dShortMarginRatio(self, arg0: float) -> None:
        ...
    @property
    def m_dUpStopPrice(self) -> float:
        """
        涨停价
        """
    @m_dUpStopPrice.setter
    def m_dUpStopPrice(self, arg0: float) -> None:
        ...
    @property
    def m_eExDivdendType(self) -> EXtExDivdendType:
        """
        除权除息标志
        """
    @m_eExDivdendType.setter
    def m_eExDivdendType(self, arg0: EXtExDivdendType) -> None:
        ...
    @property
    def m_eMaxMarginSideAlgorithm(self) -> EXtMaxMarginSideAlgorithmType:
        """
        是否使用大额单边保证金算法
        """
    @m_eMaxMarginSideAlgorithm.setter
    def m_eMaxMarginSideAlgorithm(self, arg0: EXtMaxMarginSideAlgorithmType) -> None:
        ...
    @property
    def m_eProductClass(self) -> EProductClass:
        """
        合约类型，仅期货和期货期权合约用
        """
    @m_eProductClass.setter
    def m_eProductClass(self, arg0: EProductClass) -> None:
        ...
    @property
    def m_eStockType(self) -> EStockType:
        """
        证券类别
        """
    @m_eStockType.setter
    def m_eStockType(self, arg0: EStockType) -> None:
        ...
    @property
    def m_eSuspendedType(self) -> EXtSuspendedType:
        """
        停牌状态
        """
    @m_eSuspendedType.setter
    def m_eSuspendedType(self, arg0: EXtSuspendedType) -> None:
        ...
    @property
    def m_nCallOrPut(self) -> int:
        """
        合约种类(个股期权：0认购，1认沽)
        """
    @m_nCallOrPut.setter
    def m_nCallOrPut(self, arg0: int) -> None:
        ...
    @property
    def m_nDeliveryMonth(self) -> int:
        """
        交割月
        """
    @m_nDeliveryMonth.setter
    def m_nDeliveryMonth(self, arg0: int) -> None:
        ...
    @property
    def m_nDeliveryYear(self) -> int:
        """
        交割年份
        """
    @m_nDeliveryYear.setter
    def m_nDeliveryYear(self, arg0: int) -> None:
        ...
    @property
    def m_nIsTrading(self) -> int:
        """
        当前是否交易
        """
    @m_nIsTrading.setter
    def m_nIsTrading(self, arg0: int) -> None:
        ...
    @property
    def m_nMaxLimitOrderVolume(self) -> int:
        """
        限价单最大下单量
        """
    @m_nMaxLimitOrderVolume.setter
    def m_nMaxLimitOrderVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nMaxMarketOrderVolume(self) -> int:
        """
        市价单最大下单量
        """
    @m_nMaxMarketOrderVolume.setter
    def m_nMaxMarketOrderVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nMinLimitOrderVolume(self) -> int:
        """
        限价单最小下单量
        """
    @m_nMinLimitOrderVolume.setter
    def m_nMinLimitOrderVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nMinMarketOrderVolume(self) -> int:
        """
        市价单最小下单量
        """
    @m_nMinMarketOrderVolume.setter
    def m_nMinMarketOrderVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nVolumeMultiple(self) -> int:
        """
        合约数量乘数
        """
    @m_nVolumeMultiple.setter
    def m_nVolumeMultiple(self, arg0: int) -> None:
        ...
    @property
    def m_strCreateDate(self) -> str:
        """
        创建日
        """
    @m_strCreateDate.setter
    def m_strCreateDate(self, arg1: str) -> None:
        ...
    @property
    def m_strEndDelivDate(self) -> str:
        """
        结束交割日
        """
    @m_strEndDelivDate.setter
    def m_strEndDelivDate(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易所代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeInstID(self) -> str:
        """
        合约在交易所的代码
        """
    @m_strExchangeInstID.setter
    def m_strExchangeInstID(self, arg1: str) -> None:
        ...
    @property
    def m_strExpireDate(self) -> str:
        """
        到期日
        """
    @m_strExpireDate.setter
    def m_strExpireDate(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentName(self) -> str:
        """
        合约名称
        """
    @m_strInstrumentName.setter
    def m_strInstrumentName(self, arg1: str) -> None:
        ...
    @property
    def m_strOpenDate(self) -> str:
        """
        上市日
        """
    @m_strOpenDate.setter
    def m_strOpenDate(self, arg1: str) -> None:
        ...
    @property
    def m_strOptUndlCode(self) -> str:
        """
        期权标的代码
        """
    @m_strOptUndlCode.setter
    def m_strOptUndlCode(self, arg1: str) -> None:
        ...
    @property
    def m_strOptUndlMarket(self) -> str:
        """
        期权标的市场
        """
    @m_strOptUndlMarket.setter
    def m_strOptUndlMarket(self, arg1: str) -> None:
        ...
    @property
    def m_strProductID(self) -> str:
        """
        品种代码
        """
    @m_strProductID.setter
    def m_strProductID(self, arg1: str) -> None:
        ...
    @property
    def m_strStartDelivDate(self) -> str:
        """
        开始交割日
        """
    @m_strStartDelivDate.setter
    def m_strStartDelivDate(self, arg1: str) -> None:
        ...
class CIntelligentAlgorithmOrder:
    """
    智能算法单下单参数
    """
    def __init__(self) -> None:
        ...
    @property
    def m_bOnlySellAmountUsed(self) -> bool:
        """
        用卖出金额  0,1  换仓特有
        """
    @m_bOnlySellAmountUsed.setter
    def m_bOnlySellAmountUsed(self, arg0: bool) -> None:
        ...
    @property
    def m_dBuySellAmountDeltaPct(self) -> float:
        """
        卖偏差上限0.03-1  换仓特有
        """
    @m_dBuySellAmountDeltaPct.setter
    def m_dBuySellAmountDeltaPct(self, arg0: float) -> None:
        ...
    @property
    def m_dMaxPartRate(self) -> float:
        """
        量比比例, 用户设定, 当MaxPartRate==100%, 表示没有限制
        """
    @m_dMaxPartRate.setter
    def m_dMaxPartRate(self, arg0: float) -> None:
        ...
    @property
    def m_dMinAmountPerOrder(self) -> float:
        """
        委托最小金额
        """
    @m_dMinAmountPerOrder.setter
    def m_dMinAmountPerOrder(self, arg0: float) -> None:
        ...
    @property
    def m_dOrderRateInOpenAcution(self) -> float:
        """
        开盘集合竞价参与比例(取值0-1) 仅开盘+算法有用
        """
    @m_dOrderRateInOpenAcution.setter
    def m_dOrderRateInOpenAcution(self, arg0: float) -> None:
        ...
    @property
    def m_dPrice(self) -> float:
        """
        基准价
        """
    @m_dPrice.setter
    def m_dPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dPriceOffsetBpsForAuction(self) -> int:
        """
        开盘集合竞价价格偏移量(取值0-10000) 仅开盘+算法有用
        """
    @m_dPriceOffsetBpsForAuction.setter
    def m_dPriceOffsetBpsForAuction(self, arg0: int) -> None:
        ...
    @property
    def m_dTriggerPrice(self) -> float:
        """
        触价价格
        """
    @m_dTriggerPrice.setter
    def m_dTriggerPrice(self, arg0: float) -> None:
        ...
    @property
    def m_eCmdDateLimit(self) -> EXTCommandDateLimit:
        """
        指令跨日开关
        """
    @m_eCmdDateLimit.setter
    def m_eCmdDateLimit(self, arg0: EXTCommandDateLimit) -> None:
        ...
    @property
    def m_eHedgeFlag(self) -> EHedgeFlagType:
        """
        套利标志
        """
    @m_eHedgeFlag.setter
    def m_eHedgeFlag(self, arg0: EHedgeFlagType) -> None:
        ...
    @property
    def m_eOperationType(self) -> EOperationType:
        """
        下单操作：买入卖出
        """
    @m_eOperationType.setter
    def m_eOperationType(self, arg0: EOperationType) -> None:
        ...
    @property
    def m_eOrderStrategyType(self) -> EOrderStrategyType:
        """
        算法下单方式
        """
    @m_eOrderStrategyType.setter
    def m_eOrderStrategyType(self, arg0: EOrderStrategyType) -> None:
        ...
    @property
    def m_ePriceType(self) -> EPriceType:
        """
        报价方式：市价和指定价
        """
    @m_ePriceType.setter
    def m_ePriceType(self, arg0: EPriceType) -> None:
        ...
    @property
    def m_eTriggerType(self) -> EOpTriggerType:
        """
        触价类型
        """
    @m_eTriggerType.setter
    def m_eTriggerType(self, arg0: EOpTriggerType) -> None:
        ...
    @property
    def m_eUndealtEntrustRule(self) -> EPriceType:
        """
        未成委托处理
        """
    @m_eUndealtEntrustRule.setter
    def m_eUndealtEntrustRule(self, arg0: EPriceType) -> None:
        ...
    @property
    def m_nLimitedPriceType(self) -> int:
        """
        条件单价格限制类型
        """
    @m_nLimitedPriceType.setter
    def m_nLimitedPriceType(self, arg0: int) -> None:
        ...
    @property
    def m_nMaxTradeDurationAfterET(self) -> int:
        """
        收盘后是否继续执行， 0不继续，非0继续
        """
    @m_nMaxTradeDurationAfterET.setter
    def m_nMaxTradeDurationAfterET(self, arg0: int) -> None:
        ...
    @property
    def m_nOpenTrade(self) -> int:
        """
        开盘集合竞价, 0，不参与，1，参与， 默认0
        """
    @m_nOpenTrade.setter
    def m_nOpenTrade(self, arg0: int) -> None:
        ...
    @property
    def m_nStopTradeForOwnHiLow(self) -> EStopTradeForOwnHiLow:
        """
        涨跌停控制
        """
    @m_nStopTradeForOwnHiLow.setter
    def m_nStopTradeForOwnHiLow(self, arg0: EStopTradeForOwnHiLow) -> None:
        ...
    @property
    def m_nTimeType(self) -> int:
        """
        时间类型，0，按区间，1，按执行时间， 默认0
        """
    @m_nTimeType.setter
    def m_nTimeType(self, arg0: int) -> None:
        ...
    @property
    def m_nTimeValue(self) -> int:
        """
        执行时间
        """
    @m_nTimeValue.setter
    def m_nTimeValue(self, arg0: int) -> None:
        ...
    @property
    def m_nValidTimeEnd(self) -> int:
        """
        有效结束时间 
        """
    @m_nValidTimeEnd.setter
    def m_nValidTimeEnd(self, arg0: int) -> None:
        ...
    @property
    def m_nValidTimeStart(self) -> int:
        """
        有效开始时间 
        """
    @m_nValidTimeStart.setter
    def m_nValidTimeStart(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> int:
        """
        下单总量
        """
    @m_nVolume.setter
    def m_nVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrument(self) -> str:
        """
        合约
        """
    @m_strInstrument.setter
    def m_strInstrument(self, arg1: str) -> None:
        ...
    @property
    def m_strMarket(self) -> str:
        """
        市场
        """
    @m_strMarket.setter
    def m_strMarket(self, arg1: str) -> None:
        ...
    @property
    def m_strOrderType(self) -> str:
        """
        算法名称，VWAP，TWAP，VP，PINLINE，DMA，FLOAT，MSO，SWITCH，ICEBERG，MOC，GRID，VWAPPLUS，MOO，IS，STWAP，SLOS，VPPLUS，XTFAST，SLOH，MOOPLUS，IVWAP，VWAPPLUS2
        """
    @m_strOrderType.setter
    def m_strOrderType(self, arg1: str) -> None:
        ...
    @property
    def m_strOtherParam(self) -> str:
        """
        条件单其他参数
        """
    @m_strOtherParam.setter
    def m_strOtherParam(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark1(self) -> str:
        """
        投资备注1
        """
    @m_strRemark1.setter
    def m_strRemark1(self, arg1: str) -> None:
        ...
    @property
    def m_strStrategyID(self) -> str:
        """
        收益互换策略ID
        """
    @m_strStrategyID.setter
    def m_strStrategyID(self, arg1: str) -> None:
        ...
class CMarginRateDetail:
    """
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dLongMarginRatioByMoney(self) -> float:
        """
        按金额多头保证金率
        """
    @m_dLongMarginRatioByMoney.setter
    def m_dLongMarginRatioByMoney(self, arg0: float) -> None:
        ...
    @property
    def m_dLongMarginRatioByVolume(self) -> float:
        """
        按数量多头保证金费
        """
    @m_dLongMarginRatioByVolume.setter
    def m_dLongMarginRatioByVolume(self, arg0: float) -> None:
        ...
    @property
    def m_dShortMarginRatioByMoney(self) -> float:
        """
        按金额空头保证金率
        """
    @m_dShortMarginRatioByMoney.setter
    def m_dShortMarginRatioByMoney(self, arg0: float) -> None:
        ...
    @property
    def m_dShortMarginRatioByVolume(self) -> float:
        """
        按数量空头保证金费
        """
    @m_dShortMarginRatioByVolume.setter
    def m_dShortMarginRatioByVolume(self, arg0: float) -> None:
        ...
    @property
    def m_nHedgeFlag(self) -> int:
        """
        投机套保标志
        """
    @m_nHedgeFlag.setter
    def m_nHedgeFlag(self, arg0: int) -> None:
        ...
    @property
    def m_nIsRelative(self) -> int:
        """
        是否相对交易所收取
        """
    @m_nIsRelative.setter
    def m_nIsRelative(self, arg0: int) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        市场代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strTradeDate(self) -> str:
        """
        交易日
        """
    @m_strTradeDate.setter
    def m_strTradeDate(self, arg1: str) -> None:
        ...
class CNetValue:
    """
    产品净值信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dAccumulateIncome(self) -> float:
        """
         产品累计盈亏
        """
    @m_dAccumulateIncome.setter
    def m_dAccumulateIncome(self, arg0: float) -> None:
        ...
    @property
    def m_dBNetValue(self) -> float:
        """
        B级基金单位净值
        """
    @m_dBNetValue.setter
    def m_dBNetValue(self, arg0: float) -> None:
        ...
    @property
    def m_dCloseTotalIncome(self) -> float:
        """
         产品收盘盈亏
        """
    @m_dCloseTotalIncome.setter
    def m_dCloseTotalIncome(self, arg0: float) -> None:
        ...
    @property
    def m_dNetValue(self) -> float:
        """
        母基金单位净值
        """
    @m_dNetValue.setter
    def m_dNetValue(self, arg0: float) -> None:
        ...
    @property
    def m_dPrevNetValue(self) -> float:
        """
         前日单位净值
        """
    @m_dPrevNetValue.setter
    def m_dPrevNetValue(self, arg0: float) -> None:
        ...
    @property
    def m_dPrevTotalNetValue(self) -> float:
        """
         前日产品净值
        """
    @m_dPrevTotalNetValue.setter
    def m_dPrevTotalNetValue(self, arg0: float) -> None:
        ...
    @property
    def m_dShare(self) -> float:
        """
        产品份额
        """
    @m_dShare.setter
    def m_dShare(self, arg0: float) -> None:
        ...
    @property
    def m_dTotalIncome(self) -> float:
        """
        当日产品盈亏
        """
    @m_dTotalIncome.setter
    def m_dTotalIncome(self, arg0: float) -> None:
        ...
    @property
    def m_dTotalNetValue(self) -> float:
        """
        产品净资产, 产品净值
        """
    @m_dTotalNetValue.setter
    def m_dTotalNetValue(self, arg0: float) -> None:
        ...
    @property
    def m_nProductId(self) -> int:
        """
        迅投产品ID
        """
    @m_nProductId.setter
    def m_nProductId(self, arg0: int) -> None:
        ...
    @property
    def m_nTypes(self) -> int:
        """
        产品类型 1-普通基金 2-分级基金
        """
    @m_nTypes.setter
    def m_nTypes(self, arg0: int) -> None:
        ...
    @property
    def m_nUpdateTime(self) -> int:
        """
        更新时间
        """
    @m_nUpdateTime.setter
    def m_nUpdateTime(self, arg0: int) -> None:
        ...
class CNewPortfolioReq:
    """
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dRawBalance(self) -> float:
        """
        初始资产
        """
    @m_dRawBalance.setter
    def m_dRawBalance(self, arg0: float) -> None:
        ...
    @property
    def m_nProductID(self) -> int:
        """
        产品编号
        """
    @m_nProductID.setter
    def m_nProductID(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strName(self) -> str:
        """
        投资组合名称
        """
    @m_strName.setter
    def m_strName(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
    @property
    def m_strStrategy(self) -> str:
        """
        策略名称
        """
    @m_strStrategy.setter
    def m_strStrategy(self, arg1: str) -> None:
        ...
class COpVolumeReq:
    """
    查询可下单量
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dPrice(self) -> float:
        """
         价格
        """
    @m_dPrice.setter
    def m_dPrice(self, arg0: float) -> None:
        ...
    @property
    def m_eHedgeFlag(self) -> EHedgeFlagType:
        """
         投机 套利 套保
        """
    @m_eHedgeFlag.setter
    def m_eHedgeFlag(self, arg0: EHedgeFlagType) -> None:
        ...
    @property
    def m_eOperationType(self) -> EOperationType:
        """
         下单类型，开、平、买、卖…
        """
    @m_eOperationType.setter
    def m_eOperationType(self, arg0: EOperationType) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
         资金账户ID，如果为子账户，则为子账户ID
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrument(self) -> str:
        """
         委托合约.
        """
    @m_strInstrument.setter
    def m_strInstrument(self, arg1: str) -> None:
        ...
    @property
    def m_strMarket(self) -> str:
        """
         合约市场
        """
    @m_strMarket.setter
    def m_strMarket(self, arg1: str) -> None:
        ...
class COrderDetail:
    """
    委托信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dAveragePrice(self) -> float:
        """
        成交均价
        """
    @m_dAveragePrice.setter
    def m_dAveragePrice(self, arg0: float) -> None:
        ...
    @property
    def m_dFrozenCommission(self) -> float:
        """
        冻结手续费
        """
    @m_dFrozenCommission.setter
    def m_dFrozenCommission(self, arg0: float) -> None:
        ...
    @property
    def m_dFrozenMargin(self) -> float:
        """
        冻结保证金
        """
    @m_dFrozenMargin.setter
    def m_dFrozenMargin(self, arg0: float) -> None:
        ...
    @property
    def m_dLimitPrice(self) -> float:
        """
        限价单的限价，就是报价
        """
    @m_dLimitPrice.setter
    def m_dLimitPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dTradeAmount(self) -> float:
        """
        成交额 期货=均价*量*合约乘数
        """
    @m_dTradeAmount.setter
    def m_dTradeAmount(self, arg0: float) -> None:
        ...
    @property
    def m_eCoveredFlag(self) -> ECoveredFlag:
        """
        备兑标记 '0' - 非备兑，'1' - 备兑
        """
    @m_eCoveredFlag.setter
    def m_eCoveredFlag(self, arg0: ECoveredFlag) -> None:
        ...
    @property
    def m_eEntrustType(self) -> EEntrustTypes:
        """
        委托类别
        """
    @m_eEntrustType.setter
    def m_eEntrustType(self, arg0: EEntrustTypes) -> None:
        ...
    @property
    def m_eHedgeFlag(self) -> EHedgeFlagType:
        """
        投机 套利 套保
        """
    @m_eHedgeFlag.setter
    def m_eHedgeFlag(self, arg0: EHedgeFlagType) -> None:
        ...
    @property
    def m_eOffsetFlag(self) -> EOffsetFlagType:
        """
        期货开平，股票买卖
        """
    @m_eOffsetFlag.setter
    def m_eOffsetFlag(self, arg0: EOffsetFlagType) -> None:
        ...
    @property
    def m_eOrderStatus(self) -> EEntrustStatus:
        """
        委托状态
        """
    @m_eOrderStatus.setter
    def m_eOrderStatus(self, arg0: EEntrustStatus) -> None:
        ...
    @property
    def m_eOrderSubmitStatus(self) -> EEntrustSubmitStatus:
        """
        提交状态，股票里面不需要报单状态
        """
    @m_eOrderSubmitStatus.setter
    def m_eOrderSubmitStatus(self, arg0: EEntrustSubmitStatus) -> None:
        ...
    @property
    def m_nAccountType(self) -> int:
        """
        账号类型
        """
    @m_nAccountType.setter
    def m_nAccountType(self, arg0: int) -> None:
        ...
    @property
    def m_nDirection(self) -> EEntrustBS:
        """
        期货多空，该字段与m_eOffsetFlag一起判断期货的报单类型。股票无用
        """
    @m_nDirection.setter
    def m_nDirection(self, arg0: EEntrustBS) -> None:
        ...
    @property
    def m_nErrorID(self) -> int:
        """
        错误号
        """
    @m_nErrorID.setter
    def m_nErrorID(self, arg0: int) -> None:
        ...
    @property
    def m_nOrderID(self) -> int:
        """
        指令ID
        """
    @m_nOrderID.setter
    def m_nOrderID(self, arg0: int) -> None:
        ...
    @property
    def m_nOrderPriceType(self) -> EBrokerPriceType:
        """
        类型，例如市价单 限价单
        """
    @m_nOrderPriceType.setter
    def m_nOrderPriceType(self, arg0: EBrokerPriceType) -> None:
        ...
    @property
    def m_nTotalVolume(self) -> int:
        """
        当前总委托量
        """
    @m_nTotalVolume.setter
    def m_nTotalVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nTradedVolume(self) -> int:
        """
        已成交量
        """
    @m_nTradedVolume.setter
    def m_nTradedVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strCancelInfo(self) -> str:
        """
        废单信息
        """
    @m_strCancelInfo.setter
    def m_strCancelInfo(self, arg1: str) -> None:
        ...
    @property
    def m_strCombID(self) -> str:
        """
        组合持仓编号，用于解除组合策略
        """
    @m_strCombID.setter
    def m_strCombID(self, arg1: str) -> None:
        ...
    @property
    def m_strErrorMsg(self) -> str:
        """
        错误描述
        """
    @m_strErrorMsg.setter
    def m_strErrorMsg(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易所代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInsertDate(self) -> str:
        """
        日期
        """
    @m_strInsertDate.setter
    def m_strInsertDate(self, arg1: str) -> None:
        ...
    @property
    def m_strInsertTime(self) -> str:
        """
        时间
        """
    @m_strInsertTime.setter
    def m_strInsertTime(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentName(self) -> str:
        """
        合约名称
        """
    @m_strInstrumentName.setter
    def m_strInstrumentName(self, arg1: str) -> None:
        ...
    @property
    def m_strOrderSysID(self) -> str:
        """
        委托号
        """
    @m_strOrderSysID.setter
    def m_strOrderSysID(self, arg1: str) -> None:
        ...
    @property
    def m_strProductID(self) -> str:
        """
        合约品种
        """
    @m_strProductID.setter
    def m_strProductID(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
    @property
    def m_strSecuAccount(self) -> str:
        """
        股东号
        """
    @m_strSecuAccount.setter
    def m_strSecuAccount(self, arg1: str) -> None:
        ...
    @property
    def m_strStrategyID(self) -> str:
        """
        收益互换策略ID
        """
    @m_strStrategyID.setter
    def m_strStrategyID(self, arg1: str) -> None:
        ...
class COrderError:
    """
    指令错误
    """
    def __init__(self) -> None:
        ...
    @property
    def m_nDirection(self) -> EEntrustBS:
        """
        期货多空，该字段与m_eOffsetFlag一起判断期货的报单类型。股票无用
        """
    @m_nDirection.setter
    def m_nDirection(self, arg0: EEntrustBS) -> None:
        ...
    @property
    def m_nErrorID(self) -> int:
        """
        错误号
        """
    @m_nErrorID.setter
    def m_nErrorID(self, arg0: int) -> None:
        ...
    @property
    def m_nHedgeFlag(self) -> EHedgeFlagType:
        """
        投机 套利 套保
        """
    @m_nHedgeFlag.setter
    def m_nHedgeFlag(self, arg0: EHedgeFlagType) -> None:
        ...
    @property
    def m_nOffsetFlag(self) -> EOffsetFlagType:
        """
        操作,开平,买卖,操作
        """
    @m_nOffsetFlag.setter
    def m_nOffsetFlag(self, arg0: EOffsetFlagType) -> None:
        ...
    @property
    def m_nOrderID(self) -> int:
        """
        指令ID
        """
    @m_nOrderID.setter
    def m_nOrderID(self, arg0: int) -> None:
        ...
    @property
    def m_nRequestID(self) -> int:
        """
        请求ID
        """
    @m_nRequestID.setter
    def m_nRequestID(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> int:
        """
        委托量
        """
    @m_nVolume.setter
    def m_nVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strErrorMsg(self) -> str:
        """
        错误描述
        """
    @m_strErrorMsg.setter
    def m_strErrorMsg(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易所代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
class COrderInfo:
    """
    """
    def __init__(self) -> None:
        ...
    @property
    def m_canceler(self) -> str:
        """
        撤销者
        """
    @m_canceler.setter
    def m_canceler(self, arg1: str) -> None:
        ...
    @property
    def m_dMaxPartRate(self) -> float:
        """
        量比比例  仅三方算法指令有值
        """
    @m_dMaxPartRate.setter
    def m_dMaxPartRate(self, arg0: float) -> None:
        ...
    @property
    def m_dMinAmountPerOrder(self) -> float:
        """
        委托最小金额  仅三方算法指令有值
        """
    @m_dMinAmountPerOrder.setter
    def m_dMinAmountPerOrder(self, arg0: float) -> None:
        ...
    @property
    def m_dPrice(self) -> float:
        """
        基准价  仅三方算法指令有值
        """
    @m_dPrice.setter
    def m_dPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dTradedAmount(self) -> float:
        """
        成交金额
        """
    @m_dTradedAmount.setter
    def m_dTradedAmount(self, arg0: float) -> None:
        ...
    @property
    def m_dTradedPrice(self) -> float:
        """
        成交均价
        """
    @m_dTradedPrice.setter
    def m_dTradedPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dTradedVolume(self) -> float:
        """
        成交量
        """
    @m_dTradedVolume.setter
    def m_dTradedVolume(self, arg0: float) -> None:
        ...
    @property
    def m_eBrokerType(self) -> EXTBrokerType:
        """
        账号类型
        """
    @m_eBrokerType.setter
    def m_eBrokerType(self, arg0: EXTBrokerType) -> None:
        ...
    @property
    def m_eOperationType(self) -> EOperationType:
        """
        下单操作：买入卖出  仅三方算法指令有值
        """
    @m_eOperationType.setter
    def m_eOperationType(self, arg0: EOperationType) -> None:
        ...
    @property
    def m_eStatus(self) -> EOrderCommandStatus:
        """
        状态
        """
    @m_eStatus.setter
    def m_eStatus(self, arg0: EOrderCommandStatus) -> None:
        ...
    @property
    def m_endTime(self) -> int:
        """
        结束时间
        """
    @m_endTime.setter
    def m_endTime(self, arg0: int) -> None:
        ...
    @property
    def m_nAccountType(self) -> int:
        """
        账号类型
        """
    @m_nAccountType.setter
    def m_nAccountType(self, arg0: int) -> None:
        ...
    @property
    def m_nCmdSource(self) -> int:
        """
        指令来源
        """
    @m_nCmdSource.setter
    def m_nCmdSource(self, arg0: int) -> None:
        ...
    @property
    def m_nLimitedPriceType(self) -> int:
        """
        条件单价格限制类型
        """
    @m_nLimitedPriceType.setter
    def m_nLimitedPriceType(self, arg0: int) -> None:
        ...
    @property
    def m_nOrderID(self) -> int:
        """
        指令ID
        """
    @m_nOrderID.setter
    def m_nOrderID(self, arg0: int) -> None:
        ...
    @property
    def m_nStopTradeForOwnHiLow(self) -> EStopTradeForOwnHiLow:
        """
        涨跌停控制  仅三方算法指令有值
        """
    @m_nStopTradeForOwnHiLow.setter
    def m_nStopTradeForOwnHiLow(self, arg0: EStopTradeForOwnHiLow) -> None:
        ...
    @property
    def m_nValidTimeEnd(self) -> int:
        """
        有效结束时间  仅三方算法指令有值
        """
    @m_nValidTimeEnd.setter
    def m_nValidTimeEnd(self, arg0: int) -> None:
        ...
    @property
    def m_nValidTimeStart(self) -> int:
        """
        有效开始时间  仅三方算法指令有值
        """
    @m_nValidTimeStart.setter
    def m_nValidTimeStart(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> int:
        """
        下单总量  仅三方算法指令有值
        """
    @m_nVolume.setter
    def m_nVolume(self, arg0: int) -> None:
        ...
    @property
    def m_startTime(self) -> int:
        """
        下达时间
        """
    @m_startTime.setter
    def m_startTime(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        资金账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrument(self) -> str:
        """
        合约  仅三方算法指令有值
        """
    @m_strInstrument.setter
    def m_strInstrument(self, arg1: str) -> None:
        ...
    @property
    def m_strMarket(self) -> str:
        """
        市场  仅三方算法指令有值
        """
    @m_strMarket.setter
    def m_strMarket(self, arg1: str) -> None:
        ...
    @property
    def m_strMsg(self) -> str:
        """
        指令执行信息
        """
    @m_strMsg.setter
    def m_strMsg(self, arg1: str) -> None:
        ...
    @property
    def m_strOrderType(self) -> str:
        """
        算法名称  仅三方算法指令有值
        """
    @m_strOrderType.setter
    def m_strOrderType(self, arg1: str) -> None:
        ...
    @property
    def m_strOtherParam(self) -> str:
        """
        条件单其他参数
        """
    @m_strOtherParam.setter
    def m_strOtherParam(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
class COrderStat:
    """
    指令级成交统计
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dAveragePrice(self) -> float:
        """
        成交均价
        """
    @m_dAveragePrice.setter
    def m_dAveragePrice(self, arg0: float) -> None:
        ...
    @property
    def m_nOrderID(self) -> int:
        """
        指令ID
        """
    @m_nOrderID.setter
    def m_nOrderID(self, arg0: int) -> None:
        ...
    @property
    def m_nTradeNum(self) -> int:
        """
        成交笔数
        """
    @m_nTradeNum.setter
    def m_nTradeNum(self, arg0: int) -> None:
        ...
    @property
    def m_nTradedVolume(self) -> int:
        """
        已成交量
        """
    @m_nTradedVolume.setter
    def m_nTradedVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易所代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
class COrdinaryGroupOrder:
    """
    普通组合单下单参数
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dPrice(self) -> list:
        """
        每只股票的下单价格
        """
    @m_dPrice.setter
    def m_dPrice(self, arg1: list) -> None:
        ...
    @property
    def m_dSuperPrice(self) -> float:
        """
        单笔超价,和m_dSuperPriceRate只用设置一个，优先使用m_dSuperPriceRate
        """
    @m_dSuperPrice.setter
    def m_dSuperPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dSuperPriceRate(self) -> float:
        """
        单笔超价百分比
        """
    @m_dSuperPriceRate.setter
    def m_dSuperPriceRate(self, arg0: float) -> None:
        ...
    @property
    def m_eHedgeFlag(self) -> EHedgeFlagType:
        """
        套利标志
        """
    @m_eHedgeFlag.setter
    def m_eHedgeFlag(self, arg0: EHedgeFlagType) -> None:
        ...
    @property
    def m_eOperationType(self) -> list:
        """
        每只股票的下单类型
        """
    @m_eOperationType.setter
    def m_eOperationType(self, arg1: list) -> None:
        ...
    @property
    def m_eOverFreqOrderMode(self) -> EXtOverFreqOrderMode:
        """
        委托频率过快时的处理方式
        """
    @m_eOverFreqOrderMode.setter
    def m_eOverFreqOrderMode(self, arg0: EXtOverFreqOrderMode) -> None:
        ...
    @property
    def m_ePriceType(self) -> EPriceType:
        """
        报价方式： 指定价，最新价 对手价……
        """
    @m_ePriceType.setter
    def m_ePriceType(self, arg0: EPriceType) -> None:
        ...
    @property
    def m_eTimeCondition(self) -> ETimeCondition:
        """
        期货条件单时间条件
        """
    @m_eTimeCondition.setter
    def m_eTimeCondition(self, arg0: ETimeCondition) -> None:
        ...
    @property
    def m_eVolumeCondition(self) -> EVolumeCondition:
        """
        期货条件单数量条件
        """
    @m_eVolumeCondition.setter
    def m_eVolumeCondition(self, arg0: EVolumeCondition) -> None:
        ...
    @property
    def m_nLimitedPriceType(self) -> int:
        """
        条件单价格限制类型
        """
    @m_nLimitedPriceType.setter
    def m_nLimitedPriceType(self, arg0: int) -> None:
        ...
    @property
    def m_nOrderNum(self) -> int:
        """
        股票只数
        """
    @m_nOrderNum.setter
    def m_nOrderNum(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> list:
        """
        每只股票的下单量
        """
    @m_nVolume.setter
    def m_nVolume(self, arg1: list) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        资金账户ID，如果为子账户，则为子账户ID
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> list:
        """
        每个合约的下单资金账号Key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: list) -> None:
        ...
    @property
    def m_strInstrument(self) -> list:
        """
        证券代码
        """
    @m_strInstrument.setter
    def m_strInstrument(self, arg1: list) -> None:
        ...
    @property
    def m_strMarket(self) -> list:
        """
        市场列表
        """
    @m_strMarket.setter
    def m_strMarket(self, arg1: list) -> None:
        ...
    @property
    def m_strOtherParam(self) -> str:
        """
        条件单其他参数
        """
    @m_strOtherParam.setter
    def m_strOtherParam(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
    @property
    def m_strStrategyID(self) -> str:
        """
        收益互换策略ID
        """
    @m_strStrategyID.setter
    def m_strStrategyID(self, arg1: str) -> None:
        ...
class COrdinaryOrder:
    """
    普通单下单参数
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dOccurBalance(self) -> float:
        """
        直接还款的金额, 仅直接还款用
        """
    @m_dOccurBalance.setter
    def m_dOccurBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dPrice(self) -> float:
        """
        指定价，仅在报价方式为PRTP_FIX(指定价)时有效;
        """
    @m_dPrice.setter
    def m_dPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dSecondPrice(self) -> float:
        """
        期权组合委托价
        """
    @m_dSecondPrice.setter
    def m_dSecondPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dSuperPrice(self) -> float:
        """
        单笔超价,和m_dSuperPriceRate只用设置一个，优先使用m_dSuperPriceRate
        """
    @m_dSuperPrice.setter
    def m_dSuperPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dSuperPriceRate(self) -> float:
        """
        单笔超价百分比
        """
    @m_dSuperPriceRate.setter
    def m_dSuperPriceRate(self, arg0: float) -> None:
        ...
    @property
    def m_dTriggerPrice(self) -> float:
        """
        触价价格
        """
    @m_dTriggerPrice.setter
    def m_dTriggerPrice(self, arg0: float) -> None:
        ...
    @property
    def m_eAbroadDurationType(self) -> EAbroadDurationType:
        """
        外盘期货报价类型
        """
    @m_eAbroadDurationType.setter
    def m_eAbroadDurationType(self, arg0: EAbroadDurationType) -> None:
        ...
    @property
    def m_eAdjustOrderNum(self) -> EAdjustOrderNum:
        """
        下单根据可用调整可下单量，仅api直连pb时有效
        """
    @m_eAdjustOrderNum.setter
    def m_eAdjustOrderNum(self, arg0: EAdjustOrderNum) -> None:
        ...
    @property
    def m_eCmdDateLimit(self) -> EXTCommandDateLimit:
        """
        指令跨日开关
        """
    @m_eCmdDateLimit.setter
    def m_eCmdDateLimit(self, arg0: EXTCommandDateLimit) -> None:
        ...
    @property
    def m_eFirstSideFlag(self) -> ESideFlag:
        """
        第一腿合约持仓类型
        """
    @m_eFirstSideFlag.setter
    def m_eFirstSideFlag(self, arg0: ESideFlag) -> None:
        ...
    @property
    def m_eHedgeFlag(self) -> EHedgeFlagType:
        """
        套利标志
        """
    @m_eHedgeFlag.setter
    def m_eHedgeFlag(self, arg0: EHedgeFlagType) -> None:
        ...
    @property
    def m_eOperationType(self) -> EOperationType:
        """
        下单类型，开、平、买、卖…
        """
    @m_eOperationType.setter
    def m_eOperationType(self, arg0: EOperationType) -> None:
        ...
    @property
    def m_ePriceType(self) -> EPriceType:
        """
        报价方式： 指定价，最新价 对手价……
        """
    @m_ePriceType.setter
    def m_ePriceType(self, arg0: EPriceType) -> None:
        ...
    @property
    def m_eSecondSideFlag(self) -> ESideFlag:
        """
        第二腿合约持仓类型
        """
    @m_eSecondSideFlag.setter
    def m_eSecondSideFlag(self, arg0: ESideFlag) -> None:
        ...
    @property
    def m_eTimeCondition(self) -> ETimeCondition:
        """
        期货条件单时间条件
        """
    @m_eTimeCondition.setter
    def m_eTimeCondition(self, arg0: ETimeCondition) -> None:
        ...
    @property
    def m_eTriggerType(self) -> EOpTriggerType:
        """
        触价类型
        """
    @m_eTriggerType.setter
    def m_eTriggerType(self, arg0: EOpTriggerType) -> None:
        ...
    @property
    def m_eVolumeCondition(self) -> EVolumeCondition:
        """
        期货条件单数量条件
        """
    @m_eVolumeCondition.setter
    def m_eVolumeCondition(self, arg0: EVolumeCondition) -> None:
        ...
    @property
    def m_nLimitedPriceType(self) -> int:
        """
        条件单价格限制类型
        """
    @m_nLimitedPriceType.setter
    def m_nLimitedPriceType(self, arg0: int) -> None:
        ...
    @property
    def m_nPortfolioID(self) -> int:
        """
        投组类型编号
        """
    @m_nPortfolioID.setter
    def m_nPortfolioID(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> int:
        """
        委托量, 直接还券的数量
        """
    @m_nVolume.setter
    def m_nVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        资金账户ID，如果为子账户，则为子账户ID
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strCombID(self) -> str:
        """
        组合持仓编号，用于解除组合策略
        """
    @m_strCombID.setter
    def m_strCombID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrument(self) -> str:
        """
        委托合约.
        """
    @m_strInstrument.setter
    def m_strInstrument(self, arg1: str) -> None:
        ...
    @property
    def m_strMarket(self) -> str:
        """
        合约市场
        """
    @m_strMarket.setter
    def m_strMarket(self, arg1: str) -> None:
        ...
    @property
    def m_strOtherParam(self) -> str:
        """
        条件单其他参数
        """
    @m_strOtherParam.setter
    def m_strOtherParam(self, arg1: str) -> None:
        ...
    @property
    def m_strPortfolioName(self) -> str:
        """
        投组组合名称，优先使用m_nPortfolioID
        """
    @m_strPortfolioName.setter
    def m_strPortfolioName(self, arg1: str) -> None:
        ...
    @property
    def m_strPortfolioStrategyName(self) -> str:
        """
        投组策略名称，优先使用m_nPortfolioID
        """
    @m_strPortfolioStrategyName.setter
    def m_strPortfolioStrategyName(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
    @property
    def m_strSecondInstrument(self) -> str:
        """
        期权组合委托合约
        """
    @m_strSecondInstrument.setter
    def m_strSecondInstrument(self, arg1: str) -> None:
        ...
    @property
    def m_strSecuAccount(self) -> str:
        """
        股票多股东时指定下单的股东号
        """
    @m_strSecuAccount.setter
    def m_strSecuAccount(self, arg1: str) -> None:
        ...
    @property
    def m_strStrategyID(self) -> str:
        """
        收益互换策略ID
        """
    @m_strStrategyID.setter
    def m_strStrategyID(self, arg1: str) -> None:
        ...
class CPortfolioInfo:
    """
    投资组合信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dInitBalance(self) -> float:
        """
        初始资产
        """
    @m_dInitBalance.setter
    def m_dInitBalance(self, arg0: float) -> None:
        ...
    @property
    def m_eType(self) -> EPortfolioType:
        """
        投组类型
        """
    @m_eType.setter
    def m_eType(self, arg0: EPortfolioType) -> None:
        ...
    @property
    def m_nCreateDate(self) -> int:
        """
        创建日期
        """
    @m_nCreateDate.setter
    def m_nCreateDate(self, arg0: int) -> None:
        ...
    @property
    def m_nPortfolioID(self) -> int:
        """
        投组类型编号
        """
    @m_nPortfolioID.setter
    def m_nPortfolioID(self, arg0: int) -> None:
        ...
    @property
    def m_nProductID(self) -> int:
        """
        产品编号
        """
    @m_nProductID.setter
    def m_nProductID(self, arg0: int) -> None:
        ...
    @property
    def m_nStatus(self) -> int:
        """
        投资组合停用状态
        """
    @m_nStatus.setter
    def m_nStatus(self, arg0: int) -> None:
        ...
    @property
    def m_nUserId(self) -> int:
        """
        用户编号
        """
    @m_nUserId.setter
    def m_nUserId(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strName(self) -> str:
        """
        投资组合名称
        """
    @m_strName.setter
    def m_strName(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
    @property
    def m_strStrategy(self) -> str:
        """
        策略名称
        """
    @m_strStrategy.setter
    def m_strStrategy(self, arg1: str) -> None:
        ...
class CPortfolioStat:
    """
    投资组合状态信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dAvailable(self) -> float:
        """
        可用资金
        """
    @m_dAvailable.setter
    def m_dAvailable(self, arg0: float) -> None:
        ...
    @property
    def m_dBalance(self) -> float:
        """
        资产
        """
    @m_dBalance.setter
    def m_dBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dCloseProfit(self) -> float:
        """
        平仓盈亏
        """
    @m_dCloseProfit.setter
    def m_dCloseProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dCommission(self) -> float:
        """
        手续费
        """
    @m_dCommission.setter
    def m_dCommission(self, arg0: float) -> None:
        ...
    @property
    def m_dDailyCloseProfit(self) -> float:
        """
        当日盈亏（收）
        """
    @m_dDailyCloseProfit.setter
    def m_dDailyCloseProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dDailyDeposit(self) -> float:
        """
        当日入金
        """
    @m_dDailyDeposit.setter
    def m_dDailyDeposit(self, arg0: float) -> None:
        ...
    @property
    def m_dDailyProfit(self) -> float:
        """
        当日盈亏（结）
        """
    @m_dDailyProfit.setter
    def m_dDailyProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dDailyWithdraw(self) -> float:
        """
        当日出金
        """
    @m_dDailyWithdraw.setter
    def m_dDailyWithdraw(self, arg0: float) -> None:
        ...
    @property
    def m_dDebt(self) -> float:
        """
        总负债
        """
    @m_dDebt.setter
    def m_dDebt(self, arg0: float) -> None:
        ...
    @property
    def m_dDeposit(self) -> float:
        """
        入金
        """
    @m_dDeposit.setter
    def m_dDeposit(self, arg0: float) -> None:
        ...
    @property
    def m_dExpenditure(self) -> float:
        """
        支出
        """
    @m_dExpenditure.setter
    def m_dExpenditure(self, arg0: float) -> None:
        ...
    @property
    def m_dFundBalance(self) -> float:
        """
        现金资产
        """
    @m_dFundBalance.setter
    def m_dFundBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dInitBalance(self) -> float:
        """
        初始资产
        """
    @m_dInitBalance.setter
    def m_dInitBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dNav(self) -> float:
        """
        单位净值
        """
    @m_dNav.setter
    def m_dNav(self, arg0: float) -> None:
        ...
    @property
    def m_dNetAsset(self) -> float:
        """
        净资产
        """
    @m_dNetAsset.setter
    def m_dNetAsset(self, arg0: float) -> None:
        ...
    @property
    def m_dPortfolioProfit(self) -> float:
        """
        组合盈亏
        """
    @m_dPortfolioProfit.setter
    def m_dPortfolioProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dPositionCost(self) -> float:
        """
        持仓成本
        """
    @m_dPositionCost.setter
    def m_dPositionCost(self, arg0: float) -> None:
        ...
    @property
    def m_dPositionProfit(self) -> float:
        """
        持仓盈亏
        """
    @m_dPositionProfit.setter
    def m_dPositionProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dPrevBalance(self) -> float:
        """
        期初权益
        """
    @m_dPrevBalance.setter
    def m_dPrevBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dRevenue(self) -> float:
        """
        收入
        """
    @m_dRevenue.setter
    def m_dRevenue(self, arg0: float) -> None:
        ...
    @property
    def m_dShare(self) -> float:
        """
        份额
        """
    @m_dShare.setter
    def m_dShare(self, arg0: float) -> None:
        ...
    @property
    def m_dUsedMargin(self) -> float:
        """
        已用保证金
        """
    @m_dUsedMargin.setter
    def m_dUsedMargin(self, arg0: float) -> None:
        ...
    @property
    def m_dWithdraw(self) -> float:
        """
        出金
        """
    @m_dWithdraw.setter
    def m_dWithdraw(self, arg0: float) -> None:
        ...
    @property
    def m_nPortfolioID(self) -> int:
        """
        投组类型编号
        """
    @m_nPortfolioID.setter
    def m_nPortfolioID(self, arg0: int) -> None:
        ...
    @property
    def m_strTradeDate(self) -> str:
        """
        交易日期
        """
    @m_strTradeDate.setter
    def m_strTradeDate(self, arg1: str) -> None:
        ...
class CPositionDetail:
    """
    持仓信息
    """
    m_strOpenDate: str
    def __init__(self) -> None:
        ...
    @property
    def m_bIsToday(self) -> bool:
        """
        是否今仓
        """
    @m_bIsToday.setter
    def m_bIsToday(self, arg0: bool) -> None:
        ...
    @property
    def m_dCloseAmount(self) -> float:
        """
        平仓额 等于股票每次卖出的量*卖出价*合约乘数（股票为1）的累加 股票不需要
        """
    @m_dCloseAmount.setter
    def m_dCloseAmount(self, arg0: float) -> None:
        ...
    @property
    def m_dCloseProfit(self) -> float:
        """
        平仓盈亏 平仓额 - 开仓价*平仓量*合约乘数（股票为1） 股票不需要
        """
    @m_dCloseProfit.setter
    def m_dCloseProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dFloatProfit(self) -> float:
        """
        浮动盈亏 当前量*（当前价-开仓价）*合约乘数（股票为1）
        """
    @m_dFloatProfit.setter
    def m_dFloatProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dInstrumentValue(self) -> float:
        """
        合约价值 股票不需要
        """
    @m_dInstrumentValue.setter
    def m_dInstrumentValue(self, arg0: float) -> None:
        ...
    @property
    def m_dLastPrice(self) -> float:
        """
        结算价 对于股票的当前价
        """
    @m_dLastPrice.setter
    def m_dLastPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dLastSettlementPrice(self) -> float:
        """
        最新结算价 股票不需要
        """
    @m_dLastSettlementPrice.setter
    def m_dLastSettlementPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dMargin(self) -> float:
        """
        使用的保证金 历史的直接用ctp的，新的自己用成本价*存量*系数算  股票不需要
        """
    @m_dMargin.setter
    def m_dMargin(self, arg0: float) -> None:
        ...
    @property
    def m_dMarketValue(self) -> float:
        """
        市值 合约价值
        """
    @m_dMarketValue.setter
    def m_dMarketValue(self, arg0: float) -> None:
        ...
    @property
    def m_dOpenCost(self) -> float:
        """
        开仓成本 等于股票的成本价*第一次建仓的量，后续减持不影响，不算手续费 股票不需要
        """
    @m_dOpenCost.setter
    def m_dOpenCost(self, arg0: float) -> None:
        ...
    @property
    def m_dOpenPrice(self) -> float:
        """
        开仓价
        """
    @m_dOpenPrice.setter
    def m_dOpenPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dPositionCost(self) -> float:
        """
        持仓成本 股票不需要
        """
    @m_dPositionCost.setter
    def m_dPositionCost(self, arg0: float) -> None:
        ...
    @property
    def m_dPositionProfit(self) -> float:
        """
        持仓盈亏 股票不需要
        """
    @m_dPositionProfit.setter
    def m_dPositionProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dProfitRate(self) -> float:
        """
        持仓盈亏比例
        """
    @m_dProfitRate.setter
    def m_dProfitRate(self, arg0: float) -> None:
        ...
    @property
    def m_dSettlementPrice(self) -> float:
        """
        结算价 对于股票的当前价
        """
    @m_dSettlementPrice.setter
    def m_dSettlementPrice(self, arg0: float) -> None:
        ...
    @property
    def m_nAccountType(self) -> int:
        """
        账号类型
        """
    @m_nAccountType.setter
    def m_nAccountType(self, arg0: int) -> None:
        ...
    @property
    def m_nCanUseVolume(self) -> int:
        """
        股票的可用数量, 期货不用这个字段
        """
    @m_nCanUseVolume.setter
    def m_nCanUseVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nCloseVolume(self) -> int:
        """
        平仓量 等于股票已经卖掉的 股票不需要
        """
    @m_nCloseVolume.setter
    def m_nCloseVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nCoveredAmount(self) -> int:
        """
        备兑数量
        """
    @m_nCoveredAmount.setter
    def m_nCoveredAmount(self, arg0: int) -> None:
        ...
    @property
    def m_nDirection(self) -> EEntrustBS:
        """
        期货多空，该字段与m_eOffsetFlag一起判断期货的报单类型。股票无用
        """
    @m_nDirection.setter
    def m_nDirection(self, arg0: EEntrustBS) -> None:
        ...
    @property
    def m_nFrozenVolume(self) -> int:
        """
        冻结数量, 期货不用这个字段
        """
    @m_nFrozenVolume.setter
    def m_nFrozenVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nHedgeFlag(self) -> EHedgeFlagType:
        """
        投机 套利 套保
        """
    @m_nHedgeFlag.setter
    def m_nHedgeFlag(self, arg0: EHedgeFlagType) -> None:
        ...
    @property
    def m_nOnRoadVolume(self) -> int:
        """
        股票的在途数量, 期货不用这个字段
        """
    @m_nOnRoadVolume.setter
    def m_nOnRoadVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nOrderID(self) -> int:
        """
        指令ID
        """
    @m_nOrderID.setter
    def m_nOrderID(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> int:
        """
        持仓量 当前拥股
        """
    @m_nVolume.setter
    def m_nVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nYesterdayVolume(self) -> int:
        """
        股票的股份余额, 期货不用这个字段
        """
    @m_nYesterdayVolume.setter
    def m_nYesterdayVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        资金账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        市场代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentName(self) -> str:
        """
        合约名称
        """
    @m_strInstrumentName.setter
    def m_strInstrumentName(self, arg1: str) -> None:
        ...
    @property
    def m_strProductID(self) -> str:
        """
        合约品种
        """
    @m_strProductID.setter
    def m_strProductID(self, arg1: str) -> None:
        ...
    @property
    def m_strSecuAccount(self) -> str:
        """
        股东号
        """
    @m_strSecuAccount.setter
    def m_strSecuAccount(self, arg1: str) -> None:
        ...
    @property
    def m_strStrategyID(self) -> str:
        """
        收益互换策略ID
        """
    @m_strStrategyID.setter
    def m_strStrategyID(self, arg1: str) -> None:
        ...
    @property
    def m_strTradeID(self) -> str:
        """
        最初开仓位的成交编号
        """
    @m_strTradeID.setter
    def m_strTradeID(self, arg1: str) -> None:
        ...
    @property
    def m_strTradingDay(self) -> str:
        """
        交易日
        """
    @m_strTradingDay.setter
    def m_strTradingDay(self, arg1: str) -> None:
        ...
class CPositionStatics:
    """
    持仓统计
    """
    def __init__(self) -> None:
        ...
    @property
    def m_bIsToday(self) -> bool:
        """
        是否今仓
        """
    @m_bIsToday.setter
    def m_bIsToday(self, arg0: bool) -> None:
        ...
    @property
    def m_dAveragePrice(self) -> float:
        """
        算法待找
        """
    @m_dAveragePrice.setter
    def m_dAveragePrice(self, arg0: float) -> None:
        ...
    @property
    def m_dFloatProfit(self) -> float:
        """
        浮动盈亏 detail的汇总
        """
    @m_dFloatProfit.setter
    def m_dFloatProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dFrozenCommission(self) -> float:
        """
        冻结手续费
        """
    @m_dFrozenCommission.setter
    def m_dFrozenCommission(self, arg0: float) -> None:
        ...
    @property
    def m_dFrozenMargin(self) -> float:
        """
        冻结保证金
        """
    @m_dFrozenMargin.setter
    def m_dFrozenMargin(self, arg0: float) -> None:
        ...
    @property
    def m_dInstrumentValue(self) -> float:
        """
        合约价值
        """
    @m_dInstrumentValue.setter
    def m_dInstrumentValue(self, arg0: float) -> None:
        ...
    @property
    def m_dLastPrice(self) -> float:
        """
        最新价
        """
    @m_dLastPrice.setter
    def m_dLastPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dOpenCost(self) -> float:
        """
        非任务平冻结
        """
    @m_dOpenCost.setter
    def m_dOpenCost(self, arg0: float) -> None:
        ...
    @property
    def m_dOpenPrice(self) -> float:
        """
        开仓均价 股票不需要
        """
    @m_dOpenPrice.setter
    def m_dOpenPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dPositionCost(self) -> float:
        """
        持仓成本 detail的汇总
        """
    @m_dPositionCost.setter
    def m_dPositionCost(self, arg0: float) -> None:
        ...
    @property
    def m_dPositionProfit(self) -> float:
        """
        持仓盈亏 detail的汇总
        """
    @m_dPositionProfit.setter
    def m_dPositionProfit(self, arg0: float) -> None:
        ...
    @property
    def m_dProfitRate(self) -> float:
        """
        持仓盈亏比例
        """
    @m_dProfitRate.setter
    def m_dProfitRate(self, arg0: float) -> None:
        ...
    @property
    def m_dReferenceRate(self) -> float:
        """
        汇率
        """
    @m_dReferenceRate.setter
    def m_dReferenceRate(self, arg0: float) -> None:
        ...
    @property
    def m_dSettlementPrice(self) -> float:
        """
        前收盘价
        """
    @m_dSettlementPrice.setter
    def m_dSettlementPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dUsedCommission(self) -> float:
        """
        已使用的手续费
        """
    @m_dUsedCommission.setter
    def m_dUsedCommission(self, arg0: float) -> None:
        ...
    @property
    def m_dUsedMargin(self) -> float:
        """
        已使用保证金
        """
    @m_dUsedMargin.setter
    def m_dUsedMargin(self, arg0: float) -> None:
        ...
    @property
    def m_eSideFlag(self) -> ESideFlag:
        """
        期权合约持仓类型
        """
    @m_eSideFlag.setter
    def m_eSideFlag(self, arg0: ESideFlag) -> None:
        ...
    @property
    def m_nAccountType(self) -> int:
        """
        账号类型
        """
    @m_nAccountType.setter
    def m_nAccountType(self, arg0: int) -> None:
        ...
    @property
    def m_nCanCloseVolume(self) -> int:
        """
        可平
        """
    @m_nCanCloseVolume.setter
    def m_nCanCloseVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nCanUseVolume(self) -> int:
        """
        期货不用这个字段，股票的可用数量
        """
    @m_nCanUseVolume.setter
    def m_nCanUseVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nCancelTimes(self) -> int:
        """
        撤单次数
        """
    @m_nCancelTimes.setter
    def m_nCancelTimes(self, arg0: int) -> None:
        ...
    @property
    def m_nCoveredAmount(self) -> int:
        """
        备兑数量
        """
    @m_nCoveredAmount.setter
    def m_nCoveredAmount(self, arg0: int) -> None:
        ...
    @property
    def m_nDirection(self) -> EEntrustBS:
        """
        期货多空，该字段与m_eOffsetFlag一起判断期货的报单类型。股票无用
        """
    @m_nDirection.setter
    def m_nDirection(self, arg0: EEntrustBS) -> None:
        ...
    @property
    def m_nFrozenVolume(self) -> int:
        """
        期货不用这个字段，冻结数量
        """
    @m_nFrozenVolume.setter
    def m_nFrozenVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nHedgeFlag(self) -> EHedgeFlagType:
        """
        投机 套利 套保
        """
    @m_nHedgeFlag.setter
    def m_nHedgeFlag(self, arg0: EHedgeFlagType) -> None:
        ...
    @property
    def m_nOnRoadVolume(self) -> int:
        """
        期货不用这个字段，股票的在途数量
        """
    @m_nOnRoadVolume.setter
    def m_nOnRoadVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nOpenTimes(self) -> int:
        """
        开仓次数
        """
    @m_nOpenTimes.setter
    def m_nOpenTimes(self, arg0: int) -> None:
        ...
    @property
    def m_nOpenVolume(self) -> int:
        """
        总开仓量 中间平仓不减
        """
    @m_nOpenVolume.setter
    def m_nOpenVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nPortfolioPositionType(self) -> PortfolioPositionType:
        """
        投资组合持仓类型
        """
    @m_nPortfolioPositionType.setter
    def m_nPortfolioPositionType(self, arg0: PortfolioPositionType) -> None:
        ...
    @property
    def m_nPosition(self) -> int:
        """
        持仓 需要
        """
    @m_nPosition.setter
    def m_nPosition(self, arg0: int) -> None:
        ...
    @property
    def m_nYesterdayVolume(self) -> int:
        """
        期货不用这个字段，股票的股份余额
        """
    @m_nYesterdayVolume.setter
    def m_nYesterdayVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        资金账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易所
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strExpireDate(self) -> str:
        """
        到期日/投资组合解禁日
        """
    @m_strExpireDate.setter
    def m_strExpireDate(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentName(self) -> str:
        """
        合约名称
        """
    @m_strInstrumentName.setter
    def m_strInstrumentName(self, arg1: str) -> None:
        ...
    @property
    def m_strProductID(self) -> str:
        """
        合约品种
        """
    @m_strProductID.setter
    def m_strProductID(self, arg1: str) -> None:
        ...
    @property
    def m_strSecuAccount(self) -> str:
        """
        股东号
        """
    @m_strSecuAccount.setter
    def m_strSecuAccount(self, arg1: str) -> None:
        ...
    @property
    def m_strStrategyID(self) -> str:
        """
        收益互换策略ID
        """
    @m_strStrategyID.setter
    def m_strStrategyID(self, arg1: str) -> None:
        ...
class CPriceData:
    """
    行情数据
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dAskPrice1(self) -> float:
        """
        申卖价一
        """
    @m_dAskPrice1.setter
    def m_dAskPrice1(self, arg0: float) -> None:
        ...
    @property
    def m_dAskPrice2(self) -> float:
        """
        申卖价二
        """
    @m_dAskPrice2.setter
    def m_dAskPrice2(self, arg0: float) -> None:
        ...
    @property
    def m_dAskPrice3(self) -> float:
        """
        申卖价三
        """
    @m_dAskPrice3.setter
    def m_dAskPrice3(self, arg0: float) -> None:
        ...
    @property
    def m_dAskPrice4(self) -> float:
        """
        申卖价四
        """
    @m_dAskPrice4.setter
    def m_dAskPrice4(self, arg0: float) -> None:
        ...
    @property
    def m_dAskPrice5(self) -> float:
        """
        申卖价五
        """
    @m_dAskPrice5.setter
    def m_dAskPrice5(self, arg0: float) -> None:
        ...
    @property
    def m_dAveragePrice(self) -> float:
        """
        当日均价
        """
    @m_dAveragePrice.setter
    def m_dAveragePrice(self, arg0: float) -> None:
        ...
    @property
    def m_dBidPrice1(self) -> float:
        """
        申买价一
        """
    @m_dBidPrice1.setter
    def m_dBidPrice1(self, arg0: float) -> None:
        ...
    @property
    def m_dBidPrice2(self) -> float:
        """
        申买价二
        """
    @m_dBidPrice2.setter
    def m_dBidPrice2(self, arg0: float) -> None:
        ...
    @property
    def m_dBidPrice3(self) -> float:
        """
        申买价三
        """
    @m_dBidPrice3.setter
    def m_dBidPrice3(self, arg0: float) -> None:
        ...
    @property
    def m_dBidPrice4(self) -> float:
        """
        申买价四
        """
    @m_dBidPrice4.setter
    def m_dBidPrice4(self, arg0: float) -> None:
        ...
    @property
    def m_dBidPrice5(self) -> float:
        """
        申买价五
        """
    @m_dBidPrice5.setter
    def m_dBidPrice5(self, arg0: float) -> None:
        ...
    @property
    def m_dClosePrice(self) -> float:
        """
        今收盘
        """
    @m_dClosePrice.setter
    def m_dClosePrice(self, arg0: float) -> None:
        ...
    @property
    def m_dCurrDelta(self) -> float:
        """
        今虚实度
        """
    @m_dCurrDelta.setter
    def m_dCurrDelta(self, arg0: float) -> None:
        ...
    @property
    def m_dHighestPrice(self) -> float:
        """
        最高价
        """
    @m_dHighestPrice.setter
    def m_dHighestPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dLastPrice(self) -> float:
        """
        最新价
        """
    @m_dLastPrice.setter
    def m_dLastPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dLowerLimitPrice(self) -> float:
        """
        跌停板价
        """
    @m_dLowerLimitPrice.setter
    def m_dLowerLimitPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dLowestPrice(self) -> float:
        """
        最低价
        """
    @m_dLowestPrice.setter
    def m_dLowestPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dOpenInterest(self) -> float:
        """
        持仓量
        """
    @m_dOpenInterest.setter
    def m_dOpenInterest(self, arg0: float) -> None:
        ...
    @property
    def m_dOpenPrice(self) -> float:
        """
        今开盘
        """
    @m_dOpenPrice.setter
    def m_dOpenPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dPreClosePrice(self) -> float:
        """
        昨收盘
        """
    @m_dPreClosePrice.setter
    def m_dPreClosePrice(self, arg0: float) -> None:
        ...
    @property
    def m_dPreDelta(self) -> float:
        """
        昨虚实度
        """
    @m_dPreDelta.setter
    def m_dPreDelta(self, arg0: float) -> None:
        ...
    @property
    def m_dPreOpenInterest(self) -> float:
        """
        昨持仓量
        """
    @m_dPreOpenInterest.setter
    def m_dPreOpenInterest(self, arg0: float) -> None:
        ...
    @property
    def m_dPrePrice(self) -> float:
        """
        前一次的价格
        """
    @m_dPrePrice.setter
    def m_dPrePrice(self, arg0: float) -> None:
        ...
    @property
    def m_dPreSettlementPrice(self) -> float:
        """
        上次结算价
        """
    @m_dPreSettlementPrice.setter
    def m_dPreSettlementPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dSettlementPrice(self) -> float:
        """
        本次结算价
        """
    @m_dSettlementPrice.setter
    def m_dSettlementPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dTurnover(self) -> float:
        """
        成交金额
        """
    @m_dTurnover.setter
    def m_dTurnover(self, arg0: float) -> None:
        ...
    @property
    def m_dUpDown(self) -> float:
        """
        涨跌
        """
    @m_dUpDown.setter
    def m_dUpDown(self, arg0: float) -> None:
        ...
    @property
    def m_dUpDownRate(self) -> float:
        """
        涨跌幅
        """
    @m_dUpDownRate.setter
    def m_dUpDownRate(self, arg0: float) -> None:
        ...
    @property
    def m_dUpperLimitPrice(self) -> float:
        """
        涨停板价
        """
    @m_dUpperLimitPrice.setter
    def m_dUpperLimitPrice(self, arg0: float) -> None:
        ...
    @property
    def m_nAskVolume1(self) -> int:
        """
        申卖量一
        """
    @m_nAskVolume1.setter
    def m_nAskVolume1(self, arg0: int) -> None:
        ...
    @property
    def m_nAskVolume2(self) -> int:
        """
        申卖量二
        """
    @m_nAskVolume2.setter
    def m_nAskVolume2(self, arg0: int) -> None:
        ...
    @property
    def m_nAskVolume3(self) -> int:
        """
        申卖量三
        """
    @m_nAskVolume3.setter
    def m_nAskVolume3(self, arg0: int) -> None:
        ...
    @property
    def m_nAskVolume4(self) -> int:
        """
        申卖量四
        """
    @m_nAskVolume4.setter
    def m_nAskVolume4(self, arg0: int) -> None:
        ...
    @property
    def m_nAskVolume5(self) -> int:
        """
        申卖量五
        """
    @m_nAskVolume5.setter
    def m_nAskVolume5(self, arg0: int) -> None:
        ...
    @property
    def m_nBidVolume1(self) -> int:
        """
        申买量一
        """
    @m_nBidVolume1.setter
    def m_nBidVolume1(self, arg0: int) -> None:
        ...
    @property
    def m_nBidVolume2(self) -> int:
        """
        申买量二
        """
    @m_nBidVolume2.setter
    def m_nBidVolume2(self, arg0: int) -> None:
        ...
    @property
    def m_nBidVolume3(self) -> int:
        """
        申买量三
        """
    @m_nBidVolume3.setter
    def m_nBidVolume3(self, arg0: int) -> None:
        ...
    @property
    def m_nBidVolume4(self) -> int:
        """
        申买量四
        """
    @m_nBidVolume4.setter
    def m_nBidVolume4(self, arg0: int) -> None:
        ...
    @property
    def m_nBidVolume5(self) -> int:
        """
        申买量五
        """
    @m_nBidVolume5.setter
    def m_nBidVolume5(self, arg0: int) -> None:
        ...
    @property
    def m_nStockStatus(self) -> int:
        """
        股票状态
        """
    @m_nStockStatus.setter
    def m_nStockStatus(self, arg0: int) -> None:
        ...
    @property
    def m_nUpdateMillisec(self) -> int:
        """
        最后修改毫秒
        """
    @m_nUpdateMillisec.setter
    def m_nUpdateMillisec(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> int:
        """
        数量
        """
    @m_nVolume.setter
    def m_nVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易所代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeInstID(self) -> str:
        """
        合约在交易所的代码
        """
    @m_strExchangeInstID.setter
    def m_strExchangeInstID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentName(self) -> str:
        """
        合约名称
        """
    @m_strInstrumentName.setter
    def m_strInstrumentName(self, arg1: str) -> None:
        ...
    @property
    def m_strTradingDay(self) -> str:
        """
        交易日
        """
    @m_strTradingDay.setter
    def m_strTradingDay(self, arg1: str) -> None:
        ...
    @property
    def m_strUpdateTime(self) -> str:
        """
        最后修改时间
        """
    @m_strUpdateTime.setter
    def m_strUpdateTime(self, arg1: str) -> None:
        ...
class CProductData:
    """
    产品信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dAccumulateIncome(self) -> float:
        """
         产品累计盈亏
        """
    @m_dAccumulateIncome.setter
    def m_dAccumulateIncome(self, arg0: float) -> None:
        ...
    @property
    def m_dAvaliableFuture(self) -> float:
        """
         期货帐号的可用资金之和
        """
    @m_dAvaliableFuture.setter
    def m_dAvaliableFuture(self, arg0: float) -> None:
        ...
    @property
    def m_dBalance(self) -> float:
        """
         当前资金余额（期货的动态权益和证券的可用）
        """
    @m_dBalance.setter
    def m_dBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dBalancefuture(self) -> float:
        """
         期货动态权益之和
        """
    @m_dBalancefuture.setter
    def m_dBalancefuture(self, arg0: float) -> None:
        ...
    @property
    def m_dCloseTotalIncome(self) -> float:
        """
         产品收盘盈亏
        """
    @m_dCloseTotalIncome.setter
    def m_dCloseTotalIncome(self, arg0: float) -> None:
        ...
    @property
    def m_dCurrMargin(self) -> float:
        """
         期货账号占用保证金
        """
    @m_dCurrMargin.setter
    def m_dCurrMargin(self, arg0: float) -> None:
        ...
    @property
    def m_dFundValue(self) -> float:
        """
         基金总市值，包括ETF和封闭式基金，期货没有
        """
    @m_dFundValue.setter
    def m_dFundValue(self, arg0: float) -> None:
        ...
    @property
    def m_dGGTStockValue(self) -> float:
        """
         港股市值 （人民币）
        """
    @m_dGGTStockValue.setter
    def m_dGGTStockValue(self, arg0: float) -> None:
        ...
    @property
    def m_dLoanValue(self) -> float:
        """
         债券总市值，期货没有
        """
    @m_dLoanValue.setter
    def m_dLoanValue(self, arg0: float) -> None:
        ...
    @property
    def m_dPreBalance(self) -> float:
        """
         期初资金余额（期货静态权益和证券的资金余额）
        """
    @m_dPreBalance.setter
    def m_dPreBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dPrevNetValue(self) -> float:
        """
         前日单位净值
        """
    @m_dPrevNetValue.setter
    def m_dPrevNetValue(self, arg0: float) -> None:
        ...
    @property
    def m_dPrevTotalNetValue(self) -> float:
        """
         前日产品净值
        """
    @m_dPrevTotalNetValue.setter
    def m_dPrevTotalNetValue(self, arg0: float) -> None:
        ...
    @property
    def m_dRepurchaseValue(self) -> float:
        """
         回购总市值，所有回购，期货没有
        """
    @m_dRepurchaseValue.setter
    def m_dRepurchaseValue(self, arg0: float) -> None:
        ...
    @property
    def m_dShare(self) -> float:
        """
        产品份额
        """
    @m_dShare.setter
    def m_dShare(self, arg0: float) -> None:
        ...
    @property
    def m_dStockValue(self) -> float:
        """
         股票总市值
        """
    @m_dStockValue.setter
    def m_dStockValue(self, arg0: float) -> None:
        ...
    @property
    def m_dTotalDebt(self) -> float:
        """
         总负债
        """
    @m_dTotalDebt.setter
    def m_dTotalDebt(self, arg0: float) -> None:
        ...
    @property
    def m_dTotalIncome(self) -> float:
        """
        当日产品盈亏
        """
    @m_dTotalIncome.setter
    def m_dTotalIncome(self, arg0: float) -> None:
        ...
    @property
    def m_dTotalNetValue(self) -> float:
        """
         产品净资产, 产品净值
        """
    @m_dTotalNetValue.setter
    def m_dTotalNetValue(self, arg0: float) -> None:
        ...
    @property
    def m_nProductId(self) -> int:
        """
         迅投产品ID
        """
    @m_nProductId.setter
    def m_nProductId(self, arg0: int) -> None:
        ...
    @property
    def m_strCreateDate(self) -> str:
        """
         迅投产品创建日期
        """
    @m_strCreateDate.setter
    def m_strCreateDate(self, arg1: str) -> None:
        ...
    @property
    def m_strProductCode(self) -> str:
        """
         迅投产品代码
        """
    @m_strProductCode.setter
    def m_strProductCode(self, arg1: str) -> None:
        ...
    @property
    def m_strProductName(self) -> str:
        """
         迅投产品名称
        """
    @m_strProductName.setter
    def m_strProductName(self, arg1: str) -> None:
        ...
class CQueryBankAmount:
    """
    银证转账银行余额信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dBalance(self) -> float:
        """
         银行余额
        """
    @m_dBalance.setter
    def m_dBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dEnableBalance(self) -> float:
        """
         可转金额
        """
    @m_dEnableBalance.setter
    def m_dEnableBalance(self, arg0: float) -> None:
        ...
    @property
    def m_eMoneyType(self) -> EMoneyType:
        """
         币种
        """
    @m_eMoneyType.setter
    def m_eMoneyType(self, arg0: EMoneyType) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
         资金账户ID，如果为子账户，则为子账户ID
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
         账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strBankAccount(self) -> str:
        """
         银行账号
        """
    @m_strBankAccount.setter
    def m_strBankAccount(self, arg1: str) -> None:
        ...
class CQueryBankInfo:
    """
    银证转账银行信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_eMoneyType(self) -> EMoneyType:
        """
         币种
        """
    @m_eMoneyType.setter
    def m_eMoneyType(self, arg0: EMoneyType) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
         资金账户ID，如果为子账户，则为子账户ID
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
         账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strBankAccount(self) -> str:
        """
         银行账号
        """
    @m_strBankAccount.setter
    def m_strBankAccount(self, arg1: str) -> None:
        ...
    @property
    def m_strBankName(self) -> str:
        """
         银行名称，查询时可不送
        """
    @m_strBankName.setter
    def m_strBankName(self, arg1: str) -> None:
        ...
    @property
    def m_strBankNo(self) -> str:
        """
         银行代码
        """
    @m_strBankNo.setter
    def m_strBankNo(self, arg1: str) -> None:
        ...
class CRandomOrder:
    """
    随机单下单参数
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dPrice(self) -> float:
        """
        基准价
        """
    @m_dPrice.setter
    def m_dPrice(self, arg0: float) -> None:
        ...
    @property
    def m_eOperationType(self) -> EOperationType:
        """
        下单操作：开平、多空……
        """
    @m_eOperationType.setter
    def m_eOperationType(self, arg0: EOperationType) -> None:
        ...
    @property
    def m_ePriceType(self) -> EPriceType:
        """
        报价方式：对手、最新……
        """
    @m_ePriceType.setter
    def m_ePriceType(self, arg0: EPriceType) -> None:
        ...
    @property
    def m_nSingleNumMax(self) -> int:
        """
        单比下单量最大值
        """
    @m_nSingleNumMax.setter
    def m_nSingleNumMax(self, arg0: int) -> None:
        ...
    @property
    def m_nSingleNumMin(self) -> int:
        """
        单比下单量最小值
        """
    @m_nSingleNumMin.setter
    def m_nSingleNumMin(self, arg0: int) -> None:
        ...
    @property
    def m_nValidTimeElapse(self) -> int:
        """
        下单间隔
        """
    @m_nValidTimeElapse.setter
    def m_nValidTimeElapse(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> int:
        """
        下单总量
        """
    @m_nVolume.setter
    def m_nVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrument(self) -> str:
        """
        合约
        """
    @m_strInstrument.setter
    def m_strInstrument(self, arg1: str) -> None:
        ...
    @property
    def m_strMarket(self) -> str:
        """
        市场
        """
    @m_strMarket.setter
    def m_strMarket(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        投资备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
class CReferenceRate:
    """
    汇率信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_bAskReferenceRate(self) -> float:
        """
        卖出参考汇率
        """
    @m_bAskReferenceRate.setter
    def m_bAskReferenceRate(self, arg0: float) -> None:
        ...
    @property
    def m_bAskSettlementRate(self) -> float:
        """
        卖出结算汇率
        """
    @m_bAskSettlementRate.setter
    def m_bAskSettlementRate(self, arg0: float) -> None:
        ...
    @property
    def m_bBidReferenceRate(self) -> float:
        """
        买入参考汇率
        """
    @m_bBidReferenceRate.setter
    def m_bBidReferenceRate(self, arg0: float) -> None:
        ...
    @property
    def m_bBidSettlementRate(self) -> float:
        """
        买入结算汇率
        """
    @m_bBidSettlementRate.setter
    def m_bBidSettlementRate(self, arg0: float) -> None:
        ...
    @property
    def m_bMidReferenceRate(self) -> float:
        """
        参考汇率中间价
        """
    @m_bMidReferenceRate.setter
    def m_bMidReferenceRate(self, arg0: float) -> None:
        ...
    @property
    def m_dDayBuyRiseRate(self) -> float:
        """
        日间买入参考汇率浮动比例
        """
    @m_dDayBuyRiseRate.setter
    def m_dDayBuyRiseRate(self, arg0: float) -> None:
        ...
    @property
    def m_dDaySaleRiseRate(self) -> float:
        """
        日间卖出参考汇率浮动比例
        """
    @m_dDaySaleRiseRate.setter
    def m_dDaySaleRiseRate(self, arg0: float) -> None:
        ...
    @property
    def m_dNightBuyRiseRate(self) -> float:
        """
        夜市买入参考汇率浮动比例
        """
    @m_dNightBuyRiseRate.setter
    def m_dNightBuyRiseRate(self, arg0: float) -> None:
        ...
    @property
    def m_dNightSaleRiseRate(self) -> float:
        """
        日间卖出参考汇率浮动比例
        """
    @m_dNightSaleRiseRate.setter
    def m_dNightSaleRiseRate(self, arg0: float) -> None:
        ...
    @property
    def m_eMoneyType(self) -> EMoneyType:
        """
        币种
        """
    @m_eMoneyType.setter
    def m_eMoneyType(self, arg0: EMoneyType) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        市场代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeName(self) -> str:
        """
        市场名字
        """
    @m_strExchangeName.setter
    def m_strExchangeName(self, arg1: str) -> None:
        ...
class CSecuAccount:
    """
    股东号信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_eMainFlag(self) -> EMainFlag:
        """
        主副标记
        """
    @m_eMainFlag.setter
    def m_eMainFlag(self, arg0: EMainFlag) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        市场代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strSecuAccount(self) -> str:
        """
        股东号
        """
    @m_strSecuAccount.setter
    def m_strSecuAccount(self, arg1: str) -> None:
        ...
class CSecuFundTransferReq:
    """
    资金股份划拨
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dOccurBalance(self) -> float:
        """
         资金划拨金额
        """
    @m_dOccurBalance.setter
    def m_dOccurBalance(self, arg0: float) -> None:
        ...
    @property
    def m_eCredttransType(self) -> ETransTypeCreditFlag:
        """
         股份划拨信用调拨类别
        """
    @m_eCredttransType.setter
    def m_eCredttransType(self, arg0: ETransTypeCreditFlag) -> None:
        ...
    @property
    def m_eTransDirection(self) -> ESecuFundTransDirection:
        """
         划拨方向
        """
    @m_eTransDirection.setter
    def m_eTransDirection(self, arg0: ESecuFundTransDirection) -> None:
        ...
    @property
    def m_nOccurAmount(self) -> int:
        """
         股份划拨数量
        """
    @m_nOccurAmount.setter
    def m_nOccurAmount(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
         资金账户ID，如果为子账户，则为子账户ID
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
         股份划拨市场
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
         股份划拨合约
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
class CStkClosedCompacts:
    """
    已了结负债数据
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dBusinessBalance(self) -> float:
        """
        合约金额
        """
    @m_dBusinessBalance.setter
    def m_dBusinessBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dBusinessFare(self) -> float:
        """
        合约息费
        """
    @m_dBusinessFare.setter
    def m_dBusinessFare(self, arg0: float) -> None:
        ...
    @property
    def m_dEntrustBalance(self) -> float:
        """
        委托金额
        """
    @m_dEntrustBalance.setter
    def m_dEntrustBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dRepaidBalance(self) -> float:
        """
        已还金额
        """
    @m_dRepaidBalance.setter
    def m_dRepaidBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dRepaidFare(self) -> float:
        """
        已还息费
        """
    @m_dRepaidFare.setter
    def m_dRepaidFare(self, arg0: float) -> None:
        ...
    @property
    def m_eCashgroupProp(self) -> EXTCompactBrushSource:
        """
        头寸来源
        """
    @m_eCashgroupProp.setter
    def m_eCashgroupProp(self, arg0: EXTCompactBrushSource) -> None:
        ...
    @property
    def m_eCompactType(self) -> EXTCompactType:
        """
        合约类型
        """
    @m_eCompactType.setter
    def m_eCompactType(self, arg0: EXTCompactType) -> None:
        ...
    @property
    def m_nBusinessVol(self) -> int:
        """
        合约证券数量
        """
    @m_nBusinessVol.setter
    def m_nBusinessVol(self, arg0: int) -> None:
        ...
    @property
    def m_nDateClear(self) -> int:
        """
        了结日期
        """
    @m_nDateClear.setter
    def m_nDateClear(self, arg0: int) -> None:
        ...
    @property
    def m_nEntrustVol(self) -> int:
        """
        委托数量
        """
    @m_nEntrustVol.setter
    def m_nEntrustVol(self, arg0: int) -> None:
        ...
    @property
    def m_nOpenDate(self) -> int:
        """
        开仓日期
        """
    @m_nOpenDate.setter
    def m_nOpenDate(self, arg0: int) -> None:
        ...
    @property
    def m_nRetEndDate(self) -> int:
        """
        到期日
        """
    @m_nRetEndDate.setter
    def m_nRetEndDate(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号ID
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strCompactId(self) -> str:
        """
        合约编号
        """
    @m_strCompactId.setter
    def m_strCompactId(self, arg1: str) -> None:
        ...
    @property
    def m_strEntrustNo(self) -> str:
        """
        委托编号
        """
    @m_strEntrustNo.setter
    def m_strEntrustNo(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易所代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strPositionStr(self) -> str:
        """
        定位串
        """
    @m_strPositionStr.setter
    def m_strPositionStr(self, arg1: str) -> None:
        ...
class CStkCompacts:
    """
    两融负债信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dBusinessBalance(self) -> float:
        """
        合约开仓金额
        """
    @m_dBusinessBalance.setter
    def m_dBusinessBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dBusinessFare(self) -> float:
        """
        合约开仓费用
        """
    @m_dBusinessFare.setter
    def m_dBusinessFare(self, arg0: float) -> None:
        ...
    @property
    def m_dCompactInterest(self) -> float:
        """
        合约总利息
        """
    @m_dCompactInterest.setter
    def m_dCompactInterest(self, arg0: float) -> None:
        ...
    @property
    def m_dCrdtRatio(self) -> float:
        """
        融资融券保证金比例
        """
    @m_dCrdtRatio.setter
    def m_dCrdtRatio(self, arg0: float) -> None:
        ...
    @property
    def m_dEntrustPrice(self) -> float:
        """
        委托价格
        """
    @m_dEntrustPrice.setter
    def m_dEntrustPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dPrice(self) -> float:
        """
        最新价
        """
    @m_dPrice.setter
    def m_dPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dRealCompactBalance(self) -> float:
        """
        未还合约金额
        """
    @m_dRealCompactBalance.setter
    def m_dRealCompactBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dRealCompactFare(self) -> float:
        """
        未还合约费用
        """
    @m_dRealCompactFare.setter
    def m_dRealCompactFare(self, arg0: float) -> None:
        ...
    @property
    def m_dRealCompactInterest(self) -> float:
        """
        未还合约利息
        """
    @m_dRealCompactInterest.setter
    def m_dRealCompactInterest(self, arg0: float) -> None:
        ...
    @property
    def m_dRepaidBalance(self) -> float:
        """
        已还金额
        """
    @m_dRepaidBalance.setter
    def m_dRepaidBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dRepaidInterest(self) -> float:
        """
        已还利息
        """
    @m_dRepaidInterest.setter
    def m_dRepaidInterest(self, arg0: float) -> None:
        ...
    @property
    def m_dUsedBailBalance(self) -> float:
        """
        占用保证金
        """
    @m_dUsedBailBalance.setter
    def m_dUsedBailBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dYearRate(self) -> float:
        """
        合约年利率
        """
    @m_dYearRate.setter
    def m_dYearRate(self, arg0: float) -> None:
        ...
    @property
    def m_eCompactStatus(self) -> EXTCompactStatus:
        """
        合约状态
        """
    @m_eCompactStatus.setter
    def m_eCompactStatus(self, arg0: EXTCompactStatus) -> None:
        ...
    @property
    def m_eCompactType(self) -> EXTCompactType:
        """
        合约类型
        """
    @m_eCompactType.setter
    def m_eCompactType(self, arg0: EXTCompactType) -> None:
        ...
    @property
    def m_nBusinessVol(self) -> int:
        """
        合约开仓数量
        """
    @m_nBusinessVol.setter
    def m_nBusinessVol(self, arg0: int) -> None:
        ...
    @property
    def m_nCancelVol(self) -> int:
        """
        合约对应的委托的撤单数量
        """
    @m_nCancelVol.setter
    def m_nCancelVol(self, arg0: int) -> None:
        ...
    @property
    def m_nEntrustVol(self) -> int:
        """
        委托数量
        """
    @m_nEntrustVol.setter
    def m_nEntrustVol(self, arg0: int) -> None:
        ...
    @property
    def m_nOffsetFlag(self) -> EOffsetFlagType:
        """
        操作,开平,买卖,操作
        """
    @m_nOffsetFlag.setter
    def m_nOffsetFlag(self, arg0: EOffsetFlagType) -> None:
        ...
    @property
    def m_nOpenDate(self) -> int:
        """
        合约开仓日期
        """
    @m_nOpenDate.setter
    def m_nOpenDate(self, arg0: int) -> None:
        ...
    @property
    def m_nOpenTime(self) -> int:
        """
        开仓的时间，不展示，部分券商可能用的上
        """
    @m_nOpenTime.setter
    def m_nOpenTime(self, arg0: int) -> None:
        ...
    @property
    def m_nOrderPriceType(self) -> EBrokerPriceType:
        """
        类型，例如市价单 限价单
        """
    @m_nOrderPriceType.setter
    def m_nOrderPriceType(self, arg0: EBrokerPriceType) -> None:
        ...
    @property
    def m_nRealCompactVol(self) -> int:
        """
        未还合约数量
        """
    @m_nRealCompactVol.setter
    def m_nRealCompactVol(self, arg0: int) -> None:
        ...
    @property
    def m_nRepaidVol(self) -> int:
        """
        已还数量
        """
    @m_nRepaidVol.setter
    def m_nRepaidVol(self, arg0: int) -> None:
        ...
    @property
    def m_nRetEndDate(self) -> int:
        """
        归还截止日
        """
    @m_nRetEndDate.setter
    def m_nRetEndDate(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strCompactId(self) -> str:
        """
        合约编号
        """
    @m_strCompactId.setter
    def m_strCompactId(self, arg1: str) -> None:
        ...
    @property
    def m_strDateClear(self) -> str:
        """
        了结日期
        """
    @m_strDateClear.setter
    def m_strDateClear(self, arg1: str) -> None:
        ...
    @property
    def m_strEntrustNo(self) -> str:
        """
        委托编号
        """
    @m_strEntrustNo.setter
    def m_strEntrustNo(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易所
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        证券代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
class CStkUnClosedCompacts:
    """
    未了结负债数据
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dBusinessBalance(self) -> float:
        """
        合约金额
        """
    @m_dBusinessBalance.setter
    def m_dBusinessBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dBusinessFare(self) -> float:
        """
        合约息费
        """
    @m_dBusinessFare.setter
    def m_dBusinessFare(self, arg0: float) -> None:
        ...
    @property
    def m_dRealCompactBalance(self) -> float:
        """
        未还合约金额
        """
    @m_dRealCompactBalance.setter
    def m_dRealCompactBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dRealCompactFare(self) -> float:
        """
        未还合约息费
        """
    @m_dRealCompactFare.setter
    def m_dRealCompactFare(self, arg0: float) -> None:
        ...
    @property
    def m_dRepaidBalance(self) -> float:
        """
        已还金额
        """
    @m_dRepaidBalance.setter
    def m_dRepaidBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dRepaidFare(self) -> float:
        """
        已还息费
        """
    @m_dRepaidFare.setter
    def m_dRepaidFare(self, arg0: float) -> None:
        ...
    @property
    def m_eCashgroupProp(self) -> EXTCompactBrushSource:
        """
        头寸来源
        """
    @m_eCashgroupProp.setter
    def m_eCashgroupProp(self, arg0: EXTCompactBrushSource) -> None:
        ...
    @property
    def m_eCompactType(self) -> EXTCompactType:
        """
        合约类型
        """
    @m_eCompactType.setter
    def m_eCompactType(self, arg0: EXTCompactType) -> None:
        ...
    @property
    def m_nBusinessVol(self) -> int:
        """
        合约证券数量
        """
    @m_nBusinessVol.setter
    def m_nBusinessVol(self, arg0: int) -> None:
        ...
    @property
    def m_nOpenDate(self) -> int:
        """
        开仓日期
        """
    @m_nOpenDate.setter
    def m_nOpenDate(self, arg0: int) -> None:
        ...
    @property
    def m_nRealCompactVol(self) -> int:
        """
        未还合约数量
        """
    @m_nRealCompactVol.setter
    def m_nRealCompactVol(self, arg0: int) -> None:
        ...
    @property
    def m_nRepayPriority(self) -> int:
        """
        偿还优先级
        """
    @m_nRepayPriority.setter
    def m_nRepayPriority(self, arg0: int) -> None:
        ...
    @property
    def m_nRetEndDate(self) -> int:
        """
        到期日
        """
    @m_nRetEndDate.setter
    def m_nRetEndDate(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号ID
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strCompactId(self) -> str:
        """
        合约编号
        """
    @m_strCompactId.setter
    def m_strCompactId(self, arg1: str) -> None:
        ...
    @property
    def m_strEntrustNo(self) -> str:
        """
        委托编号
        """
    @m_strEntrustNo.setter
    def m_strEntrustNo(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易所代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strPositionStr(self) -> str:
        """
        定位串
        """
    @m_strPositionStr.setter
    def m_strPositionStr(self, arg1: str) -> None:
        ...
class CStockComFund:
    """
    普通柜台资金信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dAvailable(self) -> float:
        """
        可用资金
        """
    @m_dAvailable.setter
    def m_dAvailable(self, arg0: float) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
         资金账户ID，如果为子账户，则为子账户ID
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
         账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
class CStockComPosition:
    """
    普通柜台持仓信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_bFast(self) -> bool:
        """
        是否是从极速接口查到的
        """
    @m_bFast.setter
    def m_bFast(self, arg0: bool) -> None:
        ...
    @property
    def m_dCostBalance(self) -> float:
        """
        成本总额
        """
    @m_dCostBalance.setter
    def m_dCostBalance(self, arg0: float) -> None:
        ...
    @property
    def m_dCostPrice(self) -> float:
        """
        成本价
        """
    @m_dCostPrice.setter
    def m_dCostPrice(self, arg0: float) -> None:
        ...
    @property
    def m_dIncome(self) -> float:
        """
        盈亏
        """
    @m_dIncome.setter
    def m_dIncome(self, arg0: float) -> None:
        ...
    @property
    def m_dIncomeRate(self) -> float:
        """
        盈亏比例
        """
    @m_dIncomeRate.setter
    def m_dIncomeRate(self, arg0: float) -> None:
        ...
    @property
    def m_dInstrumentValue(self) -> float:
        """
        市值
        """
    @m_dInstrumentValue.setter
    def m_dInstrumentValue(self, arg0: float) -> None:
        ...
    @property
    def m_dLastPrice(self) -> float:
        """
        最新价
        """
    @m_dLastPrice.setter
    def m_dLastPrice(self, arg0: float) -> None:
        ...
    @property
    def m_nCanUseVolume(self) -> int:
        """
        可用数量
        """
    @m_nCanUseVolume.setter
    def m_nCanUseVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nOnRoadVolume(self) -> int:
        """
        在途量
        """
    @m_nOnRoadVolume.setter
    def m_nOnRoadVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nPREnableVolume(self) -> int:
        """
        申赎可用量
        """
    @m_nPREnableVolume.setter
    def m_nPREnableVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> int:
        """
        持仓量
        """
    @m_nVolume.setter
    def m_nVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
         资金账户ID，如果为子账户，则为子账户ID
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
         账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        市场代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strHandFlag(self) -> str:
        """
        股手标记
        """
    @m_strHandFlag.setter
    def m_strHandFlag(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentName(self) -> str:
        """
        合约名称
        """
    @m_strInstrumentName.setter
    def m_strInstrumentName(self, arg1: str) -> None:
        ...
    @property
    def m_strStockAccount(self) -> str:
        """
        证券账号
        """
    @m_strStockAccount.setter
    def m_strStockAccount(self, arg1: str) -> None:
        ...
class CStockOptionCombPositionDetail:
    """
    股票期权组合策略持仓信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dCombBailBalance(self) -> float:
        """
        占用保证金
        """
    @m_dCombBailBalance.setter
    def m_dCombBailBalance(self, arg0: float) -> None:
        ...
    @property
    def m_eFirstCodePosType(self) -> ESideFlag:
        """
        合约一持仓类型
        """
    @m_eFirstCodePosType.setter
    def m_eFirstCodePosType(self, arg0: ESideFlag) -> None:
        ...
    @property
    def m_eFirstCodeType(self) -> EOptionType:
        """
        合约一类型
        """
    @m_eFirstCodeType.setter
    def m_eFirstCodeType(self, arg0: EOptionType) -> None:
        ...
    @property
    def m_eSecondCodePosType(self) -> ESideFlag:
        """
        合约二持仓类型
        """
    @m_eSecondCodePosType.setter
    def m_eSecondCodePosType(self, arg0: ESideFlag) -> None:
        ...
    @property
    def m_eSecondCodeType(self) -> EOptionType:
        """
        合约二类型
        """
    @m_eSecondCodeType.setter
    def m_eSecondCodeType(self, arg0: EOptionType) -> None:
        ...
    @property
    def m_nCanUseVolume(self) -> int:
        """
        可用数量
        """
    @m_nCanUseVolume.setter
    def m_nCanUseVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nFirstCodeAmt(self) -> int:
        """
        合约一数量
        """
    @m_nFirstCodeAmt.setter
    def m_nFirstCodeAmt(self, arg0: int) -> None:
        ...
    @property
    def m_nFrozenVolume(self) -> int:
        """
        冻结数量
        """
    @m_nFrozenVolume.setter
    def m_nFrozenVolume(self, arg0: int) -> None:
        ...
    @property
    def m_nSecondCodeAmt(self) -> int:
        """
        合约二数量
        """
    @m_nSecondCodeAmt.setter
    def m_nSecondCodeAmt(self, arg0: int) -> None:
        ...
    @property
    def m_nVolume(self) -> int:
        """
        总持仓量
        """
    @m_nVolume.setter
    def m_nVolume(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strCombCode(self) -> str:
        """
        组合策略编码
        """
    @m_strCombCode.setter
    def m_strCombCode(self, arg1: str) -> None:
        ...
    @property
    def m_strCombCodeName(self) -> str:
        """
        组合策略名称
        """
    @m_strCombCodeName.setter
    def m_strCombCodeName(self, arg1: str) -> None:
        ...
    @property
    def m_strCombID(self) -> str:
        """
        组合编号
        """
    @m_strCombID.setter
    def m_strCombID(self, arg1: str) -> None:
        ...
    @property
    def m_strContractAccount(self) -> str:
        """
        合约账号
        """
    @m_strContractAccount.setter
    def m_strContractAccount(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易类别
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeName(self) -> str:
        """
        市场名字
        """
    @m_strExchangeName.setter
    def m_strExchangeName(self, arg1: str) -> None:
        ...
    @property
    def m_strFirstCode(self) -> str:
        """
        合约一
        """
    @m_strFirstCode.setter
    def m_strFirstCode(self, arg1: str) -> None:
        ...
    @property
    def m_strFirstCodeName(self) -> str:
        """
        合约一名称
        """
    @m_strFirstCodeName.setter
    def m_strFirstCodeName(self, arg1: str) -> None:
        ...
    @property
    def m_strSecondCode(self) -> str:
        """
        合约二
        """
    @m_strSecondCode.setter
    def m_strSecondCode(self, arg1: str) -> None:
        ...
    @property
    def m_strSecondCodeName(self) -> str:
        """
        合约二名称
        """
    @m_strSecondCodeName.setter
    def m_strSecondCodeName(self, arg1: str) -> None:
        ...
class CStrategyInfo:
    """
    框架号信息
    """
    def __init__(self) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strStrategyID(self) -> str:
        """
        收益互换策略ID
        """
    @m_strStrategyID.setter
    def m_strStrategyID(self, arg1: str) -> None:
        ...
    @property
    def m_strstrategyName(self) -> str:
        """
        策略名称
        """
    @m_strstrategyName.setter
    def m_strstrategyName(self, arg1: str) -> None:
        ...
class CSubscribData:
    """
    订阅行情请求
    """
    def __init__(self) -> None:
        ...
    @property
    def m_eOfferStatus(self) -> EXTOfferStatus:
        """
        报盘状态
        """
    @m_eOfferStatus.setter
    def m_eOfferStatus(self, arg0: EXTOfferStatus) -> None:
        ...
    @property
    def m_nPlatformID(self) -> int:
        """
        平台ID
        """
    @m_nPlatformID.setter
    def m_nPlatformID(self, arg0: int) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        市场代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码,当其值为allCode时，订阅整个市场
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
class CSubscribeInfo:
    """
    新股额度数据
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dPurchaseAmount(self) -> int:
        """
        申购额度
        """
    @m_dPurchaseAmount.setter
    def m_dPurchaseAmount(self, arg0: int) -> None:
        ...
    @property
    def m_dTechPurchaseAmount(self) -> int:
        """
        创板可申购额度
        """
    @m_dTechPurchaseAmount.setter
    def m_dTechPurchaseAmount(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        账号ID
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strExchangeID(self) -> str:
        """
        交易所代码
        """
    @m_strExchangeID.setter
    def m_strExchangeID(self, arg1: str) -> None:
        ...
    @property
    def m_strInstrumentID(self) -> str:
        """
        合约代码
        """
    @m_strInstrumentID.setter
    def m_strInstrumentID(self, arg1: str) -> None:
        ...
class CTaskOpRecord:
    """
    """
    def __init__(self) -> None:
        ...
    @property
    def m_eOperator(self) -> ETaskFlowOperation:
        """
        任务操作
        """
    @m_eOperator.setter
    def m_eOperator(self, arg0: ETaskFlowOperation) -> None:
        ...
    @property
    def m_nCmdId(self) -> int:
        """
        指令ID
        """
    @m_nCmdId.setter
    def m_nCmdId(self, arg0: int) -> None:
        ...
    @property
    def m_strReason(self) -> str:
        """
        操作原因
        """
    @m_strReason.setter
    def m_strReason(self, arg1: str) -> None:
        ...
class CTransferReq:
    """
    银证转账
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dOccurBalance(self) -> float:
        """
         转账金额
        """
    @m_dOccurBalance.setter
    def m_dOccurBalance(self, arg0: float) -> None:
        ...
    @property
    def m_eMoneyType(self) -> EMoneyType:
        """
         币种
        """
    @m_eMoneyType.setter
    def m_eMoneyType(self, arg0: EMoneyType) -> None:
        ...
    @property
    def m_eTransDirection(self) -> ETransDirection:
        """
         银证转账方向
        """
    @m_eTransDirection.setter
    def m_eTransDirection(self, arg0: ETransDirection) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
         资金账户ID，如果为子账户，则为子账户ID
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strBankAccount(self) -> str:
        """
         银行账号
        """
    @m_strBankAccount.setter
    def m_strBankAccount(self, arg1: str) -> None:
        ...
    @property
    def m_strBankNo(self) -> str:
        """
         银行代码
        """
    @m_strBankNo.setter
    def m_strBankNo(self, arg1: str) -> None:
        ...
    @property
    def m_strFundPwd(self) -> str:
        """
         资金密码
        """
    @m_strFundPwd.setter
    def m_strFundPwd(self, arg1: str) -> None:
        ...
class CTransferSerial:
    """
    查询银证转账银行流水
    """
    def __init__(self) -> None:
        ...
    @property
    def m_dTransferBalance(self) -> float:
        """
        转账金额
        """
    @m_dTransferBalance.setter
    def m_dTransferBalance(self, arg0: float) -> None:
        ...
    @property
    def m_eMoneyType(self) -> EMoneyType:
        """
        币种
        """
    @m_eMoneyType.setter
    def m_eMoneyType(self, arg0: EMoneyType) -> None:
        ...
    @property
    def m_eTransDirection(self) -> ETransDirection:
        """
        转账方向
        """
    @m_eTransDirection.setter
    def m_eTransDirection(self, arg0: ETransDirection) -> None:
        ...
    @property
    def m_nTransferResult(self) -> int:
        """
        申赎可用量
        """
    @m_nTransferResult.setter
    def m_nTransferResult(self, arg0: int) -> None:
        ...
    @property
    def m_strAccountID(self) -> str:
        """
        资金账户ID，如果为子账户，则为子账户ID
        """
    @m_strAccountID.setter
    def m_strAccountID(self, arg1: str) -> None:
        ...
    @property
    def m_strAccountKey(self) -> str:
        """
        账号key
        """
    @m_strAccountKey.setter
    def m_strAccountKey(self, arg1: str) -> None:
        ...
    @property
    def m_strBankAccount(self) -> str:
        """
        银行账号
        """
    @m_strBankAccount.setter
    def m_strBankAccount(self, arg1: str) -> None:
        ...
    @property
    def m_strBankName(self) -> str:
        """
        银行名称
        """
    @m_strBankName.setter
    def m_strBankName(self, arg1: str) -> None:
        ...
    @property
    def m_strBankNo(self) -> str:
        """
        银行代码
        """
    @m_strBankNo.setter
    def m_strBankNo(self, arg1: str) -> None:
        ...
    @property
    def m_strRemark(self) -> str:
        """
        备注
        """
    @m_strRemark.setter
    def m_strRemark(self, arg1: str) -> None:
        ...
    @property
    def m_strTransferDate(self) -> str:
        """
        转账日期
        """
    @m_strTransferDate.setter
    def m_strTransferDate(self, arg1: str) -> None:
        ...
    @property
    def m_strTransferNo(self) -> str:
        """
        流水号
        """
    @m_strTransferNo.setter
    def m_strTransferNo(self, arg1: str) -> None:
        ...
    @property
    def m_strTransferTime(self) -> str:
        """
        转账时间
        """
    @m_strTransferTime.setter
    def m_strTransferTime(self, arg1: str) -> None:
        ...
class CUserConfig:
    """
    用户配置信息
    """
    m_bsonContent: str
    m_nId: int
    m_nMetaId: int
    m_strContent: str
    m_strDescription: str
    m_strUpdateTime: str
    m_strUser: str
    def __init__(self) -> None:
        ...
    @property
    def m_nPermission(self) -> int:
        """
        私人还是全局
        """
    @m_nPermission.setter
    def m_nPermission(self, arg0: int) -> None:
        ...
class EAbroadDurationType:
    """
    外盘期货报单类型
    
    Members:
    
      TYPE_DURATION_MKT : 市价单
    
      TYPE_DURATION_LMT : 限价单
    
      TYPE_DURATION_AO : 竞价单
    
      TYPE_DURATION_ALO : 竞价限价单
    
      TYPE_DURATION_ELO : 增强限价单
    
      TYPE_DURATION_SLO : 特别限价盘单
    
      TYPE_DURATION_OLI : 碎股限价单
    """
    TYPE_DURATION_ALO: typing.ClassVar[EAbroadDurationType]  # value = <EAbroadDurationType.TYPE_DURATION_ALO: 51>
    TYPE_DURATION_AO: typing.ClassVar[EAbroadDurationType]  # value = <EAbroadDurationType.TYPE_DURATION_AO: 50>
    TYPE_DURATION_ELO: typing.ClassVar[EAbroadDurationType]  # value = <EAbroadDurationType.TYPE_DURATION_ELO: 52>
    TYPE_DURATION_LMT: typing.ClassVar[EAbroadDurationType]  # value = <EAbroadDurationType.TYPE_DURATION_LMT: 49>
    TYPE_DURATION_MKT: typing.ClassVar[EAbroadDurationType]  # value = <EAbroadDurationType.TYPE_DURATION_MKT: 48>
    TYPE_DURATION_OLI: typing.ClassVar[EAbroadDurationType]  # value = <EAbroadDurationType.TYPE_DURATION_OLI: 54>
    TYPE_DURATION_SLO: typing.ClassVar[EAbroadDurationType]  # value = <EAbroadDurationType.TYPE_DURATION_SLO: 53>
    __members__: typing.ClassVar[dict[str, EAbroadDurationType]]  # value = {'TYPE_DURATION_MKT': <EAbroadDurationType.TYPE_DURATION_MKT: 48>, 'TYPE_DURATION_LMT': <EAbroadDurationType.TYPE_DURATION_LMT: 49>, 'TYPE_DURATION_AO': <EAbroadDurationType.TYPE_DURATION_AO: 50>, 'TYPE_DURATION_ALO': <EAbroadDurationType.TYPE_DURATION_ALO: 51>, 'TYPE_DURATION_ELO': <EAbroadDurationType.TYPE_DURATION_ELO: 52>, 'TYPE_DURATION_SLO': <EAbroadDurationType.TYPE_DURATION_SLO: 53>, 'TYPE_DURATION_OLI': <EAbroadDurationType.TYPE_DURATION_OLI: 54>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EAdjustOrderNum:
    """
    下单根据可用调整可下单量
    
    Members:
    
      ADJUST_FLAG_OFF : 不允许
    
      ADJUST_FLAG_ON : 允许
    """
    ADJUST_FLAG_OFF: typing.ClassVar[EAdjustOrderNum]  # value = <EAdjustOrderNum.ADJUST_FLAG_OFF: 0>
    ADJUST_FLAG_ON: typing.ClassVar[EAdjustOrderNum]  # value = <EAdjustOrderNum.ADJUST_FLAG_ON: 1>
    __members__: typing.ClassVar[dict[str, EAdjustOrderNum]]  # value = {'ADJUST_FLAG_OFF': <EAdjustOrderNum.ADJUST_FLAG_OFF: 0>, 'ADJUST_FLAG_ON': <EAdjustOrderNum.ADJUST_FLAG_ON: 1>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EAlgoPriceType:
    """
    普通算法订单类型
    
    Members:
    
      EALGO_PRT_MARKET : 市价
    
      EALGO_PRT_FIX : 限价
    """
    EALGO_PRT_FIX: typing.ClassVar[EAlgoPriceType]  # value = <EAlgoPriceType.EALGO_PRT_FIX: 1>
    EALGO_PRT_MARKET: typing.ClassVar[EAlgoPriceType]  # value = <EAlgoPriceType.EALGO_PRT_MARKET: 0>
    __members__: typing.ClassVar[dict[str, EAlgoPriceType]]  # value = {'EALGO_PRT_MARKET': <EAlgoPriceType.EALGO_PRT_MARKET: 0>, 'EALGO_PRT_FIX': <EAlgoPriceType.EALGO_PRT_FIX: 1>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EBrokerLoginStatus:
    """
    账号状态
    
    Members:
    
      BROKER_LOGIN_STATUS_INALID : 
    
      BROKER_LOGIN_STATUS_OK : 可用，初始化完成
    
      BROKER_LOGIN_STATUS_WAITING_LOGIN : 连接中
    
      BROKER_LOGIN_STATUS_LOGINING : 登录中
    
      BROKER_LOGIN_STATUS_FAIL : 失败
    
      BROKER_LOGIN_STATUS_INITING : 在初始化中
    
      BROKER_LOGIN_STATUS_CORRECTING : 数据刷新校正中
    
      BROKER_LOGIN_STATUS_CLOSED : 收盘后
    """
    BROKER_LOGIN_STATUS_CLOSED: typing.ClassVar[EBrokerLoginStatus]  # value = <EBrokerLoginStatus.BROKER_LOGIN_STATUS_CLOSED: 6>
    BROKER_LOGIN_STATUS_CORRECTING: typing.ClassVar[EBrokerLoginStatus]  # value = <EBrokerLoginStatus.BROKER_LOGIN_STATUS_CORRECTING: 5>
    BROKER_LOGIN_STATUS_FAIL: typing.ClassVar[EBrokerLoginStatus]  # value = <EBrokerLoginStatus.BROKER_LOGIN_STATUS_FAIL: 3>
    BROKER_LOGIN_STATUS_INALID: typing.ClassVar[EBrokerLoginStatus]  # value = <EBrokerLoginStatus.BROKER_LOGIN_STATUS_INALID: -1>
    BROKER_LOGIN_STATUS_INITING: typing.ClassVar[EBrokerLoginStatus]  # value = <EBrokerLoginStatus.BROKER_LOGIN_STATUS_INITING: 4>
    BROKER_LOGIN_STATUS_LOGINING: typing.ClassVar[EBrokerLoginStatus]  # value = <EBrokerLoginStatus.BROKER_LOGIN_STATUS_LOGINING: 2>
    BROKER_LOGIN_STATUS_OK: typing.ClassVar[EBrokerLoginStatus]  # value = <EBrokerLoginStatus.BROKER_LOGIN_STATUS_OK: 0>
    BROKER_LOGIN_STATUS_WAITING_LOGIN: typing.ClassVar[EBrokerLoginStatus]  # value = <EBrokerLoginStatus.BROKER_LOGIN_STATUS_WAITING_LOGIN: 1>
    __members__: typing.ClassVar[dict[str, EBrokerLoginStatus]]  # value = {'BROKER_LOGIN_STATUS_INALID': <EBrokerLoginStatus.BROKER_LOGIN_STATUS_INALID: -1>, 'BROKER_LOGIN_STATUS_OK': <EBrokerLoginStatus.BROKER_LOGIN_STATUS_OK: 0>, 'BROKER_LOGIN_STATUS_WAITING_LOGIN': <EBrokerLoginStatus.BROKER_LOGIN_STATUS_WAITING_LOGIN: 1>, 'BROKER_LOGIN_STATUS_LOGINING': <EBrokerLoginStatus.BROKER_LOGIN_STATUS_LOGINING: 2>, 'BROKER_LOGIN_STATUS_FAIL': <EBrokerLoginStatus.BROKER_LOGIN_STATUS_FAIL: 3>, 'BROKER_LOGIN_STATUS_INITING': <EBrokerLoginStatus.BROKER_LOGIN_STATUS_INITING: 4>, 'BROKER_LOGIN_STATUS_CORRECTING': <EBrokerLoginStatus.BROKER_LOGIN_STATUS_CORRECTING: 5>, 'BROKER_LOGIN_STATUS_CLOSED': <EBrokerLoginStatus.BROKER_LOGIN_STATUS_CLOSED: 6>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EBrokerPriceType:
    """
    委托明细价格类型
    
    Members:
    
      BROKER_PRICE_ANY : 市价
    
      BROKER_PRICE_LIMIT : 限价
    
      BROKER_PRICE_BEST : 最优价
    
      BROKER_PRICE_PROP_ALLOTMENT : 配股
    
      BROKER_PRICE_PROP_REFER : 转托
    
      BROKER_PRICE_PROP_SUBSCRIBE : 申购
    
      BROKER_PRICE_PROP_BUYBACK : 回购
    
      BROKER_PRICE_PROP_PLACING : 配售
    
      BROKER_PRICE_PROP_DECIDE : 指定
    
      BROKER_PRICE_PROP_EQUITY : 转股
    
      BROKER_PRICE_PROP_SELLBACK : 回售
    
      BROKER_PRICE_PROP_DIVIDEND : 股息
    
      BROKER_PRICE_PROP_SHENZHEN_PLACING : 深圳配售确认
    
      BROKER_PRICE_PROP_CANCEL_PLACING : 配售放弃
    
      BROKER_PRICE_PROP_WDZY : 无冻质押
    
      BROKER_PRICE_PROP_DJZY : 冻结质押
    
      BROKER_PRICE_PROP_WDJY : 无冻解押
    
      BROKER_PRICE_PROP_JDJY : 解冻解押
    
      BROKER_PRICE_PROP_VOTE : 投票
    
      BROKER_PRICE_PROP_YYSGYS : 要约收购预售
    
      BROKER_PRICE_PROP_YSYYJC : 预售要约解除
    
      BROKER_PRICE_PROP_FUND_DEVIDEND : 基金设红
    
      BROKER_PRICE_PROP_FUND_ENTRUST : 基金申赎
    
      BROKER_PRICE_PROP_CROSS_MARKET : 跨市转托
    
      BROKER_PRICE_PROP_ETF : ETF申购
    
      BROKER_PRICE_PROP_EXERCIS : 权证行权
    
      BROKER_PRICE_PROP_PEER_PRICE_FIRST : 对手方最优价格
    
      BROKER_PRICE_PROP_L5_FIRST_LIMITPX : 最优五档即时成交剩余转限价
    
      BROKER_PRICE_PROP_MIME_PRICE_FIRST : 本方最优价格
    
      BROKER_PRICE_PROP_INSTBUSI_RESTCANCEL : 即时成交剩余撤销
    
      BROKER_PRICE_PROP_L5_FIRST_CANCEL : 最优五档即时成交剩余撤销
    
      BROKER_PRICE_PROP_FULL_REAL_CANCEL : 全额成交并撤单
    
      BROKER_PRICE_PROP_FUND_CHAIHE : 基金拆合
    
      BROKER_PRICE_PROP_DIRECT_SECU_REPAY : 直接还券
    
      BROKER_PRICE_PROP_TIMELY_SECU_REPAY : 即时还券
    
      BROKER_PRICE_PROP_MARKET : 市价_涨跌停价
    
      BROKER_PRICE_PROP_MARKET_BEST : 市价_最优价
    
      BROKER_PRICE_PROP_MARKET_CANCEL : 市价_即成剩撤
    
      BROKER_PRICE_PROP_MARKET_CANCEL_ALL : 市价_全额成交或撤
    
      BROKER_PRICE_PROP_MARKET_CANCEL_1 : 市价_最优1档即成剩撤
    
      BROKER_PRICE_PROP_MARKET_CANCEL_5 : 市价_最优5档即成剩撤
    
      BROKER_PRICE_PROP_MARKET_CONVERT_1 : 市价_最优1档即成剩转
    
      BROKER_PRICE_PROP_MARKET_CONVERT_5 : 市价_最优5档即成剩转
    
      BROKER_PRICE_PROP_STK_OPTION_ASK : 股票期权-询价
    
      BROKER_PRICE_PROP_STK_OPTION_FIX_CANCEL_ALL : 股票期权-限价即时全部成交否则撤单
    
      BROKER_PRICE_PROP_STK_OPTION_MARKET_CACEL_LEFT : 股票期权-市价即时成交剩余撤单
    
      BROKER_PRICE_PROP_STK_OPTION_MARKET_CANCEL_ALL : 股票期权-市价即时全部成交否则撤单
    
      BROKER_PRICE_PROP_STK_OPTION_MARKET_CONVERT_FIX : 股票期权-市价剩余转限价
    
      BROKER_PRICE_PROP_OPTION_COMB_EXERCISE : 股票期权-组合行权
    
      BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_CNSJC : 股票期权-构建认购牛市价差策略
    
      BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_PXSJC : 股票期权-构建认沽熊市价差策略
    
      BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_PNSJC : 股票期权-构建认沽牛市价差策略
    
      BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_CXSJC : 股票期权-构建认购熊市价差策略
    
      BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_KS : 股票期权-构建跨式空头策略
    
      BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_KKS : 股票期权-构建宽跨式空头策略
    
      BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_ZBD : 股票期权-普通转备兑
    
      BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_ZXJ : 股票期权-备兑转普通
    
      BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_CNSJC : 股票期权-解除认购牛市价差策略
    
      BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_PXSJC : 股票期权-解除认沽熊市价差策略
    
      BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_PNSJC : 股票期权-解除认沽牛市价差策略
    
      BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_CXSJC : 股票期权-解除认购熊市价差策略
    
      BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_KS : 股票期权-解除跨式空头策略
    
      BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_KKS : 股票期权-解除宽跨式空头策略
    
      _C_BRPT_COUNT : 
    """
    BROKER_PRICE_ANY: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_ANY: 49>
    BROKER_PRICE_BEST: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_BEST: 51>
    BROKER_PRICE_LIMIT: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_LIMIT: 50>
    BROKER_PRICE_PROP_ALLOTMENT: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_ALLOTMENT: 52>
    BROKER_PRICE_PROP_BUYBACK: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_BUYBACK: 55>
    BROKER_PRICE_PROP_CANCEL_PLACING: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_CANCEL_PLACING: 69>
    BROKER_PRICE_PROP_CROSS_MARKET: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_CROSS_MARKET: 80>
    BROKER_PRICE_PROP_DECIDE: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_DECIDE: 57>
    BROKER_PRICE_PROP_DIRECT_SECU_REPAY: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_DIRECT_SECU_REPAY: 101>
    BROKER_PRICE_PROP_DIVIDEND: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_DIVIDEND: 60>
    BROKER_PRICE_PROP_DJZY: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_DJZY: 71>
    BROKER_PRICE_PROP_EQUITY: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_EQUITY: 58>
    BROKER_PRICE_PROP_ETF: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_ETF: 81>
    BROKER_PRICE_PROP_EXERCIS: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_EXERCIS: 83>
    BROKER_PRICE_PROP_FULL_REAL_CANCEL: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_FULL_REAL_CANCEL: 89>
    BROKER_PRICE_PROP_FUND_CHAIHE: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_FUND_CHAIHE: 90>
    BROKER_PRICE_PROP_FUND_DEVIDEND: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_FUND_DEVIDEND: 78>
    BROKER_PRICE_PROP_FUND_ENTRUST: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_FUND_ENTRUST: 79>
    BROKER_PRICE_PROP_INSTBUSI_RESTCANCEL: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_INSTBUSI_RESTCANCEL: 87>
    BROKER_PRICE_PROP_JDJY: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_JDJY: 73>
    BROKER_PRICE_PROP_L5_FIRST_CANCEL: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_L5_FIRST_CANCEL: 88>
    BROKER_PRICE_PROP_L5_FIRST_LIMITPX: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_L5_FIRST_LIMITPX: 85>
    BROKER_PRICE_PROP_MARKET: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_MARKET: 130>
    BROKER_PRICE_PROP_MARKET_BEST: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_MARKET_BEST: 131>
    BROKER_PRICE_PROP_MARKET_CANCEL: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_MARKET_CANCEL: 132>
    BROKER_PRICE_PROP_MARKET_CANCEL_1: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_MARKET_CANCEL_1: 134>
    BROKER_PRICE_PROP_MARKET_CANCEL_5: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_MARKET_CANCEL_5: 135>
    BROKER_PRICE_PROP_MARKET_CANCEL_ALL: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_MARKET_CANCEL_ALL: 133>
    BROKER_PRICE_PROP_MARKET_CONVERT_1: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_MARKET_CONVERT_1: 136>
    BROKER_PRICE_PROP_MARKET_CONVERT_5: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_MARKET_CONVERT_5: 137>
    BROKER_PRICE_PROP_MIME_PRICE_FIRST: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_MIME_PRICE_FIRST: 86>
    BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_CNSJC: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_CNSJC: 165>
    BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_CXSJC: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_CXSJC: 168>
    BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_KKS: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_KKS: 170>
    BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_KS: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_KS: 169>
    BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_PNSJC: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_PNSJC: 167>
    BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_PXSJC: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_PXSJC: 166>
    BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_ZBD: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_ZBD: 171>
    BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_ZXJ: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_ZXJ: 172>
    BROKER_PRICE_PROP_OPTION_COMB_EXERCISE: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_COMB_EXERCISE: 164>
    BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_CNSJC: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_CNSJC: 173>
    BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_CXSJC: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_CXSJC: 176>
    BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_KKS: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_KKS: 178>
    BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_KS: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_KS: 177>
    BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_PNSJC: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_PNSJC: 175>
    BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_PXSJC: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_PXSJC: 174>
    BROKER_PRICE_PROP_PEER_PRICE_FIRST: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_PEER_PRICE_FIRST: 84>
    BROKER_PRICE_PROP_PLACING: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_PLACING: 56>
    BROKER_PRICE_PROP_REFER: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_REFER: 53>
    BROKER_PRICE_PROP_SELLBACK: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_SELLBACK: 59>
    BROKER_PRICE_PROP_SHENZHEN_PLACING: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_SHENZHEN_PLACING: 68>
    BROKER_PRICE_PROP_STK_OPTION_ASK: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_STK_OPTION_ASK: 138>
    BROKER_PRICE_PROP_STK_OPTION_FIX_CANCEL_ALL: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_STK_OPTION_FIX_CANCEL_ALL: 139>
    BROKER_PRICE_PROP_STK_OPTION_MARKET_CACEL_LEFT: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_STK_OPTION_MARKET_CACEL_LEFT: 140>
    BROKER_PRICE_PROP_STK_OPTION_MARKET_CANCEL_ALL: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_STK_OPTION_MARKET_CANCEL_ALL: 141>
    BROKER_PRICE_PROP_STK_OPTION_MARKET_CONVERT_FIX: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_STK_OPTION_MARKET_CONVERT_FIX: 142>
    BROKER_PRICE_PROP_SUBSCRIBE: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_SUBSCRIBE: 54>
    BROKER_PRICE_PROP_TIMELY_SECU_REPAY: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_TIMELY_SECU_REPAY: 103>
    BROKER_PRICE_PROP_VOTE: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_VOTE: 75>
    BROKER_PRICE_PROP_WDJY: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_WDJY: 72>
    BROKER_PRICE_PROP_WDZY: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_WDZY: 70>
    BROKER_PRICE_PROP_YSYYJC: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_YSYYJC: 77>
    BROKER_PRICE_PROP_YYSGYS: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType.BROKER_PRICE_PROP_YYSGYS: 76>
    _C_BRPT_COUNT: typing.ClassVar[EBrokerPriceType]  # value = <EBrokerPriceType._C_BRPT_COUNT: 179>
    __members__: typing.ClassVar[dict[str, EBrokerPriceType]]  # value = {'BROKER_PRICE_ANY': <EBrokerPriceType.BROKER_PRICE_ANY: 49>, 'BROKER_PRICE_LIMIT': <EBrokerPriceType.BROKER_PRICE_LIMIT: 50>, 'BROKER_PRICE_BEST': <EBrokerPriceType.BROKER_PRICE_BEST: 51>, 'BROKER_PRICE_PROP_ALLOTMENT': <EBrokerPriceType.BROKER_PRICE_PROP_ALLOTMENT: 52>, 'BROKER_PRICE_PROP_REFER': <EBrokerPriceType.BROKER_PRICE_PROP_REFER: 53>, 'BROKER_PRICE_PROP_SUBSCRIBE': <EBrokerPriceType.BROKER_PRICE_PROP_SUBSCRIBE: 54>, 'BROKER_PRICE_PROP_BUYBACK': <EBrokerPriceType.BROKER_PRICE_PROP_BUYBACK: 55>, 'BROKER_PRICE_PROP_PLACING': <EBrokerPriceType.BROKER_PRICE_PROP_PLACING: 56>, 'BROKER_PRICE_PROP_DECIDE': <EBrokerPriceType.BROKER_PRICE_PROP_DECIDE: 57>, 'BROKER_PRICE_PROP_EQUITY': <EBrokerPriceType.BROKER_PRICE_PROP_EQUITY: 58>, 'BROKER_PRICE_PROP_SELLBACK': <EBrokerPriceType.BROKER_PRICE_PROP_SELLBACK: 59>, 'BROKER_PRICE_PROP_DIVIDEND': <EBrokerPriceType.BROKER_PRICE_PROP_DIVIDEND: 60>, 'BROKER_PRICE_PROP_SHENZHEN_PLACING': <EBrokerPriceType.BROKER_PRICE_PROP_SHENZHEN_PLACING: 68>, 'BROKER_PRICE_PROP_CANCEL_PLACING': <EBrokerPriceType.BROKER_PRICE_PROP_CANCEL_PLACING: 69>, 'BROKER_PRICE_PROP_WDZY': <EBrokerPriceType.BROKER_PRICE_PROP_WDZY: 70>, 'BROKER_PRICE_PROP_DJZY': <EBrokerPriceType.BROKER_PRICE_PROP_DJZY: 71>, 'BROKER_PRICE_PROP_WDJY': <EBrokerPriceType.BROKER_PRICE_PROP_WDJY: 72>, 'BROKER_PRICE_PROP_JDJY': <EBrokerPriceType.BROKER_PRICE_PROP_JDJY: 73>, 'BROKER_PRICE_PROP_VOTE': <EBrokerPriceType.BROKER_PRICE_PROP_VOTE: 75>, 'BROKER_PRICE_PROP_YYSGYS': <EBrokerPriceType.BROKER_PRICE_PROP_YYSGYS: 76>, 'BROKER_PRICE_PROP_YSYYJC': <EBrokerPriceType.BROKER_PRICE_PROP_YSYYJC: 77>, 'BROKER_PRICE_PROP_FUND_DEVIDEND': <EBrokerPriceType.BROKER_PRICE_PROP_FUND_DEVIDEND: 78>, 'BROKER_PRICE_PROP_FUND_ENTRUST': <EBrokerPriceType.BROKER_PRICE_PROP_FUND_ENTRUST: 79>, 'BROKER_PRICE_PROP_CROSS_MARKET': <EBrokerPriceType.BROKER_PRICE_PROP_CROSS_MARKET: 80>, 'BROKER_PRICE_PROP_ETF': <EBrokerPriceType.BROKER_PRICE_PROP_ETF: 81>, 'BROKER_PRICE_PROP_EXERCIS': <EBrokerPriceType.BROKER_PRICE_PROP_EXERCIS: 83>, 'BROKER_PRICE_PROP_PEER_PRICE_FIRST': <EBrokerPriceType.BROKER_PRICE_PROP_PEER_PRICE_FIRST: 84>, 'BROKER_PRICE_PROP_L5_FIRST_LIMITPX': <EBrokerPriceType.BROKER_PRICE_PROP_L5_FIRST_LIMITPX: 85>, 'BROKER_PRICE_PROP_MIME_PRICE_FIRST': <EBrokerPriceType.BROKER_PRICE_PROP_MIME_PRICE_FIRST: 86>, 'BROKER_PRICE_PROP_INSTBUSI_RESTCANCEL': <EBrokerPriceType.BROKER_PRICE_PROP_INSTBUSI_RESTCANCEL: 87>, 'BROKER_PRICE_PROP_L5_FIRST_CANCEL': <EBrokerPriceType.BROKER_PRICE_PROP_L5_FIRST_CANCEL: 88>, 'BROKER_PRICE_PROP_FULL_REAL_CANCEL': <EBrokerPriceType.BROKER_PRICE_PROP_FULL_REAL_CANCEL: 89>, 'BROKER_PRICE_PROP_FUND_CHAIHE': <EBrokerPriceType.BROKER_PRICE_PROP_FUND_CHAIHE: 90>, 'BROKER_PRICE_PROP_DIRECT_SECU_REPAY': <EBrokerPriceType.BROKER_PRICE_PROP_DIRECT_SECU_REPAY: 101>, 'BROKER_PRICE_PROP_TIMELY_SECU_REPAY': <EBrokerPriceType.BROKER_PRICE_PROP_TIMELY_SECU_REPAY: 103>, 'BROKER_PRICE_PROP_MARKET': <EBrokerPriceType.BROKER_PRICE_PROP_MARKET: 130>, 'BROKER_PRICE_PROP_MARKET_BEST': <EBrokerPriceType.BROKER_PRICE_PROP_MARKET_BEST: 131>, 'BROKER_PRICE_PROP_MARKET_CANCEL': <EBrokerPriceType.BROKER_PRICE_PROP_MARKET_CANCEL: 132>, 'BROKER_PRICE_PROP_MARKET_CANCEL_ALL': <EBrokerPriceType.BROKER_PRICE_PROP_MARKET_CANCEL_ALL: 133>, 'BROKER_PRICE_PROP_MARKET_CANCEL_1': <EBrokerPriceType.BROKER_PRICE_PROP_MARKET_CANCEL_1: 134>, 'BROKER_PRICE_PROP_MARKET_CANCEL_5': <EBrokerPriceType.BROKER_PRICE_PROP_MARKET_CANCEL_5: 135>, 'BROKER_PRICE_PROP_MARKET_CONVERT_1': <EBrokerPriceType.BROKER_PRICE_PROP_MARKET_CONVERT_1: 136>, 'BROKER_PRICE_PROP_MARKET_CONVERT_5': <EBrokerPriceType.BROKER_PRICE_PROP_MARKET_CONVERT_5: 137>, 'BROKER_PRICE_PROP_STK_OPTION_ASK': <EBrokerPriceType.BROKER_PRICE_PROP_STK_OPTION_ASK: 138>, 'BROKER_PRICE_PROP_STK_OPTION_FIX_CANCEL_ALL': <EBrokerPriceType.BROKER_PRICE_PROP_STK_OPTION_FIX_CANCEL_ALL: 139>, 'BROKER_PRICE_PROP_STK_OPTION_MARKET_CACEL_LEFT': <EBrokerPriceType.BROKER_PRICE_PROP_STK_OPTION_MARKET_CACEL_LEFT: 140>, 'BROKER_PRICE_PROP_STK_OPTION_MARKET_CANCEL_ALL': <EBrokerPriceType.BROKER_PRICE_PROP_STK_OPTION_MARKET_CANCEL_ALL: 141>, 'BROKER_PRICE_PROP_STK_OPTION_MARKET_CONVERT_FIX': <EBrokerPriceType.BROKER_PRICE_PROP_STK_OPTION_MARKET_CONVERT_FIX: 142>, 'BROKER_PRICE_PROP_OPTION_COMB_EXERCISE': <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_COMB_EXERCISE: 164>, 'BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_CNSJC': <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_CNSJC: 165>, 'BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_PXSJC': <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_PXSJC: 166>, 'BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_PNSJC': <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_PNSJC: 167>, 'BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_CXSJC': <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_CXSJC: 168>, 'BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_KS': <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_KS: 169>, 'BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_KKS': <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_KKS: 170>, 'BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_ZBD': <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_ZBD: 171>, 'BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_ZXJ': <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_BUILD_COMB_STRATEGY_ZXJ: 172>, 'BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_CNSJC': <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_CNSJC: 173>, 'BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_PXSJC': <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_PXSJC: 174>, 'BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_PNSJC': <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_PNSJC: 175>, 'BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_CXSJC': <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_CXSJC: 176>, 'BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_KS': <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_KS: 177>, 'BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_KKS': <EBrokerPriceType.BROKER_PRICE_PROP_OPTION_RELEASE_COMB_STRATEGY_KKS: 178>, '_C_BRPT_COUNT': <EBrokerPriceType._C_BRPT_COUNT: 179>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ECoveredFlag:
    """
    备兑标志
    
    Members:
    
      COVERED_FLAG_FALSE : 非备兑
    
      COVERED_FLAG_TRUE : 备兑
    """
    COVERED_FLAG_FALSE: typing.ClassVar[ECoveredFlag]  # value = <ECoveredFlag.COVERED_FLAG_FALSE: 48>
    COVERED_FLAG_TRUE: typing.ClassVar[ECoveredFlag]  # value = <ECoveredFlag.COVERED_FLAG_TRUE: 49>
    __members__: typing.ClassVar[dict[str, ECoveredFlag]]  # value = {'COVERED_FLAG_FALSE': <ECoveredFlag.COVERED_FLAG_FALSE: 48>, 'COVERED_FLAG_TRUE': <ECoveredFlag.COVERED_FLAG_TRUE: 49>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EDualStatus:
    """
    双中心状态
    
    Members:
    
      E_DUAL_STATUS_NONE : 无双中心
    
      E_DUAL_STATUS_SH : 仅有上海
    
      E_DUAL_STATUS_SZ : 仅有深圳
    
      E_DUAL_STATUS_ALL : 上海深圳双中心均有
    """
    E_DUAL_STATUS_ALL: typing.ClassVar[EDualStatus]  # value = <EDualStatus.E_DUAL_STATUS_ALL: 2>
    E_DUAL_STATUS_NONE: typing.ClassVar[EDualStatus]  # value = <EDualStatus.E_DUAL_STATUS_NONE: -1>
    E_DUAL_STATUS_SH: typing.ClassVar[EDualStatus]  # value = <EDualStatus.E_DUAL_STATUS_SH: 0>
    E_DUAL_STATUS_SZ: typing.ClassVar[EDualStatus]  # value = <EDualStatus.E_DUAL_STATUS_SZ: 1>
    __members__: typing.ClassVar[dict[str, EDualStatus]]  # value = {'E_DUAL_STATUS_NONE': <EDualStatus.E_DUAL_STATUS_NONE: -1>, 'E_DUAL_STATUS_SH': <EDualStatus.E_DUAL_STATUS_SH: 0>, 'E_DUAL_STATUS_SZ': <EDualStatus.E_DUAL_STATUS_SZ: 1>, 'E_DUAL_STATUS_ALL': <EDualStatus.E_DUAL_STATUS_ALL: 2>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EEntrustBS:
    """
    买卖方向
    
    Members:
    
      ENTRUST_BUY : 买入
    
      ENTRUST_SELL : 卖出
    
      ENTRUST_COVERED : 备兑
    
      ENTRUST_PLEDGE_IN : 质押入库
    
      ENTRUST_PLEDGE_OUT : 质押出库
    """
    ENTRUST_BUY: typing.ClassVar[EEntrustBS]  # value = <EEntrustBS.ENTRUST_BUY: 48>
    ENTRUST_COVERED: typing.ClassVar[EEntrustBS]  # value = <EEntrustBS.ENTRUST_COVERED: 50>
    ENTRUST_PLEDGE_IN: typing.ClassVar[EEntrustBS]  # value = <EEntrustBS.ENTRUST_PLEDGE_IN: 81>
    ENTRUST_PLEDGE_OUT: typing.ClassVar[EEntrustBS]  # value = <EEntrustBS.ENTRUST_PLEDGE_OUT: 66>
    ENTRUST_SELL: typing.ClassVar[EEntrustBS]  # value = <EEntrustBS.ENTRUST_SELL: 49>
    __members__: typing.ClassVar[dict[str, EEntrustBS]]  # value = {'ENTRUST_BUY': <EEntrustBS.ENTRUST_BUY: 48>, 'ENTRUST_SELL': <EEntrustBS.ENTRUST_SELL: 49>, 'ENTRUST_COVERED': <EEntrustBS.ENTRUST_COVERED: 50>, 'ENTRUST_PLEDGE_IN': <EEntrustBS.ENTRUST_PLEDGE_IN: 81>, 'ENTRUST_PLEDGE_OUT': <EEntrustBS.ENTRUST_PLEDGE_OUT: 66>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EEntrustStatus:
    """
    委托状态
    
    Members:
    
      ENTRUST_STATUS_WAIT_END : 委托状态已经在ENTRUST_STATUS_CANCELED或以上，但是成交数额还不够，等成交回报来
    
      ENTRUST_STATUS_UNREPORTED : 未报
    
      ENTRUST_STATUS_WAIT_REPORTING : 待报
    
      ENTRUST_STATUS_REPORTED : 已报
    
      ENTRUST_STATUS_REPORTED_CANCEL : 已报待撤
    
      ENTRUST_STATUS_PARTSUCC_CANCEL : 部成待撤
    
      ENTRUST_STATUS_PART_CANCEL : 部撤
    
      ENTRUST_STATUS_CANCELED : 已撤
    
      ENTRUST_STATUS_PART_SUCC : 部成
    
      ENTRUST_STATUS_SUCCEEDED : 已成
    
      ENTRUST_STATUS_JUNK : 废单
    
      ENTRUST_STATUS_ACCEPT : 已受理
    
      ENTRUST_STATUS_CONFIRMED : 已确认 担保品划转已确认状态
    
      ENTRUST_STATUS_DETERMINED : 已确认 协议回购已确认状态
    
      ENTRUST_STATUS_PREPARE_ORDER : 预埋
    
      ENTRUST_STATUS_PREPARE_CANCELED : 预埋已撤
    
      ENTRUST_STATUS_UNKNOWN : 未知
    """
    ENTRUST_STATUS_ACCEPT: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_ACCEPT: 58>
    ENTRUST_STATUS_CANCELED: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_CANCELED: 54>
    ENTRUST_STATUS_CONFIRMED: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_CONFIRMED: 59>
    ENTRUST_STATUS_DETERMINED: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_DETERMINED: 86>
    ENTRUST_STATUS_JUNK: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_JUNK: 57>
    ENTRUST_STATUS_PARTSUCC_CANCEL: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_PARTSUCC_CANCEL: 52>
    ENTRUST_STATUS_PART_CANCEL: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_PART_CANCEL: 53>
    ENTRUST_STATUS_PART_SUCC: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_PART_SUCC: 55>
    ENTRUST_STATUS_PREPARE_CANCELED: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_PREPARE_CANCELED: 88>
    ENTRUST_STATUS_PREPARE_ORDER: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_PREPARE_ORDER: 87>
    ENTRUST_STATUS_REPORTED: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_REPORTED: 50>
    ENTRUST_STATUS_REPORTED_CANCEL: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_REPORTED_CANCEL: 51>
    ENTRUST_STATUS_SUCCEEDED: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_SUCCEEDED: 56>
    ENTRUST_STATUS_UNKNOWN: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_UNKNOWN: 255>
    ENTRUST_STATUS_UNREPORTED: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_UNREPORTED: 48>
    ENTRUST_STATUS_WAIT_END: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_WAIT_END: 0>
    ENTRUST_STATUS_WAIT_REPORTING: typing.ClassVar[EEntrustStatus]  # value = <EEntrustStatus.ENTRUST_STATUS_WAIT_REPORTING: 49>
    __members__: typing.ClassVar[dict[str, EEntrustStatus]]  # value = {'ENTRUST_STATUS_WAIT_END': <EEntrustStatus.ENTRUST_STATUS_WAIT_END: 0>, 'ENTRUST_STATUS_UNREPORTED': <EEntrustStatus.ENTRUST_STATUS_UNREPORTED: 48>, 'ENTRUST_STATUS_WAIT_REPORTING': <EEntrustStatus.ENTRUST_STATUS_WAIT_REPORTING: 49>, 'ENTRUST_STATUS_REPORTED': <EEntrustStatus.ENTRUST_STATUS_REPORTED: 50>, 'ENTRUST_STATUS_REPORTED_CANCEL': <EEntrustStatus.ENTRUST_STATUS_REPORTED_CANCEL: 51>, 'ENTRUST_STATUS_PARTSUCC_CANCEL': <EEntrustStatus.ENTRUST_STATUS_PARTSUCC_CANCEL: 52>, 'ENTRUST_STATUS_PART_CANCEL': <EEntrustStatus.ENTRUST_STATUS_PART_CANCEL: 53>, 'ENTRUST_STATUS_CANCELED': <EEntrustStatus.ENTRUST_STATUS_CANCELED: 54>, 'ENTRUST_STATUS_PART_SUCC': <EEntrustStatus.ENTRUST_STATUS_PART_SUCC: 55>, 'ENTRUST_STATUS_SUCCEEDED': <EEntrustStatus.ENTRUST_STATUS_SUCCEEDED: 56>, 'ENTRUST_STATUS_JUNK': <EEntrustStatus.ENTRUST_STATUS_JUNK: 57>, 'ENTRUST_STATUS_ACCEPT': <EEntrustStatus.ENTRUST_STATUS_ACCEPT: 58>, 'ENTRUST_STATUS_CONFIRMED': <EEntrustStatus.ENTRUST_STATUS_CONFIRMED: 59>, 'ENTRUST_STATUS_DETERMINED': <EEntrustStatus.ENTRUST_STATUS_DETERMINED: 86>, 'ENTRUST_STATUS_PREPARE_ORDER': <EEntrustStatus.ENTRUST_STATUS_PREPARE_ORDER: 87>, 'ENTRUST_STATUS_PREPARE_CANCELED': <EEntrustStatus.ENTRUST_STATUS_PREPARE_CANCELED: 88>, 'ENTRUST_STATUS_UNKNOWN': <EEntrustStatus.ENTRUST_STATUS_UNKNOWN: 255>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EEntrustSubmitStatus:
    """
    期货委托发送状态
    
    Members:
    
      ENTRUST_SUBMIT_STATUS_InsertSubmitted : 已经提交
    
      ENTRUST_SUBMIT_STATUS_CancelSubmitted : 撤单已经提交
    
      ENTRUST_SUBMIT_STATUS_ModifySubmitted : 修改已经提交
    
      ENTRUST_SUBMIT_STATUS_OSS_Accepted : 已经接受
    
      ENTRUST_SUBMIT_STATUS_InsertRejected : 报单已经被拒绝
    
      ENTRUST_SUBMIT_STATUS_CancelRejected : 撤单已经被拒绝
    
      ENTRUST_SUBMIT_STATUS_ModifyRejected : 改单已经被拒绝
    """
    ENTRUST_SUBMIT_STATUS_CancelRejected: typing.ClassVar[EEntrustSubmitStatus]  # value = <EEntrustSubmitStatus.ENTRUST_SUBMIT_STATUS_CancelRejected: 53>
    ENTRUST_SUBMIT_STATUS_CancelSubmitted: typing.ClassVar[EEntrustSubmitStatus]  # value = <EEntrustSubmitStatus.ENTRUST_SUBMIT_STATUS_CancelSubmitted: 49>
    ENTRUST_SUBMIT_STATUS_InsertRejected: typing.ClassVar[EEntrustSubmitStatus]  # value = <EEntrustSubmitStatus.ENTRUST_SUBMIT_STATUS_InsertRejected: 52>
    ENTRUST_SUBMIT_STATUS_InsertSubmitted: typing.ClassVar[EEntrustSubmitStatus]  # value = <EEntrustSubmitStatus.ENTRUST_SUBMIT_STATUS_InsertSubmitted: 48>
    ENTRUST_SUBMIT_STATUS_ModifyRejected: typing.ClassVar[EEntrustSubmitStatus]  # value = <EEntrustSubmitStatus.ENTRUST_SUBMIT_STATUS_ModifyRejected: 54>
    ENTRUST_SUBMIT_STATUS_ModifySubmitted: typing.ClassVar[EEntrustSubmitStatus]  # value = <EEntrustSubmitStatus.ENTRUST_SUBMIT_STATUS_ModifySubmitted: 50>
    ENTRUST_SUBMIT_STATUS_OSS_Accepted: typing.ClassVar[EEntrustSubmitStatus]  # value = <EEntrustSubmitStatus.ENTRUST_SUBMIT_STATUS_OSS_Accepted: 51>
    __members__: typing.ClassVar[dict[str, EEntrustSubmitStatus]]  # value = {'ENTRUST_SUBMIT_STATUS_InsertSubmitted': <EEntrustSubmitStatus.ENTRUST_SUBMIT_STATUS_InsertSubmitted: 48>, 'ENTRUST_SUBMIT_STATUS_CancelSubmitted': <EEntrustSubmitStatus.ENTRUST_SUBMIT_STATUS_CancelSubmitted: 49>, 'ENTRUST_SUBMIT_STATUS_ModifySubmitted': <EEntrustSubmitStatus.ENTRUST_SUBMIT_STATUS_ModifySubmitted: 50>, 'ENTRUST_SUBMIT_STATUS_OSS_Accepted': <EEntrustSubmitStatus.ENTRUST_SUBMIT_STATUS_OSS_Accepted: 51>, 'ENTRUST_SUBMIT_STATUS_InsertRejected': <EEntrustSubmitStatus.ENTRUST_SUBMIT_STATUS_InsertRejected: 52>, 'ENTRUST_SUBMIT_STATUS_CancelRejected': <EEntrustSubmitStatus.ENTRUST_SUBMIT_STATUS_CancelRejected: 53>, 'ENTRUST_SUBMIT_STATUS_ModifyRejected': <EEntrustSubmitStatus.ENTRUST_SUBMIT_STATUS_ModifyRejected: 54>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EEntrustTypes:
    """
    委托类型
    
    Members:
    
      ENTRUST_BUY_SELL : 买卖
    
      ENTRUST_QUERY : 查询
    
      ENTRUST_CANCEL : 撤单
    
      ENTRUST_APPEND : 补单
    
      ENTRUST_COMFIRM : 确认
    
      ENTRUST_BIG : 大宗
    
      ENTRUST_FIN : 融资委托
    
      ENTRUST_SLO : 融券委托
    
      ENTRUST_CLOSE : 信用平仓
    
      ENTRUST_CREDIT_NORMAL : 信用普通委托
    
      ENTRUST_CANCEL_OPEN : 撤单补单
    
      ENTRUST_TYPE_OPTION_EXERCISE : 行权
    
      ENTRUST_TYPE_OPTION_SECU_LOCK : 锁定
    
      ENTRUST_TYPE_OPTION_SECU_UNLOCK : 解锁
    
      ENTRUST_TYPE_OPTION_COMB_EXERCISE : 组合行权
    
      ENTRUST_TYPE_OPTION_BUILD_COMB_STRATEGY : 构建组合策略持仓
    
      ENTRUST_TYPE_OPTION_RELEASE_COMB_STRATEGY : 解除组合策略持仓
    """
    ENTRUST_APPEND: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_APPEND: 51>
    ENTRUST_BIG: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_BIG: 53>
    ENTRUST_BUY_SELL: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_BUY_SELL: 48>
    ENTRUST_CANCEL: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_CANCEL: 50>
    ENTRUST_CANCEL_OPEN: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_CANCEL_OPEN: 58>
    ENTRUST_CLOSE: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_CLOSE: 56>
    ENTRUST_COMFIRM: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_COMFIRM: 52>
    ENTRUST_CREDIT_NORMAL: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_CREDIT_NORMAL: 57>
    ENTRUST_FIN: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_FIN: 54>
    ENTRUST_QUERY: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_QUERY: 49>
    ENTRUST_SLO: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_SLO: 55>
    ENTRUST_TYPE_OPTION_BUILD_COMB_STRATEGY: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_TYPE_OPTION_BUILD_COMB_STRATEGY: 66>
    ENTRUST_TYPE_OPTION_COMB_EXERCISE: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_TYPE_OPTION_COMB_EXERCISE: 65>
    ENTRUST_TYPE_OPTION_EXERCISE: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_TYPE_OPTION_EXERCISE: 59>
    ENTRUST_TYPE_OPTION_RELEASE_COMB_STRATEGY: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_TYPE_OPTION_RELEASE_COMB_STRATEGY: 67>
    ENTRUST_TYPE_OPTION_SECU_LOCK: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_TYPE_OPTION_SECU_LOCK: 60>
    ENTRUST_TYPE_OPTION_SECU_UNLOCK: typing.ClassVar[EEntrustTypes]  # value = <EEntrustTypes.ENTRUST_TYPE_OPTION_SECU_UNLOCK: 61>
    __members__: typing.ClassVar[dict[str, EEntrustTypes]]  # value = {'ENTRUST_BUY_SELL': <EEntrustTypes.ENTRUST_BUY_SELL: 48>, 'ENTRUST_QUERY': <EEntrustTypes.ENTRUST_QUERY: 49>, 'ENTRUST_CANCEL': <EEntrustTypes.ENTRUST_CANCEL: 50>, 'ENTRUST_APPEND': <EEntrustTypes.ENTRUST_APPEND: 51>, 'ENTRUST_COMFIRM': <EEntrustTypes.ENTRUST_COMFIRM: 52>, 'ENTRUST_BIG': <EEntrustTypes.ENTRUST_BIG: 53>, 'ENTRUST_FIN': <EEntrustTypes.ENTRUST_FIN: 54>, 'ENTRUST_SLO': <EEntrustTypes.ENTRUST_SLO: 55>, 'ENTRUST_CLOSE': <EEntrustTypes.ENTRUST_CLOSE: 56>, 'ENTRUST_CREDIT_NORMAL': <EEntrustTypes.ENTRUST_CREDIT_NORMAL: 57>, 'ENTRUST_CANCEL_OPEN': <EEntrustTypes.ENTRUST_CANCEL_OPEN: 58>, 'ENTRUST_TYPE_OPTION_EXERCISE': <EEntrustTypes.ENTRUST_TYPE_OPTION_EXERCISE: 59>, 'ENTRUST_TYPE_OPTION_SECU_LOCK': <EEntrustTypes.ENTRUST_TYPE_OPTION_SECU_LOCK: 60>, 'ENTRUST_TYPE_OPTION_SECU_UNLOCK': <EEntrustTypes.ENTRUST_TYPE_OPTION_SECU_UNLOCK: 61>, 'ENTRUST_TYPE_OPTION_COMB_EXERCISE': <EEntrustTypes.ENTRUST_TYPE_OPTION_COMB_EXERCISE: 65>, 'ENTRUST_TYPE_OPTION_BUILD_COMB_STRATEGY': <EEntrustTypes.ENTRUST_TYPE_OPTION_BUILD_COMB_STRATEGY: 66>, 'ENTRUST_TYPE_OPTION_RELEASE_COMB_STRATEGY': <EEntrustTypes.ENTRUST_TYPE_OPTION_RELEASE_COMB_STRATEGY: 67>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EErrorType:
    """
    错误号
    
    Members:
    
      XT_ERROR_SUCCESS : 无错误
    
      XT_ERROR_NET_DISCONNECTED : 未建立连接
    
      XT_ERROR_NOT_LOGINED : 未登录
    
      XT_ERROR_NOT_INITIALIZED : 初始化未完成
    
      XT_ERROR_TIME_OUT : 超时
    
      XT_ERROR_NOT_FIND_ACCOUNT : 未找到账号
    
      XT_ERROR_NOT_FIND_FUNCTION : 未找到处理函数
    
      XT_ERROR_INVALID_PARAM : 参数有误
    
      XT_ERROR_DEFAULT : 默认错误号
    
      XT_ERROR_UNKNOWN : 未知错误
    
      XT_ERROR_REPEAT_LOGIN : 重复登录
    
      XT_ERROR_LOGIN_MD5_NOT_MATCH : md5值不匹配
    
      XT_ERROR_LOGIN_API_VERSINO_TOO_LOW : api版本较低
    
      XT_ERROR_LOGIN_USER_NOT_ALLOWEDLOGIN : 用户不允许登陆
    
      XT_ERROR_CREATECOMMOND_PARAM : 创建指令时，解析参数失败
    
      XT_ERROR_CREATECOMMOND_QUOTE : 创建指令时，获取行情数据失败
    
      XT_ERROR_CREATECOMMOND_PRICE_TYPE : 创建指令时，获取有关报价类型的价格失败（如最新价等）
    
      XT_ERROR_ORDER_FLOW_CONTROL : 下单超过流量控制
    
      XT_ERROR_ORDER_NOT_AUTHORIZE_STOCK_FUTURE : 股票期货业务没有授权
    
      XT_ERROR_ORDER_NOT_AUTHORIZE_STOCKOPTION : 股票期权业务没有授权
    
      XT_ERROR_ORDER_NOT_AUTHORIZE_CREDIT : 信用业务没有授权
    
      XT_ERROR_ORDER_NOT_AUTHORIZE_GOLD : 黄金业务没有授权
    
      XT_ERROR_ORDER_NOT_AUTHORIZE_HGT : 沪港通业务没有授权
    
      XT_ERROR_ORDER_NOT_AUTHORIZE_SGT : 深港通业务没有授权
    
      XT_ERROR_QUERYDATA_FLOW_CONTROL : 请求超过流量控制
    
      XT_ERROR_LOGIN_MAC_NOT_MATCH : mac不匹配
    
      XT_ERROR_LOGIN_MAC_NOT_AUTHORIZE : mac未授权
    
      XT_ERROR_SUBSCRIBE_QUOTE : 订阅行情时报错
    
      XT_ERROR_CREATECOMMOND_TRANSUNABLE : 创建指令时，合约不可交易
    """
    XT_ERROR_CREATECOMMOND_PARAM: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_CREATECOMMOND_PARAM: 300006>
    XT_ERROR_CREATECOMMOND_PRICE_TYPE: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_CREATECOMMOND_PRICE_TYPE: 300008>
    XT_ERROR_CREATECOMMOND_QUOTE: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_CREATECOMMOND_QUOTE: 300007>
    XT_ERROR_CREATECOMMOND_TRANSUNABLE: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_CREATECOMMOND_TRANSUNABLE: 300020>
    XT_ERROR_DEFAULT: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_DEFAULT: 300000>
    XT_ERROR_INVALID_PARAM: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_INVALID_PARAM: 200006>
    XT_ERROR_LOGIN_API_VERSINO_TOO_LOW: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_LOGIN_API_VERSINO_TOO_LOW: 300004>
    XT_ERROR_LOGIN_MAC_NOT_AUTHORIZE: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_LOGIN_MAC_NOT_AUTHORIZE: 300018>
    XT_ERROR_LOGIN_MAC_NOT_MATCH: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_LOGIN_MAC_NOT_MATCH: 300017>
    XT_ERROR_LOGIN_MD5_NOT_MATCH: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_LOGIN_MD5_NOT_MATCH: 300003>
    XT_ERROR_LOGIN_USER_NOT_ALLOWEDLOGIN: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_LOGIN_USER_NOT_ALLOWEDLOGIN: 300005>
    XT_ERROR_NET_DISCONNECTED: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_NET_DISCONNECTED: 200000>
    XT_ERROR_NOT_FIND_ACCOUNT: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_NOT_FIND_ACCOUNT: 200004>
    XT_ERROR_NOT_FIND_FUNCTION: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_NOT_FIND_FUNCTION: 200005>
    XT_ERROR_NOT_INITIALIZED: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_NOT_INITIALIZED: 200002>
    XT_ERROR_NOT_LOGINED: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_NOT_LOGINED: 200001>
    XT_ERROR_ORDER_FLOW_CONTROL: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_ORDER_FLOW_CONTROL: 300009>
    XT_ERROR_ORDER_NOT_AUTHORIZE_CREDIT: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_ORDER_NOT_AUTHORIZE_CREDIT: 300012>
    XT_ERROR_ORDER_NOT_AUTHORIZE_GOLD: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_ORDER_NOT_AUTHORIZE_GOLD: 300013>
    XT_ERROR_ORDER_NOT_AUTHORIZE_HGT: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_ORDER_NOT_AUTHORIZE_HGT: 300014>
    XT_ERROR_ORDER_NOT_AUTHORIZE_SGT: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_ORDER_NOT_AUTHORIZE_SGT: 300015>
    XT_ERROR_ORDER_NOT_AUTHORIZE_STOCKOPTION: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_ORDER_NOT_AUTHORIZE_STOCKOPTION: 300011>
    XT_ERROR_ORDER_NOT_AUTHORIZE_STOCK_FUTURE: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_ORDER_NOT_AUTHORIZE_STOCK_FUTURE: 300010>
    XT_ERROR_QUERYDATA_FLOW_CONTROL: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_QUERYDATA_FLOW_CONTROL: 300016>
    XT_ERROR_REPEAT_LOGIN: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_REPEAT_LOGIN: 300002>
    XT_ERROR_SUBSCRIBE_QUOTE: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_SUBSCRIBE_QUOTE: 300019>
    XT_ERROR_SUCCESS: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_SUCCESS: 0>
    XT_ERROR_TIME_OUT: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_TIME_OUT: 200003>
    XT_ERROR_UNKNOWN: typing.ClassVar[EErrorType]  # value = <EErrorType.XT_ERROR_UNKNOWN: 300001>
    __members__: typing.ClassVar[dict[str, EErrorType]]  # value = {'XT_ERROR_SUCCESS': <EErrorType.XT_ERROR_SUCCESS: 0>, 'XT_ERROR_NET_DISCONNECTED': <EErrorType.XT_ERROR_NET_DISCONNECTED: 200000>, 'XT_ERROR_NOT_LOGINED': <EErrorType.XT_ERROR_NOT_LOGINED: 200001>, 'XT_ERROR_NOT_INITIALIZED': <EErrorType.XT_ERROR_NOT_INITIALIZED: 200002>, 'XT_ERROR_TIME_OUT': <EErrorType.XT_ERROR_TIME_OUT: 200003>, 'XT_ERROR_NOT_FIND_ACCOUNT': <EErrorType.XT_ERROR_NOT_FIND_ACCOUNT: 200004>, 'XT_ERROR_NOT_FIND_FUNCTION': <EErrorType.XT_ERROR_NOT_FIND_FUNCTION: 200005>, 'XT_ERROR_INVALID_PARAM': <EErrorType.XT_ERROR_INVALID_PARAM: 200006>, 'XT_ERROR_DEFAULT': <EErrorType.XT_ERROR_DEFAULT: 300000>, 'XT_ERROR_UNKNOWN': <EErrorType.XT_ERROR_UNKNOWN: 300001>, 'XT_ERROR_REPEAT_LOGIN': <EErrorType.XT_ERROR_REPEAT_LOGIN: 300002>, 'XT_ERROR_LOGIN_MD5_NOT_MATCH': <EErrorType.XT_ERROR_LOGIN_MD5_NOT_MATCH: 300003>, 'XT_ERROR_LOGIN_API_VERSINO_TOO_LOW': <EErrorType.XT_ERROR_LOGIN_API_VERSINO_TOO_LOW: 300004>, 'XT_ERROR_LOGIN_USER_NOT_ALLOWEDLOGIN': <EErrorType.XT_ERROR_LOGIN_USER_NOT_ALLOWEDLOGIN: 300005>, 'XT_ERROR_CREATECOMMOND_PARAM': <EErrorType.XT_ERROR_CREATECOMMOND_PARAM: 300006>, 'XT_ERROR_CREATECOMMOND_QUOTE': <EErrorType.XT_ERROR_CREATECOMMOND_QUOTE: 300007>, 'XT_ERROR_CREATECOMMOND_PRICE_TYPE': <EErrorType.XT_ERROR_CREATECOMMOND_PRICE_TYPE: 300008>, 'XT_ERROR_ORDER_FLOW_CONTROL': <EErrorType.XT_ERROR_ORDER_FLOW_CONTROL: 300009>, 'XT_ERROR_ORDER_NOT_AUTHORIZE_STOCK_FUTURE': <EErrorType.XT_ERROR_ORDER_NOT_AUTHORIZE_STOCK_FUTURE: 300010>, 'XT_ERROR_ORDER_NOT_AUTHORIZE_STOCKOPTION': <EErrorType.XT_ERROR_ORDER_NOT_AUTHORIZE_STOCKOPTION: 300011>, 'XT_ERROR_ORDER_NOT_AUTHORIZE_CREDIT': <EErrorType.XT_ERROR_ORDER_NOT_AUTHORIZE_CREDIT: 300012>, 'XT_ERROR_ORDER_NOT_AUTHORIZE_GOLD': <EErrorType.XT_ERROR_ORDER_NOT_AUTHORIZE_GOLD: 300013>, 'XT_ERROR_ORDER_NOT_AUTHORIZE_HGT': <EErrorType.XT_ERROR_ORDER_NOT_AUTHORIZE_HGT: 300014>, 'XT_ERROR_ORDER_NOT_AUTHORIZE_SGT': <EErrorType.XT_ERROR_ORDER_NOT_AUTHORIZE_SGT: 300015>, 'XT_ERROR_QUERYDATA_FLOW_CONTROL': <EErrorType.XT_ERROR_QUERYDATA_FLOW_CONTROL: 300016>, 'XT_ERROR_LOGIN_MAC_NOT_MATCH': <EErrorType.XT_ERROR_LOGIN_MAC_NOT_MATCH: 300017>, 'XT_ERROR_LOGIN_MAC_NOT_AUTHORIZE': <EErrorType.XT_ERROR_LOGIN_MAC_NOT_AUTHORIZE: 300018>, 'XT_ERROR_SUBSCRIBE_QUOTE': <EErrorType.XT_ERROR_SUBSCRIBE_QUOTE: 300019>, 'XT_ERROR_CREATECOMMOND_TRANSUNABLE': <EErrorType.XT_ERROR_CREATECOMMOND_TRANSUNABLE: 300020>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EFutureTradeType:
    """
    期货交易类型
    
    Members:
    
      FUTRUE_TRADE_TYPE_COMMON : 普通成交
    
      FUTURE_TRADE_TYPE_OPTIONSEXECUTION : 期权成交ptionsExecution
    
      FUTURE_TRADE_TYPE_OTC : OTC成交
    
      FUTURE_TRADE_TYPE_EFPDIRVED : 期转现衍生成交
    
      FUTURE_TRADE_TYPE_COMBINATION_DERIVED : 组合衍生成交
    """
    FUTRUE_TRADE_TYPE_COMMON: typing.ClassVar[EFutureTradeType]  # value = <EFutureTradeType.FUTRUE_TRADE_TYPE_COMMON: 48>
    FUTURE_TRADE_TYPE_COMBINATION_DERIVED: typing.ClassVar[EFutureTradeType]  # value = <EFutureTradeType.FUTURE_TRADE_TYPE_COMBINATION_DERIVED: 52>
    FUTURE_TRADE_TYPE_EFPDIRVED: typing.ClassVar[EFutureTradeType]  # value = <EFutureTradeType.FUTURE_TRADE_TYPE_EFPDIRVED: 51>
    FUTURE_TRADE_TYPE_OPTIONSEXECUTION: typing.ClassVar[EFutureTradeType]  # value = <EFutureTradeType.FUTURE_TRADE_TYPE_OPTIONSEXECUTION: 49>
    FUTURE_TRADE_TYPE_OTC: typing.ClassVar[EFutureTradeType]  # value = <EFutureTradeType.FUTURE_TRADE_TYPE_OTC: 50>
    __members__: typing.ClassVar[dict[str, EFutureTradeType]]  # value = {'FUTRUE_TRADE_TYPE_COMMON': <EFutureTradeType.FUTRUE_TRADE_TYPE_COMMON: 48>, 'FUTURE_TRADE_TYPE_OPTIONSEXECUTION': <EFutureTradeType.FUTURE_TRADE_TYPE_OPTIONSEXECUTION: 49>, 'FUTURE_TRADE_TYPE_OTC': <EFutureTradeType.FUTURE_TRADE_TYPE_OTC: 50>, 'FUTURE_TRADE_TYPE_EFPDIRVED': <EFutureTradeType.FUTURE_TRADE_TYPE_EFPDIRVED: 51>, 'FUTURE_TRADE_TYPE_COMBINATION_DERIVED': <EFutureTradeType.FUTURE_TRADE_TYPE_COMBINATION_DERIVED: 52>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EHedgeFlagType:
    """
    投保标志
    
    Members:
    
      HEDGE_FLAG_SPECULATION : 投机
    
      HEDGE_FLAG_ARBITRAGE : 套利
    
      HEDGE_FLAG_HEDGE : 套保
    """
    HEDGE_FLAG_ARBITRAGE: typing.ClassVar[EHedgeFlagType]  # value = <EHedgeFlagType.HEDGE_FLAG_ARBITRAGE: 50>
    HEDGE_FLAG_HEDGE: typing.ClassVar[EHedgeFlagType]  # value = <EHedgeFlagType.HEDGE_FLAG_HEDGE: 51>
    HEDGE_FLAG_SPECULATION: typing.ClassVar[EHedgeFlagType]  # value = <EHedgeFlagType.HEDGE_FLAG_SPECULATION: 49>
    __members__: typing.ClassVar[dict[str, EHedgeFlagType]]  # value = {'HEDGE_FLAG_SPECULATION': <EHedgeFlagType.HEDGE_FLAG_SPECULATION: 49>, 'HEDGE_FLAG_ARBITRAGE': <EHedgeFlagType.HEDGE_FLAG_ARBITRAGE: 50>, 'HEDGE_FLAG_HEDGE': <EHedgeFlagType.HEDGE_FLAG_HEDGE: 51>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EMainFlag:
    """
    主副标记
    
    Members:
    
      MAIN_FLAG_VICE : 副账户
    
      MAIN_FLAG_MAIN : 主账户
    """
    MAIN_FLAG_MAIN: typing.ClassVar[EMainFlag]  # value = <EMainFlag.MAIN_FLAG_MAIN: 49>
    MAIN_FLAG_VICE: typing.ClassVar[EMainFlag]  # value = <EMainFlag.MAIN_FLAG_VICE: 48>
    __members__: typing.ClassVar[dict[str, EMainFlag]]  # value = {'MAIN_FLAG_VICE': <EMainFlag.MAIN_FLAG_VICE: 48>, 'MAIN_FLAG_MAIN': <EMainFlag.MAIN_FLAG_MAIN: 49>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EMoneyType:
    """
    币种
    
    Members:
    
      MONEY_TYPE_RMB : 人民币
    
      MONEY_TYPE_USD : 美元
    
      MONEY_TYPE_HK : 港币
    """
    MONEY_TYPE_HK: typing.ClassVar[EMoneyType]  # value = <EMoneyType.MONEY_TYPE_HK: 50>
    MONEY_TYPE_RMB: typing.ClassVar[EMoneyType]  # value = <EMoneyType.MONEY_TYPE_RMB: 48>
    MONEY_TYPE_USD: typing.ClassVar[EMoneyType]  # value = <EMoneyType.MONEY_TYPE_USD: 49>
    __members__: typing.ClassVar[dict[str, EMoneyType]]  # value = {'MONEY_TYPE_RMB': <EMoneyType.MONEY_TYPE_RMB: 48>, 'MONEY_TYPE_USD': <EMoneyType.MONEY_TYPE_USD: 49>, 'MONEY_TYPE_HK': <EMoneyType.MONEY_TYPE_HK: 50>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EOffsetFlagType:
    """
    开平标志
    
    Members:
    
      EOFF_THOST_FTDC_OF_INVALID : 未知
    
      EOFF_THOST_FTDC_OF_Open : 开仓，对应股票买入
    
      EOFF_THOST_FTDC_OF_Close : 平仓，对应股票卖出
    
      EOFF_THOST_FTDC_OF_ForceClose : 强平
    
      EOFF_THOST_FTDC_OF_CloseToday : 平今
    
      EOFF_THOST_FTDC_OF_CloseYesterday : 平昨
    
      EOFF_THOST_FTDC_OF_ForceOff : 强减
    
      EOFF_THOST_FTDC_OF_LocalForceClose : 本地强平
    
      EOFF_THOST_FTDC_OF_PLEDGE_IN : 质押入库
    
      EOFF_THOST_FTDC_OF_PLEDGE_OUT : 质押出库
    
      EOFF_THOST_FTDC_OF_ALLOTMENT : 股票配股
    
      EOFF_THOST_FTDC_OF_OPTION_EXERCISE : 行权
    
      EOFF_THOST_FTDC_OF_OPTION_LOCK : 锁定
    
      EOFF_THOST_FTDC_OF_OPTION_UNLOCK : 解锁
    """
    EOFF_THOST_FTDC_OF_ALLOTMENT: typing.ClassVar[EOffsetFlagType]  # value = <EOffsetFlagType.EOFF_THOST_FTDC_OF_ALLOTMENT: 67>
    EOFF_THOST_FTDC_OF_Close: typing.ClassVar[EOffsetFlagType]  # value = <EOffsetFlagType.EOFF_THOST_FTDC_OF_Close: 49>
    EOFF_THOST_FTDC_OF_CloseToday: typing.ClassVar[EOffsetFlagType]  # value = <EOffsetFlagType.EOFF_THOST_FTDC_OF_CloseToday: 51>
    EOFF_THOST_FTDC_OF_CloseYesterday: typing.ClassVar[EOffsetFlagType]  # value = <EOffsetFlagType.EOFF_THOST_FTDC_OF_CloseYesterday: 52>
    EOFF_THOST_FTDC_OF_ForceClose: typing.ClassVar[EOffsetFlagType]  # value = <EOffsetFlagType.EOFF_THOST_FTDC_OF_ForceClose: 50>
    EOFF_THOST_FTDC_OF_ForceOff: typing.ClassVar[EOffsetFlagType]  # value = <EOffsetFlagType.EOFF_THOST_FTDC_OF_ForceOff: 53>
    EOFF_THOST_FTDC_OF_INVALID: typing.ClassVar[EOffsetFlagType]  # value = <EOffsetFlagType.EOFF_THOST_FTDC_OF_INVALID: -1>
    EOFF_THOST_FTDC_OF_LocalForceClose: typing.ClassVar[EOffsetFlagType]  # value = <EOffsetFlagType.EOFF_THOST_FTDC_OF_LocalForceClose: 54>
    EOFF_THOST_FTDC_OF_OPTION_EXERCISE: typing.ClassVar[EOffsetFlagType]  # value = <EOffsetFlagType.EOFF_THOST_FTDC_OF_OPTION_EXERCISE: 68>
    EOFF_THOST_FTDC_OF_OPTION_LOCK: typing.ClassVar[EOffsetFlagType]  # value = <EOffsetFlagType.EOFF_THOST_FTDC_OF_OPTION_LOCK: 69>
    EOFF_THOST_FTDC_OF_OPTION_UNLOCK: typing.ClassVar[EOffsetFlagType]  # value = <EOffsetFlagType.EOFF_THOST_FTDC_OF_OPTION_UNLOCK: 70>
    EOFF_THOST_FTDC_OF_Open: typing.ClassVar[EOffsetFlagType]  # value = <EOffsetFlagType.EOFF_THOST_FTDC_OF_Open: 48>
    EOFF_THOST_FTDC_OF_PLEDGE_IN: typing.ClassVar[EOffsetFlagType]  # value = <EOffsetFlagType.EOFF_THOST_FTDC_OF_PLEDGE_IN: 81>
    EOFF_THOST_FTDC_OF_PLEDGE_OUT: typing.ClassVar[EOffsetFlagType]  # value = <EOffsetFlagType.EOFF_THOST_FTDC_OF_PLEDGE_OUT: 66>
    __members__: typing.ClassVar[dict[str, EOffsetFlagType]]  # value = {'EOFF_THOST_FTDC_OF_INVALID': <EOffsetFlagType.EOFF_THOST_FTDC_OF_INVALID: -1>, 'EOFF_THOST_FTDC_OF_Open': <EOffsetFlagType.EOFF_THOST_FTDC_OF_Open: 48>, 'EOFF_THOST_FTDC_OF_Close': <EOffsetFlagType.EOFF_THOST_FTDC_OF_Close: 49>, 'EOFF_THOST_FTDC_OF_ForceClose': <EOffsetFlagType.EOFF_THOST_FTDC_OF_ForceClose: 50>, 'EOFF_THOST_FTDC_OF_CloseToday': <EOffsetFlagType.EOFF_THOST_FTDC_OF_CloseToday: 51>, 'EOFF_THOST_FTDC_OF_CloseYesterday': <EOffsetFlagType.EOFF_THOST_FTDC_OF_CloseYesterday: 52>, 'EOFF_THOST_FTDC_OF_ForceOff': <EOffsetFlagType.EOFF_THOST_FTDC_OF_ForceOff: 53>, 'EOFF_THOST_FTDC_OF_LocalForceClose': <EOffsetFlagType.EOFF_THOST_FTDC_OF_LocalForceClose: 54>, 'EOFF_THOST_FTDC_OF_PLEDGE_IN': <EOffsetFlagType.EOFF_THOST_FTDC_OF_PLEDGE_IN: 81>, 'EOFF_THOST_FTDC_OF_PLEDGE_OUT': <EOffsetFlagType.EOFF_THOST_FTDC_OF_PLEDGE_OUT: 66>, 'EOFF_THOST_FTDC_OF_ALLOTMENT': <EOffsetFlagType.EOFF_THOST_FTDC_OF_ALLOTMENT: 67>, 'EOFF_THOST_FTDC_OF_OPTION_EXERCISE': <EOffsetFlagType.EOFF_THOST_FTDC_OF_OPTION_EXERCISE: 68>, 'EOFF_THOST_FTDC_OF_OPTION_LOCK': <EOffsetFlagType.EOFF_THOST_FTDC_OF_OPTION_LOCK: 69>, 'EOFF_THOST_FTDC_OF_OPTION_UNLOCK': <EOffsetFlagType.EOFF_THOST_FTDC_OF_OPTION_UNLOCK: 70>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EOpTriggerType:
    """
    触价类型
    
    Members:
    
      OTT_NONE : 不使用触价
    
      OTT_UP : 向上触价
    
      OTT_DOWN : 向下触价
    """
    OTT_DOWN: typing.ClassVar[EOpTriggerType]  # value = <EOpTriggerType.OTT_DOWN: 2>
    OTT_NONE: typing.ClassVar[EOpTriggerType]  # value = <EOpTriggerType.OTT_NONE: 0>
    OTT_UP: typing.ClassVar[EOpTriggerType]  # value = <EOpTriggerType.OTT_UP: 1>
    __members__: typing.ClassVar[dict[str, EOpTriggerType]]  # value = {'OTT_NONE': <EOpTriggerType.OTT_NONE: 0>, 'OTT_UP': <EOpTriggerType.OTT_UP: 1>, 'OTT_DOWN': <EOpTriggerType.OTT_DOWN: 2>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EOperationType:
    """
    下单类型
    
    Members:
    
      OPT_INVALID : 
    
      OPT_OPEN_LONG : 开多 0
    
      OPT_CLOSE_LONG_HISTORY : 平昨多 1
    
      OPT_CLOSE_LONG_TODAY : 平昨多 2
    
      OPT_OPEN_SHORT : 开空 3
    
      OPT_CLOSE_SHORT_HISTORY : 平昨空 4
    
      OPT_CLOSE_SHORT_TODAY : 平今空 5
    
      OPT_CLOSE_LONG_TODAY_FIRST : 平多，优先平今  6
    
      OPT_CLOSE_LONG_HISTORY_FIRST : 平多，优先平昨 7
    
      OPT_CLOSE_SHORT_TODAY_FIRST : 平空，优先平今 8
    
      OPT_CLOSE_SHORT_HISTORY_FIRST : 平空，优先平昨 9
    
      OPT_CLOSE_LONG_TODAY_HISTORY_THEN_OPEN_SHORT : 开空，优先平今多
    
      OPT_CLOSE_LONG_HISTORY_TODAY_THEN_OPEN_SHORT : 开空，优先平昨多
    
      OPT_CLOSE_SHORT_TODAY_HISTORY_THEN_OPEN_LONG : 开多，优先平今空
    
      OPT_CLOSE_SHORT_HISTORY_TODAY_THEN_OPEN_LONG : 开多，优先平昨空
    
      OPT_SELL_PRIORITY_OPEN : 卖出，优先开仓
    
      OPT_BUY_PRIORITY_OPEN : 买入，优先开仓
    
      OPT_SELL_OPTIMAL_COMSSION : 卖出，最优手续费
    
      OPT_BUY_OPTIMAL_COMSSION : 买入，最优手续费
    
      OPT_BUY : 买入，担保品买入， 18
    
      OPT_SELL : 卖出，担保品卖出， 19
    
      OPT_FIN_BUY : 融资买入
    
      OPT_SLO_SELL : 融券卖出
    
      OPT_BUY_SECU_REPAY : 买券还券
    
      OPT_DIRECT_SECU_REPAY : 直接还券
    
      OPT_SELL_CASH_REPAY : 卖券还款
    
      OPT_DIRECT_CASH_REPAY : 直接还款
    
      OPT_FUND_SUBSCRIBE : 基金申购
    
      OPT_FUND_REDEMPTION : 基金赎回
    
      OPT_FUND_MERGE : 基金合并
    
      OPT_FUND_SPLIT : 基金分拆
    
      OPT_PLEDGE_IN : 质押入库
    
      OPT_PLEDGE_OUT : 质押出库
    
      OPT_OPTION_BUY_OPEN : 买入开仓
    
      OPT_OPTION_SELL_CLOSE : 卖出平仓
    
      OPT_OPTION_SELL_OPEN : 卖出开仓
    
      OPT_OPTION_BUY_CLOSE : 买入平仓
    
      OPT_OPTION_COVERED_OPEN : 备兑开仓
    
      OPT_OPTION_COVERED_CLOSE : 备兑平仓
    
      OPT_OPTION_CALL_EXERCISE : 认购行权
    
      OPT_OPTION_PUT_EXERCISE : 认沽行权
    
      OPT_OPTION_SECU_LOCK : 证券锁定
    
      OPT_OPTION_SECU_UNLOCK : 证券解锁
    
      OPT_FUTURE_OPTION_EXERCISE : 期货期权行权
    
      OPT_CONVERT_BONDS : 可转债转股
    
      OPT_SELL_BACK_BONDS : 可转债回售
    
      OPT_COLLATERAL_TRANSFER_IN : 担保品划入
    
      OPT_COLLATERAL_TRANSFER_OUT : 担保品划出
    
      OPT_ETF_PURCHASE : ETF申购
    
      OPT_ETF_REDEMPTION : ETF赎回
    
      OPT_AFTER_FIX_BUY : 盘后定价买入
    
      OPT_AFTER_FIX_SELL : 盘后定价卖出
    
      OPT_OPTION_COMB_EXERCISE : 组合行权
    
      OPT_OPTION_BUILD_COMB_STRATEGY : 构建组合策略
    
      OPT_OPTION_RELEASE_COMB_STRATEGY : 解除组合策略
    
      OPT_SLO_SELL_SPECIAL : 专项融券卖出
    
      OPT_BUY_SECU_REPAY_SPECIAL : 专项买券还券
    
      OPT_DIRECT_SECU_REPAY_SPECIAL : 专项直接还券
    
      OPT_FIN_BUY_SPECIAL : 专项融资买入
    
      OPT_SELL_CASH_REPAY_SPECIAL : 专项卖券还款
    
      OPT_DIRECT_CASH_REPAY_SPECIAL : 专项直接还款
    
      OPT_OPTION_BUY_CLOSE_THEN_OPEN : 买入优先平仓
    
      OPT_OPTION_SELL_CLOSE_THEN_OPEN : 卖出优先平仓
    
      OPT_N3B_PRICE_BUY : 协议转让-定价买入
    
      OPT_N3B_PRICE_SELL : 协议转让-定价卖出
    
      OPT_N3B_CONFIRM_BUY : 协议转让-成交确认买入
    
      OPT_N3B_CONFIRM_SELL : 协议转让-成交确认卖出
    
      OPT_N3B_REPORT_CONFIRM_BUY : 协议转让-互报成交确认买入
    
      OPT_N3B_REPORT_CONFIRM_SELL : 协议转让-互报成交确认卖出
    
      OPT_N3B_LIMIT_PRICE_BUY : 全国股转-挂牌公司交易-做市转让-限价买入
    
      OPT_N3B_LIMIT_PRICE_SELL : 全国股转-挂牌公司交易-做市转让-限价卖出
    
      OPT_NEEQ_O3B_LIMIT_PRICE_BUY : 全国股转-两网及退市交易-限价买入
    
      OPT_NEEQ_O3B_LIMIT_PRICE_SELL : 全国股转-两网及退市交易-限价卖出
    
      OPT_N3B_CALL_AUCTION_BUY : 协议转让-集合竞价买入
    
      OPT_N3B_CALL_AUCTION_SELL : 协议转让-集合竞价卖出
    
      OPT_N3B_AFTER_HOURS_BUY : 全国股转-盘后协议买入
    
      OPT_N3B_AFTER_HOURS_SELL : 全国股转-盘后协议卖出
    
      OPT_NEEQ_O3B_CONTINUOUS_AUCTION_BUY : 全国股转-北交所买入
    
      OPT_NEEQ_O3B_CONTINUOUS_AUCTION_SELL : 全国股转-北交所卖出
    
      OPT_NEEQ_O3B_ASK_PRICE : 全国股转-申购-询价申报
    
      OPT_NEEQ_O3B_PRICE_CONFIRM : 全国股转-申购-申购申报
    
      OPT_NEEQ_O3B_BLOCKTRADING_BUY : 全国股转-大宗交易买入
    
      OPT_NEEQ_O3B_BLOCKTRADING_SELL : 全国股转-大宗交易卖出
    """
    OPT_AFTER_FIX_BUY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_AFTER_FIX_BUY: 1043>
    OPT_AFTER_FIX_SELL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_AFTER_FIX_SELL: 1044>
    OPT_BUY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_BUY: 18>
    OPT_BUY_OPTIMAL_COMSSION: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_BUY_OPTIMAL_COMSSION: 17>
    OPT_BUY_PRIORITY_OPEN: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_BUY_PRIORITY_OPEN: 15>
    OPT_BUY_SECU_REPAY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_BUY_SECU_REPAY: 22>
    OPT_BUY_SECU_REPAY_SPECIAL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_BUY_SECU_REPAY_SPECIAL: 1011>
    OPT_CLOSE_LONG_HISTORY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_CLOSE_LONG_HISTORY: 1>
    OPT_CLOSE_LONG_HISTORY_FIRST: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_CLOSE_LONG_HISTORY_FIRST: 7>
    OPT_CLOSE_LONG_HISTORY_TODAY_THEN_OPEN_SHORT: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_CLOSE_LONG_HISTORY_TODAY_THEN_OPEN_SHORT: 11>
    OPT_CLOSE_LONG_TODAY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_CLOSE_LONG_TODAY: 2>
    OPT_CLOSE_LONG_TODAY_FIRST: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_CLOSE_LONG_TODAY_FIRST: 6>
    OPT_CLOSE_LONG_TODAY_HISTORY_THEN_OPEN_SHORT: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_CLOSE_LONG_TODAY_HISTORY_THEN_OPEN_SHORT: 10>
    OPT_CLOSE_SHORT_HISTORY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_CLOSE_SHORT_HISTORY: 4>
    OPT_CLOSE_SHORT_HISTORY_FIRST: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_CLOSE_SHORT_HISTORY_FIRST: 9>
    OPT_CLOSE_SHORT_HISTORY_TODAY_THEN_OPEN_LONG: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_CLOSE_SHORT_HISTORY_TODAY_THEN_OPEN_LONG: 13>
    OPT_CLOSE_SHORT_TODAY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_CLOSE_SHORT_TODAY: 5>
    OPT_CLOSE_SHORT_TODAY_FIRST: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_CLOSE_SHORT_TODAY_FIRST: 8>
    OPT_CLOSE_SHORT_TODAY_HISTORY_THEN_OPEN_LONG: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_CLOSE_SHORT_TODAY_HISTORY_THEN_OPEN_LONG: 12>
    OPT_COLLATERAL_TRANSFER_IN: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_COLLATERAL_TRANSFER_IN: 55>
    OPT_COLLATERAL_TRANSFER_OUT: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_COLLATERAL_TRANSFER_OUT: 56>
    OPT_CONVERT_BONDS: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_CONVERT_BONDS: 51>
    OPT_DIRECT_CASH_REPAY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_DIRECT_CASH_REPAY: 25>
    OPT_DIRECT_CASH_REPAY_SPECIAL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_DIRECT_CASH_REPAY_SPECIAL: 1024>
    OPT_DIRECT_SECU_REPAY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_DIRECT_SECU_REPAY: 23>
    OPT_DIRECT_SECU_REPAY_SPECIAL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_DIRECT_SECU_REPAY_SPECIAL: 1012>
    OPT_ETF_PURCHASE: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_ETF_PURCHASE: 1004>
    OPT_ETF_REDEMPTION: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_ETF_REDEMPTION: 1005>
    OPT_FIN_BUY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_FIN_BUY: 20>
    OPT_FIN_BUY_SPECIAL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_FIN_BUY_SPECIAL: 1022>
    OPT_FUND_MERGE: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_FUND_MERGE: 28>
    OPT_FUND_REDEMPTION: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_FUND_REDEMPTION: 27>
    OPT_FUND_SPLIT: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_FUND_SPLIT: 29>
    OPT_FUND_SUBSCRIBE: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_FUND_SUBSCRIBE: 26>
    OPT_FUTURE_OPTION_EXERCISE: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_FUTURE_OPTION_EXERCISE: 50>
    OPT_INVALID: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_INVALID: -1>
    OPT_N3B_AFTER_HOURS_BUY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_N3B_AFTER_HOURS_BUY: 1029>
    OPT_N3B_AFTER_HOURS_SELL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_N3B_AFTER_HOURS_SELL: 1030>
    OPT_N3B_CALL_AUCTION_BUY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_N3B_CALL_AUCTION_BUY: 1027>
    OPT_N3B_CALL_AUCTION_SELL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_N3B_CALL_AUCTION_SELL: 1028>
    OPT_N3B_CONFIRM_BUY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_N3B_CONFIRM_BUY: 44>
    OPT_N3B_CONFIRM_SELL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_N3B_CONFIRM_SELL: 45>
    OPT_N3B_LIMIT_PRICE_BUY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_N3B_LIMIT_PRICE_BUY: 48>
    OPT_N3B_LIMIT_PRICE_SELL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_N3B_LIMIT_PRICE_SELL: 49>
    OPT_N3B_PRICE_BUY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_N3B_PRICE_BUY: 42>
    OPT_N3B_PRICE_SELL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_N3B_PRICE_SELL: 43>
    OPT_N3B_REPORT_CONFIRM_BUY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_N3B_REPORT_CONFIRM_BUY: 46>
    OPT_N3B_REPORT_CONFIRM_SELL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_N3B_REPORT_CONFIRM_SELL: 47>
    OPT_NEEQ_O3B_ASK_PRICE: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_NEEQ_O3B_ASK_PRICE: 1101>
    OPT_NEEQ_O3B_BLOCKTRADING_BUY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_NEEQ_O3B_BLOCKTRADING_BUY: 1103>
    OPT_NEEQ_O3B_BLOCKTRADING_SELL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_NEEQ_O3B_BLOCKTRADING_SELL: 1104>
    OPT_NEEQ_O3B_CONTINUOUS_AUCTION_BUY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_NEEQ_O3B_CONTINUOUS_AUCTION_BUY: 1099>
    OPT_NEEQ_O3B_CONTINUOUS_AUCTION_SELL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_NEEQ_O3B_CONTINUOUS_AUCTION_SELL: 1100>
    OPT_NEEQ_O3B_LIMIT_PRICE_BUY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_NEEQ_O3B_LIMIT_PRICE_BUY: 1013>
    OPT_NEEQ_O3B_LIMIT_PRICE_SELL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_NEEQ_O3B_LIMIT_PRICE_SELL: 1014>
    OPT_NEEQ_O3B_PRICE_CONFIRM: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_NEEQ_O3B_PRICE_CONFIRM: 1102>
    OPT_OPEN_LONG: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPEN_LONG: 0>
    OPT_OPEN_SHORT: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPEN_SHORT: 3>
    OPT_OPTION_BUILD_COMB_STRATEGY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPTION_BUILD_COMB_STRATEGY: 1090>
    OPT_OPTION_BUY_CLOSE: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPTION_BUY_CLOSE: 35>
    OPT_OPTION_BUY_CLOSE_THEN_OPEN: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPTION_BUY_CLOSE_THEN_OPEN: 1154>
    OPT_OPTION_BUY_OPEN: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPTION_BUY_OPEN: 32>
    OPT_OPTION_CALL_EXERCISE: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPTION_CALL_EXERCISE: 38>
    OPT_OPTION_COMB_EXERCISE: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPTION_COMB_EXERCISE: 1089>
    OPT_OPTION_COVERED_CLOSE: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPTION_COVERED_CLOSE: 37>
    OPT_OPTION_COVERED_OPEN: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPTION_COVERED_OPEN: 36>
    OPT_OPTION_PUT_EXERCISE: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPTION_PUT_EXERCISE: 39>
    OPT_OPTION_RELEASE_COMB_STRATEGY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPTION_RELEASE_COMB_STRATEGY: 1091>
    OPT_OPTION_SECU_LOCK: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPTION_SECU_LOCK: 40>
    OPT_OPTION_SECU_UNLOCK: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPTION_SECU_UNLOCK: 41>
    OPT_OPTION_SELL_CLOSE: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPTION_SELL_CLOSE: 33>
    OPT_OPTION_SELL_CLOSE_THEN_OPEN: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPTION_SELL_CLOSE_THEN_OPEN: 1155>
    OPT_OPTION_SELL_OPEN: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_OPTION_SELL_OPEN: 34>
    OPT_PLEDGE_IN: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_PLEDGE_IN: 30>
    OPT_PLEDGE_OUT: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_PLEDGE_OUT: 31>
    OPT_SELL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_SELL: 19>
    OPT_SELL_BACK_BONDS: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_SELL_BACK_BONDS: 52>
    OPT_SELL_CASH_REPAY: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_SELL_CASH_REPAY: 24>
    OPT_SELL_CASH_REPAY_SPECIAL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_SELL_CASH_REPAY_SPECIAL: 1023>
    OPT_SELL_OPTIMAL_COMSSION: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_SELL_OPTIMAL_COMSSION: 16>
    OPT_SELL_PRIORITY_OPEN: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_SELL_PRIORITY_OPEN: 14>
    OPT_SLO_SELL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_SLO_SELL: 21>
    OPT_SLO_SELL_SPECIAL: typing.ClassVar[EOperationType]  # value = <EOperationType.OPT_SLO_SELL_SPECIAL: 1010>
    __members__: typing.ClassVar[dict[str, EOperationType]]  # value = {'OPT_INVALID': <EOperationType.OPT_INVALID: -1>, 'OPT_OPEN_LONG': <EOperationType.OPT_OPEN_LONG: 0>, 'OPT_CLOSE_LONG_HISTORY': <EOperationType.OPT_CLOSE_LONG_HISTORY: 1>, 'OPT_CLOSE_LONG_TODAY': <EOperationType.OPT_CLOSE_LONG_TODAY: 2>, 'OPT_OPEN_SHORT': <EOperationType.OPT_OPEN_SHORT: 3>, 'OPT_CLOSE_SHORT_HISTORY': <EOperationType.OPT_CLOSE_SHORT_HISTORY: 4>, 'OPT_CLOSE_SHORT_TODAY': <EOperationType.OPT_CLOSE_SHORT_TODAY: 5>, 'OPT_CLOSE_LONG_TODAY_FIRST': <EOperationType.OPT_CLOSE_LONG_TODAY_FIRST: 6>, 'OPT_CLOSE_LONG_HISTORY_FIRST': <EOperationType.OPT_CLOSE_LONG_HISTORY_FIRST: 7>, 'OPT_CLOSE_SHORT_TODAY_FIRST': <EOperationType.OPT_CLOSE_SHORT_TODAY_FIRST: 8>, 'OPT_CLOSE_SHORT_HISTORY_FIRST': <EOperationType.OPT_CLOSE_SHORT_HISTORY_FIRST: 9>, 'OPT_CLOSE_LONG_TODAY_HISTORY_THEN_OPEN_SHORT': <EOperationType.OPT_CLOSE_LONG_TODAY_HISTORY_THEN_OPEN_SHORT: 10>, 'OPT_CLOSE_LONG_HISTORY_TODAY_THEN_OPEN_SHORT': <EOperationType.OPT_CLOSE_LONG_HISTORY_TODAY_THEN_OPEN_SHORT: 11>, 'OPT_CLOSE_SHORT_TODAY_HISTORY_THEN_OPEN_LONG': <EOperationType.OPT_CLOSE_SHORT_TODAY_HISTORY_THEN_OPEN_LONG: 12>, 'OPT_CLOSE_SHORT_HISTORY_TODAY_THEN_OPEN_LONG': <EOperationType.OPT_CLOSE_SHORT_HISTORY_TODAY_THEN_OPEN_LONG: 13>, 'OPT_SELL_PRIORITY_OPEN': <EOperationType.OPT_SELL_PRIORITY_OPEN: 14>, 'OPT_BUY_PRIORITY_OPEN': <EOperationType.OPT_BUY_PRIORITY_OPEN: 15>, 'OPT_SELL_OPTIMAL_COMSSION': <EOperationType.OPT_SELL_OPTIMAL_COMSSION: 16>, 'OPT_BUY_OPTIMAL_COMSSION': <EOperationType.OPT_BUY_OPTIMAL_COMSSION: 17>, 'OPT_BUY': <EOperationType.OPT_BUY: 18>, 'OPT_SELL': <EOperationType.OPT_SELL: 19>, 'OPT_FIN_BUY': <EOperationType.OPT_FIN_BUY: 20>, 'OPT_SLO_SELL': <EOperationType.OPT_SLO_SELL: 21>, 'OPT_BUY_SECU_REPAY': <EOperationType.OPT_BUY_SECU_REPAY: 22>, 'OPT_DIRECT_SECU_REPAY': <EOperationType.OPT_DIRECT_SECU_REPAY: 23>, 'OPT_SELL_CASH_REPAY': <EOperationType.OPT_SELL_CASH_REPAY: 24>, 'OPT_DIRECT_CASH_REPAY': <EOperationType.OPT_DIRECT_CASH_REPAY: 25>, 'OPT_FUND_SUBSCRIBE': <EOperationType.OPT_FUND_SUBSCRIBE: 26>, 'OPT_FUND_REDEMPTION': <EOperationType.OPT_FUND_REDEMPTION: 27>, 'OPT_FUND_MERGE': <EOperationType.OPT_FUND_MERGE: 28>, 'OPT_FUND_SPLIT': <EOperationType.OPT_FUND_SPLIT: 29>, 'OPT_PLEDGE_IN': <EOperationType.OPT_PLEDGE_IN: 30>, 'OPT_PLEDGE_OUT': <EOperationType.OPT_PLEDGE_OUT: 31>, 'OPT_OPTION_BUY_OPEN': <EOperationType.OPT_OPTION_BUY_OPEN: 32>, 'OPT_OPTION_SELL_CLOSE': <EOperationType.OPT_OPTION_SELL_CLOSE: 33>, 'OPT_OPTION_SELL_OPEN': <EOperationType.OPT_OPTION_SELL_OPEN: 34>, 'OPT_OPTION_BUY_CLOSE': <EOperationType.OPT_OPTION_BUY_CLOSE: 35>, 'OPT_OPTION_COVERED_OPEN': <EOperationType.OPT_OPTION_COVERED_OPEN: 36>, 'OPT_OPTION_COVERED_CLOSE': <EOperationType.OPT_OPTION_COVERED_CLOSE: 37>, 'OPT_OPTION_CALL_EXERCISE': <EOperationType.OPT_OPTION_CALL_EXERCISE: 38>, 'OPT_OPTION_PUT_EXERCISE': <EOperationType.OPT_OPTION_PUT_EXERCISE: 39>, 'OPT_OPTION_SECU_LOCK': <EOperationType.OPT_OPTION_SECU_LOCK: 40>, 'OPT_OPTION_SECU_UNLOCK': <EOperationType.OPT_OPTION_SECU_UNLOCK: 41>, 'OPT_FUTURE_OPTION_EXERCISE': <EOperationType.OPT_FUTURE_OPTION_EXERCISE: 50>, 'OPT_CONVERT_BONDS': <EOperationType.OPT_CONVERT_BONDS: 51>, 'OPT_SELL_BACK_BONDS': <EOperationType.OPT_SELL_BACK_BONDS: 52>, 'OPT_COLLATERAL_TRANSFER_IN': <EOperationType.OPT_COLLATERAL_TRANSFER_IN: 55>, 'OPT_COLLATERAL_TRANSFER_OUT': <EOperationType.OPT_COLLATERAL_TRANSFER_OUT: 56>, 'OPT_ETF_PURCHASE': <EOperationType.OPT_ETF_PURCHASE: 1004>, 'OPT_ETF_REDEMPTION': <EOperationType.OPT_ETF_REDEMPTION: 1005>, 'OPT_AFTER_FIX_BUY': <EOperationType.OPT_AFTER_FIX_BUY: 1043>, 'OPT_AFTER_FIX_SELL': <EOperationType.OPT_AFTER_FIX_SELL: 1044>, 'OPT_OPTION_COMB_EXERCISE': <EOperationType.OPT_OPTION_COMB_EXERCISE: 1089>, 'OPT_OPTION_BUILD_COMB_STRATEGY': <EOperationType.OPT_OPTION_BUILD_COMB_STRATEGY: 1090>, 'OPT_OPTION_RELEASE_COMB_STRATEGY': <EOperationType.OPT_OPTION_RELEASE_COMB_STRATEGY: 1091>, 'OPT_SLO_SELL_SPECIAL': <EOperationType.OPT_SLO_SELL_SPECIAL: 1010>, 'OPT_BUY_SECU_REPAY_SPECIAL': <EOperationType.OPT_BUY_SECU_REPAY_SPECIAL: 1011>, 'OPT_DIRECT_SECU_REPAY_SPECIAL': <EOperationType.OPT_DIRECT_SECU_REPAY_SPECIAL: 1012>, 'OPT_FIN_BUY_SPECIAL': <EOperationType.OPT_FIN_BUY_SPECIAL: 1022>, 'OPT_SELL_CASH_REPAY_SPECIAL': <EOperationType.OPT_SELL_CASH_REPAY_SPECIAL: 1023>, 'OPT_DIRECT_CASH_REPAY_SPECIAL': <EOperationType.OPT_DIRECT_CASH_REPAY_SPECIAL: 1024>, 'OPT_OPTION_BUY_CLOSE_THEN_OPEN': <EOperationType.OPT_OPTION_BUY_CLOSE_THEN_OPEN: 1154>, 'OPT_OPTION_SELL_CLOSE_THEN_OPEN': <EOperationType.OPT_OPTION_SELL_CLOSE_THEN_OPEN: 1155>, 'OPT_N3B_PRICE_BUY': <EOperationType.OPT_N3B_PRICE_BUY: 42>, 'OPT_N3B_PRICE_SELL': <EOperationType.OPT_N3B_PRICE_SELL: 43>, 'OPT_N3B_CONFIRM_BUY': <EOperationType.OPT_N3B_CONFIRM_BUY: 44>, 'OPT_N3B_CONFIRM_SELL': <EOperationType.OPT_N3B_CONFIRM_SELL: 45>, 'OPT_N3B_REPORT_CONFIRM_BUY': <EOperationType.OPT_N3B_REPORT_CONFIRM_BUY: 46>, 'OPT_N3B_REPORT_CONFIRM_SELL': <EOperationType.OPT_N3B_REPORT_CONFIRM_SELL: 47>, 'OPT_N3B_LIMIT_PRICE_BUY': <EOperationType.OPT_N3B_LIMIT_PRICE_BUY: 48>, 'OPT_N3B_LIMIT_PRICE_SELL': <EOperationType.OPT_N3B_LIMIT_PRICE_SELL: 49>, 'OPT_NEEQ_O3B_LIMIT_PRICE_BUY': <EOperationType.OPT_NEEQ_O3B_LIMIT_PRICE_BUY: 1013>, 'OPT_NEEQ_O3B_LIMIT_PRICE_SELL': <EOperationType.OPT_NEEQ_O3B_LIMIT_PRICE_SELL: 1014>, 'OPT_N3B_CALL_AUCTION_BUY': <EOperationType.OPT_N3B_CALL_AUCTION_BUY: 1027>, 'OPT_N3B_CALL_AUCTION_SELL': <EOperationType.OPT_N3B_CALL_AUCTION_SELL: 1028>, 'OPT_N3B_AFTER_HOURS_BUY': <EOperationType.OPT_N3B_AFTER_HOURS_BUY: 1029>, 'OPT_N3B_AFTER_HOURS_SELL': <EOperationType.OPT_N3B_AFTER_HOURS_SELL: 1030>, 'OPT_NEEQ_O3B_CONTINUOUS_AUCTION_BUY': <EOperationType.OPT_NEEQ_O3B_CONTINUOUS_AUCTION_BUY: 1099>, 'OPT_NEEQ_O3B_CONTINUOUS_AUCTION_SELL': <EOperationType.OPT_NEEQ_O3B_CONTINUOUS_AUCTION_SELL: 1100>, 'OPT_NEEQ_O3B_ASK_PRICE': <EOperationType.OPT_NEEQ_O3B_ASK_PRICE: 1101>, 'OPT_NEEQ_O3B_PRICE_CONFIRM': <EOperationType.OPT_NEEQ_O3B_PRICE_CONFIRM: 1102>, 'OPT_NEEQ_O3B_BLOCKTRADING_BUY': <EOperationType.OPT_NEEQ_O3B_BLOCKTRADING_BUY: 1103>, 'OPT_NEEQ_O3B_BLOCKTRADING_SELL': <EOperationType.OPT_NEEQ_O3B_BLOCKTRADING_SELL: 1104>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EOptionType:
    """
    股票期权合约类型
    
    Members:
    
      OPTION_TYPE_CALL : 认购合约
    
      OPTION_TYPE_PUT : 认沽合约
    """
    OPTION_TYPE_CALL: typing.ClassVar[EOptionType]  # value = <EOptionType.OPTION_TYPE_CALL: 48>
    OPTION_TYPE_PUT: typing.ClassVar[EOptionType]  # value = <EOptionType.OPTION_TYPE_PUT: 49>
    __members__: typing.ClassVar[dict[str, EOptionType]]  # value = {'OPTION_TYPE_CALL': <EOptionType.OPTION_TYPE_CALL: 48>, 'OPTION_TYPE_PUT': <EOptionType.OPTION_TYPE_PUT: 49>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EOrderCommandStatus:
    """
    指令状态
    
    Members:
    
      OCS_CHECKING : 风控检查中
    
      OCS_APPROVING : 审批中
    
      OCS_REJECTED : 已驳回
    
      OCS_RUNNING : 运行中
    
      OCS_CANCELING : 撤销中
    
      OCS_FINISHED : 已完成
    
      OCS_STOPPED : 已撤销
    
      OCS_FROCE_COMPLETED : 强制撤销
    
      OCS_CHECKFAILED : 风控驳回
    
      OCS_CANCELING_APPROVING : 撤销审批中
    
      OCS_CANCELING_REJECTED : 撤销驳回
    
      OCS_PAUSE_PAUSEORDER : 暂停指令并暂停任务
    
      OCS_PAUSE_CANCELORDER : 暂停指令并撤销任务
    """
    OCS_APPROVING: typing.ClassVar[EOrderCommandStatus]  # value = <EOrderCommandStatus.OCS_APPROVING: 0>
    OCS_CANCELING: typing.ClassVar[EOrderCommandStatus]  # value = <EOrderCommandStatus.OCS_CANCELING: 3>
    OCS_CANCELING_APPROVING: typing.ClassVar[EOrderCommandStatus]  # value = <EOrderCommandStatus.OCS_CANCELING_APPROVING: 8>
    OCS_CANCELING_REJECTED: typing.ClassVar[EOrderCommandStatus]  # value = <EOrderCommandStatus.OCS_CANCELING_REJECTED: 9>
    OCS_CHECKFAILED: typing.ClassVar[EOrderCommandStatus]  # value = <EOrderCommandStatus.OCS_CHECKFAILED: 7>
    OCS_CHECKING: typing.ClassVar[EOrderCommandStatus]  # value = <EOrderCommandStatus.OCS_CHECKING: -1>
    OCS_FINISHED: typing.ClassVar[EOrderCommandStatus]  # value = <EOrderCommandStatus.OCS_FINISHED: 4>
    OCS_FROCE_COMPLETED: typing.ClassVar[EOrderCommandStatus]  # value = <EOrderCommandStatus.OCS_FROCE_COMPLETED: 6>
    OCS_PAUSE_CANCELORDER: typing.ClassVar[EOrderCommandStatus]  # value = <EOrderCommandStatus.OCS_PAUSE_CANCELORDER: 15>
    OCS_PAUSE_PAUSEORDER: typing.ClassVar[EOrderCommandStatus]  # value = <EOrderCommandStatus.OCS_PAUSE_PAUSEORDER: 14>
    OCS_REJECTED: typing.ClassVar[EOrderCommandStatus]  # value = <EOrderCommandStatus.OCS_REJECTED: 1>
    OCS_RUNNING: typing.ClassVar[EOrderCommandStatus]  # value = <EOrderCommandStatus.OCS_RUNNING: 2>
    OCS_STOPPED: typing.ClassVar[EOrderCommandStatus]  # value = <EOrderCommandStatus.OCS_STOPPED: 5>
    __members__: typing.ClassVar[dict[str, EOrderCommandStatus]]  # value = {'OCS_CHECKING': <EOrderCommandStatus.OCS_CHECKING: -1>, 'OCS_APPROVING': <EOrderCommandStatus.OCS_APPROVING: 0>, 'OCS_REJECTED': <EOrderCommandStatus.OCS_REJECTED: 1>, 'OCS_RUNNING': <EOrderCommandStatus.OCS_RUNNING: 2>, 'OCS_CANCELING': <EOrderCommandStatus.OCS_CANCELING: 3>, 'OCS_FINISHED': <EOrderCommandStatus.OCS_FINISHED: 4>, 'OCS_STOPPED': <EOrderCommandStatus.OCS_STOPPED: 5>, 'OCS_FROCE_COMPLETED': <EOrderCommandStatus.OCS_FROCE_COMPLETED: 6>, 'OCS_CHECKFAILED': <EOrderCommandStatus.OCS_CHECKFAILED: 7>, 'OCS_CANCELING_APPROVING': <EOrderCommandStatus.OCS_CANCELING_APPROVING: 8>, 'OCS_CANCELING_REJECTED': <EOrderCommandStatus.OCS_CANCELING_REJECTED: 9>, 'OCS_PAUSE_PAUSEORDER': <EOrderCommandStatus.OCS_PAUSE_PAUSEORDER: 14>, 'OCS_PAUSE_CANCELORDER': <EOrderCommandStatus.OCS_PAUSE_CANCELORDER: 15>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EOrderStrategyType:
    """
    算法下单方式
    
    Members:
    
      E_ORDER_STRATEGY_TYPE_NORMAL : 普通
    
      E_ORDER_STRATEGY_TYPE_APPROACH : 近场交易，需要服务支持
    """
    E_ORDER_STRATEGY_TYPE_APPROACH: typing.ClassVar[EOrderStrategyType]  # value = <EOrderStrategyType.E_ORDER_STRATEGY_TYPE_APPROACH: 0>
    E_ORDER_STRATEGY_TYPE_NORMAL: typing.ClassVar[EOrderStrategyType]  # value = <EOrderStrategyType.E_ORDER_STRATEGY_TYPE_NORMAL: -1>
    __members__: typing.ClassVar[dict[str, EOrderStrategyType]]  # value = {'E_ORDER_STRATEGY_TYPE_NORMAL': <EOrderStrategyType.E_ORDER_STRATEGY_TYPE_NORMAL: -1>, 'E_ORDER_STRATEGY_TYPE_APPROACH': <EOrderStrategyType.E_ORDER_STRATEGY_TYPE_APPROACH: 0>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EPortfolioType:
    """
    投组类型
    
    Members:
    
      PF_TYPE_NORMAL : 普通
    
      PF_TYPE_USER : 用户默认
    
      PF_TYPE_ACCOUNT : 账号默认
    
      PF_TYPE_DAILY_PRODUCT_DEFAULT : 按照产品每日自动创建的用于归集没有投组编号的数据
    
      PF_TYPE_EMULATION_ACCOUNT : 仿真账号
    
      PF_TYPE_NON_SELF_DEFAULT : 用于存储用户所在产品非用户产生的所有交易的默认投组
    
      PF_TYPE_PRODUCT_DEFAULT : 按照产品归集没有投组编号的数据
    
      PF_TYPE_COMPETITION_ACCOUNT : 炒股大赛仿真账号, 不能调用修改持仓类的API
    
      PF_TYPE_ETF_ARBITRAGE : ETF套利数据
    
      PF_TYPE_ACCOUNT_ETF_REDEMPTION : 用于存储账号所有ETF申赎数据
    
      PF_TYPE_ASSETUNIT_STAT : 用于资产单元比对数据
    """
    PF_TYPE_ACCOUNT: typing.ClassVar[EPortfolioType]  # value = <EPortfolioType.PF_TYPE_ACCOUNT: 2>
    PF_TYPE_ACCOUNT_ETF_REDEMPTION: typing.ClassVar[EPortfolioType]  # value = <EPortfolioType.PF_TYPE_ACCOUNT_ETF_REDEMPTION: 9>
    PF_TYPE_ASSETUNIT_STAT: typing.ClassVar[EPortfolioType]  # value = <EPortfolioType.PF_TYPE_ASSETUNIT_STAT: 10>
    PF_TYPE_COMPETITION_ACCOUNT: typing.ClassVar[EPortfolioType]  # value = <EPortfolioType.PF_TYPE_COMPETITION_ACCOUNT: 7>
    PF_TYPE_DAILY_PRODUCT_DEFAULT: typing.ClassVar[EPortfolioType]  # value = <EPortfolioType.PF_TYPE_DAILY_PRODUCT_DEFAULT: 3>
    PF_TYPE_EMULATION_ACCOUNT: typing.ClassVar[EPortfolioType]  # value = <EPortfolioType.PF_TYPE_EMULATION_ACCOUNT: 4>
    PF_TYPE_ETF_ARBITRAGE: typing.ClassVar[EPortfolioType]  # value = <EPortfolioType.PF_TYPE_ETF_ARBITRAGE: 8>
    PF_TYPE_NON_SELF_DEFAULT: typing.ClassVar[EPortfolioType]  # value = <EPortfolioType.PF_TYPE_NON_SELF_DEFAULT: 6>
    PF_TYPE_NORMAL: typing.ClassVar[EPortfolioType]  # value = <EPortfolioType.PF_TYPE_NORMAL: 0>
    PF_TYPE_PRODUCT_DEFAULT: typing.ClassVar[EPortfolioType]  # value = <EPortfolioType.PF_TYPE_PRODUCT_DEFAULT: 5>
    PF_TYPE_USER: typing.ClassVar[EPortfolioType]  # value = <EPortfolioType.PF_TYPE_USER: 1>
    __members__: typing.ClassVar[dict[str, EPortfolioType]]  # value = {'PF_TYPE_NORMAL': <EPortfolioType.PF_TYPE_NORMAL: 0>, 'PF_TYPE_USER': <EPortfolioType.PF_TYPE_USER: 1>, 'PF_TYPE_ACCOUNT': <EPortfolioType.PF_TYPE_ACCOUNT: 2>, 'PF_TYPE_DAILY_PRODUCT_DEFAULT': <EPortfolioType.PF_TYPE_DAILY_PRODUCT_DEFAULT: 3>, 'PF_TYPE_EMULATION_ACCOUNT': <EPortfolioType.PF_TYPE_EMULATION_ACCOUNT: 4>, 'PF_TYPE_NON_SELF_DEFAULT': <EPortfolioType.PF_TYPE_NON_SELF_DEFAULT: 6>, 'PF_TYPE_PRODUCT_DEFAULT': <EPortfolioType.PF_TYPE_PRODUCT_DEFAULT: 5>, 'PF_TYPE_COMPETITION_ACCOUNT': <EPortfolioType.PF_TYPE_COMPETITION_ACCOUNT: 7>, 'PF_TYPE_ETF_ARBITRAGE': <EPortfolioType.PF_TYPE_ETF_ARBITRAGE: 8>, 'PF_TYPE_ACCOUNT_ETF_REDEMPTION': <EPortfolioType.PF_TYPE_ACCOUNT_ETF_REDEMPTION: 9>, 'PF_TYPE_ASSETUNIT_STAT': <EPortfolioType.PF_TYPE_ASSETUNIT_STAT: 10>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EPriceType:
    """
    下单价格类型
    
    Members:
    
      PRTP_INVALID : 
    
      PRTP_SALE5 : 卖5
    
      PRTP_SALE4 : 卖4
    
      PRTP_SALE3 : 卖3
    
      PRTP_SALE2 : 卖2
    
      PRTP_SALE1 : 卖1
    
      PRTP_LATEST : 最新价
    
      PRTP_BUY1 : 买1
    
      PRTP_BUY2 : 买2
    
      PRTP_BUY3 : 买3
    
      PRTP_BUY4 : 买4
    
      PRTP_BUY5 : 买5
    
      PRTP_FIX : 指定价
    
      PRTP_MARKET : 市价
    
      PRTP_HANG : 挂单价 跟盘价
    
      PRTP_COMPETE : 对手价
    
      PRTP_MARKET_BEST : 市价_最优价
    
      PRTP_MARKET_CANCEL : 市价_即成剩撤
    
      PRTP_MARKET_CANCEL_ALL : 市价_全额成交或撤
    
      PRTP_MARKET_CANCEL_1 : 市价_最优1档即成剩撤
    
      PRTP_MARKET_CANCEL_5 : 市价_最优5档即成剩撤
    
      PRTP_MARKET_CONVERT_1 : 市价_最优1档即成剩转
    
      PRTP_MARKET_CONVERT_5 : 市价_最优5档即成剩转
    
      PRTP_STK_OPTION_FIX_CANCEL_ALL : 限价即时全部成交否则撤单
    
      PRTP_STK_OPTION_MARKET_CACEL_LEFT : 市价即时成交剩余撤单
    
      PRTP_STK_OPTION_MARKET_CANCEL_ALL : 市价即时全部成交否则撤单
    
      PRTP_STK_OPTION_MARKET_CONVERT_FIX : 市价剩余转限价
    
      PRTP_MARKET_SH_CONVERT_5_CANCEL : 最优五档即时成交剩余撤销
    
      PRTP_MARKET_SH_CONVERT_5_LIMIT : 最优五档即时成交剩转限价
    
      PRTP_MARKET_PEER_PRICE_FIRST : 对手方最优价格委托，可用于上海科创板市价
    
      PRTP_MARKET_MINE_PRICE_FIRST : 本方最优价格委托，可用于上海科创板市价
    
      PRTP_MARKET_SZ_INSTBUSI_RESTCANCEL : 即时成交剩余撤销委托
    
      PRTP_MARKET_SZ_CONVERT_5_CANCEL : 最优五档即时成交剩余撤销委托
    
      PRTP_MARKET_SZ_FULL_REAL_CANCEL : 全额成交或撤销委托
    
      PRTP_AFTER_FIX_PRICE : 盘后定价申报
    
      PRTP_OPTION_COMB_STRATEGY_CNSJC : 股票期权-认购牛市价差策略
    
      PRTP_OPTION_COMB_STRATEGY_PXSJC : 股票期权-认沽熊市价差策略
    
      PRTP_OPTION_COMB_STRATEGY_PNSJC : 股票期权-认沽牛市价差策略
    
      PRTP_OPTION_COMB_STRATEGY_CXSJC : 股票期权-认购熊市价差策略
    
      PRTP_OPTION_COMB_STRATEGY_KS : 股票期权-跨式空头
    
      PRTP_OPTION_COMB_STRATEGY_KKS : 股票期权-宽跨式空头
    
      PRTP_OPTION_COMB_STRATEGY_ZBD : 股票期权-保证金开仓转备兑开仓
    
      PRTP_OPTION_COMB_STRATEGY_ZXJ : 股票期权-备兑开仓转保证金开仓
    
      _C_PRTP_COUNT : 
    """
    PRTP_AFTER_FIX_PRICE: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_AFTER_FIX_PRICE: 49>
    PRTP_BUY1: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_BUY1: 6>
    PRTP_BUY2: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_BUY2: 7>
    PRTP_BUY3: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_BUY3: 8>
    PRTP_BUY4: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_BUY4: 9>
    PRTP_BUY5: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_BUY5: 10>
    PRTP_COMPETE: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_COMPETE: 14>
    PRTP_FIX: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_FIX: 11>
    PRTP_HANG: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_HANG: 13>
    PRTP_INVALID: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_INVALID: -1>
    PRTP_LATEST: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_LATEST: 5>
    PRTP_MARKET: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_MARKET: 12>
    PRTP_MARKET_BEST: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_MARKET_BEST: 18>
    PRTP_MARKET_CANCEL: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_MARKET_CANCEL: 19>
    PRTP_MARKET_CANCEL_1: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_MARKET_CANCEL_1: 21>
    PRTP_MARKET_CANCEL_5: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_MARKET_CANCEL_5: 22>
    PRTP_MARKET_CANCEL_ALL: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_MARKET_CANCEL_ALL: 20>
    PRTP_MARKET_CONVERT_1: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_MARKET_CONVERT_1: 23>
    PRTP_MARKET_CONVERT_5: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_MARKET_CONVERT_5: 24>
    PRTP_MARKET_MINE_PRICE_FIRST: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_MARKET_MINE_PRICE_FIRST: 45>
    PRTP_MARKET_PEER_PRICE_FIRST: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_MARKET_PEER_PRICE_FIRST: 44>
    PRTP_MARKET_SH_CONVERT_5_CANCEL: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_MARKET_SH_CONVERT_5_CANCEL: 42>
    PRTP_MARKET_SH_CONVERT_5_LIMIT: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_MARKET_SH_CONVERT_5_LIMIT: 43>
    PRTP_MARKET_SZ_CONVERT_5_CANCEL: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_MARKET_SZ_CONVERT_5_CANCEL: 47>
    PRTP_MARKET_SZ_FULL_REAL_CANCEL: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_MARKET_SZ_FULL_REAL_CANCEL: 48>
    PRTP_MARKET_SZ_INSTBUSI_RESTCANCEL: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_MARKET_SZ_INSTBUSI_RESTCANCEL: 46>
    PRTP_OPTION_COMB_STRATEGY_CNSJC: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_OPTION_COMB_STRATEGY_CNSJC: 50>
    PRTP_OPTION_COMB_STRATEGY_CXSJC: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_OPTION_COMB_STRATEGY_CXSJC: 53>
    PRTP_OPTION_COMB_STRATEGY_KKS: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_OPTION_COMB_STRATEGY_KKS: 55>
    PRTP_OPTION_COMB_STRATEGY_KS: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_OPTION_COMB_STRATEGY_KS: 54>
    PRTP_OPTION_COMB_STRATEGY_PNSJC: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_OPTION_COMB_STRATEGY_PNSJC: 52>
    PRTP_OPTION_COMB_STRATEGY_PXSJC: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_OPTION_COMB_STRATEGY_PXSJC: 51>
    PRTP_OPTION_COMB_STRATEGY_ZBD: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_OPTION_COMB_STRATEGY_ZBD: 56>
    PRTP_OPTION_COMB_STRATEGY_ZXJ: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_OPTION_COMB_STRATEGY_ZXJ: 57>
    PRTP_SALE1: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_SALE1: 4>
    PRTP_SALE2: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_SALE2: 3>
    PRTP_SALE3: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_SALE3: 2>
    PRTP_SALE4: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_SALE4: 1>
    PRTP_SALE5: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_SALE5: 0>
    PRTP_STK_OPTION_FIX_CANCEL_ALL: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_STK_OPTION_FIX_CANCEL_ALL: 26>
    PRTP_STK_OPTION_MARKET_CACEL_LEFT: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_STK_OPTION_MARKET_CACEL_LEFT: 27>
    PRTP_STK_OPTION_MARKET_CANCEL_ALL: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_STK_OPTION_MARKET_CANCEL_ALL: 28>
    PRTP_STK_OPTION_MARKET_CONVERT_FIX: typing.ClassVar[EPriceType]  # value = <EPriceType.PRTP_STK_OPTION_MARKET_CONVERT_FIX: 29>
    _C_PRTP_COUNT: typing.ClassVar[EPriceType]  # value = <EPriceType._C_PRTP_COUNT: 58>
    __members__: typing.ClassVar[dict[str, EPriceType]]  # value = {'PRTP_INVALID': <EPriceType.PRTP_INVALID: -1>, 'PRTP_SALE5': <EPriceType.PRTP_SALE5: 0>, 'PRTP_SALE4': <EPriceType.PRTP_SALE4: 1>, 'PRTP_SALE3': <EPriceType.PRTP_SALE3: 2>, 'PRTP_SALE2': <EPriceType.PRTP_SALE2: 3>, 'PRTP_SALE1': <EPriceType.PRTP_SALE1: 4>, 'PRTP_LATEST': <EPriceType.PRTP_LATEST: 5>, 'PRTP_BUY1': <EPriceType.PRTP_BUY1: 6>, 'PRTP_BUY2': <EPriceType.PRTP_BUY2: 7>, 'PRTP_BUY3': <EPriceType.PRTP_BUY3: 8>, 'PRTP_BUY4': <EPriceType.PRTP_BUY4: 9>, 'PRTP_BUY5': <EPriceType.PRTP_BUY5: 10>, 'PRTP_FIX': <EPriceType.PRTP_FIX: 11>, 'PRTP_MARKET': <EPriceType.PRTP_MARKET: 12>, 'PRTP_HANG': <EPriceType.PRTP_HANG: 13>, 'PRTP_COMPETE': <EPriceType.PRTP_COMPETE: 14>, 'PRTP_MARKET_BEST': <EPriceType.PRTP_MARKET_BEST: 18>, 'PRTP_MARKET_CANCEL': <EPriceType.PRTP_MARKET_CANCEL: 19>, 'PRTP_MARKET_CANCEL_ALL': <EPriceType.PRTP_MARKET_CANCEL_ALL: 20>, 'PRTP_MARKET_CANCEL_1': <EPriceType.PRTP_MARKET_CANCEL_1: 21>, 'PRTP_MARKET_CANCEL_5': <EPriceType.PRTP_MARKET_CANCEL_5: 22>, 'PRTP_MARKET_CONVERT_1': <EPriceType.PRTP_MARKET_CONVERT_1: 23>, 'PRTP_MARKET_CONVERT_5': <EPriceType.PRTP_MARKET_CONVERT_5: 24>, 'PRTP_STK_OPTION_FIX_CANCEL_ALL': <EPriceType.PRTP_STK_OPTION_FIX_CANCEL_ALL: 26>, 'PRTP_STK_OPTION_MARKET_CACEL_LEFT': <EPriceType.PRTP_STK_OPTION_MARKET_CACEL_LEFT: 27>, 'PRTP_STK_OPTION_MARKET_CANCEL_ALL': <EPriceType.PRTP_STK_OPTION_MARKET_CANCEL_ALL: 28>, 'PRTP_STK_OPTION_MARKET_CONVERT_FIX': <EPriceType.PRTP_STK_OPTION_MARKET_CONVERT_FIX: 29>, 'PRTP_MARKET_SH_CONVERT_5_CANCEL': <EPriceType.PRTP_MARKET_SH_CONVERT_5_CANCEL: 42>, 'PRTP_MARKET_SH_CONVERT_5_LIMIT': <EPriceType.PRTP_MARKET_SH_CONVERT_5_LIMIT: 43>, 'PRTP_MARKET_PEER_PRICE_FIRST': <EPriceType.PRTP_MARKET_PEER_PRICE_FIRST: 44>, 'PRTP_MARKET_MINE_PRICE_FIRST': <EPriceType.PRTP_MARKET_MINE_PRICE_FIRST: 45>, 'PRTP_MARKET_SZ_INSTBUSI_RESTCANCEL': <EPriceType.PRTP_MARKET_SZ_INSTBUSI_RESTCANCEL: 46>, 'PRTP_MARKET_SZ_CONVERT_5_CANCEL': <EPriceType.PRTP_MARKET_SZ_CONVERT_5_CANCEL: 47>, 'PRTP_MARKET_SZ_FULL_REAL_CANCEL': <EPriceType.PRTP_MARKET_SZ_FULL_REAL_CANCEL: 48>, 'PRTP_AFTER_FIX_PRICE': <EPriceType.PRTP_AFTER_FIX_PRICE: 49>, 'PRTP_OPTION_COMB_STRATEGY_CNSJC': <EPriceType.PRTP_OPTION_COMB_STRATEGY_CNSJC: 50>, 'PRTP_OPTION_COMB_STRATEGY_PXSJC': <EPriceType.PRTP_OPTION_COMB_STRATEGY_PXSJC: 51>, 'PRTP_OPTION_COMB_STRATEGY_PNSJC': <EPriceType.PRTP_OPTION_COMB_STRATEGY_PNSJC: 52>, 'PRTP_OPTION_COMB_STRATEGY_CXSJC': <EPriceType.PRTP_OPTION_COMB_STRATEGY_CXSJC: 53>, 'PRTP_OPTION_COMB_STRATEGY_KS': <EPriceType.PRTP_OPTION_COMB_STRATEGY_KS: 54>, 'PRTP_OPTION_COMB_STRATEGY_KKS': <EPriceType.PRTP_OPTION_COMB_STRATEGY_KKS: 55>, 'PRTP_OPTION_COMB_STRATEGY_ZBD': <EPriceType.PRTP_OPTION_COMB_STRATEGY_ZBD: 56>, 'PRTP_OPTION_COMB_STRATEGY_ZXJ': <EPriceType.PRTP_OPTION_COMB_STRATEGY_ZXJ: 57>, '_C_PRTP_COUNT': <EPriceType._C_PRTP_COUNT: 58>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EProductClass:
    """
    合约类型
    
    Members:
    
      PRODECT_CLASS_NORMAL : 其他合约
    
      PRODECT_CLASS_FUTURE : 期货合约
    
      PRODECT_CLASS_FUTURE_OPTION : 期货期权合约
    """
    PRODECT_CLASS_FUTURE: typing.ClassVar[EProductClass]  # value = <EProductClass.PRODECT_CLASS_FUTURE: 1>
    PRODECT_CLASS_FUTURE_OPTION: typing.ClassVar[EProductClass]  # value = <EProductClass.PRODECT_CLASS_FUTURE_OPTION: 2>
    PRODECT_CLASS_NORMAL: typing.ClassVar[EProductClass]  # value = <EProductClass.PRODECT_CLASS_NORMAL: 0>
    __members__: typing.ClassVar[dict[str, EProductClass]]  # value = {'PRODECT_CLASS_NORMAL': <EProductClass.PRODECT_CLASS_NORMAL: 0>, 'PRODECT_CLASS_FUTURE': <EProductClass.PRODECT_CLASS_FUTURE: 1>, 'PRODECT_CLASS_FUTURE_OPTION': <EProductClass.PRODECT_CLASS_FUTURE_OPTION: 2>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EReplaceFlag:
    """
    现金替代标识
    
    Members:
    
      XT_REPLACE_FLAG_CASH_FORBID : 禁止现金替代（必须有股票）
    
      XT_REPLACE_FLAG_CASH_ENABLE : 允许现金替代（先用股票，股票不足的话用现金替代）
    
      XT_REPLACE_FLAG_CASH_REQUIRED : 必须现金替代
    
      XT_REPLACE_FLAG_NO_SH_CASH_FILL : 非沪市（股票）退补现金替代
    
      XT_REPLACE_FLAG_NO_SH_CASH_REQ : 非沪市（股票）必须现金替代
    
      XT_REPLACE_FLAG_NO_SH_SZ_CASH_FILL : 非沪深退补现金替代
    
      XT_REPLACE_FLAG_NO_SH_SZ_CASH_REQ : 非沪深必须现金替代
    
      XT_REPLACE_FLAG_RETURN_SH_SZ_HK : 港市退补现金替代（仅适用于跨沪深ETF产品）
    
      XT_REPLACE_FLAG_MUST_SH_SZ_HK : 港市必须现金替代（仅适用于跨沪深ETF产品）
    """
    XT_REPLACE_FLAG_CASH_ENABLE: typing.ClassVar[EReplaceFlag]  # value = <EReplaceFlag.XT_REPLACE_FLAG_CASH_ENABLE: 49>
    XT_REPLACE_FLAG_CASH_FORBID: typing.ClassVar[EReplaceFlag]  # value = <EReplaceFlag.XT_REPLACE_FLAG_CASH_FORBID: 48>
    XT_REPLACE_FLAG_CASH_REQUIRED: typing.ClassVar[EReplaceFlag]  # value = <EReplaceFlag.XT_REPLACE_FLAG_CASH_REQUIRED: 50>
    XT_REPLACE_FLAG_MUST_SH_SZ_HK: typing.ClassVar[EReplaceFlag]  # value = <EReplaceFlag.XT_REPLACE_FLAG_MUST_SH_SZ_HK: 56>
    XT_REPLACE_FLAG_NO_SH_CASH_FILL: typing.ClassVar[EReplaceFlag]  # value = <EReplaceFlag.XT_REPLACE_FLAG_NO_SH_CASH_FILL: 51>
    XT_REPLACE_FLAG_NO_SH_CASH_REQ: typing.ClassVar[EReplaceFlag]  # value = <EReplaceFlag.XT_REPLACE_FLAG_NO_SH_CASH_REQ: 52>
    XT_REPLACE_FLAG_NO_SH_SZ_CASH_FILL: typing.ClassVar[EReplaceFlag]  # value = <EReplaceFlag.XT_REPLACE_FLAG_NO_SH_SZ_CASH_FILL: 53>
    XT_REPLACE_FLAG_NO_SH_SZ_CASH_REQ: typing.ClassVar[EReplaceFlag]  # value = <EReplaceFlag.XT_REPLACE_FLAG_NO_SH_SZ_CASH_REQ: 54>
    XT_REPLACE_FLAG_RETURN_SH_SZ_HK: typing.ClassVar[EReplaceFlag]  # value = <EReplaceFlag.XT_REPLACE_FLAG_RETURN_SH_SZ_HK: 55>
    __members__: typing.ClassVar[dict[str, EReplaceFlag]]  # value = {'XT_REPLACE_FLAG_CASH_FORBID': <EReplaceFlag.XT_REPLACE_FLAG_CASH_FORBID: 48>, 'XT_REPLACE_FLAG_CASH_ENABLE': <EReplaceFlag.XT_REPLACE_FLAG_CASH_ENABLE: 49>, 'XT_REPLACE_FLAG_CASH_REQUIRED': <EReplaceFlag.XT_REPLACE_FLAG_CASH_REQUIRED: 50>, 'XT_REPLACE_FLAG_NO_SH_CASH_FILL': <EReplaceFlag.XT_REPLACE_FLAG_NO_SH_CASH_FILL: 51>, 'XT_REPLACE_FLAG_NO_SH_CASH_REQ': <EReplaceFlag.XT_REPLACE_FLAG_NO_SH_CASH_REQ: 52>, 'XT_REPLACE_FLAG_NO_SH_SZ_CASH_FILL': <EReplaceFlag.XT_REPLACE_FLAG_NO_SH_SZ_CASH_FILL: 53>, 'XT_REPLACE_FLAG_NO_SH_SZ_CASH_REQ': <EReplaceFlag.XT_REPLACE_FLAG_NO_SH_SZ_CASH_REQ: 54>, 'XT_REPLACE_FLAG_RETURN_SH_SZ_HK': <EReplaceFlag.XT_REPLACE_FLAG_RETURN_SH_SZ_HK: 55>, 'XT_REPLACE_FLAG_MUST_SH_SZ_HK': <EReplaceFlag.XT_REPLACE_FLAG_MUST_SH_SZ_HK: 56>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ESecuFundTransDirection:
    """
    资金股份划拨划拨方向
    
    Members:
    
      SECUFUNDTRANS_TRANSFER_NORMAL_TO_FAST : 从普通柜台拨入到极速柜台
    
      SECUFUNDTRANS_TRANSFER_FAST_TO_NORMAL : 从极速柜台拨出到普通柜台
    
      SECUFUNDTRANS_TRANSFER_SH_TO_SZ : 上海划到深圳(节点划拨)
    
      SECUFUNDTRANS_TRANSFER_SZ_TO_SH : 深圳划到上海(节点划拨)
    """
    SECUFUNDTRANS_TRANSFER_FAST_TO_NORMAL: typing.ClassVar[ESecuFundTransDirection]  # value = <ESecuFundTransDirection.SECUFUNDTRANS_TRANSFER_FAST_TO_NORMAL: 1>
    SECUFUNDTRANS_TRANSFER_NORMAL_TO_FAST: typing.ClassVar[ESecuFundTransDirection]  # value = <ESecuFundTransDirection.SECUFUNDTRANS_TRANSFER_NORMAL_TO_FAST: 0>
    SECUFUNDTRANS_TRANSFER_SH_TO_SZ: typing.ClassVar[ESecuFundTransDirection]  # value = <ESecuFundTransDirection.SECUFUNDTRANS_TRANSFER_SH_TO_SZ: 2>
    SECUFUNDTRANS_TRANSFER_SZ_TO_SH: typing.ClassVar[ESecuFundTransDirection]  # value = <ESecuFundTransDirection.SECUFUNDTRANS_TRANSFER_SZ_TO_SH: 3>
    __members__: typing.ClassVar[dict[str, ESecuFundTransDirection]]  # value = {'SECUFUNDTRANS_TRANSFER_NORMAL_TO_FAST': <ESecuFundTransDirection.SECUFUNDTRANS_TRANSFER_NORMAL_TO_FAST: 0>, 'SECUFUNDTRANS_TRANSFER_FAST_TO_NORMAL': <ESecuFundTransDirection.SECUFUNDTRANS_TRANSFER_FAST_TO_NORMAL: 1>, 'SECUFUNDTRANS_TRANSFER_SH_TO_SZ': <ESecuFundTransDirection.SECUFUNDTRANS_TRANSFER_SH_TO_SZ: 2>, 'SECUFUNDTRANS_TRANSFER_SZ_TO_SH': <ESecuFundTransDirection.SECUFUNDTRANS_TRANSFER_SZ_TO_SH: 3>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ESideFlag:
    """
    期权持仓类型
    
    Members:
    
      SIDE_FLAG_RIGHT : 权利
    
      SIDE_FLAG_DUTY : 义务
    
      SIDE_FLAG_COVERED : 备兑
    """
    SIDE_FLAG_COVERED: typing.ClassVar[ESideFlag]  # value = <ESideFlag.SIDE_FLAG_COVERED: 50>
    SIDE_FLAG_DUTY: typing.ClassVar[ESideFlag]  # value = <ESideFlag.SIDE_FLAG_DUTY: 49>
    SIDE_FLAG_RIGHT: typing.ClassVar[ESideFlag]  # value = <ESideFlag.SIDE_FLAG_RIGHT: 48>
    __members__: typing.ClassVar[dict[str, ESideFlag]]  # value = {'SIDE_FLAG_RIGHT': <ESideFlag.SIDE_FLAG_RIGHT: 48>, 'SIDE_FLAG_DUTY': <ESideFlag.SIDE_FLAG_DUTY: 49>, 'SIDE_FLAG_COVERED': <ESideFlag.SIDE_FLAG_COVERED: 50>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EStockType:
    """
    证券类别
    
    Members:
    
      MINOR_KIND_UNDEFINED : 默认
    
      MAJOR_KIND_INDEX : 指数
    
      MAJOR_KIND_STOCK : 股票
    
      MAJOR_KIND_FUND : 基金
    
      MAJOR_KIND_BOND : 债券
    
      MAJOR_KIND_WARRANT : 权证
    
      MAJOR_KIND_REPO : 质押式回购交易
    
      MAJOR_KIND_OPTION : 期权
    
      MAJOR_KIND_PREFERRED_STOCK : 优先股
    
      MAJOR_KIND_ABS : 资产支持证券
    
      MAJOR_KIND_FJY : 非交易
    
      MAJOR_KIND_REIT : 房地产信托投资基金
    
      SH_MINOR_KIND_STOCK_ASH : 以人民币交易的股票（主板）
    
      SH_MINOR_KIND_STOCK_BSH : 以美元交易的股票
    
      SH_MINOR_KIND_STOCK_KSH : 以人民币交易的股票（科创板）
    
      SH_MINOR_KIND_STOCK_OEQ : 其它股票
    
      SH_MINOR_KIND_FUND_CEF : 封闭式基金
    
      SH_MINOR_KIND_FUND_OEF : 开放式基金
    
      SH_MINOR_KIND_FUND_EBS : ETF基金
    
      SH_MINOR_KIND_FUND_FBL : 跨市场 / 跨境基金
    
      SH_MINOR_KIND_FUND_OFN : 其它基金
    
      SH_MINOR_KIND_FUND_LOF : LOF基金
    
      SH_MINOR_KIND_BOND_GBF : 国债、地方债、政府支持债、政策性金融债
    
      SH_MINOR_KIND_BOND_GBZ : 无息国债 (弃用)
    
      SH_MINOR_KIND_BOND_DST : 国债分销（仅用于分销阶段）
    
      SH_MINOR_KIND_BOND_DVP : 公司债（地方债）分销
    
      SH_MINOR_KIND_BOND_CBF : 企业债券
    
      SH_MINOR_KIND_BOND_CCF : 可转换企业债券
    
      SH_MINOR_KIND_BOND_CPF : 公司债、企业债、可交换债、政府支持债
    
      SH_MINOR_KIND_BOND_FBF : 金融机构发行债券 (弃用)
    
      SH_MINOR_KIND_BOND_CRP : 通用质押式回购
    
      SH_MINOR_KIND_BOND_BRP : 质押式企债回购 (弃用)
    
      SH_MINOR_KIND_BOND_ORP : 买断式债券回购 (弃用)
    
      SH_MINOR_KIND_BOND_CBD : 分离式可转债 (弃用)
    
      SH_MINOR_KIND_BOND_OBD : 其它债券
    
      SH_MINOR_KIND_BOND_WIT : 国债预发行
    
      SH_MINOR_KIND_AMP : 集合资产管理计划
    
      SH_MINOR_KIND_OPS : 公开发行优先股
    
      SH_MINOR_KIND_PPS : 非公开发行优先股
    
      SH_MINOR_KIND_QRP : 报价回购
    
      SH_MINOR_KIND_CMD : 控制指令
    
      SH_FJY_MINOR_KIND_IN : 上网证券发行申购
    
      SH_FJY_MINOR_KIND_IS : 老股东增发证券发行申购
    
      SH_FJY_MINOR_KIND_PH : IPO配号
    
      SH_FJY_MINOR_KIND_KK : IPO扣款
    
      SH_FJY_MINOR_KIND_HK : IPO还款
    
      SH_FJY_MINOR_KIND_CV : 可转债转股 / 可交换公司债换股
    
      SH_FJY_MINOR_KIND_CR : 可转债回售
    
      SH_FJY_MINOR_KIND_R1 : 股票配股行权行权
    
      SH_FJY_MINOR_KIND_R2 : 股票转配股配股行权
    
      SH_FJY_MINOR_KIND_R3 : 职工股转配股配股行权
    
      SH_FJY_MINOR_KIND_R4 : 股票配转债行权
    
      SH_FJY_MINOR_KIND_OS : 开放式基金认购
    
      SH_FJY_MINOR_KIND_OC : 开放式基金申购
    
      SH_FJY_MINOR_KIND_OR : 开放式基金赎回
    
      SH_FJY_MINOR_KIND_OD : 开放式基金分红选择
    
      SH_FJY_MINOR_KIND_OT : 开放式基金份额转出
    
      SH_FJY_MINOR_KIND_OV : 开放式基金转换
    
      SH_FJY_MINOR_KIND_EC : ETF申购
    
      SH_FJY_MINOR_KIND_ER : ETF赎回
    
      SH_FJY_MINOR_KIND_EZ : 申赎资金代码
    
      SH_FJY_MINOR_KIND_BD : 回购入库
    
      SH_FJY_MINOR_KIND_BW : 回购出库
    
      SH_FJY_MINOR_KIND_FS : 要约预受
    
      SH_FJY_MINOR_KIND_FC : 要约撤销
    
      SH_FJY_MINOR_KIND_ST : 余券划转
    
      SH_FJY_MINOR_KIND_SR : 还券划转
    
      SH_FJY_MINOR_KIND_CI : 担保品划入
    
      SH_FJY_MINOR_KIND_CO : 担保品划出
    
      SH_FJY_MINOR_KIND_SI : 券源划入
    
      SH_FJY_MINOR_KIND_SO : 券源划出
    
      SH_FJY_MINOR_KIND_PA : 密码激活(注销)
    
      SH_FJY_MINOR_KIND_DT : 指定登记
    
      SH_FJY_MINOR_KIND_DC : 指定撤销
    
      SH_FJY_MINOR_KIND_QT : 其它
    
      SH_MINOR_KIND_FUND_KES : 科创板ETF基金
    
      SH_MINOR_KIND_FUND_KOF : 科创板LOF基金
    
      SH_MINOR_KIND_BOND_TCB : 定向可转债
    
      SH_MINOR_KIND_BOND_KCCF : 科创板可转债
    
      SH_MINOR_KIND_REITS_RET : REITs
    
      SZ_MINOR_KIND_STOCK_ZHU_BAN_A : 主板 A 股
    
      SZ_MINOR_KIND_STOCK_ZHONG_XIAO_BAN : 中小板股票
    
      SZ_MINOR_KIND_STOCK_CHUANG_YE_BAN : 创业板股票
    
      SZ_MINOR_KIND_STOCK_ZHU_BAN_B : 主板 B 股
    
      SZ_MINOR_KIND_BOND_TREASURY_BOND : 国债（含地方债）
    
      SZ_MINOR_KIND_BOND_ENTERPRISE_BOND : 企业债
    
      SZ_MINOR_KIND_BOND_CORPORATE_BOND : 公司债
    
      SZ_MINOR_KIND_BOND_CONVERTIBLE_BOND : 可转债
    
      SZ_MINOR_KIND_BOND_PRIVATELY_RAISED_COMPANY_BONDS : 私募债
    
      SZ_MINOR_KIND_BOND_EXCHANGEABLE_PB : 可交换私募债
    
      SZ_MINOR_KIND_BOND_SECURITY_COMPANY_SUB_DEBT : 证券公司次级债
    
      SZ_MINOR_KIND_REPO_PLEDGE_STYLE_REPO : 质押式回购
    
      SZ_MINOR_KIND_ASSET_BACKED_SECURITIES : 资产支持证券
    
      SZ_MINOR_KIND_FUND_STOCK_ETF : 本市场股票 ETF
    
      SZ_MINOR_KIND_FUND_INTER_MARKET_STOCK_ETF : 跨市场股票 ETF
    
      SZ_MINOR_KIND_FUND_CROSS_BORDER_ETF : 跨境 ETF
    
      SZ_MINOR_KIND_FUND_BEARER_BOND_ETF : 本市场实物债券 ETF
    
      SZ_MINOR_KIND_FUND_CASH_BOND_ETF : 现金债券 ETF
    
      SZ_MINOR_KIND_FUND_GOLD_ETF : 黄金ETF
    
      SZ_MINOR_KIND_FUND_CURRENCY_ETF : 货币ETF
    
      SZ_MINOR_KIND_FUND_LEVER_ETF : 杠杆ETF
    
      SZ_MINOR_KIND_FUND_COMMODITY_FUTURES_ETF : 商品期货ETF
    
      SZ_MINOR_KIND_FUND_STANDARD_LOF : 标准 LOF
    
      SZ_MINOR_KIND_FUND_GRADED_SUB_FUNDS : 分级子基金
    
      SZ_MINOR_KIND_FUND_CLOSED_END_FUNDS : 封闭式基金
    
      SZ_MINOR_KIND_FUND_REDEMPTION_FUND : 仅申赎基金
    
      SZ_MINOR_KIND_WARRANT : 权证
    
      SZ_MINOR_KIND_OPTION_STOCK_OPTION : 个股期权
    
      SZ_MINOR_KIND_OPTION_ETF_OPTION : ETF期权
    
      SZ_MINOR_KIND_PREFERRED_STOCK : 优先股
    
      SZ_MINOR_KIND_BOND_SECURITY_COMPANY_SHORT_TERM_BOND : 证券公司短期债
    
      SZ_MINOR_KIND_BOND_EXCHANGEABLE_CORPORATE_BOND : 可交换公司债
    
      SZ_MINOR_KIND_STOCK_CDR : 主板、中小板存托凭证
    
      SZ_MINOR_KIND_STOCK_CHUANG_YE_CDR : 创业板存托凭证
    
      SZ_MINOR_KIND_FUND_INFRASTRUCTURE_FUND : 基础设施基金
    
      SZ_MINOR_KIND_BOND_ORIENT_CONVERTIBLE_BOND : 定向可转债
    
      SZ_FJY_MINOR_KIND_ISSUE : 网上认购
    
      SZ_FJY_MINOR_KIND_BOND_DISTRIBUTION : 债券分销
    
      SZ_FJY_MINOR_KIND_RIGHTS_ISSUE : 配股
    
      SZ_FJY_MINOR_KIND_DERIVATIVEAUCTION : 衍生品交易
    
      SZ_FJY_MINOR_KIND_NEGOTIATION : 协议交易
    
      SZ_FJY_MINOR_KIND_ISSUE_ADDITIONNAL : 增发
    
      SZ_FJY_MINOR_KIND_BOND_RIGHTS_ISSUE : 配债
    
      NEEQ_MINOR_KIND_STOCK_DELIST_COMPANY_A : 两网公司及退市公司A股
    
      NEEQ_MINOR_KIND_STOCK_DELIST_COMPANY_B : 两网公司及退市公司B股
    
      NEEQ_MINOR_KIND_STOCK_LISTED_COMPANY : 挂牌公司股票
    
      NEEQ_MINOR_KIND_PREFERRED_STOCK : 优先股
    
      NEEQ_MINOR_KIND_TENDER_OFFER : 要约收购
    
      NEEQ_MINOR_KIND_OFFER_TO_REPURCHASE : 要约回购
    
      NEEQ_MINOR_KIND_EQUITY_INCENTIVE_OPTION : 股权激励期权
    
      NEEQ_MINOR_KIND_INDEX : 指数
    
      NEEQ_MINOR_KIND_ISSUE_TRANSACTION : 发行业务
    
      NEEQ_MINOR_KIND_CONVERTIBLE_BOND : 可转债
    
      NEEQ_MINOR_KIND_ORIENT_CONVERTIBLE_BOND : 定向可转债
    
      NEEQ_MINOR_KIND_DELIST_CONVERTIBLE_BOND : 退市可转债
    
      SHFI_MINOR_KIND_TREASURY_BOND : 国债
    
      SHFI_MINOR_KIND_CORPORATE_BOND : 公司债
    
      SHFI_MINOR_KIND_PRIVATE_PLACEMENT_BOND : 私募债券
    
      SHFI_MINOR_KIND_ABS : 信贷资产支持证券
    
      SHFI_MINOR_KIND_SPECIAL_BOND : 特定债券
    
      SHFI_MINOR_KIND_REITS : 公募REITs
    
      SHFI_MINOR_KIND_CONVERTIBLE_BOND : 公开市场转换债券
    """
    MAJOR_KIND_ABS: typing.ClassVar[EStockType]  # value = <EStockType.MAJOR_KIND_ABS: 9>
    MAJOR_KIND_BOND: typing.ClassVar[EStockType]  # value = <EStockType.MAJOR_KIND_BOND: 4>
    MAJOR_KIND_FJY: typing.ClassVar[EStockType]  # value = <EStockType.MAJOR_KIND_FJY: 10>
    MAJOR_KIND_FUND: typing.ClassVar[EStockType]  # value = <EStockType.MAJOR_KIND_FUND: 3>
    MAJOR_KIND_INDEX: typing.ClassVar[EStockType]  # value = <EStockType.MAJOR_KIND_INDEX: 1>
    MAJOR_KIND_OPTION: typing.ClassVar[EStockType]  # value = <EStockType.MAJOR_KIND_OPTION: 7>
    MAJOR_KIND_PREFERRED_STOCK: typing.ClassVar[EStockType]  # value = <EStockType.MAJOR_KIND_PREFERRED_STOCK: 8>
    MAJOR_KIND_REIT: typing.ClassVar[EStockType]  # value = <EStockType.MAJOR_KIND_REIT: 11>
    MAJOR_KIND_REPO: typing.ClassVar[EStockType]  # value = <EStockType.MAJOR_KIND_REPO: 6>
    MAJOR_KIND_STOCK: typing.ClassVar[EStockType]  # value = <EStockType.MAJOR_KIND_STOCK: 2>
    MAJOR_KIND_WARRANT: typing.ClassVar[EStockType]  # value = <EStockType.MAJOR_KIND_WARRANT: 5>
    MINOR_KIND_UNDEFINED: typing.ClassVar[EStockType]  # value = <EStockType.MINOR_KIND_UNDEFINED: 0>
    NEEQ_MINOR_KIND_CONVERTIBLE_BOND: typing.ClassVar[EStockType]  # value = <EStockType.NEEQ_MINOR_KIND_CONVERTIBLE_BOND: 132>
    NEEQ_MINOR_KIND_DELIST_CONVERTIBLE_BOND: typing.ClassVar[EStockType]  # value = <EStockType.NEEQ_MINOR_KIND_DELIST_CONVERTIBLE_BOND: 134>
    NEEQ_MINOR_KIND_EQUITY_INCENTIVE_OPTION: typing.ClassVar[EStockType]  # value = <EStockType.NEEQ_MINOR_KIND_EQUITY_INCENTIVE_OPTION: 129>
    NEEQ_MINOR_KIND_INDEX: typing.ClassVar[EStockType]  # value = <EStockType.NEEQ_MINOR_KIND_INDEX: 130>
    NEEQ_MINOR_KIND_ISSUE_TRANSACTION: typing.ClassVar[EStockType]  # value = <EStockType.NEEQ_MINOR_KIND_ISSUE_TRANSACTION: 131>
    NEEQ_MINOR_KIND_OFFER_TO_REPURCHASE: typing.ClassVar[EStockType]  # value = <EStockType.NEEQ_MINOR_KIND_OFFER_TO_REPURCHASE: 128>
    NEEQ_MINOR_KIND_ORIENT_CONVERTIBLE_BOND: typing.ClassVar[EStockType]  # value = <EStockType.NEEQ_MINOR_KIND_ORIENT_CONVERTIBLE_BOND: 133>
    NEEQ_MINOR_KIND_PREFERRED_STOCK: typing.ClassVar[EStockType]  # value = <EStockType.NEEQ_MINOR_KIND_PREFERRED_STOCK: 126>
    NEEQ_MINOR_KIND_STOCK_DELIST_COMPANY_A: typing.ClassVar[EStockType]  # value = <EStockType.NEEQ_MINOR_KIND_STOCK_DELIST_COMPANY_A: 123>
    NEEQ_MINOR_KIND_STOCK_DELIST_COMPANY_B: typing.ClassVar[EStockType]  # value = <EStockType.NEEQ_MINOR_KIND_STOCK_DELIST_COMPANY_B: 124>
    NEEQ_MINOR_KIND_STOCK_LISTED_COMPANY: typing.ClassVar[EStockType]  # value = <EStockType.NEEQ_MINOR_KIND_STOCK_LISTED_COMPANY: 125>
    NEEQ_MINOR_KIND_TENDER_OFFER: typing.ClassVar[EStockType]  # value = <EStockType.NEEQ_MINOR_KIND_TENDER_OFFER: 127>
    SHFI_MINOR_KIND_ABS: typing.ClassVar[EStockType]  # value = <EStockType.SHFI_MINOR_KIND_ABS: 138>
    SHFI_MINOR_KIND_CONVERTIBLE_BOND: typing.ClassVar[EStockType]  # value = <EStockType.SHFI_MINOR_KIND_CONVERTIBLE_BOND: 141>
    SHFI_MINOR_KIND_CORPORATE_BOND: typing.ClassVar[EStockType]  # value = <EStockType.SHFI_MINOR_KIND_CORPORATE_BOND: 136>
    SHFI_MINOR_KIND_PRIVATE_PLACEMENT_BOND: typing.ClassVar[EStockType]  # value = <EStockType.SHFI_MINOR_KIND_PRIVATE_PLACEMENT_BOND: 137>
    SHFI_MINOR_KIND_REITS: typing.ClassVar[EStockType]  # value = <EStockType.SHFI_MINOR_KIND_REITS: 140>
    SHFI_MINOR_KIND_SPECIAL_BOND: typing.ClassVar[EStockType]  # value = <EStockType.SHFI_MINOR_KIND_SPECIAL_BOND: 139>
    SHFI_MINOR_KIND_TREASURY_BOND: typing.ClassVar[EStockType]  # value = <EStockType.SHFI_MINOR_KIND_TREASURY_BOND: 135>
    SH_FJY_MINOR_KIND_BD: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_BD: 61>
    SH_FJY_MINOR_KIND_BW: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_BW: 62>
    SH_FJY_MINOR_KIND_CI: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_CI: 67>
    SH_FJY_MINOR_KIND_CO: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_CO: 68>
    SH_FJY_MINOR_KIND_CR: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_CR: 47>
    SH_FJY_MINOR_KIND_CV: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_CV: 46>
    SH_FJY_MINOR_KIND_DC: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_DC: 73>
    SH_FJY_MINOR_KIND_DT: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_DT: 72>
    SH_FJY_MINOR_KIND_EC: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_EC: 58>
    SH_FJY_MINOR_KIND_ER: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_ER: 59>
    SH_FJY_MINOR_KIND_EZ: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_EZ: 60>
    SH_FJY_MINOR_KIND_FC: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_FC: 64>
    SH_FJY_MINOR_KIND_FS: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_FS: 63>
    SH_FJY_MINOR_KIND_HK: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_HK: 45>
    SH_FJY_MINOR_KIND_IN: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_IN: 41>
    SH_FJY_MINOR_KIND_IS: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_IS: 42>
    SH_FJY_MINOR_KIND_KK: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_KK: 44>
    SH_FJY_MINOR_KIND_OC: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_OC: 53>
    SH_FJY_MINOR_KIND_OD: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_OD: 55>
    SH_FJY_MINOR_KIND_OR: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_OR: 54>
    SH_FJY_MINOR_KIND_OS: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_OS: 52>
    SH_FJY_MINOR_KIND_OT: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_OT: 56>
    SH_FJY_MINOR_KIND_OV: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_OV: 57>
    SH_FJY_MINOR_KIND_PA: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_PA: 71>
    SH_FJY_MINOR_KIND_PH: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_PH: 43>
    SH_FJY_MINOR_KIND_QT: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_QT: 74>
    SH_FJY_MINOR_KIND_R1: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_R1: 48>
    SH_FJY_MINOR_KIND_R2: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_R2: 49>
    SH_FJY_MINOR_KIND_R3: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_R3: 50>
    SH_FJY_MINOR_KIND_R4: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_R4: 51>
    SH_FJY_MINOR_KIND_SI: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_SI: 69>
    SH_FJY_MINOR_KIND_SO: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_SO: 70>
    SH_FJY_MINOR_KIND_SR: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_SR: 66>
    SH_FJY_MINOR_KIND_ST: typing.ClassVar[EStockType]  # value = <EStockType.SH_FJY_MINOR_KIND_ST: 65>
    SH_MINOR_KIND_AMP: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_AMP: 36>
    SH_MINOR_KIND_BOND_BRP: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_BRP: 31>
    SH_MINOR_KIND_BOND_CBD: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_CBD: 33>
    SH_MINOR_KIND_BOND_CBF: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_CBF: 26>
    SH_MINOR_KIND_BOND_CCF: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_CCF: 27>
    SH_MINOR_KIND_BOND_CPF: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_CPF: 28>
    SH_MINOR_KIND_BOND_CRP: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_CRP: 30>
    SH_MINOR_KIND_BOND_DST: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_DST: 24>
    SH_MINOR_KIND_BOND_DVP: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_DVP: 25>
    SH_MINOR_KIND_BOND_FBF: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_FBF: 29>
    SH_MINOR_KIND_BOND_GBF: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_GBF: 22>
    SH_MINOR_KIND_BOND_GBZ: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_GBZ: 23>
    SH_MINOR_KIND_BOND_KCCF: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_KCCF: 78>
    SH_MINOR_KIND_BOND_OBD: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_OBD: 34>
    SH_MINOR_KIND_BOND_ORP: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_ORP: 32>
    SH_MINOR_KIND_BOND_TCB: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_TCB: 77>
    SH_MINOR_KIND_BOND_WIT: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_BOND_WIT: 35>
    SH_MINOR_KIND_CMD: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_CMD: 40>
    SH_MINOR_KIND_FUND_CEF: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_FUND_CEF: 16>
    SH_MINOR_KIND_FUND_EBS: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_FUND_EBS: 18>
    SH_MINOR_KIND_FUND_FBL: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_FUND_FBL: 19>
    SH_MINOR_KIND_FUND_KES: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_FUND_KES: 75>
    SH_MINOR_KIND_FUND_KOF: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_FUND_KOF: 76>
    SH_MINOR_KIND_FUND_LOF: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_FUND_LOF: 21>
    SH_MINOR_KIND_FUND_OEF: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_FUND_OEF: 17>
    SH_MINOR_KIND_FUND_OFN: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_FUND_OFN: 20>
    SH_MINOR_KIND_OPS: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_OPS: 37>
    SH_MINOR_KIND_PPS: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_PPS: 38>
    SH_MINOR_KIND_QRP: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_QRP: 39>
    SH_MINOR_KIND_REITS_RET: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_REITS_RET: 79>
    SH_MINOR_KIND_STOCK_ASH: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_STOCK_ASH: 12>
    SH_MINOR_KIND_STOCK_BSH: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_STOCK_BSH: 13>
    SH_MINOR_KIND_STOCK_KSH: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_STOCK_KSH: 14>
    SH_MINOR_KIND_STOCK_OEQ: typing.ClassVar[EStockType]  # value = <EStockType.SH_MINOR_KIND_STOCK_OEQ: 15>
    SZ_FJY_MINOR_KIND_BOND_DISTRIBUTION: typing.ClassVar[EStockType]  # value = <EStockType.SZ_FJY_MINOR_KIND_BOND_DISTRIBUTION: 117>
    SZ_FJY_MINOR_KIND_BOND_RIGHTS_ISSUE: typing.ClassVar[EStockType]  # value = <EStockType.SZ_FJY_MINOR_KIND_BOND_RIGHTS_ISSUE: 122>
    SZ_FJY_MINOR_KIND_DERIVATIVEAUCTION: typing.ClassVar[EStockType]  # value = <EStockType.SZ_FJY_MINOR_KIND_DERIVATIVEAUCTION: 119>
    SZ_FJY_MINOR_KIND_ISSUE: typing.ClassVar[EStockType]  # value = <EStockType.SZ_FJY_MINOR_KIND_ISSUE: 116>
    SZ_FJY_MINOR_KIND_ISSUE_ADDITIONNAL: typing.ClassVar[EStockType]  # value = <EStockType.SZ_FJY_MINOR_KIND_ISSUE_ADDITIONNAL: 121>
    SZ_FJY_MINOR_KIND_NEGOTIATION: typing.ClassVar[EStockType]  # value = <EStockType.SZ_FJY_MINOR_KIND_NEGOTIATION: 120>
    SZ_FJY_MINOR_KIND_RIGHTS_ISSUE: typing.ClassVar[EStockType]  # value = <EStockType.SZ_FJY_MINOR_KIND_RIGHTS_ISSUE: 118>
    SZ_MINOR_KIND_ASSET_BACKED_SECURITIES: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_ASSET_BACKED_SECURITIES: 92>
    SZ_MINOR_KIND_BOND_CONVERTIBLE_BOND: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_BOND_CONVERTIBLE_BOND: 87>
    SZ_MINOR_KIND_BOND_CORPORATE_BOND: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_BOND_CORPORATE_BOND: 86>
    SZ_MINOR_KIND_BOND_ENTERPRISE_BOND: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_BOND_ENTERPRISE_BOND: 85>
    SZ_MINOR_KIND_BOND_EXCHANGEABLE_CORPORATE_BOND: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_BOND_EXCHANGEABLE_CORPORATE_BOND: 111>
    SZ_MINOR_KIND_BOND_EXCHANGEABLE_PB: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_BOND_EXCHANGEABLE_PB: 89>
    SZ_MINOR_KIND_BOND_ORIENT_CONVERTIBLE_BOND: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_BOND_ORIENT_CONVERTIBLE_BOND: 115>
    SZ_MINOR_KIND_BOND_PRIVATELY_RAISED_COMPANY_BONDS: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_BOND_PRIVATELY_RAISED_COMPANY_BONDS: 88>
    SZ_MINOR_KIND_BOND_SECURITY_COMPANY_SHORT_TERM_BOND: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_BOND_SECURITY_COMPANY_SHORT_TERM_BOND: 110>
    SZ_MINOR_KIND_BOND_SECURITY_COMPANY_SUB_DEBT: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_BOND_SECURITY_COMPANY_SUB_DEBT: 90>
    SZ_MINOR_KIND_BOND_TREASURY_BOND: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_BOND_TREASURY_BOND: 84>
    SZ_MINOR_KIND_FUND_BEARER_BOND_ETF: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_FUND_BEARER_BOND_ETF: 96>
    SZ_MINOR_KIND_FUND_CASH_BOND_ETF: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_FUND_CASH_BOND_ETF: 97>
    SZ_MINOR_KIND_FUND_CLOSED_END_FUNDS: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_FUND_CLOSED_END_FUNDS: 104>
    SZ_MINOR_KIND_FUND_COMMODITY_FUTURES_ETF: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_FUND_COMMODITY_FUTURES_ETF: 101>
    SZ_MINOR_KIND_FUND_CROSS_BORDER_ETF: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_FUND_CROSS_BORDER_ETF: 95>
    SZ_MINOR_KIND_FUND_CURRENCY_ETF: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_FUND_CURRENCY_ETF: 99>
    SZ_MINOR_KIND_FUND_GOLD_ETF: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_FUND_GOLD_ETF: 98>
    SZ_MINOR_KIND_FUND_GRADED_SUB_FUNDS: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_FUND_GRADED_SUB_FUNDS: 103>
    SZ_MINOR_KIND_FUND_INFRASTRUCTURE_FUND: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_FUND_INFRASTRUCTURE_FUND: 114>
    SZ_MINOR_KIND_FUND_INTER_MARKET_STOCK_ETF: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_FUND_INTER_MARKET_STOCK_ETF: 94>
    SZ_MINOR_KIND_FUND_LEVER_ETF: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_FUND_LEVER_ETF: 100>
    SZ_MINOR_KIND_FUND_REDEMPTION_FUND: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_FUND_REDEMPTION_FUND: 105>
    SZ_MINOR_KIND_FUND_STANDARD_LOF: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_FUND_STANDARD_LOF: 102>
    SZ_MINOR_KIND_FUND_STOCK_ETF: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_FUND_STOCK_ETF: 93>
    SZ_MINOR_KIND_OPTION_ETF_OPTION: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_OPTION_ETF_OPTION: 108>
    SZ_MINOR_KIND_OPTION_STOCK_OPTION: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_OPTION_STOCK_OPTION: 107>
    SZ_MINOR_KIND_PREFERRED_STOCK: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_PREFERRED_STOCK: 109>
    SZ_MINOR_KIND_REPO_PLEDGE_STYLE_REPO: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_REPO_PLEDGE_STYLE_REPO: 91>
    SZ_MINOR_KIND_STOCK_CDR: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_STOCK_CDR: 112>
    SZ_MINOR_KIND_STOCK_CHUANG_YE_BAN: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_STOCK_CHUANG_YE_BAN: 82>
    SZ_MINOR_KIND_STOCK_CHUANG_YE_CDR: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_STOCK_CHUANG_YE_CDR: 113>
    SZ_MINOR_KIND_STOCK_ZHONG_XIAO_BAN: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_STOCK_ZHONG_XIAO_BAN: 81>
    SZ_MINOR_KIND_STOCK_ZHU_BAN_A: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_STOCK_ZHU_BAN_A: 80>
    SZ_MINOR_KIND_STOCK_ZHU_BAN_B: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_STOCK_ZHU_BAN_B: 83>
    SZ_MINOR_KIND_WARRANT: typing.ClassVar[EStockType]  # value = <EStockType.SZ_MINOR_KIND_WARRANT: 106>
    __members__: typing.ClassVar[dict[str, EStockType]]  # value = {'MINOR_KIND_UNDEFINED': <EStockType.MINOR_KIND_UNDEFINED: 0>, 'MAJOR_KIND_INDEX': <EStockType.MAJOR_KIND_INDEX: 1>, 'MAJOR_KIND_STOCK': <EStockType.MAJOR_KIND_STOCK: 2>, 'MAJOR_KIND_FUND': <EStockType.MAJOR_KIND_FUND: 3>, 'MAJOR_KIND_BOND': <EStockType.MAJOR_KIND_BOND: 4>, 'MAJOR_KIND_WARRANT': <EStockType.MAJOR_KIND_WARRANT: 5>, 'MAJOR_KIND_REPO': <EStockType.MAJOR_KIND_REPO: 6>, 'MAJOR_KIND_OPTION': <EStockType.MAJOR_KIND_OPTION: 7>, 'MAJOR_KIND_PREFERRED_STOCK': <EStockType.MAJOR_KIND_PREFERRED_STOCK: 8>, 'MAJOR_KIND_ABS': <EStockType.MAJOR_KIND_ABS: 9>, 'MAJOR_KIND_FJY': <EStockType.MAJOR_KIND_FJY: 10>, 'MAJOR_KIND_REIT': <EStockType.MAJOR_KIND_REIT: 11>, 'SH_MINOR_KIND_STOCK_ASH': <EStockType.SH_MINOR_KIND_STOCK_ASH: 12>, 'SH_MINOR_KIND_STOCK_BSH': <EStockType.SH_MINOR_KIND_STOCK_BSH: 13>, 'SH_MINOR_KIND_STOCK_KSH': <EStockType.SH_MINOR_KIND_STOCK_KSH: 14>, 'SH_MINOR_KIND_STOCK_OEQ': <EStockType.SH_MINOR_KIND_STOCK_OEQ: 15>, 'SH_MINOR_KIND_FUND_CEF': <EStockType.SH_MINOR_KIND_FUND_CEF: 16>, 'SH_MINOR_KIND_FUND_OEF': <EStockType.SH_MINOR_KIND_FUND_OEF: 17>, 'SH_MINOR_KIND_FUND_EBS': <EStockType.SH_MINOR_KIND_FUND_EBS: 18>, 'SH_MINOR_KIND_FUND_FBL': <EStockType.SH_MINOR_KIND_FUND_FBL: 19>, 'SH_MINOR_KIND_FUND_OFN': <EStockType.SH_MINOR_KIND_FUND_OFN: 20>, 'SH_MINOR_KIND_FUND_LOF': <EStockType.SH_MINOR_KIND_FUND_LOF: 21>, 'SH_MINOR_KIND_BOND_GBF': <EStockType.SH_MINOR_KIND_BOND_GBF: 22>, 'SH_MINOR_KIND_BOND_GBZ': <EStockType.SH_MINOR_KIND_BOND_GBZ: 23>, 'SH_MINOR_KIND_BOND_DST': <EStockType.SH_MINOR_KIND_BOND_DST: 24>, 'SH_MINOR_KIND_BOND_DVP': <EStockType.SH_MINOR_KIND_BOND_DVP: 25>, 'SH_MINOR_KIND_BOND_CBF': <EStockType.SH_MINOR_KIND_BOND_CBF: 26>, 'SH_MINOR_KIND_BOND_CCF': <EStockType.SH_MINOR_KIND_BOND_CCF: 27>, 'SH_MINOR_KIND_BOND_CPF': <EStockType.SH_MINOR_KIND_BOND_CPF: 28>, 'SH_MINOR_KIND_BOND_FBF': <EStockType.SH_MINOR_KIND_BOND_FBF: 29>, 'SH_MINOR_KIND_BOND_CRP': <EStockType.SH_MINOR_KIND_BOND_CRP: 30>, 'SH_MINOR_KIND_BOND_BRP': <EStockType.SH_MINOR_KIND_BOND_BRP: 31>, 'SH_MINOR_KIND_BOND_ORP': <EStockType.SH_MINOR_KIND_BOND_ORP: 32>, 'SH_MINOR_KIND_BOND_CBD': <EStockType.SH_MINOR_KIND_BOND_CBD: 33>, 'SH_MINOR_KIND_BOND_OBD': <EStockType.SH_MINOR_KIND_BOND_OBD: 34>, 'SH_MINOR_KIND_BOND_WIT': <EStockType.SH_MINOR_KIND_BOND_WIT: 35>, 'SH_MINOR_KIND_AMP': <EStockType.SH_MINOR_KIND_AMP: 36>, 'SH_MINOR_KIND_OPS': <EStockType.SH_MINOR_KIND_OPS: 37>, 'SH_MINOR_KIND_PPS': <EStockType.SH_MINOR_KIND_PPS: 38>, 'SH_MINOR_KIND_QRP': <EStockType.SH_MINOR_KIND_QRP: 39>, 'SH_MINOR_KIND_CMD': <EStockType.SH_MINOR_KIND_CMD: 40>, 'SH_FJY_MINOR_KIND_IN': <EStockType.SH_FJY_MINOR_KIND_IN: 41>, 'SH_FJY_MINOR_KIND_IS': <EStockType.SH_FJY_MINOR_KIND_IS: 42>, 'SH_FJY_MINOR_KIND_PH': <EStockType.SH_FJY_MINOR_KIND_PH: 43>, 'SH_FJY_MINOR_KIND_KK': <EStockType.SH_FJY_MINOR_KIND_KK: 44>, 'SH_FJY_MINOR_KIND_HK': <EStockType.SH_FJY_MINOR_KIND_HK: 45>, 'SH_FJY_MINOR_KIND_CV': <EStockType.SH_FJY_MINOR_KIND_CV: 46>, 'SH_FJY_MINOR_KIND_CR': <EStockType.SH_FJY_MINOR_KIND_CR: 47>, 'SH_FJY_MINOR_KIND_R1': <EStockType.SH_FJY_MINOR_KIND_R1: 48>, 'SH_FJY_MINOR_KIND_R2': <EStockType.SH_FJY_MINOR_KIND_R2: 49>, 'SH_FJY_MINOR_KIND_R3': <EStockType.SH_FJY_MINOR_KIND_R3: 50>, 'SH_FJY_MINOR_KIND_R4': <EStockType.SH_FJY_MINOR_KIND_R4: 51>, 'SH_FJY_MINOR_KIND_OS': <EStockType.SH_FJY_MINOR_KIND_OS: 52>, 'SH_FJY_MINOR_KIND_OC': <EStockType.SH_FJY_MINOR_KIND_OC: 53>, 'SH_FJY_MINOR_KIND_OR': <EStockType.SH_FJY_MINOR_KIND_OR: 54>, 'SH_FJY_MINOR_KIND_OD': <EStockType.SH_FJY_MINOR_KIND_OD: 55>, 'SH_FJY_MINOR_KIND_OT': <EStockType.SH_FJY_MINOR_KIND_OT: 56>, 'SH_FJY_MINOR_KIND_OV': <EStockType.SH_FJY_MINOR_KIND_OV: 57>, 'SH_FJY_MINOR_KIND_EC': <EStockType.SH_FJY_MINOR_KIND_EC: 58>, 'SH_FJY_MINOR_KIND_ER': <EStockType.SH_FJY_MINOR_KIND_ER: 59>, 'SH_FJY_MINOR_KIND_EZ': <EStockType.SH_FJY_MINOR_KIND_EZ: 60>, 'SH_FJY_MINOR_KIND_BD': <EStockType.SH_FJY_MINOR_KIND_BD: 61>, 'SH_FJY_MINOR_KIND_BW': <EStockType.SH_FJY_MINOR_KIND_BW: 62>, 'SH_FJY_MINOR_KIND_FS': <EStockType.SH_FJY_MINOR_KIND_FS: 63>, 'SH_FJY_MINOR_KIND_FC': <EStockType.SH_FJY_MINOR_KIND_FC: 64>, 'SH_FJY_MINOR_KIND_ST': <EStockType.SH_FJY_MINOR_KIND_ST: 65>, 'SH_FJY_MINOR_KIND_SR': <EStockType.SH_FJY_MINOR_KIND_SR: 66>, 'SH_FJY_MINOR_KIND_CI': <EStockType.SH_FJY_MINOR_KIND_CI: 67>, 'SH_FJY_MINOR_KIND_CO': <EStockType.SH_FJY_MINOR_KIND_CO: 68>, 'SH_FJY_MINOR_KIND_SI': <EStockType.SH_FJY_MINOR_KIND_SI: 69>, 'SH_FJY_MINOR_KIND_SO': <EStockType.SH_FJY_MINOR_KIND_SO: 70>, 'SH_FJY_MINOR_KIND_PA': <EStockType.SH_FJY_MINOR_KIND_PA: 71>, 'SH_FJY_MINOR_KIND_DT': <EStockType.SH_FJY_MINOR_KIND_DT: 72>, 'SH_FJY_MINOR_KIND_DC': <EStockType.SH_FJY_MINOR_KIND_DC: 73>, 'SH_FJY_MINOR_KIND_QT': <EStockType.SH_FJY_MINOR_KIND_QT: 74>, 'SH_MINOR_KIND_FUND_KES': <EStockType.SH_MINOR_KIND_FUND_KES: 75>, 'SH_MINOR_KIND_FUND_KOF': <EStockType.SH_MINOR_KIND_FUND_KOF: 76>, 'SH_MINOR_KIND_BOND_TCB': <EStockType.SH_MINOR_KIND_BOND_TCB: 77>, 'SH_MINOR_KIND_BOND_KCCF': <EStockType.SH_MINOR_KIND_BOND_KCCF: 78>, 'SH_MINOR_KIND_REITS_RET': <EStockType.SH_MINOR_KIND_REITS_RET: 79>, 'SZ_MINOR_KIND_STOCK_ZHU_BAN_A': <EStockType.SZ_MINOR_KIND_STOCK_ZHU_BAN_A: 80>, 'SZ_MINOR_KIND_STOCK_ZHONG_XIAO_BAN': <EStockType.SZ_MINOR_KIND_STOCK_ZHONG_XIAO_BAN: 81>, 'SZ_MINOR_KIND_STOCK_CHUANG_YE_BAN': <EStockType.SZ_MINOR_KIND_STOCK_CHUANG_YE_BAN: 82>, 'SZ_MINOR_KIND_STOCK_ZHU_BAN_B': <EStockType.SZ_MINOR_KIND_STOCK_ZHU_BAN_B: 83>, 'SZ_MINOR_KIND_BOND_TREASURY_BOND': <EStockType.SZ_MINOR_KIND_BOND_TREASURY_BOND: 84>, 'SZ_MINOR_KIND_BOND_ENTERPRISE_BOND': <EStockType.SZ_MINOR_KIND_BOND_ENTERPRISE_BOND: 85>, 'SZ_MINOR_KIND_BOND_CORPORATE_BOND': <EStockType.SZ_MINOR_KIND_BOND_CORPORATE_BOND: 86>, 'SZ_MINOR_KIND_BOND_CONVERTIBLE_BOND': <EStockType.SZ_MINOR_KIND_BOND_CONVERTIBLE_BOND: 87>, 'SZ_MINOR_KIND_BOND_PRIVATELY_RAISED_COMPANY_BONDS': <EStockType.SZ_MINOR_KIND_BOND_PRIVATELY_RAISED_COMPANY_BONDS: 88>, 'SZ_MINOR_KIND_BOND_EXCHANGEABLE_PB': <EStockType.SZ_MINOR_KIND_BOND_EXCHANGEABLE_PB: 89>, 'SZ_MINOR_KIND_BOND_SECURITY_COMPANY_SUB_DEBT': <EStockType.SZ_MINOR_KIND_BOND_SECURITY_COMPANY_SUB_DEBT: 90>, 'SZ_MINOR_KIND_REPO_PLEDGE_STYLE_REPO': <EStockType.SZ_MINOR_KIND_REPO_PLEDGE_STYLE_REPO: 91>, 'SZ_MINOR_KIND_ASSET_BACKED_SECURITIES': <EStockType.SZ_MINOR_KIND_ASSET_BACKED_SECURITIES: 92>, 'SZ_MINOR_KIND_FUND_STOCK_ETF': <EStockType.SZ_MINOR_KIND_FUND_STOCK_ETF: 93>, 'SZ_MINOR_KIND_FUND_INTER_MARKET_STOCK_ETF': <EStockType.SZ_MINOR_KIND_FUND_INTER_MARKET_STOCK_ETF: 94>, 'SZ_MINOR_KIND_FUND_CROSS_BORDER_ETF': <EStockType.SZ_MINOR_KIND_FUND_CROSS_BORDER_ETF: 95>, 'SZ_MINOR_KIND_FUND_BEARER_BOND_ETF': <EStockType.SZ_MINOR_KIND_FUND_BEARER_BOND_ETF: 96>, 'SZ_MINOR_KIND_FUND_CASH_BOND_ETF': <EStockType.SZ_MINOR_KIND_FUND_CASH_BOND_ETF: 97>, 'SZ_MINOR_KIND_FUND_GOLD_ETF': <EStockType.SZ_MINOR_KIND_FUND_GOLD_ETF: 98>, 'SZ_MINOR_KIND_FUND_CURRENCY_ETF': <EStockType.SZ_MINOR_KIND_FUND_CURRENCY_ETF: 99>, 'SZ_MINOR_KIND_FUND_LEVER_ETF': <EStockType.SZ_MINOR_KIND_FUND_LEVER_ETF: 100>, 'SZ_MINOR_KIND_FUND_COMMODITY_FUTURES_ETF': <EStockType.SZ_MINOR_KIND_FUND_COMMODITY_FUTURES_ETF: 101>, 'SZ_MINOR_KIND_FUND_STANDARD_LOF': <EStockType.SZ_MINOR_KIND_FUND_STANDARD_LOF: 102>, 'SZ_MINOR_KIND_FUND_GRADED_SUB_FUNDS': <EStockType.SZ_MINOR_KIND_FUND_GRADED_SUB_FUNDS: 103>, 'SZ_MINOR_KIND_FUND_CLOSED_END_FUNDS': <EStockType.SZ_MINOR_KIND_FUND_CLOSED_END_FUNDS: 104>, 'SZ_MINOR_KIND_FUND_REDEMPTION_FUND': <EStockType.SZ_MINOR_KIND_FUND_REDEMPTION_FUND: 105>, 'SZ_MINOR_KIND_WARRANT': <EStockType.SZ_MINOR_KIND_WARRANT: 106>, 'SZ_MINOR_KIND_OPTION_STOCK_OPTION': <EStockType.SZ_MINOR_KIND_OPTION_STOCK_OPTION: 107>, 'SZ_MINOR_KIND_OPTION_ETF_OPTION': <EStockType.SZ_MINOR_KIND_OPTION_ETF_OPTION: 108>, 'SZ_MINOR_KIND_PREFERRED_STOCK': <EStockType.SZ_MINOR_KIND_PREFERRED_STOCK: 109>, 'SZ_MINOR_KIND_BOND_SECURITY_COMPANY_SHORT_TERM_BOND': <EStockType.SZ_MINOR_KIND_BOND_SECURITY_COMPANY_SHORT_TERM_BOND: 110>, 'SZ_MINOR_KIND_BOND_EXCHANGEABLE_CORPORATE_BOND': <EStockType.SZ_MINOR_KIND_BOND_EXCHANGEABLE_CORPORATE_BOND: 111>, 'SZ_MINOR_KIND_STOCK_CDR': <EStockType.SZ_MINOR_KIND_STOCK_CDR: 112>, 'SZ_MINOR_KIND_STOCK_CHUANG_YE_CDR': <EStockType.SZ_MINOR_KIND_STOCK_CHUANG_YE_CDR: 113>, 'SZ_MINOR_KIND_FUND_INFRASTRUCTURE_FUND': <EStockType.SZ_MINOR_KIND_FUND_INFRASTRUCTURE_FUND: 114>, 'SZ_MINOR_KIND_BOND_ORIENT_CONVERTIBLE_BOND': <EStockType.SZ_MINOR_KIND_BOND_ORIENT_CONVERTIBLE_BOND: 115>, 'SZ_FJY_MINOR_KIND_ISSUE': <EStockType.SZ_FJY_MINOR_KIND_ISSUE: 116>, 'SZ_FJY_MINOR_KIND_BOND_DISTRIBUTION': <EStockType.SZ_FJY_MINOR_KIND_BOND_DISTRIBUTION: 117>, 'SZ_FJY_MINOR_KIND_RIGHTS_ISSUE': <EStockType.SZ_FJY_MINOR_KIND_RIGHTS_ISSUE: 118>, 'SZ_FJY_MINOR_KIND_DERIVATIVEAUCTION': <EStockType.SZ_FJY_MINOR_KIND_DERIVATIVEAUCTION: 119>, 'SZ_FJY_MINOR_KIND_NEGOTIATION': <EStockType.SZ_FJY_MINOR_KIND_NEGOTIATION: 120>, 'SZ_FJY_MINOR_KIND_ISSUE_ADDITIONNAL': <EStockType.SZ_FJY_MINOR_KIND_ISSUE_ADDITIONNAL: 121>, 'SZ_FJY_MINOR_KIND_BOND_RIGHTS_ISSUE': <EStockType.SZ_FJY_MINOR_KIND_BOND_RIGHTS_ISSUE: 122>, 'NEEQ_MINOR_KIND_STOCK_DELIST_COMPANY_A': <EStockType.NEEQ_MINOR_KIND_STOCK_DELIST_COMPANY_A: 123>, 'NEEQ_MINOR_KIND_STOCK_DELIST_COMPANY_B': <EStockType.NEEQ_MINOR_KIND_STOCK_DELIST_COMPANY_B: 124>, 'NEEQ_MINOR_KIND_STOCK_LISTED_COMPANY': <EStockType.NEEQ_MINOR_KIND_STOCK_LISTED_COMPANY: 125>, 'NEEQ_MINOR_KIND_PREFERRED_STOCK': <EStockType.NEEQ_MINOR_KIND_PREFERRED_STOCK: 126>, 'NEEQ_MINOR_KIND_TENDER_OFFER': <EStockType.NEEQ_MINOR_KIND_TENDER_OFFER: 127>, 'NEEQ_MINOR_KIND_OFFER_TO_REPURCHASE': <EStockType.NEEQ_MINOR_KIND_OFFER_TO_REPURCHASE: 128>, 'NEEQ_MINOR_KIND_EQUITY_INCENTIVE_OPTION': <EStockType.NEEQ_MINOR_KIND_EQUITY_INCENTIVE_OPTION: 129>, 'NEEQ_MINOR_KIND_INDEX': <EStockType.NEEQ_MINOR_KIND_INDEX: 130>, 'NEEQ_MINOR_KIND_ISSUE_TRANSACTION': <EStockType.NEEQ_MINOR_KIND_ISSUE_TRANSACTION: 131>, 'NEEQ_MINOR_KIND_CONVERTIBLE_BOND': <EStockType.NEEQ_MINOR_KIND_CONVERTIBLE_BOND: 132>, 'NEEQ_MINOR_KIND_ORIENT_CONVERTIBLE_BOND': <EStockType.NEEQ_MINOR_KIND_ORIENT_CONVERTIBLE_BOND: 133>, 'NEEQ_MINOR_KIND_DELIST_CONVERTIBLE_BOND': <EStockType.NEEQ_MINOR_KIND_DELIST_CONVERTIBLE_BOND: 134>, 'SHFI_MINOR_KIND_TREASURY_BOND': <EStockType.SHFI_MINOR_KIND_TREASURY_BOND: 135>, 'SHFI_MINOR_KIND_CORPORATE_BOND': <EStockType.SHFI_MINOR_KIND_CORPORATE_BOND: 136>, 'SHFI_MINOR_KIND_PRIVATE_PLACEMENT_BOND': <EStockType.SHFI_MINOR_KIND_PRIVATE_PLACEMENT_BOND: 137>, 'SHFI_MINOR_KIND_ABS': <EStockType.SHFI_MINOR_KIND_ABS: 138>, 'SHFI_MINOR_KIND_SPECIAL_BOND': <EStockType.SHFI_MINOR_KIND_SPECIAL_BOND: 139>, 'SHFI_MINOR_KIND_REITS': <EStockType.SHFI_MINOR_KIND_REITS: 140>, 'SHFI_MINOR_KIND_CONVERTIBLE_BOND': <EStockType.SHFI_MINOR_KIND_CONVERTIBLE_BOND: 141>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EStopTradeForOwnHiLow:
    """
    涨跌停控制
    
    Members:
    
      STOPTRADE_NONE : 主动算法是无，智能算法是最优价尽快执行
    
      STOPTRADE_NO_BUY_SELL : 涨停不卖跌停不买
    
      STOPTRADE_SCHEDULED : 原定时长执行
    
      STOPTRADE_NOT_CHASE : 涨停不买跌停不卖
    """
    STOPTRADE_NONE: typing.ClassVar[EStopTradeForOwnHiLow]  # value = <EStopTradeForOwnHiLow.STOPTRADE_NONE: 0>
    STOPTRADE_NOT_CHASE: typing.ClassVar[EStopTradeForOwnHiLow]  # value = <EStopTradeForOwnHiLow.STOPTRADE_NOT_CHASE: 3>
    STOPTRADE_NO_BUY_SELL: typing.ClassVar[EStopTradeForOwnHiLow]  # value = <EStopTradeForOwnHiLow.STOPTRADE_NO_BUY_SELL: 1>
    STOPTRADE_SCHEDULED: typing.ClassVar[EStopTradeForOwnHiLow]  # value = <EStopTradeForOwnHiLow.STOPTRADE_SCHEDULED: 2>
    __members__: typing.ClassVar[dict[str, EStopTradeForOwnHiLow]]  # value = {'STOPTRADE_NONE': <EStopTradeForOwnHiLow.STOPTRADE_NONE: 0>, 'STOPTRADE_NO_BUY_SELL': <EStopTradeForOwnHiLow.STOPTRADE_NO_BUY_SELL: 1>, 'STOPTRADE_SCHEDULED': <EStopTradeForOwnHiLow.STOPTRADE_SCHEDULED: 2>, 'STOPTRADE_NOT_CHASE': <EStopTradeForOwnHiLow.STOPTRADE_NOT_CHASE: 3>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ETaskFlowOperation:
    """
    任务操作
    
    Members:
    
      TFO_PAUSE : 暂停
    
      TFO_RESUME : 恢复
    """
    TFO_PAUSE: typing.ClassVar[ETaskFlowOperation]  # value = <ETaskFlowOperation.TFO_PAUSE: 5>
    TFO_RESUME: typing.ClassVar[ETaskFlowOperation]  # value = <ETaskFlowOperation.TFO_RESUME: 6>
    __members__: typing.ClassVar[dict[str, ETaskFlowOperation]]  # value = {'TFO_PAUSE': <ETaskFlowOperation.TFO_PAUSE: 5>, 'TFO_RESUME': <ETaskFlowOperation.TFO_RESUME: 6>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ETimeCondition:
    """
    期货时间条件单类型
    
    Members:
    
      TIME_CONDITION_IOC : 立即完成，否则撤销
    
      TIME_CONDITION_GFS : 本节有效
    
      TIME_CONDITION_GFD : 当日有效
    
      TIME_CONDITION_GTD : 指定日期前有效
    
      TIME_CONDITION_GTC : 撤销前有效
    
      TIME_CONDITION_GFA : 集合竞价有效
    """
    TIME_CONDITION_GFA: typing.ClassVar[ETimeCondition]  # value = <ETimeCondition.TIME_CONDITION_GFA: 54>
    TIME_CONDITION_GFD: typing.ClassVar[ETimeCondition]  # value = <ETimeCondition.TIME_CONDITION_GFD: 51>
    TIME_CONDITION_GFS: typing.ClassVar[ETimeCondition]  # value = <ETimeCondition.TIME_CONDITION_GFS: 50>
    TIME_CONDITION_GTC: typing.ClassVar[ETimeCondition]  # value = <ETimeCondition.TIME_CONDITION_GTC: 53>
    TIME_CONDITION_GTD: typing.ClassVar[ETimeCondition]  # value = <ETimeCondition.TIME_CONDITION_GTD: 52>
    TIME_CONDITION_IOC: typing.ClassVar[ETimeCondition]  # value = <ETimeCondition.TIME_CONDITION_IOC: 49>
    __members__: typing.ClassVar[dict[str, ETimeCondition]]  # value = {'TIME_CONDITION_IOC': <ETimeCondition.TIME_CONDITION_IOC: 49>, 'TIME_CONDITION_GFS': <ETimeCondition.TIME_CONDITION_GFS: 50>, 'TIME_CONDITION_GFD': <ETimeCondition.TIME_CONDITION_GFD: 51>, 'TIME_CONDITION_GTD': <ETimeCondition.TIME_CONDITION_GTD: 52>, 'TIME_CONDITION_GTC': <ETimeCondition.TIME_CONDITION_GTC: 53>, 'TIME_CONDITION_GFA': <ETimeCondition.TIME_CONDITION_GFA: 54>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ETransDirection:
    """
    银证转账方向
    
    Members:
    
      TRANS_DIRECTION_BANK_TO_SECURITIES : 银行转证券
    
      TRANS_DIRECTION_SECURITIES_TO_BANK : 证券转银行
    
      TRANS_DIRECTION_QUICK_TO_CENTER : 快速转集中
    
      TRANS_DIRECTION_CENTER_TO_QUICK : 集中转快速
    
      TRANS_DIRECTION_QUERY : 查询
    """
    TRANS_DIRECTION_BANK_TO_SECURITIES: typing.ClassVar[ETransDirection]  # value = <ETransDirection.TRANS_DIRECTION_BANK_TO_SECURITIES: 49>
    TRANS_DIRECTION_CENTER_TO_QUICK: typing.ClassVar[ETransDirection]  # value = <ETransDirection.TRANS_DIRECTION_CENTER_TO_QUICK: 52>
    TRANS_DIRECTION_QUERY: typing.ClassVar[ETransDirection]  # value = <ETransDirection.TRANS_DIRECTION_QUERY: 53>
    TRANS_DIRECTION_QUICK_TO_CENTER: typing.ClassVar[ETransDirection]  # value = <ETransDirection.TRANS_DIRECTION_QUICK_TO_CENTER: 51>
    TRANS_DIRECTION_SECURITIES_TO_BANK: typing.ClassVar[ETransDirection]  # value = <ETransDirection.TRANS_DIRECTION_SECURITIES_TO_BANK: 50>
    __members__: typing.ClassVar[dict[str, ETransDirection]]  # value = {'TRANS_DIRECTION_BANK_TO_SECURITIES': <ETransDirection.TRANS_DIRECTION_BANK_TO_SECURITIES: 49>, 'TRANS_DIRECTION_SECURITIES_TO_BANK': <ETransDirection.TRANS_DIRECTION_SECURITIES_TO_BANK: 50>, 'TRANS_DIRECTION_QUICK_TO_CENTER': <ETransDirection.TRANS_DIRECTION_QUICK_TO_CENTER: 51>, 'TRANS_DIRECTION_CENTER_TO_QUICK': <ETransDirection.TRANS_DIRECTION_CENTER_TO_QUICK: 52>, 'TRANS_DIRECTION_QUERY': <ETransDirection.TRANS_DIRECTION_QUERY: 53>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ETransTypeCreditFlag:
    """
    股份划拨信用划拨类别
    
    Members:
    
      TRANS_TRANSFER_SHARE : 操作客户股份划拨，默认送0
    
      TRANS_TRANSFER_SPECIAL_POSITIONS : 操作客户专向头寸调拨
    
      TRANS_TRANSFER_CREDIT_SHARE : 融资融券客户股份调拨
    """
    TRANS_TRANSFER_CREDIT_SHARE: typing.ClassVar[ETransTypeCreditFlag]  # value = <ETransTypeCreditFlag.TRANS_TRANSFER_CREDIT_SHARE: 2>
    TRANS_TRANSFER_SHARE: typing.ClassVar[ETransTypeCreditFlag]  # value = <ETransTypeCreditFlag.TRANS_TRANSFER_SHARE: 0>
    TRANS_TRANSFER_SPECIAL_POSITIONS: typing.ClassVar[ETransTypeCreditFlag]  # value = <ETransTypeCreditFlag.TRANS_TRANSFER_SPECIAL_POSITIONS: 1>
    __members__: typing.ClassVar[dict[str, ETransTypeCreditFlag]]  # value = {'TRANS_TRANSFER_SHARE': <ETransTypeCreditFlag.TRANS_TRANSFER_SHARE: 0>, 'TRANS_TRANSFER_SPECIAL_POSITIONS': <ETransTypeCreditFlag.TRANS_TRANSFER_SPECIAL_POSITIONS: 1>, 'TRANS_TRANSFER_CREDIT_SHARE': <ETransTypeCreditFlag.TRANS_TRANSFER_CREDIT_SHARE: 2>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EVolumeCondition:
    """
    期货数量条件单类型
    
    Members:
    
      VOLUME_CONDITION_ANY : 任何数量
    
      VOLUME_CONDITION_MIN : 最小数量
    
      VOLUME_CONDITION_TOTAL : 全部数量
    """
    VOLUME_CONDITION_ANY: typing.ClassVar[EVolumeCondition]  # value = <EVolumeCondition.VOLUME_CONDITION_ANY: 49>
    VOLUME_CONDITION_MIN: typing.ClassVar[EVolumeCondition]  # value = <EVolumeCondition.VOLUME_CONDITION_MIN: 50>
    VOLUME_CONDITION_TOTAL: typing.ClassVar[EVolumeCondition]  # value = <EVolumeCondition.VOLUME_CONDITION_TOTAL: 51>
    __members__: typing.ClassVar[dict[str, EVolumeCondition]]  # value = {'VOLUME_CONDITION_ANY': <EVolumeCondition.VOLUME_CONDITION_ANY: 49>, 'VOLUME_CONDITION_MIN': <EVolumeCondition.VOLUME_CONDITION_MIN: 50>, 'VOLUME_CONDITION_TOTAL': <EVolumeCondition.VOLUME_CONDITION_TOTAL: 51>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EVolumeType:
    """
    下单量类型
    
    Members:
    
      VOLUME_INVALID : 
    
      VOLUME_SALE12345 : 
    
      VOLUME_SALE1234 : 
    
      VOLUME_SALE123 : 
    
      VOLUME_SALE12 : 
    
      VOLUME_SALE1 : 
    
      VOLUME_BUY1 : 买一
    
      VOLUME_BUY12 : 
    
      VOLUME_BUY123 : 
    
      VOLUME_BUY1234 : 
    
      VOLUME_BUY12345 : 
    
      VOLUME_FIX : 
    
      VOLUME_LEFT : 
    
      VOLUME_POSITION : 持仓数量
    
      _C_VOLUME_COUNT : 
    """
    VOLUME_BUY1: typing.ClassVar[EVolumeType]  # value = <EVolumeType.VOLUME_BUY1: 5>
    VOLUME_BUY12: typing.ClassVar[EVolumeType]  # value = <EVolumeType.VOLUME_BUY12: 6>
    VOLUME_BUY123: typing.ClassVar[EVolumeType]  # value = <EVolumeType.VOLUME_BUY123: 7>
    VOLUME_BUY1234: typing.ClassVar[EVolumeType]  # value = <EVolumeType.VOLUME_BUY1234: 8>
    VOLUME_BUY12345: typing.ClassVar[EVolumeType]  # value = <EVolumeType.VOLUME_BUY12345: 9>
    VOLUME_FIX: typing.ClassVar[EVolumeType]  # value = <EVolumeType.VOLUME_FIX: 10>
    VOLUME_INVALID: typing.ClassVar[EVolumeType]  # value = <EVolumeType.VOLUME_INVALID: -1>
    VOLUME_LEFT: typing.ClassVar[EVolumeType]  # value = <EVolumeType.VOLUME_LEFT: 11>
    VOLUME_POSITION: typing.ClassVar[EVolumeType]  # value = <EVolumeType.VOLUME_POSITION: 12>
    VOLUME_SALE1: typing.ClassVar[EVolumeType]  # value = <EVolumeType.VOLUME_SALE1: 4>
    VOLUME_SALE12: typing.ClassVar[EVolumeType]  # value = <EVolumeType.VOLUME_SALE12: 3>
    VOLUME_SALE123: typing.ClassVar[EVolumeType]  # value = <EVolumeType.VOLUME_SALE123: 2>
    VOLUME_SALE1234: typing.ClassVar[EVolumeType]  # value = <EVolumeType.VOLUME_SALE1234: 1>
    VOLUME_SALE12345: typing.ClassVar[EVolumeType]  # value = <EVolumeType.VOLUME_SALE12345: 0>
    _C_VOLUME_COUNT: typing.ClassVar[EVolumeType]  # value = <EVolumeType._C_VOLUME_COUNT: 13>
    __members__: typing.ClassVar[dict[str, EVolumeType]]  # value = {'VOLUME_INVALID': <EVolumeType.VOLUME_INVALID: -1>, 'VOLUME_SALE12345': <EVolumeType.VOLUME_SALE12345: 0>, 'VOLUME_SALE1234': <EVolumeType.VOLUME_SALE1234: 1>, 'VOLUME_SALE123': <EVolumeType.VOLUME_SALE123: 2>, 'VOLUME_SALE12': <EVolumeType.VOLUME_SALE12: 3>, 'VOLUME_SALE1': <EVolumeType.VOLUME_SALE1: 4>, 'VOLUME_BUY1': <EVolumeType.VOLUME_BUY1: 5>, 'VOLUME_BUY12': <EVolumeType.VOLUME_BUY12: 6>, 'VOLUME_BUY123': <EVolumeType.VOLUME_BUY123: 7>, 'VOLUME_BUY1234': <EVolumeType.VOLUME_BUY1234: 8>, 'VOLUME_BUY12345': <EVolumeType.VOLUME_BUY12345: 9>, 'VOLUME_FIX': <EVolumeType.VOLUME_FIX: 10>, 'VOLUME_LEFT': <EVolumeType.VOLUME_LEFT: 11>, 'VOLUME_POSITION': <EVolumeType.VOLUME_POSITION: 12>, '_C_VOLUME_COUNT': <EVolumeType._C_VOLUME_COUNT: 13>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EXTBrokerType:
    """
    账号类型
    
    Members:
    
      AT_FUTURE : 期货账号
    
      AT_STOCK : 股票账号
    
      AT_CREDIT : 信用账号
    
      AT_GOLD : 贵金属账号
    
      AT_FUTURE_OPTION : 期货期权账号
    
      AT_STOCK_OPTION : 股票期权账号
    
      AT_HUGANGTONG : 沪港通账号
    
      AT_INCOME_SWAP : 美股收益互换账号
    
      AT_NEW3BOARD : 全国股转账号
    
      AT_SHENGANGTONG : 深港通账号
    
      AT_FICC_COMMODITY : 期货电子盘账号
    
      AT_FICC_INTEREST : 利率电子盘账号
    
      AT_ABROAD_FUTURE : 外盘期货账号
    """
    AT_ABROAD_FUTURE: typing.ClassVar[EXTBrokerType]  # value = <EXTBrokerType.AT_ABROAD_FUTURE: 16>
    AT_CREDIT: typing.ClassVar[EXTBrokerType]  # value = <EXTBrokerType.AT_CREDIT: 3>
    AT_FICC_COMMODITY: typing.ClassVar[EXTBrokerType]  # value = <EXTBrokerType.AT_FICC_COMMODITY: 14>
    AT_FICC_INTEREST: typing.ClassVar[EXTBrokerType]  # value = <EXTBrokerType.AT_FICC_INTEREST: 15>
    AT_FUTURE: typing.ClassVar[EXTBrokerType]  # value = <EXTBrokerType.AT_FUTURE: 1>
    AT_FUTURE_OPTION: typing.ClassVar[EXTBrokerType]  # value = <EXTBrokerType.AT_FUTURE_OPTION: 5>
    AT_GOLD: typing.ClassVar[EXTBrokerType]  # value = <EXTBrokerType.AT_GOLD: 4>
    AT_HUGANGTONG: typing.ClassVar[EXTBrokerType]  # value = <EXTBrokerType.AT_HUGANGTONG: 7>
    AT_INCOME_SWAP: typing.ClassVar[EXTBrokerType]  # value = <EXTBrokerType.AT_INCOME_SWAP: 8>
    AT_NEW3BOARD: typing.ClassVar[EXTBrokerType]  # value = <EXTBrokerType.AT_NEW3BOARD: 10>
    AT_SHENGANGTONG: typing.ClassVar[EXTBrokerType]  # value = <EXTBrokerType.AT_SHENGANGTONG: 11>
    AT_STOCK: typing.ClassVar[EXTBrokerType]  # value = <EXTBrokerType.AT_STOCK: 2>
    AT_STOCK_OPTION: typing.ClassVar[EXTBrokerType]  # value = <EXTBrokerType.AT_STOCK_OPTION: 6>
    __members__: typing.ClassVar[dict[str, EXTBrokerType]]  # value = {'AT_FUTURE': <EXTBrokerType.AT_FUTURE: 1>, 'AT_STOCK': <EXTBrokerType.AT_STOCK: 2>, 'AT_CREDIT': <EXTBrokerType.AT_CREDIT: 3>, 'AT_GOLD': <EXTBrokerType.AT_GOLD: 4>, 'AT_FUTURE_OPTION': <EXTBrokerType.AT_FUTURE_OPTION: 5>, 'AT_STOCK_OPTION': <EXTBrokerType.AT_STOCK_OPTION: 6>, 'AT_HUGANGTONG': <EXTBrokerType.AT_HUGANGTONG: 7>, 'AT_INCOME_SWAP': <EXTBrokerType.AT_INCOME_SWAP: 8>, 'AT_NEW3BOARD': <EXTBrokerType.AT_NEW3BOARD: 10>, 'AT_SHENGANGTONG': <EXTBrokerType.AT_SHENGANGTONG: 11>, 'AT_FICC_COMMODITY': <EXTBrokerType.AT_FICC_COMMODITY: 14>, 'AT_FICC_INTEREST': <EXTBrokerType.AT_FICC_INTEREST: 15>, 'AT_ABROAD_FUTURE': <EXTBrokerType.AT_ABROAD_FUTURE: 16>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EXTCommandDateLimit:
    """
    指令跨日标志
    
    Members:
    
      XT_COMMAND_LIMIT_NO_OVER_DAY : 不跨日
    
      XT_COMMAND_LIMIT_CROSS_OVER_DAY : 将跨日指令
    
      XT_COMMAND_LIMIT_ALREADY_CROSSED : 已经跨日的指令
    """
    XT_COMMAND_LIMIT_ALREADY_CROSSED: typing.ClassVar[EXTCommandDateLimit]  # value = <EXTCommandDateLimit.XT_COMMAND_LIMIT_ALREADY_CROSSED: 2>
    XT_COMMAND_LIMIT_CROSS_OVER_DAY: typing.ClassVar[EXTCommandDateLimit]  # value = <EXTCommandDateLimit.XT_COMMAND_LIMIT_CROSS_OVER_DAY: 1>
    XT_COMMAND_LIMIT_NO_OVER_DAY: typing.ClassVar[EXTCommandDateLimit]  # value = <EXTCommandDateLimit.XT_COMMAND_LIMIT_NO_OVER_DAY: 0>
    __members__: typing.ClassVar[dict[str, EXTCommandDateLimit]]  # value = {'XT_COMMAND_LIMIT_NO_OVER_DAY': <EXTCommandDateLimit.XT_COMMAND_LIMIT_NO_OVER_DAY: 0>, 'XT_COMMAND_LIMIT_CROSS_OVER_DAY': <EXTCommandDateLimit.XT_COMMAND_LIMIT_CROSS_OVER_DAY: 1>, 'XT_COMMAND_LIMIT_ALREADY_CROSSED': <EXTCommandDateLimit.XT_COMMAND_LIMIT_ALREADY_CROSSED: 2>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EXTCompactBrushSource:
    """
    两融负债头寸来源
    
    Members:
    
      COMPACT_BRUSH_SOURCE_ALL : 不限制
    
      COMPACT_BRUSH_SOURCE_NORMAL : 普通头寸
    
      COMPACT_BRUSH_SOURCE_SPECIAL : 专项头寸
    """
    COMPACT_BRUSH_SOURCE_ALL: typing.ClassVar[EXTCompactBrushSource]  # value = <EXTCompactBrushSource.COMPACT_BRUSH_SOURCE_ALL: 32>
    COMPACT_BRUSH_SOURCE_NORMAL: typing.ClassVar[EXTCompactBrushSource]  # value = <EXTCompactBrushSource.COMPACT_BRUSH_SOURCE_NORMAL: 48>
    COMPACT_BRUSH_SOURCE_SPECIAL: typing.ClassVar[EXTCompactBrushSource]  # value = <EXTCompactBrushSource.COMPACT_BRUSH_SOURCE_SPECIAL: 49>
    __members__: typing.ClassVar[dict[str, EXTCompactBrushSource]]  # value = {'COMPACT_BRUSH_SOURCE_ALL': <EXTCompactBrushSource.COMPACT_BRUSH_SOURCE_ALL: 32>, 'COMPACT_BRUSH_SOURCE_NORMAL': <EXTCompactBrushSource.COMPACT_BRUSH_SOURCE_NORMAL: 48>, 'COMPACT_BRUSH_SOURCE_SPECIAL': <EXTCompactBrushSource.COMPACT_BRUSH_SOURCE_SPECIAL: 49>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EXTCompactStatus:
    """
    两融负债状态
    
    Members:
    
      COMPACT_STATUS_ALL : 不限制
    
      COMPACT_STATUS_UNDONE : 未归还
    
      COMPACT_STATUS_PART_DONE : 部分归还
    
      COMPACT_STATUS_DONE : 已归还
    
      COMPACT_STATUS_DONE_BY_SELF : 自行了结
    
      COMPACT_STATUS_DONE_BY_HAND : 手工了结
    
      COMPACT_STATUS_NOT_DEBT : 未形成负债
    
      COMPACT_STATUS_EXPIRY_NOT_CLOSE : 到期未平仓
    """
    COMPACT_STATUS_ALL: typing.ClassVar[EXTCompactStatus]  # value = <EXTCompactStatus.COMPACT_STATUS_ALL: 32>
    COMPACT_STATUS_DONE: typing.ClassVar[EXTCompactStatus]  # value = <EXTCompactStatus.COMPACT_STATUS_DONE: 50>
    COMPACT_STATUS_DONE_BY_HAND: typing.ClassVar[EXTCompactStatus]  # value = <EXTCompactStatus.COMPACT_STATUS_DONE_BY_HAND: 52>
    COMPACT_STATUS_DONE_BY_SELF: typing.ClassVar[EXTCompactStatus]  # value = <EXTCompactStatus.COMPACT_STATUS_DONE_BY_SELF: 51>
    COMPACT_STATUS_EXPIRY_NOT_CLOSE: typing.ClassVar[EXTCompactStatus]  # value = <EXTCompactStatus.COMPACT_STATUS_EXPIRY_NOT_CLOSE: 54>
    COMPACT_STATUS_NOT_DEBT: typing.ClassVar[EXTCompactStatus]  # value = <EXTCompactStatus.COMPACT_STATUS_NOT_DEBT: 53>
    COMPACT_STATUS_PART_DONE: typing.ClassVar[EXTCompactStatus]  # value = <EXTCompactStatus.COMPACT_STATUS_PART_DONE: 49>
    COMPACT_STATUS_UNDONE: typing.ClassVar[EXTCompactStatus]  # value = <EXTCompactStatus.COMPACT_STATUS_UNDONE: 48>
    __members__: typing.ClassVar[dict[str, EXTCompactStatus]]  # value = {'COMPACT_STATUS_ALL': <EXTCompactStatus.COMPACT_STATUS_ALL: 32>, 'COMPACT_STATUS_UNDONE': <EXTCompactStatus.COMPACT_STATUS_UNDONE: 48>, 'COMPACT_STATUS_PART_DONE': <EXTCompactStatus.COMPACT_STATUS_PART_DONE: 49>, 'COMPACT_STATUS_DONE': <EXTCompactStatus.COMPACT_STATUS_DONE: 50>, 'COMPACT_STATUS_DONE_BY_SELF': <EXTCompactStatus.COMPACT_STATUS_DONE_BY_SELF: 51>, 'COMPACT_STATUS_DONE_BY_HAND': <EXTCompactStatus.COMPACT_STATUS_DONE_BY_HAND: 52>, 'COMPACT_STATUS_NOT_DEBT': <EXTCompactStatus.COMPACT_STATUS_NOT_DEBT: 53>, 'COMPACT_STATUS_EXPIRY_NOT_CLOSE': <EXTCompactStatus.COMPACT_STATUS_EXPIRY_NOT_CLOSE: 54>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EXTCompactType:
    """
    两融负债类型
    
    Members:
    
      COMPACT_TYPE_ALL : 不限制
    
      COMPACT_TYPE_FIN : 融资
    
      COMPACT_TYPE_SLO : 融券
    """
    COMPACT_TYPE_ALL: typing.ClassVar[EXTCompactType]  # value = <EXTCompactType.COMPACT_TYPE_ALL: 32>
    COMPACT_TYPE_FIN: typing.ClassVar[EXTCompactType]  # value = <EXTCompactType.COMPACT_TYPE_FIN: 48>
    COMPACT_TYPE_SLO: typing.ClassVar[EXTCompactType]  # value = <EXTCompactType.COMPACT_TYPE_SLO: 49>
    __members__: typing.ClassVar[dict[str, EXTCompactType]]  # value = {'COMPACT_TYPE_ALL': <EXTCompactType.COMPACT_TYPE_ALL: 32>, 'COMPACT_TYPE_FIN': <EXTCompactType.COMPACT_TYPE_FIN: 48>, 'COMPACT_TYPE_SLO': <EXTCompactType.COMPACT_TYPE_SLO: 49>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EXTExchangeStatus:
    """
    市场状态
    
    Members:
    
      EXCHANGE_STATUS_INVALID : 
    
      EXCHANGE_STATUS_IN_BEFORE_TRADING : 开盘前
    
      EXCHANGE_STATUS_NOTRADING : 非交易
    
      EXCHANGE_STATUS_IN_CONTINOUS : 连续交易
    
      EXCHANGE_STATUS_AUCTION_ORDERING : 集合竞价报单
    
      EXCHANGE_STATUS_AUCTION_BALANCE : 集合竞价价格平衡
    
      EXCHANGE_STATUS_AUCTION_MATCH : 集合竞价撮合
    
      EXCHANGE_STATUS_IN_CLOSED : 收盘
    
      EXCHANGE_STATUS_ONLY_CANCEL : 仅允许撤单
    
      EXCHANGE_STATUS_DAZONG_ORDERING : 大宗交易申报
    
      EXCHANGE_STATUS_DAZONG_INTENTION_ORDERING : 大宗交易意向申报
    
      EXCHANGE_STATUS_DAZONG_CONFIRM_ORDERING : 大宗交易成交申报
    
      EXCHANGE_STATUS_DAZONG_CLOSE_PRICE_ORDERING : 大宗交易盘后定价申报
    
      EXCHANGE_STATUS_ONLY_GOLD_DELIVERY : 交割申报
    
      EXCHANGE_STATUS_ONLY_GOLD_MIDDLE : 中立仓申报
    
      EXCHANGE_STATUS_AFTER_HOURS_SALE : 盘后协议买卖
    
      EXCHANGE_STATUS_CLOSING_AUCTION_MATCH : 收盘集合竞价
    
      EXCHANGE_STATUS_CLOSE_PRICE_ORDERING : 盘后定价申报
    """
    EXCHANGE_STATUS_AFTER_HOURS_SALE: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_AFTER_HOURS_SALE: 62>
    EXCHANGE_STATUS_AUCTION_BALANCE: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_AUCTION_BALANCE: 52>
    EXCHANGE_STATUS_AUCTION_MATCH: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_AUCTION_MATCH: 53>
    EXCHANGE_STATUS_AUCTION_ORDERING: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_AUCTION_ORDERING: 51>
    EXCHANGE_STATUS_CLOSE_PRICE_ORDERING: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_CLOSE_PRICE_ORDERING: 64>
    EXCHANGE_STATUS_CLOSING_AUCTION_MATCH: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_CLOSING_AUCTION_MATCH: 63>
    EXCHANGE_STATUS_DAZONG_CLOSE_PRICE_ORDERING: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_DAZONG_CLOSE_PRICE_ORDERING: 59>
    EXCHANGE_STATUS_DAZONG_CONFIRM_ORDERING: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_DAZONG_CONFIRM_ORDERING: 58>
    EXCHANGE_STATUS_DAZONG_INTENTION_ORDERING: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_DAZONG_INTENTION_ORDERING: 57>
    EXCHANGE_STATUS_DAZONG_ORDERING: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_DAZONG_ORDERING: 56>
    EXCHANGE_STATUS_INVALID: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_INVALID: 0>
    EXCHANGE_STATUS_IN_BEFORE_TRADING: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_IN_BEFORE_TRADING: 48>
    EXCHANGE_STATUS_IN_CLOSED: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_IN_CLOSED: 54>
    EXCHANGE_STATUS_IN_CONTINOUS: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_IN_CONTINOUS: 50>
    EXCHANGE_STATUS_NOTRADING: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_NOTRADING: 49>
    EXCHANGE_STATUS_ONLY_CANCEL: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_ONLY_CANCEL: 55>
    EXCHANGE_STATUS_ONLY_GOLD_DELIVERY: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_ONLY_GOLD_DELIVERY: 60>
    EXCHANGE_STATUS_ONLY_GOLD_MIDDLE: typing.ClassVar[EXTExchangeStatus]  # value = <EXTExchangeStatus.EXCHANGE_STATUS_ONLY_GOLD_MIDDLE: 61>
    __members__: typing.ClassVar[dict[str, EXTExchangeStatus]]  # value = {'EXCHANGE_STATUS_INVALID': <EXTExchangeStatus.EXCHANGE_STATUS_INVALID: 0>, 'EXCHANGE_STATUS_IN_BEFORE_TRADING': <EXTExchangeStatus.EXCHANGE_STATUS_IN_BEFORE_TRADING: 48>, 'EXCHANGE_STATUS_NOTRADING': <EXTExchangeStatus.EXCHANGE_STATUS_NOTRADING: 49>, 'EXCHANGE_STATUS_IN_CONTINOUS': <EXTExchangeStatus.EXCHANGE_STATUS_IN_CONTINOUS: 50>, 'EXCHANGE_STATUS_AUCTION_ORDERING': <EXTExchangeStatus.EXCHANGE_STATUS_AUCTION_ORDERING: 51>, 'EXCHANGE_STATUS_AUCTION_BALANCE': <EXTExchangeStatus.EXCHANGE_STATUS_AUCTION_BALANCE: 52>, 'EXCHANGE_STATUS_AUCTION_MATCH': <EXTExchangeStatus.EXCHANGE_STATUS_AUCTION_MATCH: 53>, 'EXCHANGE_STATUS_IN_CLOSED': <EXTExchangeStatus.EXCHANGE_STATUS_IN_CLOSED: 54>, 'EXCHANGE_STATUS_ONLY_CANCEL': <EXTExchangeStatus.EXCHANGE_STATUS_ONLY_CANCEL: 55>, 'EXCHANGE_STATUS_DAZONG_ORDERING': <EXTExchangeStatus.EXCHANGE_STATUS_DAZONG_ORDERING: 56>, 'EXCHANGE_STATUS_DAZONG_INTENTION_ORDERING': <EXTExchangeStatus.EXCHANGE_STATUS_DAZONG_INTENTION_ORDERING: 57>, 'EXCHANGE_STATUS_DAZONG_CONFIRM_ORDERING': <EXTExchangeStatus.EXCHANGE_STATUS_DAZONG_CONFIRM_ORDERING: 58>, 'EXCHANGE_STATUS_DAZONG_CLOSE_PRICE_ORDERING': <EXTExchangeStatus.EXCHANGE_STATUS_DAZONG_CLOSE_PRICE_ORDERING: 59>, 'EXCHANGE_STATUS_ONLY_GOLD_DELIVERY': <EXTExchangeStatus.EXCHANGE_STATUS_ONLY_GOLD_DELIVERY: 60>, 'EXCHANGE_STATUS_ONLY_GOLD_MIDDLE': <EXTExchangeStatus.EXCHANGE_STATUS_ONLY_GOLD_MIDDLE: 61>, 'EXCHANGE_STATUS_AFTER_HOURS_SALE': <EXTExchangeStatus.EXCHANGE_STATUS_AFTER_HOURS_SALE: 62>, 'EXCHANGE_STATUS_CLOSING_AUCTION_MATCH': <EXTExchangeStatus.EXCHANGE_STATUS_CLOSING_AUCTION_MATCH: 63>, 'EXCHANGE_STATUS_CLOSE_PRICE_ORDERING': <EXTExchangeStatus.EXCHANGE_STATUS_CLOSE_PRICE_ORDERING: 64>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EXTOfferStatus:
    """
    订阅行情平台类型
    
    Members:
    
      XT_OFFER_STATUS_SP : 实盘
    
      XT_OFFER_STATUS_MN : 模拟盘
    """
    XT_OFFER_STATUS_MN: typing.ClassVar[EXTOfferStatus]  # value = <EXTOfferStatus.XT_OFFER_STATUS_MN: 49>
    XT_OFFER_STATUS_SP: typing.ClassVar[EXTOfferStatus]  # value = <EXTOfferStatus.XT_OFFER_STATUS_SP: 48>
    __members__: typing.ClassVar[dict[str, EXTOfferStatus]]  # value = {'XT_OFFER_STATUS_SP': <EXTOfferStatus.XT_OFFER_STATUS_SP: 48>, 'XT_OFFER_STATUS_MN': <EXTOfferStatus.XT_OFFER_STATUS_MN: 49>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EXTSubjectsStatus:
    """
    两融标的状态
    
    Members:
    
      SUBJECTS_STATUS_NORMAL : 正常
    
      SUBJECTS_STATUS_PAUSE : 暂停
    
      SUBJECTS_STATUS_NOT : 非标的
    """
    SUBJECTS_STATUS_NORMAL: typing.ClassVar[EXTSubjectsStatus]  # value = <EXTSubjectsStatus.SUBJECTS_STATUS_NORMAL: 48>
    SUBJECTS_STATUS_NOT: typing.ClassVar[EXTSubjectsStatus]  # value = <EXTSubjectsStatus.SUBJECTS_STATUS_NOT: 50>
    SUBJECTS_STATUS_PAUSE: typing.ClassVar[EXTSubjectsStatus]  # value = <EXTSubjectsStatus.SUBJECTS_STATUS_PAUSE: 49>
    __members__: typing.ClassVar[dict[str, EXTSubjectsStatus]]  # value = {'SUBJECTS_STATUS_NORMAL': <EXTSubjectsStatus.SUBJECTS_STATUS_NORMAL: 48>, 'SUBJECTS_STATUS_PAUSE': <EXTSubjectsStatus.SUBJECTS_STATUS_PAUSE: 49>, 'SUBJECTS_STATUS_NOT': <EXTSubjectsStatus.SUBJECTS_STATUS_NOT: 50>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EXtExDivdendType:
    """
    除权除息标志
    
    Members:
    
      XT_EXD_NORMAL : 不是除权除息
    
      XT_EXD_RIGHT : 除权
    
      XT_EXD_DIVDEND : 除息
    
      XT_EXD_XT_RIGHT_DIVDEND : 除权除息
    """
    XT_EXD_DIVDEND: typing.ClassVar[EXtExDivdendType]  # value = <EXtExDivdendType.XT_EXD_DIVDEND: 2>
    XT_EXD_NORMAL: typing.ClassVar[EXtExDivdendType]  # value = <EXtExDivdendType.XT_EXD_NORMAL: 0>
    XT_EXD_RIGHT: typing.ClassVar[EXtExDivdendType]  # value = <EXtExDivdendType.XT_EXD_RIGHT: 1>
    XT_EXD_XT_RIGHT_DIVDEND: typing.ClassVar[EXtExDivdendType]  # value = <EXtExDivdendType.XT_EXD_XT_RIGHT_DIVDEND: 3>
    __members__: typing.ClassVar[dict[str, EXtExDivdendType]]  # value = {'XT_EXD_NORMAL': <EXtExDivdendType.XT_EXD_NORMAL: 0>, 'XT_EXD_RIGHT': <EXtExDivdendType.XT_EXD_RIGHT: 1>, 'XT_EXD_DIVDEND': <EXtExDivdendType.XT_EXD_DIVDEND: 2>, 'XT_EXD_XT_RIGHT_DIVDEND': <EXtExDivdendType.XT_EXD_XT_RIGHT_DIVDEND: 3>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EXtMaxMarginSideAlgorithmType:
    """
    是否使用大额单边保证金算法
    
    Members:
    
      XT_FTDC_MMSA_NO : 不使用大额单边保证金算法
    
      XT_FTDC_MMSA_YES : 使用大额单边保证金算法
    """
    XT_FTDC_MMSA_NO: typing.ClassVar[EXtMaxMarginSideAlgorithmType]  # value = <EXtMaxMarginSideAlgorithmType.XT_FTDC_MMSA_NO: 48>
    XT_FTDC_MMSA_YES: typing.ClassVar[EXtMaxMarginSideAlgorithmType]  # value = <EXtMaxMarginSideAlgorithmType.XT_FTDC_MMSA_YES: 49>
    __members__: typing.ClassVar[dict[str, EXtMaxMarginSideAlgorithmType]]  # value = {'XT_FTDC_MMSA_NO': <EXtMaxMarginSideAlgorithmType.XT_FTDC_MMSA_NO: 48>, 'XT_FTDC_MMSA_YES': <EXtMaxMarginSideAlgorithmType.XT_FTDC_MMSA_YES: 49>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EXtOverFreqOrderMode:
    """
    下单超过流控时处理方式
    
    Members:
    
      OFQ_FORBID : 禁止
    
      OFQ_QUEUE : 队列
    """
    OFQ_FORBID: typing.ClassVar[EXtOverFreqOrderMode]  # value = <EXtOverFreqOrderMode.OFQ_FORBID: 0>
    OFQ_QUEUE: typing.ClassVar[EXtOverFreqOrderMode]  # value = <EXtOverFreqOrderMode.OFQ_QUEUE: 1>
    __members__: typing.ClassVar[dict[str, EXtOverFreqOrderMode]]  # value = {'OFQ_FORBID': <EXtOverFreqOrderMode.OFQ_FORBID: 0>, 'OFQ_QUEUE': <EXtOverFreqOrderMode.OFQ_QUEUE: 1>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EXtSuspendedType:
    """
    停牌标志
    
    Members:
    
      XT_NO_SUSPENDED : 不停牌
    
      XT_SUSPENDED : 停牌
    """
    XT_NO_SUSPENDED: typing.ClassVar[EXtSuspendedType]  # value = <EXtSuspendedType.XT_NO_SUSPENDED: 0>
    XT_SUSPENDED: typing.ClassVar[EXtSuspendedType]  # value = <EXtSuspendedType.XT_SUSPENDED: 1>
    __members__: typing.ClassVar[dict[str, EXtSuspendedType]]  # value = {'XT_NO_SUSPENDED': <EXtSuspendedType.XT_NO_SUSPENDED: 0>, 'XT_SUSPENDED': <EXtSuspendedType.XT_SUSPENDED: 1>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PortfolioDealType:
    """
    投资组合成交类型
    
    Members:
    
      XT_PORTFOLIO_ADJUST_COMMON : 普通调整
    
      XT_PORTFOLIO_ADJUST_RESTRICTED_STOCK : 限售股
    
      XT_PORTFOLIO_ADJUST_SUB_FUND : 子基金
    
      XT_PORTFOLIO_ADJUST_INCOME : 特殊成交类型, 收入
    
      XT_PORTFOLIO_ADJUST_COST : 特殊成交类型, 费用
    
      XT_PORTFOLIO_ADJUST_BONDS_CONVERT : 特殊成交类型, 可转债转股
    
      XT_PORTFOLIO_ADJUST_BONDS_SELLBACK : 特殊成交类型, 可转债回售
    
      XT_PORTFOLIO_ADJUST_STOCK_ALLOTMENT : 特殊成交类型, 股票配股
    
      XT_PORTFOLIO_ADJUST_STOCK_SUBSCRIPTION : 特殊成交类型, 新股申购
    
      XT_PORTFOLIO_ADJUST_DIVIDEND_STOCK : 特殊成交类型, 除权送股
    
      XT_PORTFOLIO_ADJUST_DIVIDEND_CASH : 特殊成交类型, 除权分红
    """
    XT_PORTFOLIO_ADJUST_BONDS_CONVERT: typing.ClassVar[PortfolioDealType]  # value = <PortfolioDealType.XT_PORTFOLIO_ADJUST_BONDS_CONVERT: 5>
    XT_PORTFOLIO_ADJUST_BONDS_SELLBACK: typing.ClassVar[PortfolioDealType]  # value = <PortfolioDealType.XT_PORTFOLIO_ADJUST_BONDS_SELLBACK: 6>
    XT_PORTFOLIO_ADJUST_COMMON: typing.ClassVar[PortfolioDealType]  # value = <PortfolioDealType.XT_PORTFOLIO_ADJUST_COMMON: 0>
    XT_PORTFOLIO_ADJUST_COST: typing.ClassVar[PortfolioDealType]  # value = <PortfolioDealType.XT_PORTFOLIO_ADJUST_COST: 4>
    XT_PORTFOLIO_ADJUST_DIVIDEND_CASH: typing.ClassVar[PortfolioDealType]  # value = <PortfolioDealType.XT_PORTFOLIO_ADJUST_DIVIDEND_CASH: 10>
    XT_PORTFOLIO_ADJUST_DIVIDEND_STOCK: typing.ClassVar[PortfolioDealType]  # value = <PortfolioDealType.XT_PORTFOLIO_ADJUST_DIVIDEND_STOCK: 9>
    XT_PORTFOLIO_ADJUST_INCOME: typing.ClassVar[PortfolioDealType]  # value = <PortfolioDealType.XT_PORTFOLIO_ADJUST_INCOME: 3>
    XT_PORTFOLIO_ADJUST_RESTRICTED_STOCK: typing.ClassVar[PortfolioDealType]  # value = <PortfolioDealType.XT_PORTFOLIO_ADJUST_RESTRICTED_STOCK: 1>
    XT_PORTFOLIO_ADJUST_STOCK_ALLOTMENT: typing.ClassVar[PortfolioDealType]  # value = <PortfolioDealType.XT_PORTFOLIO_ADJUST_STOCK_ALLOTMENT: 7>
    XT_PORTFOLIO_ADJUST_STOCK_SUBSCRIPTION: typing.ClassVar[PortfolioDealType]  # value = <PortfolioDealType.XT_PORTFOLIO_ADJUST_STOCK_SUBSCRIPTION: 8>
    XT_PORTFOLIO_ADJUST_SUB_FUND: typing.ClassVar[PortfolioDealType]  # value = <PortfolioDealType.XT_PORTFOLIO_ADJUST_SUB_FUND: 2>
    __members__: typing.ClassVar[dict[str, PortfolioDealType]]  # value = {'XT_PORTFOLIO_ADJUST_COMMON': <PortfolioDealType.XT_PORTFOLIO_ADJUST_COMMON: 0>, 'XT_PORTFOLIO_ADJUST_RESTRICTED_STOCK': <PortfolioDealType.XT_PORTFOLIO_ADJUST_RESTRICTED_STOCK: 1>, 'XT_PORTFOLIO_ADJUST_SUB_FUND': <PortfolioDealType.XT_PORTFOLIO_ADJUST_SUB_FUND: 2>, 'XT_PORTFOLIO_ADJUST_INCOME': <PortfolioDealType.XT_PORTFOLIO_ADJUST_INCOME: 3>, 'XT_PORTFOLIO_ADJUST_COST': <PortfolioDealType.XT_PORTFOLIO_ADJUST_COST: 4>, 'XT_PORTFOLIO_ADJUST_BONDS_CONVERT': <PortfolioDealType.XT_PORTFOLIO_ADJUST_BONDS_CONVERT: 5>, 'XT_PORTFOLIO_ADJUST_BONDS_SELLBACK': <PortfolioDealType.XT_PORTFOLIO_ADJUST_BONDS_SELLBACK: 6>, 'XT_PORTFOLIO_ADJUST_STOCK_ALLOTMENT': <PortfolioDealType.XT_PORTFOLIO_ADJUST_STOCK_ALLOTMENT: 7>, 'XT_PORTFOLIO_ADJUST_STOCK_SUBSCRIPTION': <PortfolioDealType.XT_PORTFOLIO_ADJUST_STOCK_SUBSCRIPTION: 8>, 'XT_PORTFOLIO_ADJUST_DIVIDEND_STOCK': <PortfolioDealType.XT_PORTFOLIO_ADJUST_DIVIDEND_STOCK: 9>, 'XT_PORTFOLIO_ADJUST_DIVIDEND_CASH': <PortfolioDealType.XT_PORTFOLIO_ADJUST_DIVIDEND_CASH: 10>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PortfolioPositionType:
    """
    投资组合持仓类型
    
    Members:
    
      XT_PORTFOLIO_POSITION_COMMON : 
    
      XT_PORTFOLIO_POSITION_RESTRICTED_STOCK : 限售持仓
    
      XT_PORTFOLIO_POSITION_SUB_FUND : 子基金持仓
    
      XT_PORTFOLIO_POSITION_FIN_STOCK : 融资持仓
    
      XT_PORTFOLIO_POSITION_SLO_STOCK : 融券持仓
    """
    XT_PORTFOLIO_POSITION_COMMON: typing.ClassVar[PortfolioPositionType]  # value = <PortfolioPositionType.XT_PORTFOLIO_POSITION_COMMON: 0>
    XT_PORTFOLIO_POSITION_FIN_STOCK: typing.ClassVar[PortfolioPositionType]  # value = <PortfolioPositionType.XT_PORTFOLIO_POSITION_FIN_STOCK: 1002>
    XT_PORTFOLIO_POSITION_RESTRICTED_STOCK: typing.ClassVar[PortfolioPositionType]  # value = <PortfolioPositionType.XT_PORTFOLIO_POSITION_RESTRICTED_STOCK: 1000>
    XT_PORTFOLIO_POSITION_SLO_STOCK: typing.ClassVar[PortfolioPositionType]  # value = <PortfolioPositionType.XT_PORTFOLIO_POSITION_SLO_STOCK: 1003>
    XT_PORTFOLIO_POSITION_SUB_FUND: typing.ClassVar[PortfolioPositionType]  # value = <PortfolioPositionType.XT_PORTFOLIO_POSITION_SUB_FUND: 1001>
    __members__: typing.ClassVar[dict[str, PortfolioPositionType]]  # value = {'XT_PORTFOLIO_POSITION_COMMON': <PortfolioPositionType.XT_PORTFOLIO_POSITION_COMMON: 0>, 'XT_PORTFOLIO_POSITION_RESTRICTED_STOCK': <PortfolioPositionType.XT_PORTFOLIO_POSITION_RESTRICTED_STOCK: 1000>, 'XT_PORTFOLIO_POSITION_SUB_FUND': <PortfolioPositionType.XT_PORTFOLIO_POSITION_SUB_FUND: 1001>, 'XT_PORTFOLIO_POSITION_FIN_STOCK': <PortfolioPositionType.XT_PORTFOLIO_POSITION_FIN_STOCK: 1002>, 'XT_PORTFOLIO_POSITION_SLO_STOCK': <PortfolioPositionType.XT_PORTFOLIO_POSITION_SLO_STOCK: 1003>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class XtError:
    """
    错误信息，包含错误号和错误描述
    """
    def __bool__(self) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: str) -> None:
        ...
    def errorID(self) -> int:
        ...
    def errorMsg(self) -> str:
        ...
    def isSuccess(self) -> bool:
        ...
    def setErrorId(self, id: int) -> None:
        ...
    def setErrorMsg(self, msg: str) -> None:
        ...
class XtTraderApi:
    """
    交易api
    """
    @staticmethod
    def createXtTraderApi(address: str) -> XtTraderApi:
        ...
    @staticmethod
    def destroyAll() -> None:
        """
        销毁XtTraderApi多实例线程, 所有实例停止工作, joinAll()函数解除等待状态
        """
    @staticmethod
    def joinAll() -> None:
        """
        启动XtTraderApi多实例线程, 多实例情况下必须使用该函数, 同时单实例也可调用该函数
        """
    def batchSubscribQuote(self, data: list[CSubscribData], nRequestId: int) -> None:
        """
        批量订阅行情数据
        """
    def batchUnSubscribQuote(self, data: list[CSubscribData], nRequestId: int) -> None:
        """
        批量退订行情数据
        """
    def cancel(self, orderID: int, nRequestId: int) -> None:
        """
        按指令号撤单
        """
    def cancelOrder(self, accountID: str, orderSyeId: str, exchangeId: str, instrumentId: str, nRequestId: int, accountKey: str = '') -> None:
        """
        按委托号撤单
        """
    def cancelOrderSync(self, accountID: str, orderSyeId: str, exchangeId: str, instrumentId: str, error: XtError, accountKey: str = '') -> None:
        """
        同步按委托号撤单
        """
    def cancelSync(self, orderID: int, error: XtError, accountKey: str = '') -> None:
        """
        同步撤单，按指令号撤单
        """
    @typing.overload
    def check(self, orderInfo: COrdinaryOrder, nRequestId: int) -> None:
        """
        普通单风险试算
        """
    @typing.overload
    def check(self, orderInfo: CGroupOrder, nRequestId: int) -> None:
        """
        算法单风险试算
        """
    def createPortfolio(self, newPortfolioReq: CNewPortfolioReq, nRequestId: int) -> None:
        """
        创建新投资组合
        """
    def destroy(self) -> None:
        """
        析构XtTraderApi实例
        """
    def directOrder(self, orderInfo: COrdinaryOrder, nRequestId: int, accountKey: str = '') -> None:
        """
        直接下单，支持股票，期货，个股期权，期货期权，沪港通，深港通，只支持指定价普通下单
        """
    def enableCmdCancelOrder(self) -> None:
        """
        是否启用撤指令后补撤委托，默认不启用。启用后,会主动对撤销过的指令发起委托明细查询，针对发起撤指令但对应委托未了结的委托进行撤委托操作，直到委托撤销或没撤掉成交，下游只用关心指令状态即可。本函数需在登录前调用。
        """
    def enableOrderStat(self, flag: bool) -> None:
        """
        是否启用指令级成交统计,默认不启用。启用后,会主动对运行中的指令发起成交明细查询，统计完成交后通过onRtnOrderStat回调函数推送统计数据。本函数需在登录前调用。
        """
    def fundTransfer(self, fundTransferReq: CSecuFundTransferReq, nRequestId: int, accountKey: str = '') -> None:
        """
        资金划拨
        """
    def getKey(self, accountID: str, accountKey: list, index: int) -> XtError:
        ...
    def getUserName(self) -> str:
        ...
    def getVersion(self) -> str:
        ...
    def init(self, configFilePath: str = '../config') -> bool:
        """
        创建api实例，并进行初始化
        """
    def join(self) -> None:
        """
        启动XtTraderApi单实例线程, 多实例情况必须调用joinAll()函数
        """
    def joinAll_async(self) -> None:
        """
        异步启动XtTraderApi多实例线程, 多实例情况下必须使用该函数, 同时单实例也可调用该函数
        """
    def join_async(self) -> None:
        """
        启动XtTraderApi单实例线程, 多实例情况必须调用joinAll()函数
        """
    @typing.overload
    def modifyAlgoCommands(self, orderInfo: CIntelligentAlgorithmOrder, nOrderID: int, nRequestId: int, accountKey: str = '') -> None:
        """
        智能算法指令改单
        """
    @typing.overload
    def modifyAlgoCommands(self, orderInfo: CAlgorithmOrder, nOrderID: int, nRequestId: int, accountKey: str = '') -> None:
        """
        普通算法指令改单
        """
    def operateTask(self, op: CTaskOpRecord, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        指令暂停恢复
        """
    @typing.overload
    def order(self, orderInfo: COrdinaryOrder, nRequestId: int, accountKey: str = '') -> None:
        """
        普通单下单，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    @typing.overload
    def order(self, orderInfo: CGroupOrder, nRequestId: int, accountKey: str = '') -> None:
        """
        组合算法单下单，只支持股票
        """
    @typing.overload
    def order(self, orderInfo: CAlgGroupOrder, nRequestId: int, accountKey: str = '') -> None:
        """
        组合智能算法单下单，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    @typing.overload
    def order(self, orderInfo: CAlgorithmOrder, nRequestId: int, accountKey: str = '') -> None:
        """
        算法单下单，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    @typing.overload
    def order(self, orderInfo: CRandomOrder, nRequestId: int, accountKey: str = '') -> None:
        """
        随机量交易下单，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    @typing.overload
    def order(self, orderInfo: CIntelligentAlgorithmOrder, nRequestId: int, accountKey: str = '') -> None:
        """
        智能算法下单，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    @typing.overload
    def order(self, orderInfo: CExternAlgorithmOrder, nRequestId: int, accountKey: str = '') -> None:
        """
        主动算法下单，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    @typing.overload
    def order(self, orderInfo: COrdinaryGroupOrder, nRequestId: int, accountKey: str = '') -> None:
        """
        普通组合下单，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    @typing.overload
    def order(self, orderInfo: CExternAlgGroupOrder, nRequestId: int, accountKey: str = '') -> None:
        """
        组合外部算法单下单，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    @typing.overload
    def order(self, orderInfo: CHuaChuangAlgoGroupOrder, nRequestId: int, accountKey: str = '') -> None:
        """
        华创算法组合单下单参数，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    @typing.overload
    def order(self, orderInfo: CHuaChuangAlgorithmOrder, nRequestId: int, accountKey: str = '') -> None:
        """
        华创算法单下单参数，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    @typing.overload
    def orderSync(self, orderInfo: COrdinaryOrder, error: XtError, accountKey: str = '') -> int:
        """
        同步接口普通单下单，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    @typing.overload
    def orderSync(self, orderInfo: CAlgGroupOrder, error: XtError, accountKey: str = '') -> int:
        """
        组合智能算法单下单同步接口，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    @typing.overload
    def orderSync(self, orderInfo: CAlgorithmOrder, error: XtError, accountKey: str = '') -> int:
        """
        算法单下单，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    @typing.overload
    def orderSync(self, orderInfo: CIntelligentAlgorithmOrder, error: XtError, accountKey: str = '') -> int:
        """
        智能算法下单同步接口，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    @typing.overload
    def orderSync(self, orderInfo: CExternAlgorithmOrder, error: XtError, accountKey: str = '') -> int:
        """
        主动算法下单同步接口，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    @typing.overload
    def orderSync(self, orderInfo: CExternAlgGroupOrder, error: XtError, accountKey: str = '') -> int:
        """
        组合外部算法单下单同步接口，支持股票，期货，个股期权，期货期权，沪港通，深港通
        """
    def pauseSync(self, orderID: int, error: XtError) -> None:
        """
        按指令号暂停指令并暂停任务
        """
    def refreshStkClosedCompacts(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        刷新信用账号已了结负债信息
        """
    def refreshStkUnCloseCompacts(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        刷新信用账号未了结负债信息
        """
    def registerUserSystemInfo(self, accountID: str, IpPortAddr: str, len: int, CTPSystemInfo: str, nRequestId: int, accountKey: str = '') -> None:
        """
        上传终端ctp采集信息，用于传入ctp柜台需要留痕的终端信息
        """
    def reqAccountDetail(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号资金信息
        """
    def reqAccountDetailSync(self, accountID: str, error: XtError, accountKey: str = '') -> CAccountDetail:
        """
        请求账号资金信息
        """
    def reqAccountKeys(self, nRequestId: int) -> None:
        """
        获取用户下所有账号key
        """
    def reqAccountKeysSync(self, error: XtError) -> list[CAccountKey]:
        """
        获取用户下所有账号key
        """
    def reqAccountStatus(self, nRequestId: int, accountKey: str = '') -> None:
        """
        请求资金账号状态
        """
    def reqAccountStatusSync(self, accountKey: str = '') -> bool:
        """
        请求资金账号状态
        """
    def reqBankAmount(self, bankInfo: CQueryBankInfo, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号银证转账银行余额
        """
    def reqCanCancelOrderDetail(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号可撤单委托明细信息
        """
    def reqCanOrderVolume(self, opVolumeReq: COpVolumeReq, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号可下单量(根据迅投系统当前持仓和资金计算，可能跟实际情况有误差)
        """
    def reqCanOrderVolumeSync(self, opVolumeReq: COpVolumeReq, error: XtError, accountKey: str = '') -> int:
        """
        请求账号可下单量(根据迅投系统当前持仓和资金计算，可能跟实际情况有误差)
        """
    def reqComFund(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号普通柜台资金
        """
    def reqComPosition(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号普通柜台持仓
        """
    def reqCommandsInfo(self, nRequestId: int) -> None:
        """
        请求账户所有下单信息
        """
    def reqCommandsInfoSync(self, error: XtError) -> list[COrderInfo]:
        """
        同步请求账户所有指令信息
        """
    def reqCommandsInfoWithAccKey(self, nRequestId: int, accountKey: str = '') -> None:
        """
        请求资金账号所有下单指令
        """
    def reqCommandsInfoWithAccKeySync(self, error: XtError, accountKey: str = '') -> list[COrderInfo]:
        """
        同步请求资金账号所有下单指令
        """
    def reqCoveredStockPosition(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求期权账号备兑持仓信息
        """
    def reqCreditAssure(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求两融账号担保标的信息
        """
    def reqCreditDetail(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求两融账号综合资金信息
        """
    def reqCreditDetailSync(self, accountID: str, error: XtError, accountKey: str = '') -> CCreditDetail:
        """
        请求两融账号综合资金信息
        """
    def reqCreditSloCode(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求两融账号融券可融数量信息
        """
    def reqCreditSubjects(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求两融账号融资融券标的信息
        """
    @typing.overload
    def reqDealDetail(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号成交明细信息
        """
    @typing.overload
    def reqDealDetail(self, accountID: str, nRequestId: int, nOrderID: int, accountKey: str = '') -> None:
        """
        根据指令号请求账号成交明细信息
        """
    def reqDealDetailBySysID(self, accountID: str, nRequestId: int, orderSyeId: str, exchangeId: str, accountKey: str = '') -> None:
        """
        根据委托号请求账号成交明细信息
        """
    def reqDealDetailNew(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号成交明细信息
        """
    def reqDealDetailSync(self, accountID: str, error: XtError, accountKey: str = '') -> list[CDealDetail]:
        """
        同步请求账号成交明细信息
        """
    def reqDealDetailSyncByOrderID(self, accountID: str, error: XtError, nOrderID: int, accountKey: str = '') -> list[CDealDetail]:
        """
        同步根据指令号请求账号成交明细信息
        """
    def reqDealDetail_sync(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        同步请求账号成交明细信息
        """
    def reqDealStaticsSync(self, accountID: str, error: XtError, accountKey: str = '') -> list[CDealStatics]:
        """
        同步请求账号成交统计信息
        """
    def reqDeliveryDetail(self, accountID: str, startDate: str, endDate: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号结算单信息
        """
    def reqDeliveryDetailSync(self, accountID: str, startDate: str, endDate: str, error: XtError, accountKey: str = '') -> list[CDeliveryDetail]:
        """
        请求账号结算单信息 同步接口
        """
    def reqETFComponentStockInfo(self, exchangeId: str, instrumentId: str, nRequestId: int) -> None:
        """
        查询ETF成分股信息
        """
    def reqETFComponentStockInfoSync(self, exchangeId: str, instrumentId: str, error: XtError) -> list[CETFComponentStockInfo]:
        """
        查询ETF成分股信息 同步接口
        """
    def reqEnumItemName(self, enumName: str, enumItemValue: int) -> str:
        """
        查询枚举名称
        """
    def reqEtfDetails(self, nRequestId: int) -> None:
        """
        查询ETF申赎清单
        """
    def reqEtfDetailsSync(self, error: XtError) -> list[CETFPCFDetail]:
        """
        查询ETF申赎清单 同步接口
        """
    def reqExchangeStatus(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求市场状态信息
        """
    def reqFtAccCommissionRateDetail(self, accountID: str, exchangeId: str, instrumentId: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求期货账号的保证金率
        """
    def reqFtAccMarginRateDetail(self, accountID: str, exchangeId: str, instrumentId: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求期货账号的手续费率
        """
    def reqFundFlow(self, accountID: str, startDate: str, endDate: str, nRequestId: int, accountKey: str) -> None:
        """
        查询用户资金流水信息
        """
    def reqFundFlowSync(self, accountID: str, startDate: str, endDate: str, error: XtError, accountKey: str) -> list[CFundFlow]:
        """
        查询用户资金流水信息 同步接口
        """
    def reqFuturePositionStatics(self, accountID: str, nRequestId: int, accountKey: str) -> None:
        """
        请求期货账号持仓统计信息
        """
    def reqFuturePositionStaticsSync(self, accountID: str, nRequestId: XtError, accountKey: str) -> list[CFuturePositionStatics]:
        """
        请求期货账号持仓统计信息 同步接口
        """
    def reqGGTReferenceRate(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号汇率信息
        """
    def reqHistoryAccountDetailSync(self, accountID: str, startDate: str, endDate: str, error: XtError, accountKey: str = '') -> list[CAccountDetail]:
        """
        同步请求账号历史资金信息
        """
    def reqHistoryDealDetail(self, accountID: str, startDate: str, endDate: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号历史成交明细
        """
    def reqHistoryDealDetailSync(self, accountID: str, startDate: str, endDate: str, error: XtError, accountKey: str = '') -> list[CDealDetail]:
        """
        同步请求账号历史成交明细
        """
    def reqHistoryOrderDetail(self, accountID: str, startDate: str, endDate: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号历史委托明细
        """
    def reqHistoryOrderDetailSync(self, accountID: str, startDate: str, endDate: str, error: XtError, accountKey: str = '') -> list[COrderDetail]:
        """
        同步请求账号历史委托明细
        """
    def reqHistoryPositionStatics(self, accountID: str, startDate: str, endDate: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号历史持仓统计
        """
    def reqHistoryPositionStaticsSync(self, accountID: str, startDate: str, endDate: str, error: XtError, accountKey: str = '') -> list[CPositionStatics]:
        """
        同步请求账号历史持仓统计
        """
    def reqInitialPositionStatics(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号日初持仓统计信息
        """
    def reqInitialPositionStaticsSync(self, accountID: str, error: XtError, accountKey: str = '') -> list[CPositionStatics]:
        """
        同步请求账号日初持仓统计信息
        """
    def reqInstrumentDetail(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号期权行情信息
        """
    def reqInstrumentInfoByMarket(self, exchangeId: str, nRequestId: int, tradable: int = 0) -> None:
        """
        按市场请求合约信息
        """
    def reqOpVolume(self, opVolumeReq: COpVolumeReq, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号可下单量
        """
    @typing.overload
    def reqOrderDetail(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号委托明细信息
        """
    @typing.overload
    def reqOrderDetail(self, accountID: str, nRequestId: int, nOrderID: int, accountKey: str = '') -> None:
        """
        根据指令号请求账号委托明细信息
        """
    def reqOrderDetailBySysID(self, accountID: str, nRequestId: int, orderSyeId: str, exchangeId: str, accountKey: str) -> None:
        """
        根据委托号请求账号委托明细信息
        """
    def reqOrderDetailBySysIDSync(self, accountID: str, error: XtError, orderSyeId: str, exchangeId: str, accountKey: str) -> COrderDetail:
        """
        根据委托号请求账号委托明细信息 同步接口
        """
    def reqOrderDetailNew(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号委托明细信息
        """
    def reqOrderDetailSync(self, accountID: str, error: XtError, accountKey: str = '') -> list[COrderDetail]:
        """
        同步请求账号委托明细信息
        """
    def reqOrderDetailSyncByOrderID(self, accountID: str, error: XtError, nOrderID: int, accountKey: str = '') -> list[COrderDetail]:
        """
        同步根据指令号请求账号委托明细信息
        """
    def reqOrderDetail_sync(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        同步请求账号委托明细信息
        """
    def reqPortfolioDeal(self, nPortfolioID: int, nDate: int, nRequestId: int) -> None:
        """
        请求投资组合成交信息
        """
    def reqPortfolioMultiDeal(self, nPortfolioID: int, nFromDate: int, nToDate: int, nRequestId: int) -> None:
        """
        请求投资组合一段时间内的成交信息
        """
    def reqPortfolioMultiOrder(self, nPortfolioID: int, nFromDate: int, nToDate: int, nRequestId: int) -> None:
        """
        请求投资组合一段时间内的委托信息
        """
    def reqPortfolioOrder(self, nPortfolioID: int, nDate: int, nRequestId: int) -> None:
        """
        请求投资组合委托信息
        """
    def reqPortfolioPosition(self, nPortfolioID: int, nDate: int, nRequestId: int) -> None:
        """
        请求投资组合持仓信息
        """
    def reqPortfolioStats(self, nPortfolioIds: list[int], nTradeDate: int, nRequestId: int) -> None:
        """
        查询投资组合状态信息
        """
    def reqPositionDetail(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号持仓明细信息
        """
    def reqPositionDetailSync(self, accountID: str, error: XtError, accountKey: str = '') -> list[CPositionDetail]:
        """
        同步请求账号持仓明细信息
        """
    def reqPositionDetail_sync(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        同步请求账号持仓明细信息
        """
    def reqPositionStatics(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号持仓统计信息
        """
    def reqPositionStaticsSync(self, accountID: str, error: XtError, accountKey: str = '') -> list[CPositionStatics]:
        """
        同步请求账号持仓统计信息
        """
    def reqPositionStaticsSyncWithProductId(self, error: XtError, productId: int) -> list[CPositionStatics]:
        """
        同步请求产品下所有账号持仓统计
        """
    def reqPositionStatics_sync(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        同步请求账号持仓统计信息
        """
    def reqPriceData(self, exchangeId: str, instrumentId: str, nRequestId: int) -> None:
        """
        请求行情数据信息
        """
    def reqPriceDataByMarket(self, exchangeId: str, nRequestId: int, tradable: int = 0) -> None:
        """
        按市场请求行情数据信息
        """
    def reqPriceDataSync(self, exchangeId: str, instrumentId: str, error: XtError) -> CPriceData:
        """
        请求行情数据信息 同步接口
        """
    def reqProductData(self, nRequestId: int) -> None:
        """
        请求用户产品信息
        """
    def reqProductDataSync(self, error: XtError) -> list[CProductData]:
        """
        请求用户产品信息
        """
    def reqProductIdByAccountKey(self, accountKey: str) -> int:
        """
        获取账号key对应产品Id
        """
    def reqProductIds(self, nRequestId: int) -> None:
        """
        获取用户下所有的产品Id
        """
    def reqProductPortfolio(self, nProductID: int, nRequestId: int) -> None:
        """
        查询产品Id下所有的投资组合
        """
    def reqSecuAccount(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求股东号，用于多股东时指定股东号
        """
    def reqSingleInstrumentInfo(self, exchangeId: str, instrumentId: str, nRequestId: int) -> None:
        """
        请求账号合约行情信息
        """
    def reqStkClosedCompacts(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求信用账号已了结负债信息
        """
    def reqStkClosedCompactsSync(self, accountID: str, error: XtError, accountKey: str = '') -> list[CStkClosedCompacts]:
        """
        请求信用账号已了结负债信息 同步接口
        """
    def reqStkOptCombPositionDetail(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求期权账号组合持仓信息
        """
    def reqStkUnCloseCompacts(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求信用账号未了结负债信息
        """
    def reqStkUnCloseCompactsSync(self, accountID: str, error: XtError, accountKey: str = '') -> list[CStkUnClosedCompacts]:
        """
        请求信用账号未了结负债信息 同步接口
        """
    def reqStkcompacts(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求信用账号负债合约信息，该接口已废弃
        """
    def reqStrategyInfo(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求收益互换账号框架号
        """
    def reqSubscribeInfo(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号新股额度信息
        """
    def reqTradeDay(self, nRequestId: int) -> None:
        """
        获取当前交易日
        """
    def reqTransferBank(self, accountID: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号银证转账银行信息
        """
    def reqTransferSerial(self, accountID: str, startDate: str, endDate: str, nRequestId: int, accountKey: str = '') -> None:
        """
        请求账号银证转账银行流水
        """
    def reqUserConfig(self, metaID: int, startDate: str, endDate: str, strTag: str, nRequestId: int) -> None:
        """
        查询用户设置
        """
    def reqUserConfigSync(self, metaID: int, startDate: str, endDate: str, strTag: str, error: XtError) -> list[CUserConfig]:
        """
        查询用户设置 同步接口
        """
    def resumeSync(self, orderID: int, error: XtError) -> None:
        """
        按指令号恢复指令并恢复任务
        """
    def secuTransfer(self, secuTransferReq: CSecuFundTransferReq, nRequestId: int, accountKey: str = '') -> None:
        """
        股份划拨
        """
    def setCallback(self, pCallback: ...) -> None:
        """
        设置数据回调对象
        """
    def setCmdFrzCheckOption(self, nCmdFrzCheckOption: int) -> None:
        """
        设置用户下单指令冻结选项
        """
    def startNamedTimer(self, timerName: str, intervalInMilliSecond: int, time: int, nextDay: bool) -> None:
        """
        设置用户自己的定时器
        """
    def startTimer(self, millsec: int) -> None:
        """
        设置用户自己的定时器
        """
    def stopNamedTimer(self, timerName: str) -> None:
        """
        停止用户自己的定时器
        """
    def stopTimer(self) -> None:
        """
        停止用户自己的定时器
        """
    def subscribQuote(self, data: CSubscribData, nRequestId: int) -> None:
        """
        订阅行情数据
        """
    def transfer(self, transferReq: CTransferReq, nRequestId: int, accountKey: str = '') -> None:
        """
        银证转账
        """
    def unSubscribQuote(self, data: CSubscribData, nRequestId: int) -> None:
        """
        退订行情数据
        """
    def updateCommandCondition(self, orderId: int, m_strOtherParam: str, strKey: str, nRequestId: int) -> None:
        """
        更新条件单指令
        """
    def updateCommandConditionSync(self, orderId: int, m_strOtherParam: str, strKey: str, error: XtError) -> None:
        """
        更新条件单指令 同步接口
        """
    def userLogin(self, userName: str, password: str, nRequestId: int, machineInfo: str = None, appid: str = None, authcode: str = None) -> None:
        """
        用户登陆
        """
    def userLoginSync(self, userName: str, password: str, machineInfo: str = None, appid: str = None, authcode: str = None) -> XtError:
        """
        用户登陆 同步接口
        """
    def userLogout(self, userName: str, password: str, nRequestId: int) -> None:
        """
        用户登出
        """




class XtTraderApiCallback:
    """
    交易api回调接口
    """
    def __init__(self) -> None:
        ...
    def onBatchReqAccountDetail(self, accountID: str, nRequestId: int, data: list[CAccountDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号资金的回调函数
        """
    def onBatchReqAccountDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CAccountDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号资金的回调函数
        """
    def onBatchReqAccountKey(self, nRequestId: int, data: list[CAccountKey], isLast: bool, error: XtError) -> None:
        """
        获取用户下所有账号key的回调函数
        """
    def onBatchReqCInstrumentDetail(self, accountID: str, nRequestId: int, data: list[CInstrumentDetail], isLast: bool, error: XtError) -> None:
        """
        请求合约数据的回调函数
        """
    def onBatchReqCInstrumentDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CInstrumentDetail], isLast: bool, error: XtError) -> None:
        """
        请求合约数据的回调函数
        """
    def onBatchReqCanCancelOrderDetail(self, accountID: str, nRequestId: int, data: list[COrderDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号可撤单委托明细的回调函数
        """
    def onBatchReqCanCancelOrderDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[COrderDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号可撤单委托明细的回调函数
        """
    def onBatchReqComFund(self, accountID: str, nRequestId: int, data: list[CStockComFund], isLast: bool, error: XtError) -> None:
        """
        请求账号账号普通柜台资金的回调函数
        """
    def onBatchReqComFundWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CStockComFund], isLast: bool, error: XtError) -> None:
        """
        请求账号账号普通柜台资金的回调函数
        """
    def onBatchReqComPosition(self, accountID: str, nRequestId: int, data: list[CStockComPosition], isLast: bool, error: XtError) -> None:
        """
        请求账号普通柜台持仓的回调函数
        """
    def onBatchReqComPositionWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CStockComPosition], isLast: bool, error: XtError) -> None:
        """
        请求账号普通柜台持仓的回调函数
        """
    def onBatchReqCommandsInfo(self, nRequestId: int, data: list[COrderInfo], isLast: bool, error: XtError) -> None:
        """
        请求所有下单信息的回调函数
        """
    def onBatchReqCoveredStockPosition(self, accountID: str, nRequestId: int, data: list[CCoveredStockPosition], isLast: bool, error: XtError) -> None:
        """
        请求期权账号备兑持仓的回调函数
        """
    def onBatchReqCoveredStockPositionWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CCoveredStockPosition], isLast: bool, error: XtError) -> None:
        """
        请求期权账号备兑持仓的回调函数
        """
    def onBatchReqCreditAccountDetail(self, accountID: str, nRequestId: int, data: list[CCreditAccountDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号两融资金的回调函数
        """
    def onBatchReqCreditAccountDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CCreditAccountDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号两融资金的回调函数
        """
    def onBatchReqCreditAssure(self, accountID: str, nRequestId: int, data: list[CCreditAssure], isLast: bool, error: XtError) -> None:
        """
        请求两融账号担保标的的回调函数
        """
    def onBatchReqCreditAssureWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CCreditAssure], isLast: bool, error: XtError) -> None:
        """
        请求两融账号担保标的的回调函数
        """
    def onBatchReqCreditDetail(self, accountID: str, nRequestId: int, data: list[CCreditDetail], isLast: bool, error: XtError) -> None:
        """
        请求两融账号两融综合资金数据的回调函数
        """
    def onBatchReqCreditDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CCreditDetail], isLast: bool, error: XtError) -> None:
        """
        请求两融账号两融综合资金数据的回调函数
        """
    def onBatchReqCreditSloCode(self, accountID: str, nRequestId: int, data: list[CCreditSloCode], isLast: bool, error: XtError) -> None:
        """
        请求两融账号融券可融数量的回调函数
        """
    def onBatchReqCreditSloCodeWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CCreditSloCode], isLast: bool, error: XtError) -> None:
        """
        请求两融账号融券可融数量的回调函数
        """
    def onBatchReqCreditSubjects(self, accountID: str, nRequestId: int, data: list[CCreditSubjects], isLast: bool, error: XtError) -> None:
        """
        请求两融账号融资融券标的的回调函数
        """
    def onBatchReqCreditSubjectsWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CCreditSubjects], isLast: bool, error: XtError) -> None:
        """
        请求两融账号融资融券标的的回调函数
        """
    def onBatchReqDealDetail(self, accountID: str, nRequestId: int, data: list[CDealDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号成交明细的回调函数
        """
    def onBatchReqDealDetailBySysID(self, accountID: str, nRequestId: int, orderSyeId: str, exchangeId: str, data: list[CDealDetail], isLast: bool, error: XtError) -> None:
        """
        根据委托号请求账号成交明细信息的回调函数
        """
    def onBatchReqDealDetailBySysIDWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, orderSyeId: str, exchangeId: str, data: list[CDealDetail], isLast: bool, error: XtError) -> None:
        """
        根据委托号请求账号成交明细信息的回调函数
        """
    def onBatchReqDealDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CDealDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号成交明细的回调函数
        """
    def onBatchReqDeliveryDetail(self, accountID: str, nRequestId: int, data: list[CDeliveryDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号结算单信息的回调函数
        """
    def onBatchReqDeliveryDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CDeliveryDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号结算单信息的回调函数
        """
    def onBatchReqHistoryDealDetail(self, accountID: str, nRequestId: int, data: list[CDealDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号历史成交明细的回调函数
        """
    def onBatchReqHistoryDealDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CDealDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号历史成交明细的回调函数
        """
    def onBatchReqHistoryOrderDetail(self, accountID: str, nRequestId: int, data: list[COrderDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号历史委托明细的回调函数
        """
    def onBatchReqHistoryOrderDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[COrderDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号历史委托明细的回调函数
        """
    def onBatchReqHistoryPositionStatics(self, accountID: str, nRequestId: int, data: list[CPositionStatics], isLast: bool, error: XtError) -> None:
        """
        请求账号历史持仓统计的回调函数
        """
    def onBatchReqHistoryPositionStaticsWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CPositionStatics], isLast: bool, error: XtError) -> None:
        """
        请求账号历史持仓统计的回调函数
        """
    def onBatchReqInstrumentInfoByMarket(self, nRequestId: int, data: list[CInstrumentInfo], isLast: bool, error: XtError) -> None:
        """
        按市场请求合约信息的回调函数
        """
    def onBatchReqInstrumentInfoByMarketWithMkt(self, nRequestId: int, exchangeId: str, data: list[CInstrumentInfo], isLast: bool, error: XtError) -> None:
        """
        按市场请求合约信息的回调函数
        """
    def onBatchReqOrderDetail(self, accountID: str, nRequestId: int, data: list[COrderDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号委托明细的回调函数
        """
    def onBatchReqOrderDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[COrderDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号委托明细的回调函数
        """
    def onBatchReqPortfolioDeal(self, nPortfolioID: int, nRequestId: int, data: list[CDealDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号成交明细的回调函数
        """
    def onBatchReqPortfolioMultiDeal(self, nPortfolioID: int, nRequestId: int, data: list[CDealDetail], isLast: bool, error: XtError) -> None:
        """
        请求投资组合一段时间内的成交信息的回调函数
        """
    def onBatchReqPortfolioMultiOrder(self, nPortfolioID: int, nRequestId: int, data: list[COrderDetail], isLast: bool, error: XtError) -> None:
        """
        请求投资组合一段时间内的委托信息的回调函数
        """
    def onBatchReqPortfolioOrder(self, nPortfolioID: int, nRequestId: int, data: list[COrderDetail], isLast: bool, error: XtError) -> None:
        """
        请求投资组合委托信息的回调函数
        """
    def onBatchReqPortfolioPosition(self, nPortfolioID: int, nRequestId: int, data: list[CPositionStatics], isLast: bool, error: XtError) -> None:
        """
        请求投资组合持仓信息的回调函数
        """
    def onBatchReqPositionDetail(self, accountID: str, nRequestId: int, data: list[CPositionDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号持仓明细的回调函数
        """
    def onBatchReqPositionDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CPositionDetail], isLast: bool, error: XtError) -> None:
        """
        请求账号持仓明细的回调函数
        """
    def onBatchReqPositionStatics(self, accountID: str, nRequestId: int, data: list[CPositionStatics], isLast: bool, error: XtError) -> None:
        """
        请求账号持仓统计的回调函数
        """
    def onBatchReqPositionStaticsWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CPositionStatics], isLast: bool, error: XtError) -> None:
        """
        请求账号持仓统计的回调函数
        """
    def onBatchReqProductData(self, nRequestId: int, data: list[CProductData], isLast: bool, error: XtError) -> None:
        """
        请求产品信息的回调函数
        """
    def onBatchReqProductPortfolio(self, nProductID: int, nRequestId: int, data: list[CPortfolioInfo], isLast: bool, error: XtError) -> None:
        """
        查询产品Id下所有的投资组合的回调函数
        """
    def onBatchReqReferenceRate(self, accountID: str, nRequestId: int, data: list[CReferenceRate], isLast: bool, error: XtError) -> None:
        """
        请求港股账号汇率数据的回调函数
        """
    def onBatchReqReferenceRateWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CReferenceRate], isLast: bool, error: XtError) -> None:
        """
        请求港股账号汇率数据的回调函数
        """
    def onBatchReqSecuAccount(self, accountID: str, nRequestId: int, accountKey: str, data: list[CSecuAccount], isLast: bool, error: XtError) -> None:
        """
        请求股东号的回调函数
        """
    def onBatchReqStkClosedCompact(self, accountID: str, nRequestId: int, data: list[CStkClosedCompacts], isLast: bool, error: XtError) -> None:
        """
        请求已了结负债信息的回调函数
        """
    def onBatchReqStkClosedCompactWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CStkClosedCompacts], isLast: bool, error: XtError) -> None:
        """
        请求已了结负债信息的回调函数
        """
    def onBatchReqStkOptCombPositionDetail(self, accountID: str, nRequestId: int, data: list[CStockOptionCombPositionDetail], isLast: bool, error: XtError) -> None:
        """
        请求期权账号组合持仓数据的回调函数
        """
    def onBatchReqStkOptCombPositionDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CStockOptionCombPositionDetail], isLast: bool, error: XtError) -> None:
        """
        请求期权账号组合持仓数据的回调函数
        """
    def onBatchReqStkUnCloseCompact(self, accountID: str, nRequestId: int, data: list[CStkUnClosedCompacts], isLast: bool, error: XtError) -> None:
        """
        请求未了结负债信息的回调函数
        """
    def onBatchReqStkUnCloseCompactWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CStkUnClosedCompacts], isLast: bool, error: XtError) -> None:
        """
        请求未了结负债信息的回调函数
        """
    def onBatchReqStkcompacts(self, accountID: str, nRequestId: int, data: list[CStkCompacts], isLast: bool, error: XtError) -> None:
        """
        请求两融账号负债的回调函数
        """
    def onBatchReqStkcompactsWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CStkCompacts], isLast: bool, error: XtError) -> None:
        """
        请求两融账号负债的回调函数
        """
    def onBatchReqStrategyInfo(self, accountID: str, nRequestId: int, accountKey: str, data: list[CStrategyInfo], isLast: bool, error: XtError) -> None:
        """
        请求收益互换账号框架号的回调函数
        """
    def onBatchReqSubscribeInfo(self, accountID: str, nRequestId: int, data: list[CSubscribeInfo], isLast: bool, error: XtError) -> None:
        """
        请求新股额度数据的回调函数
        """
    def onBatchReqSubscribeInfoWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CSubscribeInfo], isLast: bool, error: XtError) -> None:
        """
        请求新股额度数据的回调函数
        """
    def onBatchReqTransferBank(self, accountID: str, nRequestId: int, data: list[CQueryBankInfo], isLast: bool, error: XtError) -> None:
        """
        请求账号银证转账银行信息的回调函数
        """
    def onBatchReqTransferBankWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CQueryBankInfo], isLast: bool, error: XtError) -> None:
        """
        请求账号银证转账银行信息的回调函数
        """
    def onBatchReqTransferSerial(self, accountID: str, nRequestId: int, data: list[CTransferSerial], isLast: bool, error: XtError) -> None:
        """
        请求账号银证转账银行流水的回调函数
        """
    def onBatchReqTransferSerialWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: list[CTransferSerial], isLast: bool, error: XtError) -> None:
        """
        请求账号银证转账银行流水的回调函数
        """
    def onCancel(self, nRequestId: int, error: XtError) -> None:
        """
        撤指令的回调函数
        """
    def onCancelOrder(self, nRequestId: int, error: XtError) -> None:
        """
        撤委托的回调函数
        """
    def onCancelWithRemark(self, nRequestId: int, strRemark: str, error: XtError) -> None:
        """
        撤指令的回调函数
        """
    def onCheck(self, nRequestId: int, data: CCheckData, error: XtError) -> None:
        """
        风险试算的回调函数
        """
    def onConnected(self, success: bool, errorMsg: str) -> None:
        """
        连接服务器的回调函数
        """
    def onCreatePortfolio(self, nRequestId: int, nPortfolioID: int, strRemark: str, error: XtError) -> None:
        """
        创建新投资组合的回调函数
        """
    def onCustomTimer(self) -> None:
        """
        用户自己的定时器回调
        """
    def onDirectOrder(self, nRequestId: int, strOrderSysID: str, strRemark: str, error: XtError) -> None:
        """
        直接下单的回调函数
        """
    def onFundTransfer(self, nRequestId: int, error: XtError) -> None:
        """
        资金划拨的回调函数
        """
    def onModifyAlgoCommands(self, nRequestId: int, orderID: int, strRemark: str, error: XtError) -> None:
        """
        指令改参的回调函数
        """
    def onNamedTimer(self, timerName: str) -> None:
        """
        用户自己的定时器回调
        """
    def onOperateTask(self, accountID: str, nRequestId: int, accountKey: str, error: XtError) -> None:
        """
        暂停恢复任务回调
        """
    def onOrder(self, nRequestId: int, orderID: int, strRemark: str, error: XtError) -> None:
        """
        下单的回调函数
        """
    def onReqAccountDetail(self, accountID: str, nRequestId: int, data: CAccountDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号资金的回调函数
        """
    def onReqAccountDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CAccountDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号资金的回调函数
        """
    def onReqAccountKey(self, nRequestId: int, data: CAccountKey, isLast: bool, error: XtError) -> None:
        """
        获取用户下所有账号key的回调函数
        """
    def onReqAccountStatus(self, nRequestId: int, accountKey: str, status: bool) -> None:
        """
        请求资金账号状态的回调函数
        """
    def onReqBankAmount(self, accountID: str, nRequestId: int, data: CQueryBankAmount, error: XtError) -> None:
        """
        请求账号银证转账银行余额的回调函数
        """
    def onReqBankAmountWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CQueryBankAmount, error: XtError) -> None:
        """
        请求账号银证转账银行余额的回调函数
        """
    def onReqCInstrumentDetail(self, accountID: str, nRequestId: int, data: CInstrumentDetail, isLast: bool, error: XtError) -> None:
        """
        请求合约数据的回调函数
        """
    def onReqCInstrumentDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CInstrumentDetail, isLast: bool, error: XtError) -> None:
        """
        请求合约数据的回调函数
        """
    def onReqCanCancelOrderDetail(self, accountID: str, nRequestId: int, data: COrderDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号可撤单委托明细的回调函数
        """
    def onReqCanCancelOrderDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: COrderDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号可撤单委托明细的回调函数
        """
    def onReqCanOrderVolume(self, accountID: str, nRequestId: int, accountKey: str, market: str, instrument: str, nVolume: int, error: XtError) -> None:
        """
        请求账号可下单量的回调函数
        """
    def onReqComFund(self, accountID: str, nRequestId: int, data: CStockComFund, isLast: bool, error: XtError) -> None:
        """
        请求账号账号普通柜台资金的回调函数
        """
    def onReqComFundWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CStockComFund, isLast: bool, error: XtError) -> None:
        """
        请求账号账号普通柜台资金的回调函数
        """
    def onReqComPosition(self, accountID: str, nRequestId: int, data: CStockComPosition, isLast: bool, error: XtError) -> None:
        """
        请求账号普通柜台持仓的回调函数
        """
    def onReqComPositionWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CStockComPosition, isLast: bool, error: XtError) -> None:
        """
        请求账号普通柜台持仓的回调函数
        """
    def onReqCommandsInfo(self, nRequestId: int, data: COrderInfo, isLast: bool, error: XtError) -> None:
        """
        请求所有下单信息的回调函数
        """
    def onReqCommandsInfoWithAccKey(self, nRequestId: int, data: list[COrderInfo], isLast: bool, error: XtError) -> None:
        """
        请求资金账号下单指令信息的回调函数
        """
    def onReqCoveredStockPosition(self, accountID: str, nRequestId: int, data: CCoveredStockPosition, isLast: bool, error: XtError) -> None:
        """
        请求期权账号备兑持仓的回调函数
        """
    def onReqCoveredStockPositionWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CCoveredStockPosition, isLast: bool, error: XtError) -> None:
        """
        请求期权账号备兑持仓的回调函数
        """
    def onReqCreditAccountDetail(self, accountID: str, nRequestId: int, data: CCreditAccountDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号两融资金的回调函数
        """
    def onReqCreditAccountDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CCreditAccountDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号两融资金的回调函数
        """
    def onReqCreditAssure(self, accountID: str, nRequestId: int, data: CCreditAssure, isLast: bool, error: XtError) -> None:
        """
        请求两融账号担保标的的回调函数
        """
    def onReqCreditAssureWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CCreditAssure, isLast: bool, error: XtError) -> None:
        """
        请求两融账号担保标的的回调函数
        """
    def onReqCreditDetail(self, accountID: str, nRequestId: int, data: CCreditDetail, isLast: bool, error: XtError) -> None:
        """
        请求两融账号两融综合资金数据的回调函数
        """
    def onReqCreditDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CCreditDetail, isLast: bool, error: XtError) -> None:
        """
        请求两融账号两融综合资金数据的回调函数
        """
    def onReqCreditSloCode(self, accountID: str, nRequestId: int, data: CCreditSloCode, isLast: bool, error: XtError) -> None:
        """
        请求两融账号融券可融数量的回调函数
        """
    def onReqCreditSloCodeWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CCreditSloCode, isLast: bool, error: XtError) -> None:
        """
        请求两融账号融券可融数量的回调函数
        """
    def onReqCreditSubjects(self, accountID: str, nRequestId: int, data: CCreditSubjects, isLast: bool, error: XtError) -> None:
        """
        请求两融账号融资融券标的的回调函数
        """
    def onReqCreditSubjectsWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CCreditSubjects, isLast: bool, error: XtError) -> None:
        """
        请求两融账号融资融券标的的回调函数
        """
    def onReqDealDetail(self, accountID: str, nRequestId: int, data: CDealDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号成交明细的回调函数
        """
    def onReqDealDetailBySysID(self, accountID: str, nRequestId: int, orderSyeId: str, exchangeId: str, data: CDealDetail, isLast: bool, error: XtError) -> None:
        """
        根据委托号请求账号成交明细信息的回调函数
        """
    def onReqDealDetailBySysIDWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, orderSyeId: str, exchangeId: str, data: CDealDetail, isLast: bool, error: XtError) -> None:
        """
        根据委托号请求账号成交明细信息的回调函数
        """
    def onReqDealDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CDealDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号成交明细的回调函数
        """
    def onReqDeliveryDetail(self, accountID: str, nRequestId: int, data: CDeliveryDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号结算单信息的回调函数
        """
    def onReqDeliveryDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CDeliveryDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号结算单信息的回调函数
        """
    def onReqETFComponentStockInfo(self, nRequestId: int, data: list[CETFComponentStockInfo], error: XtError) -> None:
        """
        请求ETF成分股信息的回调函数
        """
    def onReqEtfDetails(self, nRequestId: int, data: list[CETFPCFDetail], error: XtError) -> None:
        """
        请求ETF申赎清单的回调函数
        """
    def onReqExchangeStatus(self, accountID: str, nRequestId: int, accountKey: str, data: list[CExchangeStatus], error: XtError) -> None:
        """
        市场状态信息回调接口
        """
    def onReqFtAccCommissionRateDetail(self, accountID: str, nRequestId: int, accountKey: str, data: CCommissionRateDetail, error: XtError) -> None:
        """
        请求期货账号保证金率的回调函数
        """
    def onReqFtAccMarginRateDetail(self, accountID: str, nRequestId: int, accountKey: str, data: CMarginRateDetail, isLast: bool, error: XtError) -> None:
        """
        请求期货账号手续费率的回调函数
        """
    def onReqFundFlow(self, accountID: str, nRequestId: int, accountKey: str, data: list[CFundFlow], error: XtError) -> None:
        """
        请求用户资金流水的回调函数
        """
    def onReqFuturePositionStatics(self, accountID: str, nRequestId: int, accountKey: str, data: list[CFuturePositionStatics], isLast: bool, error: XtError) -> None:
        """
        请求期货账号持仓统计的回调函数
        """
    def onReqHistoryDealDetail(self, accountID: str, nRequestId: int, data: CDealDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号历史成交明细的回调函数
        """
    def onReqHistoryDealDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CDealDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号历史成交明细的回调函数
        """
    def onReqHistoryOrderDetail(self, accountID: str, nRequestId: int, data: COrderDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号历史委托明细的回调函数
        """
    def onReqHistoryOrderDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: COrderDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号历史委托明细的回调函数
        """
    def onReqHistoryPositionStatics(self, accountID: str, nRequestId: int, data: CPositionStatics, isLast: bool, error: XtError) -> None:
        """
        请求账号历史持仓统计的回调函数
        """
    def onReqHistoryPositionStaticsWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CPositionStatics, isLast: bool, error: XtError) -> None:
        """
        请求账号历史持仓统计的回调函数
        """
    def onReqInitialPositionStatics(self, accountID: str, nRequestId: int, accountKey: str, data: list[CPositionStatics], isLast: bool, error: XtError) -> None:
        """
        请求账号日初持仓统计的回调函数
        """
    def onReqInstrumentInfoByMarket(self, nRequestId: int, data: CInstrumentInfo, isLast: bool, error: XtError) -> None:
        """
        按市场请求合约信息的回调函数
        """
    def onReqInstrumentInfoByMarketWithMkt(self, nRequestId: int, exchangeId: str, data: CInstrumentInfo, isLast: bool, error: XtError) -> None:
        """
        按市场请求合约信息的回调函数
        """
    def onReqOpVolume(self, accountID: str, nRequestId: int, dataKey: str, nVolume: int, isLast: bool, error: XtError) -> None:
        """
        请求账号可下单量的回调函数
        """
    def onReqOpVolumeWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, dataKey: str, nVolume: int, isLast: bool, error: XtError) -> None:
        """
        请求账号可下单量的回调函数
        """
    def onReqOrderDetail(self, accountID: str, nRequestId: int, data: COrderDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号委托明细的回调函数
        """
    def onReqOrderDetailBySysID(self, accountID: str, nRequestId: int, accountKey: str, orderSyeId: str, exchangeId: str, data: COrderDetail, error: XtError) -> None:
        """
        根据委托号请求账号委托明细信息
        """
    def onReqOrderDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: COrderDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号委托明细的回调函数
        """
    def onReqPortfolioDeal(self, nPortfolioID: int, nRequestId: int, data: CDealDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号成交明细的回调函数
        """
    def onReqPortfolioMultiDeal(self, nPortfolioID: int, nRequestId: int, data: CDealDetail, isLast: bool, error: XtError) -> None:
        """
        请求投资组合一段时间内的成交信息的回调函数
        """
    def onReqPortfolioMultiOrder(self, nPortfolioID: int, nRequestId: int, data: COrderDetail, isLast: bool, error: XtError) -> None:
        """
        请求投资组合一段时间内的委托信息的回调函数
        """
    def onReqPortfolioOrder(self, nPortfolioID: int, nRequestId: int, data: COrderDetail, isLast: bool, error: XtError) -> None:
        """
        请求投资组合委托信息的回调函数
        """
    def onReqPortfolioPosition(self, nPortfolioID: int, nRequestId: int, data: CPositionStatics, isLast: bool, error: XtError) -> None:
        """
        请求投资组合持仓信息的回调函数
        """
    def onReqPortfolioStat(self, nRequestId: int, nPortfolioId: int, data: CPortfolioStat, isLast: bool, error: XtError) -> None:
        """
        根据投资组合编号请求投资组合状态信息回调接口
        """
    def onReqPositionDetail(self, accountID: str, nRequestId: int, data: CPositionDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号持仓明细的回调函数
        """
    def onReqPositionDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CPositionDetail, isLast: bool, error: XtError) -> None:
        """
        请求账号持仓明细的回调函数
        """
    def onReqPositionStatics(self, accountID: str, nRequestId: int, data: CPositionStatics, isLast: bool, error: XtError) -> None:
        """
        请求账号持仓统计的回调函数
        """
    def onReqPositionStaticsWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CPositionStatics, isLast: bool, error: XtError) -> None:
        """
        请求账号持仓统计的回调函数
        """
    def onReqPriceData(self, nRequestId: int, data: CPriceData, error: XtError) -> None:
        """
        请求行情数据的回调函数
        """
    def onReqProductData(self, nRequestId: int, data: CProductData, isLast: bool, error: XtError) -> None:
        """
        请求产品信息的回调函数
        """
    def onReqProductIds(self, nRequestId: int, nProductID: int, accountKey: str, isLast: bool) -> None:
        """
        获取用户下所有的产品Id的回调函数
        """
    def onReqProductPortfolio(self, nProductID: int, nRequestId: int, data: CPortfolioInfo, isLast: bool, error: XtError) -> None:
        """
        查询产品Id下所有的投资组合的回调函数
        """
    def onReqReferenceRate(self, accountID: str, nRequestId: int, data: CReferenceRate, isLast: bool, error: XtError) -> None:
        """
        请求港股账号汇率数据的回调函数
        """
    def onReqReferenceRateWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CReferenceRate, isLast: bool, error: XtError) -> None:
        """
        请求港股账号汇率数据的回调函数
        """
    def onReqSecuAccount(self, accountID: str, nRequestId: int, accountKey: str, data: CSecuAccount, isLast: bool, error: XtError) -> None:
        """
        请求股东号的回调函数
        """
    def onReqSingleInstrumentInfo(self, nRequestId: int, data: CInstrumentInfo, error: XtError) -> None:
        """
        请求账号合约行情信息的回调函数
        """
    def onReqStkClosedCompact(self, accountID: str, nRequestId: int, data: CStkClosedCompacts, isLast: bool, error: XtError) -> None:
        """
        请求已了结负债信息的回调函数
        """
    def onReqStkClosedCompactWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CStkClosedCompacts, isLast: bool, error: XtError) -> None:
        """
        请求已了结负债信息的回调函数
        """
    def onReqStkOptCombPositionDetail(self, accountID: str, nRequestId: int, data: CStockOptionCombPositionDetail, isLast: bool, error: XtError) -> None:
        """
        请求期权账号组合持仓数据的回调函数
        """
    def onReqStkOptCombPositionDetailWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CStockOptionCombPositionDetail, isLast: bool, error: XtError) -> None:
        """
        请求期权账号组合持仓数据的回调函数
        """
    def onReqStkUnCloseCompact(self, accountID: str, nRequestId: int, data: CStkUnClosedCompacts, isLast: bool, error: XtError) -> None:
        """
        请求未了结负债信息的回调函数
        """
    def onReqStkUnCloseCompactWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CStkUnClosedCompacts, isLast: bool, error: XtError) -> None:
        """
        请求未了结负债信息的回调函数
        """
    def onReqStkcompacts(self, accountID: str, nRequestId: int, data: CStkCompacts, isLast: bool, error: XtError) -> None:
        """
        请求两融账号负债的回调函数
        """
    def onReqStkcompactsWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CStkCompacts, isLast: bool, error: XtError) -> None:
        """
        请求两融账号负债的回调函数
        """
    def onReqStrategyInfo(self, accountID: str, nRequestId: int, accountKey: str, data: CStrategyInfo, isLast: bool, error: XtError) -> None:
        """
        请求收益互换账号框架号的回调函数
        """
    def onReqSubscribeInfo(self, accountID: str, nRequestId: int, data: CSubscribeInfo, isLast: bool, error: XtError) -> None:
        """
        请求新股额度数据的回调函数
        """
    def onReqSubscribeInfoWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CSubscribeInfo, isLast: bool, error: XtError) -> None:
        """
        请求新股额度数据的回调函数
        """
    def onReqTradeDay(self, tradeDay: str, nRequestId: int, error: XtError) -> None:
        """
        请求当前交易日的回调函数
        """
    def onReqTransferBank(self, accountID: str, nRequestId: int, data: CQueryBankInfo, isLast: bool, error: XtError) -> None:
        """
        请求账号银证转账银行信息的回调函数
        """
    def onReqTransferBankWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CQueryBankInfo, isLast: bool, error: XtError) -> None:
        """
        请求账号银证转账银行信息的回调函数
        """
    def onReqTransferSerial(self, accountID: str, nRequestId: int, data: CTransferSerial, isLast: bool, error: XtError) -> None:
        """
        请求账号银证转账银行流水的回调函数
        """
    def onReqTransferSerialWithAccKey(self, accountID: str, nRequestId: int, accountKey: str, data: CTransferSerial, isLast: bool, error: XtError) -> None:
        """
        请求账号银证转账银行流水的回调函数
        """
    def onReqUserConfig(self, nRequestId: int, data: list[CUserConfig], error: XtError) -> None:
        """
        请求用户设置数据的回调函数
        """
    def onRtnAccountDetail(self, accountID: str, data: CAccountDetail) -> None:
        """
        主推的资金账号信息
        """
    def onRtnAlgoError(self, nOrderID: int, strRemark: str, error: XtError) -> None:
        """
        主推的算法母单错误信息
        """
    def onRtnCancelError(self, data: CCancelError) -> None:
        """
        主推的撤销信息
        """
    def onRtnCreditAccountDetail(self, accountID: str, data: CCreditAccountDetail) -> None:
        """
        主推的两融资金账号信息
        """
    def onRtnCreditDetail(self, data: CCreditDetail) -> None:
        """
        主推两融综合资金
        """
    def onRtnDealDetail(self, data: CDealDetail) -> None:
        """
        主推的成交明细
        """
    def onRtnExchangeStatus(self, data: CExchangeStatus) -> None:
        """
        主推市场状态信息
        """
    def onRtnLoginStatus(self, accountID: str, status: EBrokerLoginStatus, brokerType: int, errorMsg: str) -> None:
        """
        主推的用户登录状态
        """
    def onRtnLoginStatusCustom(self, accountID: str, status: EBrokerLoginStatus, brokerType: int, accountKey: str, userName: str, errorMsg: str) -> None:
        """
        主推的用户登录状态
        """
    def onRtnLoginStatusWithActKey(self, accountID: str, status: EBrokerLoginStatus, brokerType: int, accountKey: str, errorMsg: str) -> None:
        """
        主推的用户登录状态
        """
    def onRtnMarketAndTradeDay(self, market: str, tradeDay: str) -> None:
        """
        主推市场和交易日
        """
    def onRtnNetValue(self, data: CNetValue) -> None:
        """
        主推的产品净值信息
        """
    def onRtnOrder(self, data: COrderInfo) -> None:
        """
        主推的报单状态（指令）
        """
    def onRtnOrderDetail(self, data: COrderDetail) -> None:
        """
        主推的委托明细（委托）
        """
    def onRtnOrderError(self, data: COrderError) -> None:
        """
        主推的委托错误信息
        """
    def onRtnOrderStat(self, data: COrderStat) -> None:
        """
        主推的指令统计信息（指令）
        """
    def onRtnPriceData(self, data: CPriceData) -> None:
        """
        主推行情数据
        """
    def onRtnRCMsg(self, accountID: str, accountKey: str, strMsg: str) -> None:
        """
        主推风控信息
        """
    def onSecuTransfer(self, nRequestId: int, error: XtError) -> None:
        """
        股份划拨的回调函数
        """
    def onSubscribQuote(self, nRequestId: int, data: CSubscribData, error: XtError) -> None:
        """
        行情订阅的回调函数
        """
    def onTransfer(self, nRequestId: int, error: XtError) -> None:
        """
        银证转账的回调函数
        """
    def onUnSubscribQuote(self, nRequestId: int, data: CSubscribData, error: XtError) -> None:
        """
        行情退订的回调函数
        """
    def onUserLogin(self, userName: str, password: str, nRequestId: int, error: XtError) -> None:
        """
        用户登录的回调函数
        """
    def onUserLogout(self, userName: str, password: str, nRequestId: int, error: XtError) -> None:
        """
        用户登出的回调函数
        """
