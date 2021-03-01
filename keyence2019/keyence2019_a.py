# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_a

li = list(map(int,input().split()))

if li.count(1) == 1 and li.count(9) == 1 and li.count(7) == 1 and li.count(4) == 1:
    print("YES")
else:
    print("NO")