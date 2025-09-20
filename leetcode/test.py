# This file contains my manual 'tests' made for solving leetcode problems.
# This can help you understand a problem solution much easier.

haystack = "sadbudsad"
needle = "sad"

start = -1
for i in range(len(haystack)):
    if needle[0] == haystack[i]:
        print(haystack[i : i + len(needle)])

        if needle == haystack[i : i + len(needle)]:
            start = i
            break

print(start)
