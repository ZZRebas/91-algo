
'''
给定一个非空的整数数组，返回其中出现频率前  k  高的元素。
示例 1:


输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]


示例 2:


输入: nums = [1], k = 1
输出: [1]


提示：

- 你可以假设给定的  k  总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
- 你的算法的时间复杂度必须优于 O(n log n) , n  是数组的大小。
- 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
- 你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
'''



def fun(nums,k):
    nums_dict=dict.fromkeys(set(nums),0)
    for i in nums:
        nums_dict[i]+=1
    print(nums_dict)
    a=list(nums_dict.values())
    a.sort()
    a.reverse()
    res=[]
    for key,v in nums_dict.items():
        if v in a[:k]:
            res.append(key)
    return res
nums = [1,1,1,2,2,3]
k = 2
print(fun(nums,k))
