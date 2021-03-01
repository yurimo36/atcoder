# https://atcoder.jp/contests/abc082/tasks/abc082_b

s = ''.join(sorted(input()))
t = ''.join(sorted(input(), reverse=True))

if s < t:
    print("Yes")
else:
    print("No")