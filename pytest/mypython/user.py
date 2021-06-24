'''
Created on 2021年1月11日

@author: 张磊
'''
user_0 = {
    'first' : 'efeiri',
    'sec' : 'enrico',
    'mid' : 'feini',
    'last' : 'efeiri',
    }

for key,value in user_0.items():
   print(key + '.\n')
#    print('value :' + value)
    
for name in user_0.values():
    print(name.title() + '.\n')
    
for name in set(user_0.values()):   #去重
    print(name.title())