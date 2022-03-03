# 2h 30m
# def solution(s):
#   # 문자열의 길이의 절반이 넘는 길이를 기준으로 자르는 것은 무의미하다.
#   # 어차피 절반이 넘는다면 안하는 것과 동일하다.
#   # 따라서 문자열의 길이의 절반인 지점까지만 압축을 수행한다.
  
#   max_len = (len(s) // 2)
#   zip_len_list = []

  
#   for i in range(1,max_len+1):
#     queue = list(s)
#     remain_len = len(queue)
#     zip_str = ""
#     previous_str = ""
#     count = 1
    
#     while remain_len >= i:
#       curr_str = ""
#       for j in range(i):
#         curr_str += queue.pop(0)
#       if previous_str == curr_str:
#         count += 1
#       else:
#         if count == 1:
#           zip_str += previous_str
#         else:
#           zip_str = zip_str + str(count) + previous_str
#         previous_str = curr_str
#         count = 1
#       remain_len -= i

#     if count == 1:
#       zip_str += previous_str
#     else:
#       zip_str = zip_str + str(count) + previous_str
      
#     if len(queue) != 0:
#       zip_str += "".join(queue)
#     print(zip_str)
#     zip_len_list.append(len(zip_str))

#   print(zip_len_list)
#   return min(zip_len_list)

# 답안 코드 학습 이후 새로 작성하는 코드
  
def solution(s):
  answer = len(s)
  for step in range(1,len(s) // 2 + 1):
    prev = s[0:step]
    zip_str = ""
    count = 1
    for j in range(step,len(s),step):
      if prev == s[j:j + step]:
        count += 1
      else:
        zip_str += str(count) + prev if count >= 2 else prev
        count = 1
        prev = s[j:j + step]
    zip_str += str(count) + prev if count >= 2 else prev
    answer = min(answer,len(zip_str))
  return answer

print(solution("ababcdcdababcdcd"))