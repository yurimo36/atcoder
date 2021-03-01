# https://atcoder.jp/contests/abc028/tasks/abc028_a

n = int(input())
 
if n == 100:
  print("Perfect")
elif n >= 90:
  print("Great")
elif n >= 60:
  print("Good")
else:
  print("Bad")