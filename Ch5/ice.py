# n, m = map(int,input().split())
# data = []
# for i in range(n):
#   row = list(map(int,input().split()))
#   data.append(row)

# print(data)

# 걍 봐도 답을 모르겠다. 일단 답을 확인하자.

# 답안을 확인 후 작성한 코드
n, m = map(int,input().split())
data = []
for i in range(n):
  row = list(map(int,input()))
  data.append(row)

def dfs(x,y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  if data[x][y] == 0:
    data[x][y] = 1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j):
      result += 1

print(result)