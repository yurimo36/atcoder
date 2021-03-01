# https://atcoder.jp/contests/abc173/tasks/abc173_b

n = int(input())
li = [input() for i in range(n)]

print("AC x " + str(li.count("AC"))) 
print("WA x " + str(li.count("WA"))) 
print("TLE x " + str(li.count("TLE"))) 
print("RE x " + str(li.count("RE"))) 