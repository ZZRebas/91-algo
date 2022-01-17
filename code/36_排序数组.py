'''
给你一个整数数组 nums，请你将该数组升序排列。

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]


提示：

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
'''

#冒泡排序
def fun1(nums):
    j=0
    while j<len(nums)-1:
        for i in range(len(nums)-1-j):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
        j+=1
    print(nums)

nums = [5,1,1,2,0,-1,0,-2]
fun1(nums)

#计数排序
def fun2(nums):
    d=dict.fromkeys(range(-50000,50001),0)
    for key in nums:
        d[key]+=1
    for key,v in d.items():
        if v != 0:
            for i in range(v):
                print(key,end=' ')

nums = [5,1,1,2,0,-1,0,-2]
fun2(nums)