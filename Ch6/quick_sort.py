array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
  if start >= end: # 원소가 1인 경우 종료
    return
  pivot = start # 피벗은 첫 원소
  left = start + 1
  right = end
  while left <= right:
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1
    # 피벗보다 작은 데이터를 찾을 때까지 반복
    while right > start and array[right] >= array[pivot]:
      right -= 1
    # 엇갈렸다면 작은 데이터와 피벗을 교체
    # 엇갈렸다는 것은 피벗이 들어갈 자리를 찾았다는 의미로 해석하자
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
      array[left], array[right] = array[right], array[left]
  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  # 이때 right의 위치는 피벗이 존재하는 인덱스의 +1을 한 것이다.
  quick_sort(array, start, right - 1)
  quick_sort(array, right+1, end)
      
quick_sort(array, 0, len(array) - 1)
print(array)
  
