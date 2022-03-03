# 재시도 코드

# 0인 것을 확인하지 않고 그냥 먹어야 되는 그릇의 번호를 담은 리스트를 따로 둘까?


def solution(food_times, k):
    answer = 0

    # 0인 것을 확인하지 않기 위해 음식 번호를 담은 리스트를 사용
    food_num_list = list(range(1,len(food_times)+1))

    while k // len(food_num_list) != 0 or len(food_num_list) == 0:
      k -= len(food_times)
      food_times = list(map(lambda x: x-1,food_times))
      isZero(food_times,food_num_list)
    
  
    return answer

def isZero(food_times,food_num_list):
    length = len(food_times)
    i = 0
    while i < length:
        if food_times[i] == 0:
            del food_times[i]
            length -= 1
            i -= 1
        i += 1

food_times = list(map(int,input().split()))
k = int(input())

print(solution(food_times,k))