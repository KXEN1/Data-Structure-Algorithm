#!/usr/bin/env python
# coding: utf-8

# In[14]:


import heapq
import random

class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify_down(self, index):
        # 최소힙 유지를 위한 heapify_down 함수
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index
            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]  # swap
                index = smallest
            else:
                break

    def heapify_up(self, index):
        # 최소힙 유지를 위한 heapify_up 함수
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def min_heap_insert(self, value):
        # 새로운 값을 추가하고 최소힙을 유지하기 위한 insert 함수
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def min_heap_extract(self):
        # 최소값을 추출하고 최소힙을 유지하기 위한 extract 함수
        if not self.heap:
            return None

        min_value = self.heap[0]

        if len(self.heap) == 1:
            self.heap.pop()
            return min_value

        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_value

    def build_min_heap(self, arr):
        # 주어진 배열을 최소힙으로 변환하는 함수
        self.heap = arr
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i)

    def heap_sort(self):
        # 최소힙을 이용하여 힙 정렬하는 함수
        sorted_array = []
        while len(self.heap) > 0:
            min_value = self.min_heap_extract()
            sorted_array.append(min_value)

        return sorted_array

class MinHeapPriorityQueue:
    def __init__(self):
        self.pq = MinHeap()

    def push(self, item):
        # 우선순위 큐에 원소를 추가하는 함수
        self.pq.min_heap_insert(item)

    def pop(self):
        # 우선순위 큐에서 가장 우선순위가 높은 원소를 추출하는 함수
        return self.pq.min_heap_extract()

    def is_empty(self):
        # 우선순위 큐가 비어있는지 확인하는 함수
        return len(self.pq.heap) == 0

    def display(self):
        # 우선순위 큐의 현재 상태를 출력하는 함수
        print("Priority Queue:", self.pq.heap)

if __name__ == "__main__":
    # 랜덤 배열 생성
    random_array = [random.randint(1, 100) for _ in range(20)]
    print("랜덤 배열:", random_array)

    # 최소힙으로 변환
    min_heap = MinHeap()
    min_heap.build_min_heap(random_array.copy())
    print("최소힙으로 변환된 배열:", min_heap.heap)

    # 힙 정렬을 이용하여 최솟값 반환
    min_value = min_heap.min_heap_extract()

    if min_value is not None:
        print("힙 정렬을 이용한 최솟값:", min_value)
    else:
        print("배열이 비어 있습니다.")


# In[ ]:




