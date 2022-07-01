def maxSubArraySum(arr):

    aux1 = arr[0]
    aux2 = 0

    for i in range(len(arr)-1):
        aux2 += arr[i]
        if aux2 < 0:
            aux2 = 0
        elif aux1 < aux2:
            aux1 = aux2
    return aux1


print(maxSubArraySum([4, -3, 4, -1, -2, 5, -3]))