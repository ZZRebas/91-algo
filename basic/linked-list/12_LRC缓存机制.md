# 12.146-LRU缓存机制

链接：https://leetcode-cn.com/problems/lru-cache/

- [12.146-LRU缓存机制](#12146-LRU缓存机制)
    - [题目描述](#题目描述)
    - [方法 1](#方法-1)
        - [思路](#思路)
        - [代码(Python)](#代码Python)
        - [复杂度分析](#复杂度分析)

## 题目描述
```
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。


进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？



示例：

输入

["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]
解释

LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
```

## 方法 1

### 思路
python字典

### 代码(Python)
```python
class LRUCache(object):
    def __init__(self,capacity:int):
        self.capacity=capacity
        self.dd={}
        self.order=[]
    def get(self,key):
        if key in self.dd.keys():
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)
            self.order=list(set(self.order))
            return self.dd[key]
        else:
            return -1

    def put(self,key,value):
        if key in self.dd.keys():
            self.dd[key]=value
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.dd)==self.capacity:
                key_=self.order[0]
                self.dd.pop(key_)
                self.dd[key]=value
                if key in self.order:
                    self.order.remove(key)
                self.order.append(key)

            else:
                self.dd[key]=value
                if key in self.order:
                    self.order.remove(key)
                self.order.append(key)


```

### 复杂度分析
- 时间复杂度： O(N)。
- 空间复杂度：

