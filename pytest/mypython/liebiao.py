'''
Created on 2020-9-7
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错，
通过内建的isinstance函数可以判断一个变量是不是字符串：
@author: zhangsanshi
'''
# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')