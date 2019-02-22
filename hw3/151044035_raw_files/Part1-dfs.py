import pandas as pd
from pandas import ExcelFile

def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)

    return path

df = pd.read_excel('Graph_data.XLS')
graph = []
path=[]

for i in range (3,19):
    graph.append([])

graph[df['Root vertex'][3]].append(df[1][2])
for i in range (3,19):
    x =df['Root vertex'][i]
    graph[x].append(df[1][i])

dfs_recursive(graph,1,path)
print(path) 

    

