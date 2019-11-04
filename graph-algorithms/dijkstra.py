# def dijkstra(graph):
#     dist = {}
#     pred = {}
#     for u in graph:
#         dist[u] = {}
#         pred[u] = {}
#         for v in graph:
#             dist[u][v] = 1000
#             pred[u][v] = -1
#         dist[u][u] = 0
#         for neighbor in graph[u]:
#             dist[u][neighbor] = graph[u][neighbor]
#             pred[u][neighbor] = u





def main():
    graph = {0: {1: 6, 2: 8},
             1: {4: 11},
             2: {3: 9},
             3: {},
             4: {5: 3},
             5: {2: 7, 3: 4}}
    print(graph[0])
    for u in graph[0]:
        print(u)

if __name__ == "__main__":
    main()
