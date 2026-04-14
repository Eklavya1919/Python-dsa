nums = [2, 3, 5, -2, 7, -4]

maxsum = nums[0]
temsum = nums[0]

for i in nums[1:]:
    temsum = max(i, temsum + i)
    maxsum = max(maxsum, temsum)

print(maxsum)