w = "こんにちは" + "\n" + "パイパンです。"
print(len(w))
print(w)
print(w[0])
print(w[-4:])
a = "100"
b = "こんにちは"
print(a.isdigit(), b.isdigit())
if b.isdigit():
    print(int(b)+23)
else:
    print("数値じゃないよう")
lunch = ["おにぎり", "パスタ", "ハンバーガー", "カレー", "定食"]
print(lunch[3])
for i in range(5):
    print(lunch[i])
for i in lunch:
    print(i)
scorelist = [98, 33, 555, 23, 58]
total = 0
for i in scorelist:
    total = total + i
print(total)
for i in range(10):
    for j in range(10):
        print(i, "x", j, "=", i*j)