#解析：https://leetcode-solution.cn/solutionDetail?type=3&id=5&max_id=2
'''
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek(); // 返回 1
queue.pop(); // 返回 1
queue.empty(); // 返回 false
说明:

你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的、 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
'''

class MyQueue():
    def __init__(self):
        self.queue=[]
        self.out_queue=[]

    def push(self,x:int):
        self.queue.append(x)    #尾部插入
        print('queue:',self.queue)

    def __stack_exchange(self,x:list,y:list): #输入栈与输出栈交换
        while x != []:    #循环遍历x的栈顶，依次取出存入y栈中
            stack_top=x.pop()      #x删除栈顶，并返回删除的值
            y.append(stack_top)    #y插入x删除的栈顶

    def empty(self):    #判断队列是否为空
        if self.queue == []:
            return True
        else:
            return False

    def peek(self):
        if self.empty() == True:
            print(f'空栈，{self.__class__.__name__}.peek操作无效')
        else:
            self.__stack_exchange(self.queue,self.out_queue)  #交换栈
            print(self.out_queue[-1])   #返回栈顶
            self.__stack_exchange(self.out_queue,self.queue)  #再交换回去，还原
            # print('queue:',self.queue)

    def pop(self):
        if self.empty() == True:
            print(f'空栈，{self.__class__.__name__}.pop操作无效')
        else:
            self.__stack_exchange(self.queue,self.out_queue)  #交换栈
            print(self.out_queue.pop())    #删除输出栈的栈顶
            self.__stack_exchange(self.out_queue,self.queue)  #再交换回去，还原，此时已删除输入栈的栈顶
            # print('queue:',self.queue)


my_queue=MyQueue()
my_queue.push(1)    #queue: [1]
my_queue.push(2)    #queue: [1, 2]
my_queue.peek()     #1
my_queue.pop()          #1
print(my_queue.queue)   #[2]
print(my_queue.empty()) #False
my_queue.pop()          #2
print(my_queue.empty()) #True
print(my_queue.queue)   #[]



# my_queue.pop()
# my_queue.push(2)
# my_queue.push(3)
# my_queue.push(4)
# my_queue.pop()
# my_queue.pop()
# my_queue.push(5)
# my_queue.peek()
# my_queue.pop()
# my_queue.pop()
# print(my_queue.empty())
# my_queue.pop()
# my_queue.peek()
# my_queue.push(5)
# my_queue.push(6)
# my_queue.peek()
# my_queue.pop()
# my_queue.pop()
# my_queue.peek()
# my_queue.pop()

