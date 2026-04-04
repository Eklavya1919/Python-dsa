nums = [5,4,3,1,2]

while True:
    swapped = False
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            nums[i],nums[i+1]=nums[i+1],nums[i]
            swapped = True
    if swapped==False:
        break

print(nums)