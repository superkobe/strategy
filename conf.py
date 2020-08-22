'''
python version: python3
Author: chaotianjiao
Date: 2020-08-22 11:04:22
LastEditors: chaotianjiao
LastEditTime: 2020-08-22 20:38:50
'''

import os 
import random 
import sys
import time 

import pandas as pd 
import numpy as np 
import lightgbm as gbm 
import xgboost as xgb 


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(DIR_PATH, 'data')
FUND_PATH = os.path.join(DIR_PATH, 'fund_strategy')

