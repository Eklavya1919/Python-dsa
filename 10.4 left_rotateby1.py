def rotate(nums):
    return nums[1:] + [nums[0]]

nums=[1,2,3,4,5]

print(rotate(nums))