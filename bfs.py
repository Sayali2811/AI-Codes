import collections
def bfs(graph,root):
    visited=set()
    queue=collections.deque([root])
    while queue:
        vertex=queue.popleft()
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
    print("BFS search : ",visited)
graph={1:[3,2,4],2:[1,4],3:[1,6],4:[2,1,5],5:[4],6:[3]}
bfs(graph,1)