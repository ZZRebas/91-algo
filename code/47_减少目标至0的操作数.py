'''
You are given a list of positive integers nums and an integer target. Consider an operation where we remove a number v from either the front or the back of nums and decrement target by v.

Return the minimum number of operations required to decrement target to zero. If it's not possible, return -1.

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [3, 1, 1, 2, 5, 1, 1]
target = 7
Output
3
Explanation
We can remove 1, 1 and 5 from the back to decrement target to zero.

Example 2
Input
nums = [2, 4]
target = 7
Output
-1
Explanation
There's no way to decrement target = 7 to zero.
'''

def fun(nums,target):
    nums.reverse()
    sum=0
    for i in range(len(nums)):
        sum+=nums[i]
        if sum==target:
            print(i+1)
            break
        elif sum>target:
            print(-1)
            break
        if i==len(nums)-1:
            print(-1)

nums = [3, 1, 1, 2, 5, 1, 1]
target = 7
fun(nums,target)
