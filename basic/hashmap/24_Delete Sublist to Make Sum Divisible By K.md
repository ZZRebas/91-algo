# 24.Delete Sublist to Make Sum Divisible By K

链接：https://binarysearch.com/problems/Delete-Sublist-to-Make-Sum-Divisible-By-K

- [24.Delete Sublist to Make Sum Divisible By K](#24Delete Sublist to Make Sum Divisible By K)
    - [题目描述](#题目描述)
    - [方法 1](#方法-1)
        - [思路](#思路)
        - [代码(Python)](#代码Python)
        - [复杂度分析](#复杂度分析)
 

## 题目描述
```
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
```

## 方法 1

### 思路
在一个循环里面，遍历数组，依次求和，判断是否能被k整除。

### 代码(Python)
```python
from functools import reduce
def fun(nums,k):
    n=0
    while n<len(nums):
        for i in range(len(nums)-n+1):
            new_nums=nums[:i]+nums[i+n:]
            sum=reduce(lambda x,y:x+y,new_nums)
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
print(res)  #2

```

### 复杂度分析
- 时间复杂度：O(N**2)，N为数组长度。
- 空间复杂度：


