# https://atcoder.jp/contests/abc111/tasks/arc103_a

import collections

n = int(input())
li = list(map(int,input().split()))
x = li[::2]
y = li[1::2]
c = collections.Counter(li)
c0 = collections.Counter(x)
c1 = collections.Counter(y)

if c.most_common()[0][1] == len(li): #1種類だけのリストだったら
    print(n//2)

elif c0.most_common()[0][0] != c1.most_common()[0][0]: #c0に最多ものとc1に最多のものが違うなら
    print(n - c0.most_common()[0][1] - c1.most_common()[0][1])

else:
    if len(c0.keys())==1: #c0が一種類だったら
        print(n//2 - c1.most_common()[1][1]) #c1は2番目に多いものに帰る
    elif len(c1.keys())==1: #c1が一種類だったら
        print(n//2 - c0.most_common()[1][1]) #c0は2番目に多いものに帰る
    elif c0.most_common()[0][1] + c1.most_common()[1][1] < c0.most_common()[1][1] + c1.most_common()[0][1]:
        print(n - c0.most_common()[1][1] - c1.most_common()[0][1])
    else:
        print(n - c0.most_common()[0][1] - c1.most_common()[1][1])