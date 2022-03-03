# 아이디어가 도저히 떠오르지 않는다.
# 벽을 세울 수 있는 경우들을 모두 구한 뒤
# 경우들을 조합하여 감염되지 않는 곳이 가장 많은 경우를 채택하면
# 된다. 그런데 그 경우들을 어떻게 구하지?
# n, m = map(int,input().split())

# data = []
# for i in range(n):
#   data.append(list(map(int,input().split())))

# 책의 설명을 보고 난 후 작성한 코드
# 벽을 세울 수 있는 모든 경우의 수를 계산해야 한다.
# 파이썬의 조합 라이브러리를 통해 계산할 수 있다.
# 그러면 일단 다음의 과정을 수행해야 할 것이다.
# 1. 벽을 세울 수 있는 좌표를 리스트에 넣는다.
# 2. 조합 라이브러리를 활용하여 조합의 경우를 구한다.
from itertools import combinations
from collections import deque

n, m = map(int,input().split())

input_map = []
for _ in range(n):
  input_map.append(list(map(int,input().split())))

establish_xy = []
virus_xy = []
for i in range(n):
  for j in range(m):
    if input_map[i][j] == 0:
      establish_xy.append((i,j))
    if input_map[i][j] == 2:
      virus_xy.append((i,j))

combination_list = list(combinations(establish_xy,3))

# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs_virus(wall_loc_list):
  infected_map = []
  for i in range(n):
    infected_map.append(input_map[i][:])
  for x, y in wall_loc_list:
    infected_map[x][y] = 1
  
  queue = deque()
  for virus in virus_xy:
    queue.append(virus)
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if infected_map[nx][ny] == 0:
        infected_map[nx][ny] = 2
        queue.append((nx, ny))
  return infected_map
  

def check_0(data):
  result = 0
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        result += 1
  return result

maximum = 0

for wall_loc_list in combination_list:
  infected_map = bfs_virus(wall_loc_list)
  result = check_0(infected_map)
  maximum = max(result,maximum)

print(maximum)
    