# 정답 코드를 보고 난 후 다시 작성하는 코드
import heapq

def solution(food_times,k):
  if sum(food_times) <= k:
    return -1
  
  q = []
  for i in range(len(food_times)):
    heapq.heappush(q,(food_times[i],i + 1))

  length = len(food_times)
  sum_times = 0
  previous = 0
  
  while sum_times + (q[0][0] - previous) * length < k:
    now = heapq.heappop(q)[0]
    #sum_times += now * length
    sum_times += (now - previous) * length
    length -= 1
    previous = now

  #remain = k - sum_times
  result = sorted(q, key= lambda x : x[1])
  return result[(k-sum_times) % length][1]