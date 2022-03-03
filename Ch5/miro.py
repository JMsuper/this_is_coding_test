# 19m 10s (성공)
# 이 문제는 dfs를 사용해야 한다.
# (1,1)에서 (N,M)으로 가는 최단거리를 찾아야 한다.
# N x M 크기의 직사각형이므로 '아래','오른쪽'이 우선되어 움직여야 한다.

n, m = map(int,input().split())
data = []
for i in range(n):
  data.append(list(map(int,input())))

result = 0
cx = 1
cy = 1

def dfs(x,y):
  # global 키워드를 사용하는 이유는
  # 아래에서 'cx = x','result += 1','cy = y'와 같이
  # 값을 변경시키는 코드 때문에 해당 변수들을
  # 함수 외부에 있는 전역변수를 사용하는 것이 아닌
  # 지역변수를 사용하는 것이라고 착각하게 만들기 때문이다.
  # 따라서 전역변수를 사용함을 명시적으로 나타내야 한다.
  global cx, cy, result
  if cx == n and cy == m:
    return
  elif x < 1 or x > n or y < 1 or y > m:
    return
  elif data[x-1][y-1] == 0 or data[x-1][y-1] == 2:
    return
  else:
    result += 1
    cx = x
    cy = y
    data[x-1][y-1] = 2
    print(data)
    print()
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x-1,y)
    
dfs(cx,cy)
print(result)