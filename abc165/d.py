# https://atcoder.jp/contests/abc165/tasks/abc165_d

a, b, n = map(int,input().split())
 
print(int(a*min(b-1, n)/b) - a*int(min(b-1, n)/b))