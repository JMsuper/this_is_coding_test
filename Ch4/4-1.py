# n = int(input())
# data = input().split()

# row = 1
# column = 1

# for x in data:
#   if x == 'L':
#     if column > 1:
#       column -= 1
#   elif x == 'R':
#     if column < n:
#       column += 1
#   elif x == 'U':
#     if row > 1:
#       row -= 1
#   elif x == 'D':
#     if row < n:
#       row += 1

# print(row, column)

# 너무 단순하게 코드를 작성했다. 좀더 코딩스럽게 작성해야 한다. 위 코드는
# 클린하지 못하다. LRUD가 어떤 역할을 수행하는지 명시한 뒤에 이를 확용하는 것이 낫다.
# 위 코드대로 작성한다면 LRUD의 역할이 달라졌을 때 일일이 찾아서 변경해줘야 한다.
# 또한 매 if or elif 문 마다 if 문이 중첩되어 사용되어 가독성이 떨어진다.

# 수정 후

n = int(input())
plans = input().split()

x, y = 1, 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
  index = move_types.index(plan)
  nx = x + dx[index]
  ny = y + dy[index]

  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue

  x, y = nx, ny

print(x, y)
