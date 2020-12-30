'''
Created on 2020-9-8
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
@author: zhangsanshi
'''
from functools import reduce
def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def char2num(s):
        return DIGITS[s]

    #去除小数点
    s1 = s.replace('.','')
    #转成int
    integer = reduce(lambda x, y: x * 10 + y, map(char2num, s1))
    #获取小数个数
    decimalCount = len(s[s.index('.') : -1])
    #转成float
    floatNum = integer / 10 ** decimalCount

    return floatNum



#测试；
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')