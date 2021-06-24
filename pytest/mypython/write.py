# 打开一个文件
f = open("c:/USERS/张磊/Desktop/test.txt", "w")

num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)
# 关闭打开的文件
f.close()

f = open("c:/USERS/张磊/Desktop/test.txt", "r")

str = f.read()
print(str)

# 关闭打开的文件
f.close()