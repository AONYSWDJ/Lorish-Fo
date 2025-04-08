'''
task1 finish the downloading of the hisotry asset, which
are the summarize of different account 这个不知道怎么解决，api上没仔细找，应该有结果

task2 change the whole list to Dataframe and get the formate we need
    time NetvalueofTest1 NetvalueofTest2

    time TotalvalueofTest1 TotalvalueofTest2

task3 use dash to get the Historical_Net_Asset
'''
#@@
import demoforRequest
import time
import pandas as pd
import datetime
from XtTraderPyApi import *
def main(cb):


    #得到所有账号ID以及对应key
    keys_list = cb.reqAccountKeySync()
    accountId_list = []
    accountKey_list = []
    for codes in keys_list:
        accountId = codes.m_strAccountID
        accountKey = codes.m_strAccountKey
        accountId_list.append(accountId)
        accountKey_list.append(accountKey)
    account_dic = dict(zip(accountId_list,accountKey_list))
    #@@
    # pristine_date_list = cb.reqProductDataSync()
    # load_Id_list = []
    # list_Id_panels = []
    # for data in pristine_date_list:
    #     load_Id = data.m_nProductId
    #     load_Id_list.append(load_Id)
    #     # 查询产品下所有账号的持仓统计，这一步骤需要自己写一个子类中没有重写的func，要不然还不如直接用api
    #     info_Pro = cb.rePositionStaticsSyncWithProductId(int(load_Id))
    #     list_Id_panel = info_Pro[0].m_strAccountID
    #     list_Id_panels.append(list_Id_panel)
    #     # 期货账号和信用账号不连通，真无语
    start_Date = '20250106'# 我尼玛的真的傻逼，多加了一个逗号
    end_Date = '20250325'
    new_dic = {}
    account_id = [id for id in account_dic.keys()]
    for id in account_id:
        time_date = []
        data = cb.reqHistoryAccountDetailSync(account_id=id,account_key=account_dic[id],start_Date=start_Date,end_Date=end_Date)

        total_net_value_1 = []
        for i in range(0,len(data)):
            total_net_value_1.append(data[i].m_dAvailable)
            time_date.append(data[i].m_strTradingDate)
        new_dic[f'{id}'] = [total_net_value_1,time_date]

    # 得到了每一个account的资金走动，然后开始组合
    '''
    AnzhiCapitalTest2: 2004430 2004431 3000085
    AnzhiCapitalTest1: else
    '''
    account_test1 = ['2004430','2004431','3000085']
    account_test2 = [x for x in account_id if x not in account_test1]

    # 将字典改为数据表，其中设置时间为index，然后对不存在的点设置为fillna
    preMerged_dataframe_test1 = pd.DataFrame()
    preMerged_dataframe_test2 = pd.DataFrame()
    for id in account_id:
        if id in account_test1:
            NetValueFlow = new_dic[id][0]
            TimeForId = new_dic[id][1]
            preMerged = pd.DataFrame({
                "time": TimeForId,
                f"{id}value": NetValueFlow
            })
            preMerged['time'] = pd.to_datetime(preMerged['time'])
            # 得到test1的Dataframe版本
            if preMerged_dataframe_test1.empty:
                preMerged_dataframe_test1 = preMerged
            else:
                preMerged_dataframe_test1 = pd.merge(preMerged,preMerged_dataframe_test1,on='time',how='outer')
                preMerged_dataframe_test1.fillna(0,inplace=True)
        else:
            NetValueFlow = new_dic[id][0]
            TimeForId = new_dic[id][1]
            preMerged = pd.DataFrame({
                "time" : TimeForId,
                f"{id}value": NetValueFlow
            })
            preMerged['time'] = pd.to_datetime(preMerged['time'])
            # 得到test2的Dataframe版本
            if preMerged_dataframe_test2.empty:
                preMerged_dataframe_test2 = preMerged
            else:
                preMerged_dataframe_test2 = pd.merge(preMerged,preMerged_dataframe_test2,on='time',how='outer')
                preMerged_dataframe_test2.fillna(0,inplace=True)
    preMerged_dataframe_test1 = calculate_all(preMerged_dataframe_test1)
    preMerged_dataframe_test1['产品'] = '安值CapitalTest1'
    preMerged_dataframe_test2 = calculate_all(preMerged_dataframe_test2)
    preMerged_dataframe_test2['产品'] = '安值CapitalTest2'

    return preMerged_dataframe_test1,preMerged_dataframe_test2
def calculate_all(df):
    # 初始化'NetValueInProduct'为0
    df['NetValueInProduct'] = 0

    # 遍历除第一列和最后一列外的所有列
    columns_to_drop = []  # 用于存储需要删除的列
    for column_name in df.columns[1:-1]:
        df['NetValueInProduct'] += df[column_name]  # 累加该列的值
        columns_to_drop.append(column_name)  # 记录要删除的列

    # 删除记录的列
    # df.drop(columns=columns_to_drop, inplace=True)

    return df
