'''
Created on 2020-8-28
请使用迭代查找一个list中最小和最大值，并返回一个tuple：
@author: zhangsanshi
'''
# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if (len(L) > 0):
        maxForList = L[0];
        minForList = L[0];
        for i in L:
            if (maxForList < i):
                maxForList = i;
            if (minForList > i):
                minForList = i;
        return (minForList, maxForList);
    else:
        return (None, None);
    # 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')