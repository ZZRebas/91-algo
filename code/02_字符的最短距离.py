
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


def fun(S,C):
    C_index=[]
    out_list=[]
    for n,i in enumerate(S):
        out_list.append(None)
        if i ==C:
            C_index.append(n)
            out_list[n]=0

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

