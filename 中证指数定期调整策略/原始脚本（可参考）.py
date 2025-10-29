# 首先对2025年沪深300股份进行预测，简要得到其调出名单、调入名单、备选名单，随后再对中证500进行预测。
import pandas as pd
'''
具体框架如下：
    数据下载
        【注意事项】 选取2024/05/01 <--> 2025/04/30,同时注意将退市的股票重新纳入样本名单。期间上市的不需要考虑。
        选取字段【证券代码	证券简称	是否属于重要指数成份[所属指数] 沪深300指数[交易日期] 2025-5-1	
        是否属于重要指数成份[所属指数] 中证500指数[交易日期] 2025-5-1	上市日期	区间日均总市值[起始日期] 2024-5-1[截止日期] 2025-4-30[币种] 原始币种[单位] 元	上市板	区间日均成交额[起始交易日期] 2024-4-30[截止交易日期] 2025-4-30[单位] 元	区间涨跌幅[起始交易日期] 2025-5-1[截止交易日期] 2025-4-30[单位] %	净利润[报告期] 2024年报[报表类型] 合并报表[单位] 元	所属行业名称(支持历史)[行业标准] Wind行业(2024)[行业级别] 三级行业[交易日期] 最新收盘日	资产负债率[报告期] 2024年报[单位] %	经营活动产生的现金流量净额[报告期] 2024年报[报表类型] 合并报表[单位] 元】
         
    指数编制方法论
        通过数据分析粗略得到名单
    
    案头研究
        针对得到的样本名单进行优化，具体优化方法在【指数调动详尽报告】
        

'''
def load_all_info(sheet_name='原始'):
    path = r'E:\360MoveData\Users\Administrator\Desktop\intern file\项目集\股指调仓套利策略\秒转数据.xlsx'

    return pd.read_excel(path,sheet_name)


