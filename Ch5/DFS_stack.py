def DFS(graph,i,visited):
  stack = []
  stack.append(i)
  visited[i] = True
  print(i, end=" ")
  while True:
    if not stack:
      break
    top = stack[-1]
    should_pop = True
    for i in graph[top]:
      if not visited[i]:
        stack.append(i)
        visited[i] = True
        print(i, end=" ")
        should_pop = False
        break
    if should_pop:
      stack.pop()


graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9

DFS(graph,1,visited)