# 내가 구현한 이진 탐색(재귀함수)
def binary_search(array,target,start,end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array,target,start,mid-1)
  else:
    return binary_search(array,target,mid+1,end)

print("원소의 개수와 target 입력")
n, target = map(int,input().split())
print("배열 입력")
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result == None:
  print("원소를 찾을 수 없습니다.")
else:
  print(result+1)