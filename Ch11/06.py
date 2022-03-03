# 40m11s
# 잘못풀었음. 몇 번 음식인지가 변하면 안된다.
def solution(food_times, k):
    answer = 0
    
    while k // len(food_times) != 0 or len(food_times) == 0:
        k -= len(food_times)
        food_times = list(map(lambda x: x-1,food_times))
        
        isZero(food_times)
    
    if k == 0:
        answer = 1
        
    for i in range(k):
        food_times[i] -= 1
        if food_times[i] == 0:
            del food_times[i]
        if i == k-1:
            answer = i + 1
        
    if len(food_times) == 0:
        answer = -1
        
    return answer

def isZero(food_times):
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