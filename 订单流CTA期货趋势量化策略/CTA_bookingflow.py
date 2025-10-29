import os
import re
import calendar
import datetime as dtm
import numpy as np
import pandas as pd
from sqalpha.main import config_init, analyser_init, system_init, run, analyse
from sqalpha.api import *
from azdata import c
from datetime import datetime,date,time
from pymongo import MongoClient

def info(code):
        multiplier = instruments(code).contract_multiplier
        margin_rate = instruments(code).margin_rate
        return multiplier*margin_rate
class Database:
    def __init__(self, address: str, data_add: str, username='fushaohua', password='fushaohua123'):
        self.address = address
        self.data_add = data_add
        self.username_password = f'{username}:{password}'
        self.format = 'mongodb://{}@{}/?authsource=admin'
        self.client = MongoClient(self.format.format(self.username_password, self.address))
        self.database = self.client[self.data_add]

'''
此为趋势分析的第一部分，对cash_inflow进行所代表的结果进行有效检测，后续将更新对delta的回测结果，但由于求职目标（由量化QD——>商业分析）转向，后续对于QD/QR的研究已经不属于商业分析、数据分析领域，与作品集求职目的并无充分联系，故而在第一部分对cascash_inflow截至。
此处代码主要体现了博主利用python对于数据提取、清洗、撮合和过程优化能力。
后续对于回测结果的参数分析和商业分析中A/B test类似，故保留下来。
'''


