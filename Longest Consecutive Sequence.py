def longest_consecutive_sequence(nums):

    longest = 0

    for i in nums:
        if i-1 not in nums:
            lenght = 0
            while i + lenght in nums:
                longest = max(lenght, longest)
                lenght += 1
    return longest

print(longest_consecutive_sequence([1,2,3,4,0,5]))