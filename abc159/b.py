# https://atcoder.jp/contests/abc159/tasks/abc159_b

s = input()
n = len(s)
ans=""
 
half = s[:int((n-1)/2)]
 
if s==s[::-1] and half==half[::-1]:
	ans = "Yes"
else:
	ans = "No"
  
print(ans)

