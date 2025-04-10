# 获取数据的函数永远都是最好写的
'''
重点还是，在主线程中，利用传入的参数cb作为callback，进行数据的获取
当然，既然分成了这样的形式，login_main也可以写在这里
'''
from datetime import time
import demoforRequest
import datetime as dt
import time

def login_main():
    server_addr = "175.25.41.106:65300"  # 统一交易服务器的地址
    username = "xxxx"  # 测试用户，同客户端登录用户，非资金账号
    password = "xxxx"  # 用户密码，客户端登录密码，非资金密码
    cb = demoforRequest.CallBack(server_addr, username, password)
    cb.init()
    cb.join()
    time.sleep(3)
    return cb

# 需要修改的点是： return需要注意，但在data_wash中改也是可以的
def get_Data(cb):
    #第一步，得到目前的时间，然后后续按照要求进行分割即可
    current_time = dt.datetime.now()
    productlist = cb.reqProductDataSync()
    product_name_list, product_net_value_list, product_yesterday_value_list = [], [], []
    #第二步，得到产品名字列表，然后依据产品列表的长度，进行数据集合的创建
    for data in productlist:
        product_name = data.m_strProductName
        product_name_list.append(product_name)

        product_net_value = data.m_dTotalNetValue
        product_net_value_list.append(product_net_value)

        product_yesterday_value = data.m_dPrevTotalNetValue
        product_yesterday_value_list.append(product_yesterday_value)

    return [product_name_list,product_net_value_list,product_yesterday_value_list,current_time]