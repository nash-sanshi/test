'''
Created on 2020-9-8
利用闭包返回一个计数器函数，每次调用它返回递增整数：
@author: zhangsanshi
'''
def createCounter():
    # a=[0] 赋值a为list,不推荐
    b=0
    def counter():
        nonlocal b#声明为nonlocal变量
        # a[0]+=1
        b+=1
        # return a[0]
        return b
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')