# 삽입정렬의 시간 복잡도는 O(N^2)이다.
# 그러나 거의 정렬된 배열을 대상으로 동작할 경우,
# O(N)의 시간복잡도를 갖는다. 이 경우 퀵 정렬보다 빠를 수도 있다.
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
  for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
    if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break

print(array)
  