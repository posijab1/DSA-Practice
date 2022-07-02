def maxSubArraySum(arr):

    aux1 = arr[0]
    aux2 = 0

    for i in arr:
        aux2 += i
        if aux1 < 0:
            aux1 = 0
        elif aux1 > aux2:
            aux2 = aux1
    return aux2

print(maxSubArraySum([4, -3, 4, -1, -2, 5, -3]))