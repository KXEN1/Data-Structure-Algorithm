#!/usr/bin/env python
# coding: utf-8

# In[7]:


class CircularQueue:
    def __init__(self, size):
        self.SIZE = size
        self.queue = [None] * self.SIZE
        self.front = self.rear = 0

    def is_queue_full(self):
        return (self.rear + 1) % self.SIZE == self.front

    def is_queue_empty(self):
        return self.front == self.rear

    def enqueue(self, data):
        if self.is_queue_full():
            print("큐가 꽉 찼습니다.")
            return
        self.rear = (self.rear + 1) % self.SIZE
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_queue_empty():
            print("큐가 비었습니다.")
            return None
        self.front = (self.front + 1) % self.SIZE
        data = self.queue[self.front]
        self.queue[self.front] = None
        return data


def bfs(graph, start):
    visited = set() # 이미 방문한 노드를 기록
    queue = CircularQueue(len(graph))

    queue.enqueue(start) # 시작노드를 큐에 추가하고 방문여부 기록
    visited.add(start)

    while not queue.is_queue_empty(): # 큐가 비어있지 않은 동안 반복
        node = queue.dequeue()
        print(node, end='->')

        for neighbor in range(len(graph)): # 현재 노드에 연결된 이웃노드 확인
            if graph[node][neighbor] == 1 and neighbor not in visited: # 이웃이 연결되어 있고, 아직 방문하지 않은 경우 큐에 추가하고 방문여부 기록
                queue.enqueue(neighbor)
                visited.add(neighbor)

    print('None')


# 전역 변수 선언 부분
SIZE = 6
# 그래프 문제 예시 (인접 행렬로 표현)
graph = [
    [0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0]
]

bfs(graph, 0)


# In[ ]:




