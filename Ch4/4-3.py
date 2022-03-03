# 15m

# 나이트의 위치 입력받기
x, y = list(input())

# 리스트 인덱스로 입력값 치환
zx = ord(x)-ord('a')
zy = int(y) - 1

# 나이트가 이동할 수 있는 움직임
dx = [-2,-2,2,2,-1,1,-1,1]
dy = [-1,1,-1,1,-2,-2,2,2]

# 이동 가능한 경우의 수
count = 0

for i in range(len(dx)):
  nx = zx + dx[i]
  ny = zy + dy[i]
  if nx < 0 or ny < 0 or nx > 7 or ny > 7:
    continue
  count += 1

print(count)
  