'''
idea
    考虑到时间空间复杂度，在mongodb中查询的时候就把数据筛选出来：
        通过查询每一个collection中的limit
    排除掉："IF", "IH", "IC", "IM", "T", "TF", "TS"
        排除方法为：首先获得前五名，如果前五名中存在x个数据，则出栈，随后skip后在入栈limit(x)
        如果仍然是该期货类型，继续出栈，并skip().limit（）
        总结来看是 skip（5+Xi）.limit(Xi)

    INIT需要定义的：
        定义起始时间：为每天开始的时间
        定义结束时间： 夜盘23点，超过时间则直接跳过当天
        定义池的容量：默认为10
    
    handle_bar：
        同样，节省计算内存，每一次1minhandle_bar所要做的事情是： ————每一分钟查询一次可以减少滑点，而每五分钟查询一次，则会加大第五分钟的计算时间
        1. 查询数据库，计算此时1min的cash_flow增量并更新预调仓列表（此处可以选择定时器进行处理，但是放在handle_bar也一样，因为二者必须为单一线程关系，不存在优化空间）
                返回这一个datetime内的表、返回的字段仅包含'code'和'inflow'，inflow累加即可
    _______________________________
        但是五分钟查询在处理逻辑上更加的简单易懂，使用aggregate进行总和即可
        但是可以按照objects2进行同样的更新处理。这个地方可以直接可以仿照2的处理思路，直接读取所有的表的数据，然后按照此时的时间进行遍历

        2. 判断时间是否为5min，如果是，则进行调仓操作
            具体步骤为：
            1.获取此时的持仓情况
            2.将其分为买卖两种持仓，（以买为例）
            3.{持仓} - {更新} = {持仓改平仓的}  反过来就是{更新该开仓的}
            4.进行相应的平仓开仓
        3. 判断现在的时间是否为23点，如果是，则直接进入空循环，直到今天结束
    
    
    字段注意：
        数据库中的时间不统一：按照15日9：00为起始时间进行回测，
        注意datetime的类型处理
        数据库关于code的不统一：全部进行大小写处理
'''
class Bartoy:
    def __init__(self,code,interval=5):
        self.datetime = None
        self.raw_data = None
        self.cash_flow = 0
        self.interval = interval
        self.bars = {}
        self.code = code
        self.minute = None

    def terminal(self,givenTime,cash_inflow):
        interval = self.interval
        datetime = givenTime
        dt = pd.Timestamp(datetime)



        mod, lf = (dt.minute // interval, dt.minute % interval)
        if lf == 0:
            minute = dt
        else:
            minute = dt.replace(minute=mod * interval) + pd.Timedelta(minutes=interval)

        self.update(cash_inflow)
        self.bars[minute] = self.cash_flow
        self.minute = minute

    def update(self,cash_inflow):
        self.cash_flow += cash_inflow

    def clear_cash(self): #其实不太需要，但是如果不想用bars[minute]的话，就可以，我不太想用，因为涉及到了多种时间类型
        self.cash_flow = 0


def get_code(context,datetime):
    collections = context.collections
    database = context.database

    #获得每天第一分钟的code，然后这个code
    code_list = []
    for names in collections:
        code_cursor = database[names].find({'datetime':datetime},{'code':1,'cash_inflow':1,'_id':0})
        for code_doc in code_cursor:
            code = code_doc.get('code',0)
            code_list.append(code_list) # 此时保存了所有的code，然后依据code进行五分钟的撮合
    return code_list



def time_compare(interval,current_time):
    mod, lf = (current_time.minute // interval, current_time.minute % interval)
    if lf == 0:
        minute = current_time
    else:
        minute = current_time.replace(minute=mod * interval) + pd.Timedelta(minutes=interval)



    return minute,lf


def return_collections(address='192.168.1.119:62003',data_add='AZ_MINT_WIND'):
    client = Database(address=address, data_add=data_add)
    database = client.database

    return database

def return_dom_codes(context):
    # 获取当天的主力和次主力
    date = context.now.date()
    database = return_collections(address='192.168.1.119:27017',data_add='zcs')
    collection = database['wind_future_dom_day']
    cursor = collection.find({'date':str(date)},{'dom_code':1,'sdom_code':1,'code':1})

    return cursor


def exchange(context):
    database = context.database
    collections = database.list_collection_names()
    exchange_dict = {}
    for collection in collections:
        symbol_list = []
        code_cursor = database[collection].find({'datetime':datetime(2024,11,15,13,31,00)},{'symbol':1})
        for code in code_cursor:
            symbols = code.get('symbol','A')
            symbols = symbols.upper()
            symbol = symbols.split('2')[0]
            symbol_list.append(symbol)
        symbols_set = set(symbol_list)
        exchange_dict.update({f'{collection}': symbols_set})
    return  exchange_dict

def init(context):
    context.interval = 15

    context.unrequired = ["AO","IF", "IH", "IC", "IM", "T", "TF", "TS",'LC','LH']
    context.cash_inflow = 'cash_inflow2'
    #因为要反复调用，所以在这里封装
    context.database=return_collections()

    # 自己用
    context.positions = {}

    #symbol的dict，用在第一步确定好对应的exchange，这样有利于减少时间损失
    context.symbol_dict = exchange(context)




    # 在每一天before_trading的部分直接获取所有的code的数据，实现字典式保存，然后在handle内更新
    # 其实这样想的话，不如直接在before的时候用掉所有的，但是这样，其实有点失真
    context.stack_dict = {}



    context.order_amt = 1000000
    subscribe('RB99')



def before_trading(context): #回测可以保存未来数据，但是模拟实盘的时候就不行，可是模拟也很重要，又不想重写
    # 1.获取当天需要交易的所有商品的品种
    # 2.获取当天所有商品的主力和次主力合约
    # 3.获取以上合约当天的所有分钟数据
    # 4.实例化当天所有主力和次主力合约的barsToy


    unrequired = context.unrequired
    cursor = return_dom_codes(context)
    # 获取当天的主力合约
    interval = context.interval


    #每一天都重新得到一个新的stack_dict
    stack_dict = {}
    code_list = []
    signal = False
    for doc in cursor:
        code = doc.get('code',0)
        if not code in unrequired: #保存此时的dom和sdom
            database = context.database
            collections = database.list_collection_names()

            symbol_dict = context.symbol_dict

            date_ori = context.now + pd.Timedelta(days=1) #此时是15号，但是是15号夜盘开始时间，然后利用date查找，却只出现14号夜盘开始时间（实际上是米筐错了）。所以此时应该date+1
            date = str(date_ori.date())
            try:
                dom_code = doc.get('dom_code',None).lower()
                sdom_code = doc.get('sdom_code',None).lower()
            except Exception as e:
                if not doc.get('dom_code', None):
                    code_list.append(sdom_code)
                    continue
                else:
                    code_list.append(dom_code)
                    continue

            #外置cash
            cash_inflow = context.cash_inflow

            if code in symbol_dict.get(collections[0]): # 此时不需要修改大小写
                cursor_1 = database[collections[0]].find({'date':date,'code':dom_code},{'code':code,'datetime':1, f'{cash_inflow}': 1})
                cursor_2 = database[collections[0]].find({'date':date,'code':sdom_code},{'code':code,'datetime':1,f'{cash_inflow}': 1})



            elif code in symbol_dict.get(collections[1]):
                cursor_1 = database[collections[1]].find({'date': date, 'code': dom_code}, {'code':code,'datetime':1, f'{cash_inflow}': 1})
                cursor_2 = database[collections[1]].find({'date': date, 'code': sdom_code},{'code':code,'datetime':1, f'{cash_inflow}': 1})

            elif code in symbol_dict.get(collections[2]):
                dom_code = dom_code.upper()
                sdom_code = sdom_code.upper()
                cursor_1 = database[collections[2]].find({'date': date, 'code': dom_code},{'code':code,'datetime':1,f'{cash_inflow}': 1})
                cursor_2 = database[collections[2]].find({'date': date, 'code': sdom_code},{'code':code,'datetime':1, f'{cash_inflow}' :1})

            elif code in symbol_dict.get(collections[3]):
                cursor_1 = database[collections[3]].find({'date': date, 'code': dom_code}, {'code':code,'datetime':1, f'{cash_inflow}': 1})
                cursor_2 = database[collections[3]].find({'date': date, 'code': sdom_code}, {'code':code,'datetime':1, f'{cash_inflow}': 1})

            elif code in symbol_dict.get(collections[4]):
                cursor_1 = database[collections[4]].find({'date': date, 'code': dom_code}, {'code':code,'datetime':1, f'{cash_inflow}': 1})
                cursor_2 = database[collections[4]].find({'date': date, 'code': sdom_code},{'code':code,'datetime':1, f'{cash_inflow}': 1})

            else: #如果没有收录直接开始不算数
                continue
            #cursor包含着每个code的一分钟所需要的数据，转换结构，datetime作为键，每一个code的数据作为数值
            total_cash = pd.DataFrame()
            for cursor in [cursor_2,cursor_1]:
                df = pd.DataFrame(list(cursor)).reset_index()
                if df.empty:
                    signal = True
                    break
                else:
                    bartoy = Bartoy(df['code'][0].upper(),interval=interval) # 反正都一样，但是说实话，这个习惯应该不好
                    df['bartoy'] = bartoy
                    if total_cash.empty:
                        total_cash['cash_inflow'] = df.iloc[:,2]
                    else:
                        total_cash['cash_inflow'] += df.iloc[:,2]

                    total_cash['bartoy'] = df['bartoy']
            if signal:
                signal=False
                continue
            else:
                dict_2 = dict(zip(df['datetime'],total_cash[['cash_inflow','bartoy']].values.tolist()))
                for key,value in dict_2.items():
                    ori_value = stack_dict.get(key,[])
                    ori_value.append(value)
                    stack_dict.update([(key,ori_value)])

    context.stack_dict = stack_dict






def handle_bar(context,bar_dict):
    current_time = context.now
    interval = context.interval
    minute,lf = time_compare(interval,current_time)
    positions = context.positions
    bar_trader = context.stack_dict
    position = context.portfolio.positions



    current_date = current_time.date()

    # if current_date == pd.Timestamp('2025-04-21').date():
    #     print('duandian')

    current_timestamp = str(current_time.strftime('%Y%m%d%H%M%S'))[-6:]
    threshold_time_begin =str(pd.Timestamp(datetime.combine(current_date,time(21,00,00))).strftime('%Y%m%d%H%M%S'))[-6:]
    threshold_time_begin_yes = str(pd.Timestamp(datetime.combine(current_date,time(23,00,00))).strftime('%Y%m%d%H%M%S'))[-6:]
    threshold_time_end = str(pd.Timestamp(datetime.combine(current_date,time(9,00,00))).strftime('%Y%m%d%H%M%S'))[-6:]
    mid_time = str(pd.Timestamp(datetime.combine(current_date,time(15,00,00))).strftime('%Y%m%d%H%M%S'))[-6:]
    #开始比较数据


    # 如果在时间内，那么首先提取出该时刻的【dict_1,dict_2,dict_3】，每一个dict都包含了一个codeKey和cashValue
    if threshold_time_begin <= current_timestamp < threshold_time_begin_yes or threshold_time_end < current_timestamp < mid_time:
        bar_data = bar_trader.get(current_time, None) # 这个是一个list
        if not bar_data:
            pass
        else:
            list_rows = [] # 这是中间元素
            for dict_info in bar_data:
                cash_inflow = dict_info[0]
                bartoy = dict_info[1] #这是对应的实例化对象
                bartoy.terminal(current_time,cash_inflow)

                list_row = [bartoy.code,bartoy.bars[minute]]
                list_rows.append(list_row)

            series = pd.DataFrame(columns=['code','cash_inflow'],data=list_rows)
            series.set_index('code',inplace=True)
            series = series['cash_inflow']




            if lf == 0: # 如果是第五分钟，那么就要开仓和平仓
                long_pos = series.nlargest(5).index
                short_pos = series.nsmallest(5).index

                # 看看有没有是否为第一次：
                if not context.positions:
                    for long_b in long_pos:
                        price = bar_dict[long_b].last
                        amount = int(context.order_amt // (info(long_b)*price))
                        order = buy_open(long_b, amount)
                        if order.filled_quantity != amount:
                            logger.warning(f'{context.now}开多{long_b} {amount}手，实际交易{order.filled_quantity}')
                        else:
                            original_long_pos = positions.get('buy',[])
                            original_long_pos.append(long_b)
                            positions.update({'buy':original_long_pos})
                            logger.info(f'开多{long_b} {amount}手成功')

                    for short_s in short_pos:
                        price = bar_dict[short_s].last
                        amount = int(context.order_amt // (info(short_s)*price))
                        if short_s.startswith('AO'):
                            print('断点')
                        order = sell_open(short_s, amount)

                        if order.filled_quantity != amount:
                            logger.warning(f'{context.now}开空{short_s} {amount}手，实际交易{order.filled_quantity}')
                        else:
                            original_short_pos = positions.get('sell',[])
                            original_short_pos.append(short_s)
                            positions.update({'sell':original_short_pos})
                            logger.info(f'开空{short_s} {amount}手成功')
                    #然后把key放入到original


                else:#要化作差集比较
                    original_long_pos = positions.get('buy',[])
                    original_short_pos = positions.get('sell',[])


                    sellClose_in_long = set(original_long_pos) - set(long_pos)
                    buyOpen_in_long =  set(long_pos) - set(original_long_pos)

                    buyClose_in_short = set(original_short_pos) - set(short_pos)
                    sellOpen_in_short = set(short_pos) - set(original_short_pos)

                    # 如果不是空的，那么就要进行对应的平仓开仓
                    if sellClose_in_long:
                        for code in sellClose_in_long:
                            code_pos = position[code].buy_quantity
                            sell_close(code,code_pos)
                            logger.info(f'平多{code} {code_pos}手成功')


                    if buyOpen_in_long:
                        for code in buyOpen_in_long:
                            price = bar_dict[code].last
                            amount = int(context.order_amt // (info(code) * price))
                            order = buy_open(code,amount)
                            if order.filled_quantity != amount:
                                logger.warning(f'{context.now}开空{code} {amount}手，实际交易{order.filled_quantity}')
                            else:
                                logger.info(f'开多{code} {amount}手成功')
                    if buyClose_in_short:
                        for code in buyClose_in_short:
                            code_pos = position[code].sell_quantity
                            buy_close(code,code_pos)
                            logger.info(f'平空{code} {code_pos}手成功')

                    if sellOpen_in_short:
                        for code in sellOpen_in_short:
                            price = bar_dict[code].last
                            amount = int(context.order_amt // (info(code) * price))
                            order = sell_open(code,amount)
                            if order.filled_quantity != amount:
                                logger.warning(f'{context.now}开空{code} {amount}手，实际交易{order.filled_quantity}')
                            else:
                                logger.info(f'开空{code} {amount}手成功')
                    # 修改positions
                    positions.update({'buy':long_pos,'sell':short_pos})



    elif current_timestamp == threshold_time_begin_yes  or current_timestamp == mid_time:
        for pos in positions.get('buy', []):
            if not pos:
                pass
            else:
                amount = context.portfolio.positions[pos].buy_quantity
                if amount == 0:
                    pass
                else:
                    sell_close(id_or_ins=pos,amount=amount)
                    logger.info(f'平多仓{pos} {amount}手成功')

        for pos in positions.get('sell',[]):
            if not pos:
                pass
            else:
                amount = context.portfolio.positions[pos].sell_quantity
                if amount == 0:
                    pass
                else:
                    buy_close(id_or_ins=pos,amount=amount)
                    logger.info(f'平空仓{pos} {amount}手成功')
        positions.update({'buy':[],'sell':[]})


def after_trading(context):
    logger.info(f'当日收益：{context.future_account.daily_pnl}')


if __name__ == '__main__':
    config = {
        'bundle_path': r'输入米筐回测API REST',
        'strategy_file':__file__,
        'accounts': {'FUTURE': 1000000000},
        'run_type': 'b', 'frequency': '1m',
        'start_date': '2025-04-15', 'end_date': '2025-04-30',
        'broker': {'matching_type': 'current_bar', "slippage_model": "PriceRatioSlippage", "slippage": 0,},
        # 'trading': {'gateway': {'Future': 'CTP,..\setting\CTP_connect.json'}},
        }
    env = config_init(config)
    env = analyser_init(env)
    env, scope, ucontext = system_init(env)
    status = run(env, scope, ucontext)
    result = analyse(env)