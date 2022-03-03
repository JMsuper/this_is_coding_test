# 100m

def check_correct(expanded_lock,lock_len):
  for i in range(lock_len):
    for j in range(lock_len):
      if expanded_lock[lock_len + i][lock_len + j] != 1:
        return False
  return True

def sum_key_lock(key,expanded_lock,x,y):
  key_len = len(key)
  for i in range(key_len):
    for j in range(key_len):
      expanded_lock[x + i][y + j] += key[i][j]

def rotate90(key):
  len_key = len(key)
  rotated_key = [[0 for _ in range(len_key)] for _ in range(len_key)]
  for i in range(len_key):
    for j in range(len_key):
      rotated_key[j][len_key-1-i] = key[i][j]
  return rotated_key
  
def solution(key, lock):
  # key를 움직여 만들수 있는 모든 경우의 수를 계산해야한다.
  # 계산이후 각각의 경우를 lock과 합쳤을 때 배열의 모든 원소가 1이여야 한다.

  # key와 lock을 더하여 모든 원소가 1인지 확인하는 것은 시간이 오래 걸릴 것 같다.
  # 먼저 lock에서 0이 있는 부분들의 위치 정보를 구하고,
  # key에서 위 위치 정보에 해당하는 부분만 1인지 확인한다.

  # 회전해서 나올 수 있는 건 0도, 90도, 180도, 270도 이니까
  # 총 4가지 경우
  # key의 주변에 추가적인 공간을 만들어 일일이 확인한다.

  # 확장된 lock 생성
  lock_len = len(lock)
  expanded_lock = [[0 for _ in range(lock_len * 3)] for _ in range(lock_len * 3)]
  for i in range(lock_len):
    for j in range(lock_len):
      expanded_lock[lock_len + i][lock_len + j] = lock[i][j]

  for _ in range(4):
    key = rotate90(key)
    print(key)
    check_iter_num = lock_len * 3 - len(key)
    for i in range(check_iter_num):
      for j in range(check_iter_num):
        copy_expanded_lock = []
        for row in expanded_lock:
          copy_expanded_lock.append(row[:])
        sum_key_lock(key,copy_expanded_lock, i, j)
        if check_correct(copy_expanded_lock, lock_len):
          print(copy_expanded_lock)
          return True
      
  return False
  

key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]
print(solution(key, lock))