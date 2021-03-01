# https://atcoder.jp/contests/arc019/tasks/arc019_1

s = input()
ans = s.replace("O", "0").replace("D", "0").replace("I", "1").replace("Z", "2").replace("S", "5").replace("B", "8")
print(ans)