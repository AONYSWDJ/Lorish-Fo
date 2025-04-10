import time

import pandas as pd
import os
from datetime import datetime

from data_require import get_Data,is_tradeing_time


def login_judgement():
    pass

def amends_data(df,time):
    dff = df[df['净值'] != '-']
    dff = dff.sort_values(by=time,ascending=True).reset_index(drop=True)
    dff['涨跌幅'] = (dff['净值'].astype(float) / dff['净值'].astype(float).shift(1)).fillna(1)
    dff['累计涨跌幅'] = dff['涨跌幅'].cumprod() - 1

    return dff


def daily_down_data(curren_time, product_names, product_netValue, i):
    # 应该进行增量更新，保证只有一个读取和写入，这样的情况下，就不容易犯下错误
    # 那么此时写入的时候就应该调换时间
    current_time = curren_time.strftime('%H:%M:%S')
    initial_df = pd.read_csv(fr'cache_loader\{product_names[i]}_daily.csv')

    new_df = pd.DataFrame({
        '产品名': f'{product_names[i]}',
        '时间': current_time,
        "净值": [product_netValue[i]]
    })
    # 在解读的时候，会自动解码成str 所以需要
    df_product = pd.concat([initial_df, new_df], axis=0, ignore_index=True)
    df_product['时间'] = pd.to_datetime(df_product['时间'])


    df_product = df_product.sort_values(by='时间', ascending=True).reset_index(drop=True)
    df_product.to_csv(fr'cache_loader\{product_names[i]}_daily.csv', index=False)
    # 在这一步中，保存了新的时间，对本地文件进行了更新，然后出传出了df_product
    return df_product


def swtich_download_data(data_dict,data): # 进行格式上的转换，包括日期，涨跌幅，

    '''
    ######## 下载到本地，然后按照名字依次取名，历史数据记得取名字 productName_history.csv#####
    ####### 当日数据则保存为 productName_daily.csv #########
    '''

    product_amounts = len(data[0])
    product_names = data[0]
    product_netValue = data[1]
    product_yesterdayValue = data[2]
    product_currenttime = data[3]
    product_currentTime = product_currenttime.strftime('%H:%M:%S')

    historical_dataframe = pd.DataFrame()
    historical_revenue_dataframe = pd.DataFrame()





    # 拿到了daily dataframe
    if os.path.exists(fr'cache_loader\today_netvalue.csv'):
        daily_dataframe = pd.read_csv(r'cache_loader\today_netvalue.csv',index_col='时间')
        new_tick_df = pd.DataFrame(
       [product_netValue],columns=product_names,index= [product_currentTime]
        )
        daily_dataframe = pd.concat([new_tick_df,daily_dataframe],axis=0,ignore_index=False)
    else:
        daily_dataframe = pd.DataFrame(
       [product_yesterdayValue],columns=product_names,index= ['9:20:00']
        )
        new_tick_df = pd.DataFrame(
            [product_netValue], columns=product_names, index=[product_currentTime]
        )
        daily_dataframe = pd.concat([new_tick_df, daily_dataframe], axis=0, ignore_index=False)

    daily_dataframe.index.name = '时间'
    daily_dataframe.to_csv(r'cache_loader\today_netvalue.csv',index=True)
    daily_dataframe.index = pd.to_datetime(daily_dataframe.index).time
    daily_dataframe.sort_index(ascending=True,inplace=True)
    daily_dataframe.fillna(1,inplace=True)
    daily_revenue_dataframe = (daily_dataframe/daily_dataframe.shift(1)).fillna(1)
    daily_revenue_dataframe = daily_revenue_dataframe.cumprod()-1


    # 得到历史净值
    for i in range(0,product_amounts): # 录入-修改-保存
        # 读取产品最初保存在本地的地址

        product_df = pd.read_csv(fr'cache_loader\{product_names[i]}_history.csv')
        product_df['产品名'] = product_names[i]
        product_df['日期'] = pd.to_datetime(product_df['日期'].astype(str))
        product_df['日期'] = product_df['日期'].dt.date
        pd.set_option('mode.chained_assignment',None) # 忽略报错信息

        daytime = product_currenttime.date()
        if product_df['日期'].iloc[0] == daytime:
            product_df['净值'].iloc[0] = product_netValue[i]
            df_product = product_df
        else:
            new_df = pd.DataFrame({
                '产品名': f'{product_names[i]}',
                '日期': daytime,
                "净值": [float(product_netValue[i])]
            })
            df_product = pd.concat([product_df,new_df],axis=0,ignore_index=True)
        df_product = df_product.sort_values(by='日期', ascending=False).reset_index(drop=True)
        df_product.to_csv(fr'cache_loader\{product_names[i]}_history.csv',index=False)
        df_product = df_product.sort_values(by='日期', ascending=True).reset_index(drop=True)
        df_product = amends_data(df_product,'日期')




        #修改为index为日期的包含了历史净值的dataframe
        revise_df  = df_product.set_index('日期')
        revise_df[f'{product_names[i]}'] =  revise_df['净值']
        historical_dataframe = pd.concat([historical_dataframe,revise_df[f'{product_names[i]}']],axis=1)

        revise_df[f'{product_names[i]}'] =  revise_df['累计涨跌幅']
        historical_revenue_dataframe = pd.concat([historical_revenue_dataframe,revise_df[f'{product_names[i]}']],axis=1)



    # 历史实时净值的修改
    id_name1 = 'historical_dynamic'
    id_name2 = 'historical_revenue'
    id_name3 = 'daily_revenue'
    data_dict[id_name1] = historical_dataframe
    data_dict[id_name2] = historical_revenue_dataframe
    data_dict[id_name3] = daily_revenue_dataframe

    # 不需要传入参数，因为此时已经改变了全局变量字典，然后从字典中取数就好了
    # 为了满足此条件，同时需要首先运行一次改函数，然后进行多线程

def data_main(cb,data_dict): # 包装一个全局变量，用于记录已经载入了多少次
    while True:
        time.sleep(60)
        data = get_Data(cb)
        if is_tradeing_time():
            swtich_download_data(data_dict,data)
            print('字典更新完毕')
        else:
            print('休盘时间，字典不更新')


