#coding=utf-8
'''
Created on 2021年1月6号

@author: 张磊
'''
magicians = ['alice', 'david', 'carola']
for magician in magicians:
    print(magician.title() + ", that was a great trick")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you everyone, that was a great magic show!")

#.title()表示首字母大写，\n表示换行