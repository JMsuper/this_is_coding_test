# n = int(input())
# data = list(map(int,input().split()))
# data.sort()

# result = 0 # 선택된 동전들의 조합의 합
# current_value = 1

# # 누적합을 고려해야 한다.
# # 만약 1~target-1까지 동전들의 조합으로 만들 수 있는 경우라는 것을
# # 가정한다.  

# while True:


# 학습 이후 코드
n = int(input())
data = list(map(int,input().split()))
data.sort()

target = 1

for x in data:
  if target < x:
    break
  target += x

print(target-1)