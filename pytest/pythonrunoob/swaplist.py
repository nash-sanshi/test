def swaplist(newlist):
    newlist[0],newlist[-1] = newlist[-1],newlist[0]
    return newlist

newlist = [0,1,2]
#print(swaplist(newlist))

def swapList2(newList):
    size = len(newList)
     
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
     
    return newList 
print(swapList2(newlist))