'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
'''


def fun(chain,k):
    linked=chain.replace('->NULL','').split('->')
    i=0
    while i<k:
        linked.insert(0,linked.pop())
        i+=1
    print('->'.join(linked)+'->NULL')

chain='1->2->3->4->5->NULL'
k = 2
fun(chain,k)    #4->5->1->2->3->NULL
chain='0->1->2->NULL'
k = 4
fun(chain,k)    #2->0->1->NULL