# 获取产品的当日和昨日值
def second(cb):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d')
    day_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_time = datetime.datetime.strptime(current_time,'%Y-%m-%d')
    productlist = cb.reqProductDataSync()
    product_name_list, product_net_value_list, product_yesterday_value_list = [],[],[]
    for data in productlist:
        product_net_value = data.m_dTotalNetValue
        product_net_value_list.append(product_net_value)

        product_yesterday_value = data.m_dPrevTotalNetValue
        product_yesterday_value_list.append(product_yesterday_value)


        product_name = data.m_strProductName
        product_name_list.append(product_name)


    # 开始实时更新数据
    return product_name_list,product_net_value_list,product_yesterday_value_list,current_time,day_time
#组合+更新判断
def third(name,net_value,yesterday_value,current_time,day_time):
    test1_df = pd.read_csv('安值test1_history.csv', encoding='UTF-8')
    test1_df['产品名'] = [n for n in name if not n.endswith('test2')][0]
    test2_df = pd.read_csv('安值test2_history.csv', encoding='UTF-8')
    test2_df['产品名'] = [n for n in name if n.endswith('test2')][0]

    test1_df['日期'] = pd.to_datetime(test1_df['日期'].astype(str))
    test2_df['日期'] = pd.to_datetime(test2_df['日期'].astype(str))

    new_df_test1 = pd.DataFrame({
        '产品名' : '安值test',
        '日期': [test1_df['日期'].iloc[0] + pd.Timedelta(days=1)],
        "净值": [float(net_value[0])]
    })

    new_df_test2 = pd.DataFrame({
        '产品名': '安值test2',
        '日期': [test2_df['日期'].iloc[0]+pd.Timedelta(days=1)],
        "净值": [float(net_value[1])]
    })
    pd.set_option('mode.chained_assignment', None) # 忽略报错信息
    # 天为基准的实时更新当天数据 同时在interval调用过程中保存数据
    if test1_df['日期'].iloc[0] == current_time:
        test1_df['净值'].iloc[0] = net_value[0]
        test2_df['净值'].iloc[0] = net_value[1]

        df_test1 = test1_df
        df_test2 = test2_df

        df_test1.to_csv('安值test1_history.csv',index=False)
        df_test2.to_csv('安值test2_history.csv',index=False)
    elif test1_df['日期'].iloc[0] + pd.Timedelta(days=3) == current_time: # 为了解决现实中可能遇到的周末关机断电两天的现象，且数据本身就不包含周末
        new_df_test1 = pd.DataFrame({
            '产品名': '安值test',
            '日期': [test1_df['日期'].iloc[0] + pd.Timedelta(days=3)],
            "净值": [float(net_value[0])]
        })

        new_df_test2 = pd.DataFrame({
            '产品名': '安值test2',
            '日期': [test2_df['日期'].iloc[0] + pd.Timedelta(days=3)],
            "净值": [float(net_value[1])]
        })
        df_test1 = pd.concat([test1_df,new_df_test1],axis=0,ignore_index=True)
        df_test2 = pd.concat([test2_df,new_df_test2],axis=0,ignore_index=True)
        df_test1 = df_test1.sort_values(by='日期', ascending=False).reset_index(drop=True)
        df_test2 = df_test2.sort_values(by='日期', ascending=False).reset_index(drop=True)

        df_test1.to_csv('安值test1_history.csv',index=False)
        df_test2.to_csv('安值test2_history.csv',index=False)
    else:
        df_test1 = pd.concat([test1_df,new_df_test1],axis=0,ignore_index=True)
        df_test2 = pd.concat([test2_df,new_df_test2],axis=0,ignore_index=True)
        df_test1 = df_test1.sort_values(by='日期', ascending=False).reset_index(drop=True)
        df_test2 = df_test2.sort_values(by='日期', ascending=False).reset_index(drop=True)

        df_test1.to_csv('安值test1_history.csv',index=False)
        df_test2.to_csv('安值test2_history.csv',index=False)

    return df_test1, df_test2, day_time,yesterday_value
def Conclusion(cb):
    surname, value, prevalue, current_time,day_time = second(cb)
    return third(surname,value,prevalue,current_time,day_time)
#@@
# 开始dash画图练习， 主要是使用chatgpt的能力
'''
prompt： 需要legends展示，可以加上radio进行单独展示，需要时间x坐标，同时时间坐标可以进行拖动，需要定义y坐标单位，这样比例会更加清楚

'''

if __name__ == '__main__':
    server_addr = "175.25.41.106:65300"  # 统一交易服务器的地址
    username = "安值_独立交易员"  # 测试用户，同客户端登录用户，非资金账号
    password = "az913702"  # 用户密码，客户端登录密码，非资金密码
    cb = demoforRequest.CallBack(server_addr, username, password)
    cb.init()
    cb.join()
    time.sleep(4)
    Conclusion(cb)