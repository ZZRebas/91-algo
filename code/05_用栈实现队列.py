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

    def push(self,x):
        self.queue.append(x)    #尾部插入
        print(my_queue.queue)

    def pop(self):
        if self.empty() == True:
            print( f'空栈，{self.__class__.__name__}.pop操作无效')
        else:
            print(f'删除{self.queue[0]}')
            self.queue=self.queue[1:]   #首部删除

    def peek(self):
        if self.empty() == True:
            print(f'空栈，{self.__class__.__name__}.peek操作无效')
            return f'空栈，{self.__class__.__name__}.peek操作无效'
        else:
            print(self.queue[0])
            return self.queue[0]    #返回队列首部元素

    def empty(self):    #判断队列是否为空
        if self.queue == []:
            return True
        else:
            return False

my_queue=MyQueue()
my_queue.push(1)    #[1]
my_queue.push(2)    #[1, 2]
my_queue.peek()     #1
my_queue.pop()      #删除1
print(my_queue.empty())   #False
print(my_queue.queue)     #[2]

