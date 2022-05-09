graph={'A':['B','C','D'],'B':['E'],'C':['D','E'],'D':[],'E':[]}
visited=set()
def dfs(graph,visited,root):
    if root not in visited:
        print(root,end=" ")
        visited.add(root)
        for neighbour in graph[root]:
            dfs(graph,visited,neighbour)
dfs(graph,visited,'A')