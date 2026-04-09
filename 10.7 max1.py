nums = [0,1,1,0,1,1,1,1,0]
def count1(nums):
    ans=0
    c=0
    for i in nums: 
        if i==1:
            c+=1
        else:
            ans=max(ans,c)
            c=0
    return ans


print(count1(nums))