'''
python version: python3
Author: chaotianjiao
Date: 2020-08-22 11:04:22
LastEditors: chaotianjiao
LastEditTime: 2020-08-23 00:07:08
'''

import os 
import random 
import sys
import time 

import pandas as pd 
import numpy as np 
import lightgbm as gbm 
import xgboost as xgb 

from sklearn.metrics import roc_auc_score, recall_score, precision_score, accuracy_score


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(DIR_PATH, 'data')
FUND_PATH = os.path.join(DIR_PATH, 'fund_strategy')

