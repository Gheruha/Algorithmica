# This file contains my manual 'tests' made for solving leetcode problems.
# This can help you understand a problem solution much easier.

nums = [1, 2, 3, 4]
target = 7
pos = 0

for i in range(len(nums)):
    if nums[i] > target:
        pos = i - 1
        break
    elif nums[i] == target:
        pos = i
        break
    else:
        pos = i + 1

print(pos)
