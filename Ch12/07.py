# 5m
n = list(map(int,list(input())))
bisector = len(n) // 2
left_sum = sum(n[:bisector])
right_sum = sum(n[bisector:])
if(left_sum == right_sum):
  print("LUCKY")
else:
  print("READY")
