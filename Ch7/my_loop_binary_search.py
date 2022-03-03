# 내가 구현한 이진 탐색(반복문)
def binary_search(array,target,start,end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

print("원소의 개수와 target 입력")
n, target = map(int,input().split())
print("배열 입력")
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result == None:
  print("원소를 찾을 수 없습니다.")
else:
  print(result+1)