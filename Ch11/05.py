# # 18m27s
# n, m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()

# result = 0

# for i in range(n):
#   if data[i] == m:
#     break
#   for j in range(1,n-i):
#     if data[i] != data[n-j]:
#       result += 1
#     else:
#       break

# print(result)

# 학습 이후 코드
n, m = map(int,input().split())
data = list(map(int,input().split()))

array = [0] * 11

for x in data:
  array[x] += 1

result = 0

for i in range(m):
  n -= array[i]
  result += n * array[i]

print(result)