#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import sys
import json
import re
from src.util import *
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

#todo:将答案代码纳入统计



def search(caseId):
    rated = getRated(caseId)
    # 取评分前五的path
    paths = list(rated.sort_values(by='rate')['path'][:5])
    print(paths)

    # libs = getLibs()
    # print(libs)


    results_lib = []
    results_method = []
    results_candy = []
    for path in paths:
        res=searchLib(path)
        if len(res)>0:
            results_lib.append(res)
    print('results_lib: ')
    print(results_lib)

#
# def searchCode(file)
def searchLib(path):
    res = {}
    pyPath = path + '/main.py'
    with open(pyPath, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            # 除去注释行
            line = line.strip()
            if line.startswith('#'):
                continue
            if 'import' in line:
                print('found: ' + line)
                patterns = line.split(' ')

                # from xxx import xxx 的形式
                if 'from' in line:
                    lib = patterns[patterns.index('from') + 1]
                    res[lib] = 1
                # import xxx 的形式
                else:
                    lib = patterns[patterns.index('import') + 1]
                    res[lib] = 1
    return res

def searchMethod(path):
    #todo:排除用内置方法名定义的变量和方法
    res = {}
    methods = getBuiltinMethods()
    # print(methods)
    pyPath = path + '/main.py'
    with open(pyPath, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            # 除去注释行
            line = line.strip()
            if line.startswith('#'):
                continue


    return res


#todo:根据操作符切分代码
def splitLine(line):
    #操作符有的要转义，有的不用，测试清楚
    pattern=r'[+\-=*/()\[\]{\}]+'
    return re.split(pattern,line)
search('2307')

