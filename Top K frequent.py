def top_k_frequent(nums, k):
    aux1 = {}
    aux2 = [[] for i in range(len(nums))]

    for i in nums:
        aux1[i] = 1 + aux1.get(i, 0)

    for i, j in aux1.items():
        aux2[j].append(i)

    ans = []

    for i in range(len(aux2)-1,-1,-1):
        for n in aux2[i]:
            ans.append(n)
            if len(ans) == k:
                return ans
    return False


print(top_k_frequent([1,1,1,2,4,4,4,4,4,3,4],2))

#O(Klog(K)).
