'''
Created on 2020-8-25

@author: zhangsanshi
'''
weight = float(input('请输入您的体重（kg）：'))

height = float(input('请输入您的身高（m）：'))

bmi = weight / ( height * height)

if bmi < 18.5:

    print('您的BMI值为%.2f%%'% bmi,'，属于过轻')

elif bmi <25:

    #print('您的BMI值为%.2f%%'% bmi,'，属于正常')
    print('您的BMI指数为：%.2f,正常'%bmi)

elif bmi <28:

    print('您的BMI值为%.2f%%'% bmi,'，属于过重')

elif bmi <32:

    print('您的BMI值为%.2f%%'% bmi,'，属于肥胖')

else:

    print('您的BMI值为%.2f%%'% bmi,'，属于严重肥胖')
