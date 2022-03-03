# # 55m (실패)
# # state : 0(None), 1(바닥), 2(기둥), 3(보), 4(기둥+보), 5(보+보), 6(기둥+기둥)

# def isOK_pillar(x,y,wall):
#   wall_len = len(wall)
#   state = wall[wall_len-y][x]
#   if state == 1 or state == 2 or state == 3:
#     return True
#   else:
#     return False

# def isOK_paper(x,y,wall):
#   wall_len = len(wall)
#   state = wall[wall_len-y][x]
#   state_right = wall[wall_len-y][x+1]
#   if (state == 3 and state_length == 3) or state == 2 or state_right == 2:
#     return True
#   else:
#     return False

# def establish_pillar(x,y,wall):
#   state = wall[wall_len-y][x]
#   state_up = wall[wall_len-y-1][x]
#   if state == 1:
#     wall[wall_len-y][x] = 2
#   elif state == 2:
#     wall[wall_len-y][x] = 6
#   elif state == 3:
#     wall[wall_len-y][x] = 4
    
#   if state_up == 3:
#     wall[wall_len-y-1][x] = 4
#   elif state_up == 0:
#     wall[wall_len-y-1][x] = 2

# def establish_paper(x,y,wall):
#   state = wall[wall_len-y][x]
#   state_right = wall[wall_len-y][x+1]
#   if state == 2:
#     wall[wall_len-y][x] = 4
#   elif state == 3:
#     wall[wall_len-y][x] = 5
#   elif state == 0:
#     wall[wall_len-y][x] = 3

#   if state_right == 2:
#     wall[wall_len-y][x+1] = 4
#   elif state_right == 3:
#     wall[wall_len-y][x+1] = 5
#   elif state == 0:
#     wall[wall_len-y][x+1] = 3

# def solution(n, build_frame):
#   result = []
#   wall = [[0] * (n+1) for _ in range(n+1)]

#   # build_frame에서 하나씩 꺼낸다.
#   for plan in build_frame:
#     x, y, a, b = plan
#     if b == 1:
#       if a == 0:
#         if isOK_pillar(x,y,wall):
#           establish_pillar(x,y,wall)
#           result.append([x,y,a])
#         else:
#           continue
#       else:
#         if isOK_paper(x,y,wall):
#           establish_paper(x,y,wall)
#           result.append([x,y,a])
#         else:
#           continue
#     else:
#       if a == 0:
        
#       else:
      

# 실패요인
# 파라미터로 주어진 값들을 활용하지 않고 직접 2차원 배열을 선언한 후에
# 해당 2차원 배열을 이용하여 값을 확인하고자 하였다.
# 그러나 이렇게 하는 방법은 오히려 문제를 복잡하게 만들었다.
# 굳이 배열에 새롭게 지어진 건출물을 나타낼 필요없이,
# result 배열에 새롭게 지어진 건축물을 넣어서 해당 배열을 이용하여 규칙을 확인하는 것이
# 더 효율적이고 편리한 방법이다.

# 답안 코드 확인 후 작성한 코드

# 현재 설치된 구조물들이 규칙에 부합하는지 확인하는 코드
def possible(answer):
  for x,y,stuff in answer:
    if stuff == 0: # 기둥일 경우
      # '바닥 위에 있을 경우' 또는 '보의 한쪽 끝부분 위에 있을 경우' 또는 '다른 기둥 위에 있을 경우'  
      if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
        continue
      else:
        return False
    else: # 보일 경우
      # '한쪽 끝부분이 기둥 위에 있는 경우' 또는 '양쪽 끝부분이 다른 보와 연결'
      if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
        continue
      else:
        return False
  return True

def solution(n, build_frame):
  answer = []
  for x,y,stuff,operation in build_frame:
    if operation == 0: # 삭제일 경우
      answer.remove([x,y,stuff])
      if not possible(answer):
        answer.append([x,y,stuff])
    elif operation == 1: # 설치일 경우
      answer.append([x,y,stuff])
      if not possible(answer):
        answer.remove([x,y,stuff])
  return sorted(answer)