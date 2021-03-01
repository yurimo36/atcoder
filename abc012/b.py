# https://atcoder.jp/contests/abc012/tasks/abc012_2

n = int(input())

h = int(n/3600)
m = int((n-h*3600)/60)
s = n-h*3600-m*60

if h<10:
  h = "0"+str(h)
if m<10:
  m = "0"+str(m)
if s<10:
  s = "0"+str(s)
  
print(str(h)+":"+str(m)+":"+str(s))