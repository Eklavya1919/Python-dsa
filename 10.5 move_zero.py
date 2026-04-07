def move(nums):
    left = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i],nums[left]=nums[left],nums[i]
            left+=1
    return nums

nums=[1,0,2,0,5,4]

print(move(nums))