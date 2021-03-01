# https://atcoder.jp/contests/abc057/tasks/abc057_c

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
p = make_divisors(n)
ans = 1000000

for i in range((len(p)+1)//2):
    x = p[i]
    y = p[-1-i]
    z = max(len(str(x)),len(str(y)))
    if z < ans:
        ans = z

print(ans)
