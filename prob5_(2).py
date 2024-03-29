#!/usr/bin/env python
# coding: utf-8

# In[20]:


class BellmanFord:
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.vertices = set()
        self.distance = {}
        self.predecessor = {}

    def initialize(self):
        for vertex in self.graph: # 그래프의 정점들 초기화
            self.vertices.add(vertex)
            self.distance[vertex] = float('infinity')
            self.predecessor[vertex] = None
            
        self.distance[self.start] = 0 # 시작정점의 거리 0으로 설정

    def relax(self, u, v, weight): # Relaxation 과정 수행
        if self.distance[u] + weight < self.distance[v]:
            self.distance[v] = self.distance[u] + weight
            self.predecessor[v] = u
    
    def bellman_ford(self):
        self.initialize() # 초기화

        # relaxation을 |V|-1 수행
        for _ in range(len(self.vertices) - 1):
            for u in self.graph:
                if u in self.graph:
                    for v, weight in self.graph[u].items():
                        self.relax(u, v, weight)
                
        # 음의 사이클 검사
        for u in self.graph:
            if u in self.graph:
                for v, weight in self.graph[u].items():
                    if self.distance[u] + weight < self.distance[v]:
                        return "음의 사이클이 존재합니다."
                                          
        return self.distance, self.predecessor

# 입력 처리 함수
def process_input():
    V, E = map(int, input().split()) # 정점 수와 간선 수 입력
    graph = {}
    
    for _ in range(E): # 간선 정보 입력
        u, v, w = map(int, input().split())
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = w

    return graph, V

if __name__ == "__main__":
    # 입력 처리
    graph, V = process_input()
    start_vertex = int(input("시작 정점을 입력하세요: "))

    # Bellman-Ford 실행
    bellman_ford_instance = BellmanFord(graph, start_vertex)
    result = bellman_ford_instance.bellman_ford()

    # 결과 출력
    if type(result) == str:  # 결과 출력
        print()
        print(result)
    else: # 최단 거리 출력
        print("Shortest distances from source({}):".format(start_vertex))
        for vertex in sorted(result[0]):
            print(result[0][vertex], end=" ")
        print("\nShortest paths:")
        for vertex in sorted(result[1]): # 최단 경로 출력
            path = []
            current_vertex = vertex
            while current_vertex is not None:
                path.insert(0, str(current_vertex))
                current_vertex = result[1][current_vertex]
            print("{} -> {} : {}".format(start_vertex, vertex, " -> ".join(path)))


# In[ ]:




