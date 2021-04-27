def equilibriumPoint(arr,n):
    arrSum = sum(arr)
    for i,num in enumerate(arr):
        arrSum -= num
        tempSum = sum([i for i in arr[:i]])
        if arrSum == tempSum:
            return i+1
    return -1
