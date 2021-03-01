# https://atcoder.jp/contests/abc106/tasks/abc106_b

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

n = int(input())
ans = 0

for i in range(1,n+1):
  if len(make_divisors(i)) == 8 and i%2 == 1:
    ans += 1

print(ans)