# # 맵 정보 입력받기
# n, m = map(int,input().split())
# # 캐릭터의 위치, 방향 정보 입력받기
# x, y, d = map(int,input().split())

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# game_map = []
# for i in range(n):
#   row = list(map(int,input().split()))
#   game_map.append(row)

# count = 0 # 움직인 횟수

# # 매 반복마다 아래 조건문을 확인하는 것은 낭비이다. 답안 코드처럼 회전이 4번 이뤄졌을 때
# # 조건문을 수행하여야 한다.
# while True:
#   if (game_map[x + dx[0]][y + dy[0]] != 0 and
#     game_map[x + dx[1]][y + dy[1]] != 0 and
#     game_map[x + dx[2]][y + dy[2]] != 0 and
#     game_map[x + dx[3]][y + dy[3]] != 0):
#       if game_map[x + dx[(d+2) % 4]][y + dy[(d+2) % 4]] != 2:
#         break
#       else:
#         x = x + dx[(d+2) % 4]
#         y = y + dy[(d+2) % 4]
        
#   d = (d + 3) % 4
#   if game_map[x + dx[d]][y + dy[d]] == 0:
#     x = x + dx[d]
#     y = y + dy[d]
#     game_map[x][y] = 2
#     count += 1
#   else:
#     continue
# print(game_map)
# print(count)


# 답안 코드 확인 후 작성한 코드

# 맵 정보 입력받기
n, m = map(int,input().split())
# 캐릭터의 위치, 방향 정보 입력받기
x, y, d = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

game_map = []
for i in range(n):
  row = list(map(int,input().split()))
  game_map.append(row)

count = 0 # 움직인 횟수

def turn_left():
  global d
  d = (d + 3) % 4

turn_count = 0

while True:
  turn_left()
  nx = x + dx[d]
  ny = y + dy[d]
  if game_map[nx][ny] == 0:
    game_map[nx][ny] = 2
    x = nx
    y = ny
    count += 1
    turn_count = 0
  else:
    turn_count += 1
  if turn_count == 4:
    nx = x - dx[d]
    ny = y - dy[d]
    if game_map[nx][ny] != 1:
      x = nx
      y = ny
      turn_count = 0
    else:
      break

print(count)
  
    