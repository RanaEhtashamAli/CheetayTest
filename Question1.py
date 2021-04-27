def activityselection(start, end, n):
    selected = []
    arr = list(zip(*[start, end]))
    arr.sort(key=lambda x: x[1])
    i = 0
    selected.append(arr[i])
    for j in range(1, n):
        if arr[j][0] > arr[i][1]:
            selected.append(arr[j])
            i = j
    return len(selected)
