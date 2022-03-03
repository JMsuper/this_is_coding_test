n = int(input())

count = 0

for h in range(n+1):
  for m in range(60):
    for s in range(60):
      if s % 10 == 3 or s // 10 == 3 or m % 10 == 3 or m // 10 == 3 or h % 10 == 3:
        count += 1

print(count)

# 나는 3을 포함하는지 확인하기 위해 연산을 수행했지만, 답안 코드의 경우 문자열로 바뀐 뒤에
# in 을 사용하여 3을 포함하는지 확인하였다. 훨씬 효율적인 코드라고 생각한다.
# 내 코드는 일일이 연산을 수행해야 하는데 문자열로 바꿀 경우 굳이 연산을 수행하지 않아도 된다.