#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-05-21 18:37:35
# @Last Modified by:   anchen
# @Last Modified time: 2018-05-23 13:56:15
import xlrd
data = xlrd.open_workbook('D:/test.xlsx')
table = data.sheets()[5]
nrows = table.nrows
ncols = table.ncols
for i in range(2,4):
    for j in range(4,10):
        if i==0:
            continue
        x=table.row_values(i)[j]
        # ip = table.row_values(2)[4]
        # group = table.row_values(i)[j]
        # role = table.row_values(i)[j]
        # groupleader = table.row_values(i)[j]
        # isvm = table.row_values(i)[j]
        # zhuji = table.row_values(i)[j]
        # leaderema = table.row_values(i)[j]
        # ip,group,role,groupleader,isvm,zhuji,leaderema
        print x
    print '\n'

# listd=