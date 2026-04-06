def rem_dup(nums):
    seen = []
    for i in nums:
        if i not in seen:
            seen.append(i)
        
    for i in range(len(seen)):
        nums[i]=seen[i]

    print(nums)

nums = [1,1,2,2,2,3,3]

rem_dup(nums)