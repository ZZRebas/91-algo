'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
'''


def fun(nums,k):
    l=0
    r=len(nums)-1
    if k < nums[l]: #k小于数组第一个元素
        nums.insert(l,k)
        return l,nums
    if k > nums[r]: #k大于数组最后一个元素
        nums.append(k)
        return r+1,nums
    while l<=r:
        mid=(l+r)//2
        if k>nums[mid]:
            l=mid+1
            if k<nums[l]:   #k不在数组内，位于相邻两个元素之间时
                nums.insert(l,k)
                return l,nums
        elif k<nums[mid]:
            r=mid
        else:
            return mid,nums

nums=[1,3,5,6]
k=6
print(fun(nums,k))
