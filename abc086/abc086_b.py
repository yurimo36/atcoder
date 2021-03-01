# https://atcoder.jp/contests/abc086/tasks/abc086_b

li = input().split()
x = int(li[0]+li[1])

def try_square_root_naive(n):
    m = int(n**.5)
    return True if abs(m*m - n) < 1e-6 else None

if try_square_root_naive(x):
  print("Yes")
else:
  print("No")