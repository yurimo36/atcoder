# https://atcoder.jp/contests/abc182/tasks/abc182_b

import collections

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

n = int(input())
a = list(map(int,input().split()))
li = []

for i in a:
    li += make_divisors(i)

c = collections.Counter(li)
print(c.most_common()[1][0])
