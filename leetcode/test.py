# This file contains my manual 'tests' made for solving leetcode problems.
# This can help you understand a problem solution much easier.

nums = [1, 1, 1, 2, 2, 3, 4, 5, 5]
numslen = len(nums)
previous = nums[0]
i = 1

while i < numslen:
    if nums[i] == previous:
        nums.pop(i)
        numslen -= 1
    else:
        previous = nums[i]
        i += 1

for i in range(numslen):
    print(nums[i])
