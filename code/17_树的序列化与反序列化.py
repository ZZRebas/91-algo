'''
题目地址（297. 二叉树的序列化与反序列化）
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例:

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
'''

class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

import collections
class Codec:
    def serialize(self,root):
        ans=''
        queue=[root]
        while queue:
            node=queue.pop(0)
            if node :
                ans+= str(node.val)+','
                queue.append(node.left)
                queue.append(node.right)
            else:
                ans+='null,'
        print(ans[:-1])
        return ans[:-1]

    def deserialize(self,data):
        if data == 'null': return None
        nodes=data.split(',')
        root=TreeNode(nodes[0])
        #构建一个队列，元素为（当前节点，编号），编号为从1开始的完全二叉树的节点编号
        queue=collections.deque([[root,1]])
        while queue :
            node,i=queue.popleft()
            if 2*i-1<len(nodes):
                lv=nodes[2*i-1]
            if 2*i<len(nodes):
                rv=nodes[2*i]
            if lv != 'null':
                l=TreeNode(lv)
                queue.append([l,2*i])
                node.left=l
            if rv != 'null':
                r=TreeNode(rv)
                queue.append([r,2*i+1])
                node.right=r
            if i == len(nodes):
                break
        return root

    def deserialize2(self,data):
        if data == 'null': return None
        nodes=data.split(',')
        root=TreeNode(nodes[0])
        queue=collections.deque([root])
        i=0
        while queue and i< len(nodes)-2:
            cur=queue.popleft()
            lv=nodes[i+1]
            rv=nodes[i+2]
            i+=2
            if lv != 'null':
                l=TreeNode(lv)
                queue.append(l)
                cur.left=l
            if rv != 'null':
                r=TreeNode(rv)
                queue.append(r)
                cur.right=r
        return root



# data='1,2,3,null,8,5,7'
# a=Codec()
# b=a.deserialize2(data)
# print(b)
# print(b.val)
# print(b.left.val)
# print(b.right.val)
# print(b.left.right.val)
#
# a.serialize(b)


class Solution:
    def serialize(self, root):
        def preorder(root):
            if not root:
                return "null,"
            return str(root.val) + "," + preorder(root.left) + preorder(root.right)

        return preorder(root)[:-1]

    def deserialize(self, data: str):
        nodes = data.split(",")

        def preorder(i):
            if i >= len(nodes) or nodes[i] == "null":
                return i, None
            root = TreeNode(nodes[i])
            j, root.left = preorder(i + 1)
            k, root.right = preorder(j + 1)
            return k, root

        return preorder(0)[1]
data='1,2,3,null,8,5,7'
a=Solution()
b=a.deserialize(data)
print(b)
print(b.val)
print(b.left.val)
# print(b.right.val)
# print(b.left.right.val)
c=a.serialize(b)
print(c)

