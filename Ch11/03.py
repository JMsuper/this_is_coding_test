# 0이거나 1인지와는 상관없이 연속된 그룹이 몇번 존재하는지가 중요하다.
# 몇 번 바뀌는지를 기준으로 아래 숫자가 나온다.
# 1,2   3,4   5,6    
# 위에 숫자들에 +1 한 것에 대해 2로 나눈 몫이 최소 횟수이다.

data = list(map(int,list(input())))

result = 0 # 최소 뒤집는 횟수
count = 0 # 연속되는 숫자가 변하는 경우의 횟수
current_num = -1 # 연속되는 그룹의 현재 숫자

for i in data:
  if current_num != i:
    current_num = i
    count += 1

# 0, 1에 상관없이 적은 뒤집기 횟수를 선택할 것이다.
result = count // 2 
print(result)