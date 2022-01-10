'''
You are given a list of positive integers nums and a positive integer k. Return the length of the shortest sublist (can be empty sublist ) you can delete such that the resulting list's sum is divisible by k. You cannot delete the entire list. If it's not possible, return -1.

Constraints

1 ≤ n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [1, 8, 6, 4, 5]
k = 7
Output
2
Explanation
We can remove the sublist [6, 4] to get [1, 8, 5] which sums to 14 and is divisible by 7.
'''
from functools import reduce
def fun(nums,k):
    n=0
    while n<len(nums):
        for i in range(len(nums)-n+1):
            new_nums=nums[:i]+nums[i+n:]
            sum=reduce(lambda x,y:x+y,new_nums)
            print(new_nums,sum)
            if sum%k == 0:
                return n
            if n==0:
                break
        n+=1
    if n==len(nums):
        return -1

nums = [1, 8, 6, 4, 5]
k = 7
res=fun(nums,k)
print(res)


class Solution:
    def solve(self, nums, k):
        total = sum(nums)
        mod = total % k
        ans = len(nums)
        total = 0
        dic = {0: -1}
        for j in range(len(nums)):
            total += nums[j]
            cur = total % k
            target = (cur - mod + k) % k
            if target in dic:
                ans = min(ans, j - dic[target])
            dic[cur] = j

        if ans == len(nums):
            return -1
        return ans

a=Solution()
print(a.solve(nums,k))