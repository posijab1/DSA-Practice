def contains_duplicate1(nums):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

print(contains_duplicate1([1,2,3,4,1]))
#O(n2)
def contains_duplicate2(nums):

    aux1 = set()
    for i in nums:
        if i in aux1:
            return True
        aux1.add(i)
    return False

print(contains_duplicate2([1,2,3,4]))
#O(n)