# 52.Shortest-Cycle-Containing-Target-Node
链接：https://binarysearch.com/problems/Shortest-Cycle-Containing-Target-Node

- [52.Shortest-Cycle-Containing-Target-Node](#52.Shortest-Cycle-Containing-Target-Node)
    - [题目描述](#题目描述)
    - [方法 1](#方法-1)
        - [思路](#思路)
        - [代码(Python)](#代码Python)
        - [复杂度分析](#复杂度分析)

## 题目描述
```
You are given a two-dimensional list of integers graph representing a directed graph as an adjacency list. You are also given an integer target.

Return the length of a shortest cycle that contains target. If a solution does not exist, return -1.

Constraints

n, m ≤ 250 where n and m are the number of rows and columns in graph
```

## 方法 1

### 思路
BFS

### 代码(Python)
```python
import collections
class Solution:
    def solve(self, graph, target):
        q = collections.deque([target])
        visited = set()
        steps = 0
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                visited.add(cur)
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        q.append(neighbor)
                    elif neighbor == target:
                        return steps + 1
            steps += 1
        return -1


```

### 复杂度分析
令 v 节点数, e 为边数。
- 时间复杂度：O(v+e)。
- 空间复杂度：O(v)。

