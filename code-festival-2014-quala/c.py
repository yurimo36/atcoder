# https://atcoder.jp/contests/code-festival-2014-quala/tasks/code_festival_qualA_c

a, b = map(int,input().split())
ans = b//4 - b//100 + b//400 - ((a-1)//4 - (a-1)//100 + (a-1)//400)
print(ans)