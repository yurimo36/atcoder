# https://atcoder.jp/contests/cf17-final/tasks/cf17_final_a

s = input()
#AKIHABARAからAを抜いた文字列ならOK
#全抜き、1個抜き、2個抜き、3個抜き、そのまま
if s == "KIHBR" or s == "KIHABARA" or s == "AKIHBARA" or s == "AKIHABRA" or s == "AKIHABAR" or \
    s == "AKIHABARA" or s == "AKIHBR" or s == "KIHABR" or s == "KIHBAR" or s == "KIHBRA" or \
        s == "AKIHABR" or s == "AKIHBAR" or s == "AKIHBRA" or s == "KIHABAR" or s == "KIHABRA" or s == "KIHBARA":
        print("YES")
else:
    print("NO")