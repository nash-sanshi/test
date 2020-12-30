'''
Created on 2020-8-26
计算x任意n次方
@author: zhangsanshi
'''

def power(x,n):
    s=1
    while n>0:
        n = n-1
        s = s*x
    return s

print(power(5,3))