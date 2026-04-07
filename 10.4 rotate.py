def rotate_by1(nums):
    return nums[1:] + [nums[0]]

def rotate_left_byk(nums, k):
    k = k % len(nums)
    return nums[k:] + nums[:k]

def rotate_right_byk(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]    

nums = [1,2,3,4,5]

print(rotate_right_byk(nums,3))

