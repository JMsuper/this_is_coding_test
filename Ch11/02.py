# 0이면 무조건 +. * 이면 값이 0이 되어버린다ㅠ
# 1이면 무조건 +. * 해서 그대로인 것보다 1 더하는게 낫다.

# 아니면 애초에 계속 결과값을 가지고 있는 상태에서 더하는 것과 곱하는 것을
# 비교하여 더 큰 값을 값는 쪽으로 진행하면 되지 않을까?

data = list(map(int,list(input())))

result = 0
for i in data:
  add_result = result + i
  mul_result = result * i
  if add_result >= mul_result:
    result += i
  else:
    result *= i

print(result)
