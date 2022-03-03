# 잘못 푼 코드
import math

n, k = map(int,input().split())
count = 0

count += n % k
count += int(math.log((n-count),k))

print(count)
