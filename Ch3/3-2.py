n, m, k = map(int,input().split())
array = list(map(int,input().split()))
result = 0

# 가장 큰 수가 있는 인덱스를 알아야 한다.
# 그 다음으로 큰 수가 있는 인덱스를 알아야 한다.

first_max = max(array)
del array[array.index(first_max)]
second_max = max(array)
repeat_count = 0

for _ in range(m):
  if repeat_count < k:
    result += first_max
  else:
    result += second_max
    repeat_count = 0
  repeat_count += 1

print(result)