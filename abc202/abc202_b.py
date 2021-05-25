# https://atcoder.jp/contests/abc202/tasks/abc202_b

s = input()

print(s.replace('6','5').replace('9','6').replace('5','9')[::-1])
