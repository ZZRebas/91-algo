
'''
请你设计一个支持下述操作的栈。

实现自定义栈类 CustomStack ：

CustomStack(int maxSize)：用 maxSize 初始化对象，maxSize 是栈中最多能容纳的元素数量，栈在增长到 maxSize 之后则不支持 push 操作。
void push(int x)：如果栈还未增长到 maxSize ，就将 x 添加到栈顶。
int pop()：弹出栈顶元素，并返回栈顶的值，或栈为空时返回 -1 。
void increment(int k, int val)：栈底的 k 个元素的值都增加 val 。如果栈中元素总数小于 k ，则栈中的所有元素都增加 val 。


示例：

输入：
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
输出：
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
解释：
CustomStack customStack = new CustomStack(3); // 栈是空的 []
customStack.push(1); // 栈变为 [1]
customStack.push(2); // 栈变为 [1, 2]
customStack.pop(); // 返回 2 --> 返回栈顶值 2，栈变为 [1]
customStack.push(2); // 栈变为 [1, 2]
customStack.push(3); // 栈变为 [1, 2, 3]
customStack.push(4); // 栈仍然是 [1, 2, 3]，不能添加其他元素使栈大小变为 4
customStack.increment(5, 100); // 栈变为 [101, 102, 103]
customStack.increment(2, 100); // 栈变为 [201, 202, 103]
customStack.pop(); // 返回 103 --> 返回栈顶值 103，栈变为 [201, 202]
customStack.pop(); // 返回 202 --> 返回栈顶值 202，栈变为 [201]
customStack.pop(); // 返回 201 --> 返回栈顶值 201，栈变为 []
customStack.pop(); // 返回 -1 --> 栈为空，返回 -1


提示：

1 <= maxSize <= 1000
1 <= x <= 1000
1 <= k <= 1000
0 <= val <= 100
每种方法 increment，push 以及 pop 分别最多调用 1000 次
'''


class CustomStack():
    def __init__(self,maxSize:int):     #初始化
        self.maxSize=maxSize
        self.customstack=[]

    def push(self,x:int):
        if len(self.customstack)==self.maxSize:
            # print('已超出栈中最多能容纳的元素数量，无法再增加')
            pass
        else:
            self.customstack.append(x)  #入栈

    def pop(self):
        if self.customstack==[]:
            return -1
        else:
            stack_top=self.customstack[-1]
            self.customstack.pop()  #出栈
            return stack_top    #返回出栈的元素

    def increment(self,k:int,val:int):
        if len(self.customstack)>=k:   #注意，这里需要对比k与当前栈实际的长度，而不是与栈的最大长度maxSize对比
            for i in range(k):
                self.customstack[i]+=val
        else:
            self.customstack=[self.customstack[i]+val for i in range(len(self.customstack))]
        
        # for i in range(0,min(k,len(self.customstack))):
        #     self.customstack[i]+=val


def obj_API(A,B):
    C=[]
    obj=CustomStack(B[0][0])
    for i in range(len(A)):     #循环A、B，依次进行对应操作
        if i==0:
            C.append(None)
        else:
            if A[i]=='push':
                obj.push(B[i][0])
                C.append(None)
            elif A[i]=='pop':
                C.append(obj.pop())
            elif A[i]=='increment':
                obj.increment(B[i][0],B[i][1])
                C.append(None)
        # print('i:',i,C,obj.customstack)
    print(C)


A=["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
B=[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]

obj_API(A,B)    #[None, None, None, 2, None, None, None, None, None, 103, 202, 201, -1]


