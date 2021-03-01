# https://atcoder.jp/contests/abc094/tasks/arc095_a

import statistics

n = int(input())
li = list(map(int,input().split()))
median_low = statistics.median_low(li)
median_high = statistics.median_high(li)

for i in li:
    if i <= median_low:
        print(median_high)
    else:
        print(median_low)