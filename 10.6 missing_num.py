nums = [1,3,4,5,6]

def find(nums):
    n = len(nums)
    exp = (n+1)*(n+2)//2
    real = sum(nums)
    return exp-real

print(find(nums))