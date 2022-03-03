# 백준 18325번
from collections import deque

n, m, k, x = map(int,input().split())
# bfs를 사용해야 한다.
# 간선의 수가 정점의 수보다 많을 수 있기 때문에 연결리스트를 사용한다.
load_info = [[] for _ in range(n+1)]
INF = int(1e9)
for _ in range(m):
  edge = list(map(int,input().split()))
  load_info[edge[0]].append(edge[1])

def bfs(start):
  queue = deque([start])
  # 0 : start 지점. INF : 방문하지 않은 정점. not INF : 방문한 정점
  distance = [INF] * (n+1)
  distance[start] = 0
  while queue:
    v = queue.popleft()
    curr_distance = distance[v]
    if curr_distance > k:
      break
    for i in load_info[v]:
      if distance[i] == INF:
        should_distance_up = True
        distance[i] = curr_distance + 1 
        queue.append(i)

  result = []
  for i in range(n+1):
    if distance[i] == k:
      result.append(i)
  if not result:
    print(-1)
  else:
    for i in result:
      print(i)

bfs(x)