n, m = map(int,input().split())
data = []

for _ in range(n):
  data.append(list(map(int,input().split())))

# 먼저, 첫번째 행에서 가장 작은 숫자가 무엇인지 찾는다
# 다음 행에서 가장 작은 숫자가 기존의 가장 작은 숫자보다 크다면 change한다.
result = 0
for i in range(n):
  minimum = min(data[i])
  if(result < minimum):
    result = minimum

print(result)