def space(df_):
    
    # 剔除 ST *ST
    df_no_ST = df_[~df_['证券简称'].str.contains('ST')]

    # 筛选出,如果是科创板、创业板上市日期需要早于2023-04-30的公司, 其他板块上市日期超过一个季度
    # 并且不能是北证
    df_no_ST['上市日期'] = pd.to_datetime(df_no_ST['上市日期'], errors='coerce')
    df_no_ST = df_no_ST.loc[~(df_no_ST['上市板'] == '北证')]

    df_no_ST = df_no_ST.loc[~((df_no_ST['上市板'].isin(['科创板', '创业板'])) & (df_no_ST['上市日期'] > '2024-04-30'))]
    df_no_ST = df_no_ST.loc[~((~df_no_ST['上市板'].isin(['科创板', '创业板'])) & (df_no_ST['上市日期'] > '2025-02-01'))]

    # 按总市值排序
    df_no_300 = df_no_ST.sort_values(
        by='区间日均总市值[起始日期] 2024-5-1[截止日期] 2025-4-30[币种] 原始币种[单位] 元', inplace=False,
        ascending=False)
    #保留 按照日均总市值排序的index键
    df_no_300.reset_index(inplace=True, drop=True)

    # 按照日均交易额重新排序，删除排名在后百分之五十的证券
    df_ave = df_no_300.sort_values(by='区间日均成交额[起始交易日期] 2024-5-1[截止交易日期] 2025-4-30[单位] 元',
                                   inplace=False, ascending=True)
    decline = int(len(df_ave) // 2)
    df_average = df_ave[decline:]

    # 重新按日均总市值排序，也就是按照index排序
    df_average.sort_index(inplace=True)

    # 返回可以留下调整的接口
    return [df_no_300, df_ave, df_average]

def adjust(df_list):
    df_pre = df_list[0]
    df_pre_add = df_list[1]
    df_add = df_list[2]

    # 沪深300的调整规则
    decline_1 = int(len(df_pre_add)*0.4)
    decline_2 = int(len(df_pre_add)*0.5)
    df_pre_add.reset_index(inplace=True, drop=True)
    df_need = df_pre_add[df_pre_add['是否属于重要指数成份[所属指数] 沪深300指数[交易日期] 2025-5-1'] == '是']
    df_need = df_need['证券简称'].values.tolist()

    #得到由于流动性不足而提前排除掉的list
    df_out = df_pre_add[(df_pre_add.index < decline_1) & (df_pre_add['证券简称'].isin(df_need))]

    # 排名在后百分之五十之间六十的老样本
    df_req = df_pre_add[(df_pre_add.index > decline_1)&(df_pre_add.index < decline_2) & (df_pre_add['证券简称'].isin(df_need))]
    final_ = pd.concat([df_add, df_req])

    # 混合后按照日均市值排序
    final_.sort_values(by='区间日均总市值[起始日期] 2024-5-1[截止日期] 2025-4-30[币种] 原始币种[单位] 元',
                       inplace=True, ascending=False)
    final_.reset_index(inplace=True, drop=True)




    return [final_,df_out]

def rank(df_news):

    df_new = df_news[0]
    #名单1 直接纳入
    df_out_1 = df_news[1]


    df_360 = df_new[df_new.index > 360]
    # 名单2 直接纳入，但排名在前的需要结合案头进行研究
    df_out = df_360[df_360['是否属于重要指数成份[所属指数] 沪深300指数[交易日期] 2025-5-1'] == '是']

    # 案头研究名单3 需要结合案头进行研究
    df_out_3 = df_new[(df_new.index>300) & (df_new.index <360) &(df_new['是否属于重要指数成份[所属指数] 沪深300指数[交易日期] 2025-5-1'] == '是')]

    #得到调出数量，从而确定调入数量（备选名单数量一般是15个）
    length_out = int(input('案头研究结果中发现，调出证券数量为：'))

    df_300 = df_new[df_new.index < 300]
    df_in = df_300[df_300['是否属于重要指数成份[所属指数] 沪深300指数[交易日期] 2025-5-1'] == '否']

    #针对240排名之前的新加入名单，案头研究其涨跌幅等指标
    df_in_240 = df_in[df_in.index < 240]

    # df_in_index = list(map(input('调入名单索引为').split(','),int))
    # df_out_index = list(map(input('调出名单索引为').split(','),int))
    # df_sub_index = list(map(input('备选名单索引为').split(','),int))


    # prophet_in = df_new[df_new.index.isin(df_in_index)]
    # prophet_out = df_new[df_new.index.isin(df_out_index)]
    # prophet_sub = df_new[df_new.index.isin(df_sub_index)]
    # return [prophet_out, prophet_in, prophet_sub]
    return [df_out,df_300]



def get_the_sh300():
    data = load_all_info(sheet_name='2025')
    # space samples
    space_adjust = space(data)

    # adjustment buffer
    final_data = adjust(space_adjust)

    #list_of_securities = rank(final_data)
    list_prophet = rank(final_data)



    return list_prophet

def space_500(df_):
    # 剔除 ST *ST
    df_no_ST = df_[~df_['证券简称'].str.contains('ST')]

    # 筛选出,如果是科创板、创业板上市日期需要早于2024-04-30的公司, 其他板块上市日期超过一个季度
    # 并且不能是北证
    df_no_ST['上市日期'] = pd.to_datetime(df_no_ST['上市日期'], errors='coerce')
    df_no_ST = df_no_ST.loc[~(df_no_ST['上市板'] == '北证')]

    df_no_ST = df_no_ST.loc[~((df_no_ST['上市板'].isin(['科创板', '创业板'])) & (df_no_ST['上市日期'] > '2024-04-30'))]
    df_no_ST = df_no_ST.loc[~((~df_no_ST['上市板'].isin(['科创板', '创业板'])) & (df_no_ST['上市日期'] > '2025-02-01'))]

    # 按总市值排序
    df_no_300 = df_no_ST.sort_values(
        by='区间日均总市值[起始日期] 2024-5-1[截止日期] 2025-4-30[币种] 原始币种[单位] 元', inplace=False,
        ascending=False)
    df_no_300.reset_index(inplace=True, drop=True)

    # 删除所有沪深300的证券
    df_no_sh300 = df_no_300[df_no_300['是否属于重要指数成份[所属指数] 沪深300指数[交易日期] 2025-5-1'] == '否']

    # 删除所有index在前300的证券，构成并集删除
    df_final = df_no_sh300[df_no_sh300.index > 300]

    # 按照日均交易额重新排序，删除排名在后百分之二十的证券,此时从低到高排序，故而删除的是前百分之二十

    df_ave = df_final.sort_values(by='区间日均成交额[起始交易日期] 2024-5-1[截止交易日期] 2025-4-30[单位] 元',
                                  inplace=False, ascending=True)
    decline = int(len(df_ave) // 5)
    df_average = df_ave[decline:]

    # 重新按日均总市值排序，也就是按照index排序
    df_average.sort_index(inplace=True)

    # 返回可以留下调整的接口
    return [df_no_300, df_ave, df_average]

def adjust_500(df_list):
    df_pre = df_list[0]
    df_pre_add = df_list[1]
    df_add = df_list[2]

    # 沪深300的调整规则 在360之前的老样本不能进入500 ； 在 240之后的新样本需要回到中证500
    adjust_after_360 = df_pre[
        (df_pre.index > 300) & (df_pre['是否属于重要指数成份[所属指数] 沪深300指数[交易日期] 2025-5-1'] == '是')]
    adjust_after_240 = df_pre[(df_pre.index < 300) & (df_pre.index >= 240) & (
                df_pre['是否属于重要指数成份[所属指数] 中证500指数[交易日期] 2025-5-1'] == '是')]

    df_out_1 = df_pre[(df_pre.index<240) & (df_pre['是否属于重要指数成份[所属指数] 中证500指数[交易日期] 2025-5-1'] == '是')]

    # 中证500的调整规则
    decline = int(len(df_pre_add) // 5)
    df_pre_add.reset_index(inplace=True, drop=True)
    df_needy = df_pre_add[df_pre_add['是否属于重要指数成份[所属指数] 中证500指数[交易日期] 2025-5-1'] == '是']
    df_need = df_needy[50:]['证券简称'].values.tolist()
    df_no_need = df_needy[:51]
    # 排名在后百分之20 且 在老样本 前百分之九十的老样本
    df_req = df_pre_add[(df_pre_add.index < decline) & (df_pre_add['证券简称'].isin(df_need))]

    df_out_2 = df_pre_add[(df_pre_add.index < decline) & (df_pre_add['证券简称'].isin(df_no_need))]
    df_out = pd.concat([df_out_1,df_out_2])


    final_ = pd.concat([df_add, df_req, adjust_after_360, adjust_after_240])

    # 混合后按照日均市值排序
    final_.sort_values(by='区间日均总市值[起始日期] 2024-5-1[截止日期] 2025-4-30[币种] 原始币种[单位] 元', inplace=True,ascending=False)
    final_.reset_index(inplace=True, drop=True)
    return [final_, df_out]

def rank_500(sh_300,df_news):
    df_new = df_news[0]
    # 从沪深300得到的指标
    out300 = sh_300[0]
    in300 = sh_300[1]
    #in_300指的是，排名在前列的，非常有可能被调出的名单
    in_300 = in300[in300['是否属于重要指数成份[所属指数] 中证500指数[交易日期] 2025-5-1'] == '是']

    #名单1 直接纳入
    df_out_1 = df_news[1]
    # 研究名单2 需要结合沪深300调入和备选进行研究
    df_out_2 = in300[in300['是否属于重要指数成份[所属指数] 中证500指数[交易日期] 2025-5-1'] == '是']

    # 名单3，需要进行案头研究
    i = int(input('需要案头研究的头部调出'))
    df_600 = df_new[(df_new.index<i)|(df_new.index > 600)]
    df_out = df_600[df_600['是否属于重要指数成份[所属指数] 中证500指数[交易日期] 2025-5-1'] == '是']
    #得到调出数量，从而确定调入数量
    length_out = int(input('案头研究结果中发现，调出证券数量为：'))




    #调入名单
    df_500 = df_new[df_new.index < 500]
    df_in = df_500[df_500['是否属于重要指数成份[所属指数] 中证500指数[交易日期] 2025-5-1'] == '否']

    #注意！ 除去沪深300调出名单的其他所有沪深300，都进入老样本，故而不能加入到中证500新样本
    df_not_need = df_in[df_in['是否属于重要指数成份[所属指数] 沪深300指数[交易日期] 2025-5-1'] == '是'].iloc[-8:]
    df_in = df_in[(df_in['是否属于重要指数成份[所属指数] 沪深300指数[交易日期] 2025-5-1'] == '否') |(df_in['证券简称'].isin(df_not_need['证券简称'].values))]
    df_in = df_in[df_in['净利润[报告期] 2024年报[报表类型] 合并报表[单位] 元']>0]


    #sub_300指的是，排名在前列的，但是很难进入调入名单的新证券
    sub_300 = in300[(in300['是否属于重要指数成份[所属指数] 沪深300指数[交易日期] 2025-5-1'] == '否')&(in300['是否属于重要指数成份[所属指数] 中证500指数[交易日期] 2025-5-1'] == '否')]



    return
    # df_in_index = list(map(input('调入名单索引为').split(','),int))
    # df_out_index = list(map(input('调出名单索引为').split(','),int))
    #
    #
    #
    # prophet_in = df_new[df_new.index.isin(df_in_index)]
    # prophet_out = df_new[df_new.index.isin(df_out_index)]
    # prophet_sub = df_new[df_new.index.isin(df_sub_index)]
    # return prophet_out, prophet_in, prophet_sub




def get_the_zz500(sh_300:list):
    data = load_all_info(sheet_name='2025')

    # space_samples
    space_adjust = space_500(data)

    #adjustment
    final_data = adjust_500(space_adjust)

    #list_of
    list_of_securities = rank_500(sh_300,final_data)


if __name__ == '__main__':
    list_need = get_the_sh300()
    get_the_zz500(list_need)
