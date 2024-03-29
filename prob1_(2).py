#!/usr/bin/env python
# coding: utf-8

# In[5]:


import heapq

class DijkstraPriorityQueue:
    def __init__(self, graph):
        self.graph = graph
        self.num_nodes = len(graph)
        self.distance = [float('inf')] * self.num_nodes
        self.priority_queue = []

    def relax(self, current_node, neighbor, new_distance):
        if new_distance < self.distance[neighbor]:
            self.distance[neighbor] = new_distance  # 최단 거리 갱신
            heapq.heappush(self.priority_queue, (new_distance, neighbor))

    def dijkstra(self, start):
        self.distance[start] = 0
        self.priority_queue = [(0, start)]

        while self.priority_queue:
            current_distance, current_node = heapq.heappop(self.priority_queue)

            for neighbor, weight in self.graph[current_node]:
                new_distance = current_distance + weight
                self.relax(current_node, neighbor, new_distance)

        return self.distance

def get_shortest_path(graph, start_node):
    dijkstra_obj = DijkstraPriorityQueue(graph) # 인스턴스 생성
    distances = dijkstra_obj.dijkstra(start_node) # Dijkstra 알고리즘을 사용하여 출발 정점에서 각 정점까지의 최단 거리 계산

    for i in range(len(distances)):
        if i != start_node:
            print(f"출발 정점 {start_node}으로부터 도착 정점 {i}까지의 최단거리: {distances[i]}")

if __name__ == "__main__":
    # 그래프의 인접리스트를 미리 정의
    graph = [
        [(1, 2), (2, 4)], # 정점 A - 0 
        [(2, 1)], # 정점 B - 1
        [(0, 4), (3, 7)], # 정점 C - 2
        [(2, 5), (4, 2), (5, 6)], # 정점 D - 3
        [(5, 3)], # 정점 E - 4
        [(3, 6)] # 정점 F - 5
    ]

    start_node = int(input("출발 정점을 입력하세요: "))
    get_shortest_path(graph, start_node)


# In[ ]:




