# 10m
n = int(input())
data = []
for i in range(n):
  data.append(int(input()))

data.sort(reverse=True)
for x in data:
  print(x, end=" ")