# 15m
# 이진 탐색 문제
# 이진 탐색을 수행하기 위해서는 리스트가 정렬된 상태여야 한다.
import sys

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


n = int(input())
input_data1 = sys.stdin.readline().rstrip()
part_list = list(map(int,input_data1.split()))
part_list.sort()

m = int(input())
input_data2 = sys.stdin.readline().rstrip()
request_list = list(map(int,input_data2.split()))

for request in request_list:
  result = binary_search(part_list,request,0,len(part_list) - 1)
  if result == None:
    print("no", end=" ")
  else:
    print("yes", end=" ")