def product_of_array_except_self(nums):
    l, r = 1, 1
    aux1 = [0] * len(nums)

    for i in range(len(nums)):
        aux1[i] = l #
        l *= nums[i]



    for i in range(len(nums)-1,-1,-1):
        aux1[i] *= r
        r *= nums[i]

    return aux1

print(product_of_array_except_self([2,1,3]))

