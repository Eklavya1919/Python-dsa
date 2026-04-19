


# for l in range(len(nums)):
#     miniid = l
    
#     for i in range(l+1, len(nums)):
#         if nums[i] < nums[miniid]:
#             miniid = i

#     nums[l], nums[miniid] = nums[miniid], nums[l]
 
# print(nums)

nums = [4,9,8,2,3,6,7]



# revise
for i in range(len(nums)):
    mini = i
    for j in range(i+1,len(nums)):
        if nums[j]<nums[mini]:
            mini = j
    nums[i], nums[mini] = nums[mini], nums[i]

print(nums)






