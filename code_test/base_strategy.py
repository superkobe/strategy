'''
python version: python3
Author: chaotianjiao
Date: 2020-06-22 19:04:40
LastEditors: chaotianjiao
LastEditTime: 2020-08-22 23:57:58
定投策略数据回测
'''
import sys
import os
import importlib
sys.path.append('../')
importlib.reload(sys)

from conf import *
from collections import defaultdict

import pandas as pd
import numpy as np


def fixed_fund_strategy(buy_date=3, buy_money=100, expense=0):
    '''
        基金定投策略，定期定额收益计算
    '''
    df = pd.read_csv(os.path.join(DATA_PATH, 'test_data', 'df_test.csv'), usecols=[0, 2, 5],
                     delimiter='\t', 
                     nrows=10 # 全量数据需要注释掉该代码
                     )
    
    df['week_day'] = pd.to_datetime(df['date']).dt.dayofweek + 1
    print(df)
    
    # 按周定投收益计算, 先不计算交易费用，假设全是c份额
    # 结果dict： k为时间，v为基金份额，投入金额，利润
    res = defaultdict(list)  
    fund_cnt = 0
    profit = 0
    cost = 0 
    for index, value in df.iterrows():
        # 第一个交易日初始化
        if len(res) == 0:
            if value['week_day'] != 3:
                continue
            else:
                # 基金份额计算
                fund_cnt = buy_money / value['open']
                cost = buy_money
                # 利润计算
                profit = profit - expense
                res[value['date']].extend([fund_cnt, cost, profit])
        else:
            if value['week_day'] != 3:
                profit = fund_cnt * value['open'] - cost
                res[value['date']].extend([fund_cnt, cost, profit])
            else:
                fund_cnt += buy_money / value['open']
                cost += buy_money
                profit = fund_cnt * value['open'] - cost - expense
                res[value['date']].extend([fund_cnt, cost, profit])
    df = pd.DataFrame(res).T.reset_index()
    df.columns = ['date', 'fund_cnt', 'cost', 'profit']
    df.to_csv(os.path.join(DATA_PATH, 'test_data', 'fix_fund_strategy.csv'), index=False, sep='\t')
    print(df)
    return df

def pe_fund_stragety(pe_percnt=0.2, buy_money=100, des=False):
    '''
        按基金pe值进行定投，大于多少百分比的时候进行定投，
        定投的金额如何进行增加，都需要进行回测
    '''

if __name__ == '__main__':
    fixed_fund_strategy()