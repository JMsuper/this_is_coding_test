# 잘 모르겠다. 해설을 확인하자
# 이 문제 풀이의 아이디어는 적절한 높이를 찾을 때까지 절단기의 높이 H를
# 반복해서 조정하는 것이다.
# 힌트를 얻은 후에 작성한 코드
# 21m 10s

def cut_and_sum(dduck_list,h):
  result = 0
  for dduck in dduck_list:
    remain_dduck = dduck - h
    if remain_dduck > 0:
      result += remain_dduck
  return result

def binary_search(dduck_list,target,start,end):
  result = 0

  while start <= end:
    h = (start + end) // 2
    h_dduck_sum = cut_and_sum(dduck_list, h)
    if h_dduck_sum == target:
      return h
    elif h_dduck_sum > target:
      result = h
      start = h + 1
    else:
      end = h - 1
  return result

n, m = map(int,input().split())
dduck_list = list(map(int,input().split()))
dduck_list.sort()

result = binary_search(dduck_list,m,0,dduck_list[-1])
print(result)
              