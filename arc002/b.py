# https://atcoder.jp/contests/arc002/tasks/arc002_2

y, m, d = map(int,input().split("/"))

for i in range(y,3001):
	#閏年判定
	if i%400 == 0:
		x = 1
	elif i%100 == 0:
  		x = 0
	elif i%4 == 0:
  		x = 1
	else:
 		x = 0
	for j in range(1,13):
		if i == y and j < m:
			continue
		for k in range(1,32):
			if i == y and j == m and k < d:
				continue
			if (j == 4 or j == 6 or j == 9 or j == 11) and k > 30:
				continue
			if j == 2:
				if x == 1 and k > 29:
					continue
				elif x == 0 and k > 28:
					continue

			if float(i/j/k).is_integer():
				print(str(i)+"/"+(str(j).rjust(2,'0'))+"/"+(str(k).rjust(2,'0')))
				exit()