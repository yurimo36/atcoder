# https://atcoder.jp/contests/abc134/tasks/abc134_c

import heapq

n = int(input())
a = [int(input()) for i in range(n)]
b = heapq.nlargest(2, set(a))
c = a.count(b[0])

if len(b) == 1 or c > 1: #bの長さが1または、最大値が2回以上存在するなら
    for i in range(n):
        print(b[0]) #最大値のみを表示

else: #bの長さが2以上なら
    for i in range(n):
        if a[i] == b[0]: #i番目が最大値だったら
            print(b[1]) #2番目に大きい値を出力
        else: #そうでなければ
            print(b[0]) #最大値を出力