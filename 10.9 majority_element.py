nums = [7, 0, 0, 1, 7, 7, 2, 7, 7] 

tem = dict()

for i in nums:
    if i in tem:
        tem[i]+=1
    else:
        tem[i]=1

n = len(nums)

for i in tem:
    if tem[i]>n//2:
        print(i)