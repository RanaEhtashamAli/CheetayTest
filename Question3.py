def longestSubstrDitinctChar(string):
    uniqueList = []
    tempList = []
    for i,char in enumerate(string.lower()):
        if char in tempList:
            uniqueList.append(''.join(tempList))
            tempList.clear()
            tempList.append(char)
        else:
            tempList.append(char)
    if len(tempList) > 0:
        uniqueList.append(''.join(tempList))
        tempList.clear()
    return len(max(uniqueList,key=len))