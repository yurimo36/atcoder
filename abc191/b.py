# https://atcoder.jp/contests/abc191/tasks/abc191_b

n, x = map(int,input().split())
li = input().split()

ans = ' '.join([n for n in li if n != str(x)])
print(ans)
