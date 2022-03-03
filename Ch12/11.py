# 40m
n = int(input())
k = int(input())
apple_list = []
for _ in range(k):
  (x, y) = input().split()
  apple_list.append((int(x),int(y)))

move_list = []
l = int(input())
for _ in range(l):
  time, d = input().split()
  move_list.append((int(time),d))

# 1 : 벽
# 2 : 사과
# 3 : 뱀
# 0 : 빈 공간
board = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
for i in range(n + 2):
  board[0][i] = 1
  board[i][0] = 1
  board[n+1][i] = 1
  board[i][n+1] = 1

for apple in apple_list:
  board[apple[0]][apple[1]] = 2

x, y = 1, 1
board[x][y] = 3
direction = 2 # L(0) U(1) R(2) D(3)
dx = [0,-1,0,1]
dy = [-1,0,1,0]
count = 0
index = 0
move_path = [(x,y)]

while True:
  count += 1
  x += dx[direction]
  y += dy[direction]
  move_path.append((x,y))
  print(move_path)
  new_loc = board[x][y]
  if new_loc == 1 or new_loc == 3:
    isBreak = True
    break
  board[x][y] = 3
  if new_loc != 2:
    nx, ny = move_path.pop(0)
    board[nx][ny] = 0

  if index < l and count == move_list[index][0]:
    if move_list[index][1] == 'L':
      direction = ((4 + direction) - 1) % 4
    else:
      direction = ((4 + direction) + 1) % 4
    index += 1

print(board)
print(count)

# 틀렸던 이유
# 문제를 제대로 읽지 않았다. 이동 정보에 있는 시간이, 0부터 시작한 시간인 줄 알았는데
# 게임이 시작하고 나서 누적된 시간을 의미하는 것이였다.