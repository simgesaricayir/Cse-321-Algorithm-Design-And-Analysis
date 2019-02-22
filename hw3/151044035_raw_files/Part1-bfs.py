import pandas as pd
from pandas import ExcelFile


def bfs(graph, root,visited=[]):
    queue = [root]
    while queue:
        vertex = queue.pop(0)
        for w in graph[vertex]:
            if w not in visited:
                visited.append(w)
                queue.append(w)

df = pd.read_excel('Graph_data.XLS')
graph = []

for i in range (3,19):
    graph.append([])

graph[df['Root vertex'][3]].append(df[1][2])
for i in range (3,19):
    x =df['Root vertex'][i]
    graph[x].append(df[1][i])
visited = []
bfs(graph,1,visited)
print(visited) 


    


