'''
给定一组 N 人（编号为 1, 2, ..., N）， 我们想把每个人分进任意大小的两组。

每个人都可能不喜欢其他人，那么他们不应该属于同一组。

形式上，如果 dislikes[i] = [a, b]，表示不允许将编号为 a 和 b 的人归入同一组。

当可以用这种方法将每个人分进两组时，返回 true；否则返回 false。

示例 1：

输入：N = 4, dislikes = [[1,2],[1,3],[2,4]]
输出：true
解释：group1 [1,4], group2 [2,3]
示例 2：

输入：N = 3, dislikes = [[1,2],[1,3],[2,3]]
输出：false
示例 3：

输入：N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
输出：false


提示：

1 <= N <= 2000
0 <= dislikes.length <= 10000
dislikes[i].length == 2
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
对于dislikes[i] == dislikes[j] 不存在 i != j
'''



def fun(N,dislikes):
    N_lt=range(1,N+1)
    N_dict=dict.fromkeys(N_lt,0)    #先把N个人分为同一组
    flag_dict=dict.fromkeys(N_lt,0) #对每个人做一个是否遍历过的标记，未遍历设为0，遍历过记为1
    for k,v in dislikes:
        if N_dict[k]==0:
            if flag_dict[k]==1 and flag_dict[v]==1:
                return False
            N_dict[v]=1
            flag_dict[k]=1
            flag_dict[v]=1
        else:
            if N_dict[v]==1:
                return False
            flag_dict[v]=1
    print(N_dict)
    return True

N = 4
dislikes = [[1,2],[1,3],[2,4]]
print(fun(N,dislikes))  #True
N = 4
dislikes = [[1,2],[1,3],[2,3]]
print(fun(N,dislikes))  #False
N = 5
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
print(fun(N,dislikes))  #False
