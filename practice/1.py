# https://suwaru.tokyo/%E3%80%90%E5%9F%BA%E7%A4%8E%E3%81%AE%E4%B8%80%E8%A6%A7%E3%80%91python%E3%81%AE%E5%9F%BA%E6%9C%AC%E6%96%87%E6%B3%95%E3%82%92%E8%A7%A3%E8%AA%AC%E3%81%97%E3%81%A6%E3%81%BF%E3%81%9F%E3%80%90%E5%88%9D/

'''
    コメントアウト
'''

msg = "Hello World"
print(msg)
print(msg*3)

name = "kumagai"
age = 22
weight = 62.1
print("name:%s,age:%d,weight:%f" % (name, age, weight))
print("name:%5s,age:%5d,weight:%5.2f" % (name, age, weight))
print("name:{0:5s},age:{1:5d},weight:{2:5.2f}".format(name, age, weight))

s = "string"

for char in s:
    print(char)

for index, char in enumerate(s):
    print(index, char)

if "123".isdigit():
    print("この文字列は数字です")

A = True
B = True
if not A:
    print(A)
elif not(A and B):
    print("NAND")
elif A or B:
    print("or")
'''
score = int(input("score?"))
print(score)
'''

for i in range(10):
    if i == 5:
        continue
    print(i)
else:  # 終了時出力
    print("end")

Name = ["sato", "yamada", "suzuki"]
for name in Name:
    print(name)
NameAge = [["sato", 20], ["yamada", 23]]
for name, age in NameAge:
    print(name, age)
