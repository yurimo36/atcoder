# https://atcoder.jp/contests/abc149/tasks/abc149_c

import math

x = int(input())
y = 0

if x==2: #2だけは例外
  print(2)
  
else: #xの素数判定
  while y == 0: #素数でない間は続ける
    for k in range(2, int(math.sqrt(x)) + 1): #2以上ルートn以下で割り切れるか調べる
      if x % k == 0: #もし割り切れたら、
        x = x + 1 #素数ではないので、xを+1して、
        break #for文を抜けてwhileに戻る
      if k == int(math.sqrt(x)):
        y = 1
  print(x)