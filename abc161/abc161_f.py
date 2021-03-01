# https://atcoder.jp/contests/abc161/tasks/abc161_f

n = int(input())

def make_divisors(n): #約数を列挙する関数
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    divisors.remove(1)
    return divisors

ans = make_divisors(n-1) #n-1の約数(1以外)を列挙し、それらは対象になる
y = make_divisors(n) #nの約数を列挙

for i in y:
    z = n
    while z >= i and z%i == 0: #割り切れるところまで割る(nがi以上のとき)
        z = int(z / i)
        if z % i == 1: #z(=余り)が1だったら
            ans.append(i)
            break

set(ans)
#print(ans)
print(len(ans))