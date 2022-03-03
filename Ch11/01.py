# 모험가 길드 p.311
n = int(input())
data = list(map(int,input().split()))

# 공포도 순을 정렬
# 가장 작은 공포도를 가진 사람을 기준으로 그룹을 만든다.
# 공포도가 작은 사람들을 우선으로 집어넣는다.

data.sort()

result = 0

threat = 0
mem_num = 0
for i in range(n):
  if threat < data[i]:
    threat = data[i]
  mem_num += 1
  if threat <= mem_num:
    result += 1
    threat = 0
    mem_num = 0

print(result)

# threat 변수를 사용할 필요가 없다. 답안 코드처럼 data에 담긴 데이터
# 자체가 공포도를 나타내므로, 반복문을 수행하며 range(n)이 아닌
# data 리스트에 대해 요소들을 꺼내오면 공포도를 즉각 가져올 수 있다.
# 이 경우 threat에 대해서 처리하는 코드를 줄일 수 있다.

# n = int(input())
# data = list(map(int,input().split()))
# data.sort()

# result = 0
# count = 0

# for i in data:
#   count += 1
#   if i <= count:
#     result += 1
#     count = 0

# print(result)