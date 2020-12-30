'''
Created on 2020-9-8
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
@author: zhangsanshi
'''

L = list(filter(lambda x:x%2==1,range(1,20)))

print(L)