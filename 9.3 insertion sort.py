nums = [3,5,6,4,8,7,9,1]

n = len(nums)

for i in range(1,n):
    p=i
    while p>0 and nums[p-1]>nums[p]:
        nums[p], nums[p-1] = nums[p-1], nums[p]
        p-=1

print(nums)       