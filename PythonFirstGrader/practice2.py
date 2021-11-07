import random

def sayHello():
    print("こんにちは")


sayHello()
sayHello()





def omikuji():
    kuji = ['大吉', "中吉", "小吉", "凶"]
    return random.choice(kuji)


print("結果は", omikuji(), "です。")
