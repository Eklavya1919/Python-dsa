nums = [2,2,3,4,5,3,4,6,6]

def once(nums):
    tem = dict()
    for i in nums:
        if i in tem:
            tem[i]+=1
        else:
            tem[i]=1
    for i in tem:
        if tem[i]==1:
            return i
        
    return 0

print(once(nums))



# optimized answer
# a^a = 0 and a^0 = a 

def getSingleElement(nums):
    ans = 0
    for num in nums:
        ans ^= num

    return ans

nums = [4, 1, 2, 1, 2]
ans = getSingleElement(nums)
print("The single element is:", ans)
