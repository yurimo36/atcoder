# https://atcoder.jp/contests/abc201/tasks/abc201_b

n = int(input())
st = [input().split() for i in range(n)]

st2 = sorted(st, key=lambda x: int(x[1]), reverse=True)
print(st2[1][0])
