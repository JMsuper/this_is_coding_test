# 5m
n = int(input())
data = []
for i in range(n):
  name, score = input().split()
  data.append((name,int(score)))

data.sort(key = lambda x : x[1])
for x in data:
  print(x[0], end=" ")