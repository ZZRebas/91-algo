'''
给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。
示例 1：

输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例 2：

输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。


提示：

给定链表的结点数介于 1 和 100 之间。
'''



class ListNode(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Solution():
    def middleNode(self,head:ListNode) -> ListNode:
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow

linklist=[1,2,3,4,5]
# node6=ListNode(6,None)
node5=ListNode(5,None)
node4=ListNode(4,node5)
node3=ListNode(3,node4)
node2=ListNode(2,node3)
node1=ListNode(1,node2)
head=ListNode(None,node1)

obj=Solution()
print(obj.middleNode(head).data)

