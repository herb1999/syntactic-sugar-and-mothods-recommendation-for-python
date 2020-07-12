#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import sys
import json
import re
from src.util import *
import pandas as pd
import numpy as np


"""获取推荐标签

    Args:
        caseId: 题目ID

    Returns:
        使用量靠前的标签

"""
def getRecommendedLabel(caseId):
    print('-------------标签推荐开始--------------------')
    stat=getStatistics(caseId)
    sums=stat.iloc[:,1:].sum().sort_values(ascending=False) #todo:使用次数不太合适？
    # stat.sort_values()
    print(sums[:4])
    print('-------------标签推荐完成--------------------')
    return sums[:4]

# getRecommendedLabel('2307')