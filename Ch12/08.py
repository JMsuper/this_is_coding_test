# # 11m 50s
# s = list(map(ord,list(input())))

# sum = 0
# sorted_list = []
# for x in s:
#   if x < 65:
#     sum += int(chr(x))
#   else:
#     sorted_list.append(x)

# sorted_list.sort()
# sorted_list = list(map(chr,sorted_list))
# sum = str(sum)
# sorted_list.append(sum)
# print("".join(sorted_list))

# 답안 확인 후 새로 작성한 코드

s = input()
sum = 0
sorted_list = []

for x in s:
  if x.isalpha():
    sorted_list.append(x)
  else:
    sum += int(x)

sorted_list.sort()

if sum != 0:
  sorted_list.append(str(sum))

print("".join(sorted_list))