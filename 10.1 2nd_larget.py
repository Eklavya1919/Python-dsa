def second_larget(nums):
    max_ele = nums[0]
    max2_ele = nums[1]
    for i in nums:
        if i>max_ele:
            max_ele=i
    for i in nums:
        if i!=max_ele and i>max2_ele:
            max2_ele=i

    return max2_ele

nums = [5,4,6,8,1,2]

print(second_larget(nums))
