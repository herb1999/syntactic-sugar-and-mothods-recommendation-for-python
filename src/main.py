#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from src.prepare import *
from src.rating import *
caseId='2307'
downloadAndUnzip(caseId)
calcuResults(caseId)
rate(caseId)


