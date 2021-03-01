# https://atcoder.jp/contests/abc180/tasks/abc180_c

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

n = int(input())
li = make_divisors(n)

for i in li:
    print(i)
