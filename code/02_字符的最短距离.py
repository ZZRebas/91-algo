#解析：https://leetcode-solution.cn/solutionDetail?type=3&id=2&max_id=2
'''
给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。
示例 1:
输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
说明:
- 字符串 S 的长度范围为 [1, 10000]。
- C 是一个单字符，且保证是字符串 S 里的字符。
- S 和 C 中的所有字母均为小写字母。
'''


#方法1
def fun(S,C):
    C_index=[]
    out_list=[]
    for n,i in enumerate(S):
        out_list.append(None)
        if i ==C:
            C_index.append(n)
            out_list[n]=0
    # out_list=[0 if S[i]==C else None for i in range(len(S))]

    #从第一个字符C向左排序
    for n,i in enumerate(range(C_index[0]+1)[::-1]):
        out_list[n]=i
    # print(out_list)   #[3, 2, 1, 0, None, 0, 0, None, None, None, None, 0, None, None]

    #从最后一个字符C向右排序
    for n,i in enumerate(out_list[C_index[-1]:]):
        out_list[C_index[-1]+n]=n
    # print(out_list)     #[3, 2, 1, 0, None, 0, 0, None, None, None, None, 0, 1, 2]

    #中间的字符C,向两个C的中间排序
    for i in range(len(C_index)-1):
        subtract=C_index[i+1]-C_index[i]
        if subtract%2==0:
            division=subtract//2
        else:
            division=(subtract-1)//2
        for j in range(1,division+1):
            out_list[C_index[i]+j]=j
            out_list[C_index[i+1]-j]=j

    print(out_list)

S = "loveleetcodedf"
C = 'e'
fun(S,C)    #[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0, 1, 2]

#方法2
'''
思路
对于每个字符 s[i] 找出其距离左边及右边下一个目标字符 C 的距离，左右距离中的较小值即为答案。

从左往右遍历：
假设上一个 C 出现的位置为 pre，则当前 i 位置的字符距离 $C$ 的距离为 i-pre （pre <= i）；

从右往左遍历：
假设上一个 C 出现的位置为 pre，则当前 i 位置的字符距离 C 的距离为 pre-i （i <= pre）；
'''
class Solution:
    def shortestToChar(self, s: str, c: str) -> list:

        n = len(s)
        ans = []

        # 正序遍历
        pre = -n    # 设为较小的 -n 即可（距离的最大值不可能超过n）
        for (i, ch) in enumerate(s):
            if ch == c:
                pre = i
            ans.append(i-pre)

        # 逆序遍历
        pre = 2*n   # 设为较大的 2*n 即可（距离的最大值不可能超过n）
        for i in range(n-1, -1, -1):
            if s[i] == c:
                pre = i
            ans[i] = min(ans[i], pre-i)

        return ans

res=Solution()
print(res.shortestToChar(S,C))


#方法3
'''
思路
第一次循环：找到s中所有c的下标。
第二次循环：循环对比s中每个字符，到所有c的下标的距离，取其中的最小值放入answer中
'''
class Solution3(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        lab=[]
        for i in range(len(s)):
            if s[i]==c:
                lab.append(i)

        res=[0]*len(s)
        for i in range(len(s)):
            lab0 = [abs(j-i) for j in lab]
            res[i]=min(lab0)
        return res

res3=Solution3()
print(res3.shortestToChar(S,C))


#贪心
'''
先 从左往右 遍历字符串 S，用一个数组 left 记录每个字符 左侧 出现的最后一个 C 字符的下标；
再 从右往左 遍历字符串 S，用一个数组 right 记录每个字符 右侧 出现的最后一个 C 字符的下标；
然后同时遍历这两个数组，计算距离最小值。'''
class Solution4(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        res = [0 if s[i] == c else None for i in range(n)]

        for i in range(1, n):
            if res[i] != 0 and res[i - 1] is not None:
                res[i] = res[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if res[i] is None or res[i + 1] + 1 < res[i]:
                res[i] = res[i + 1] + 1
        return res

res4=Solution3()
print(res4.shortestToChar(S,C))
