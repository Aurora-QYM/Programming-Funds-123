import random

print("===== 猜数字小游戏 =====")
secret_num = random.randint(1, 100)  # 随机生成1~100的数字
count = 0

while True:
    try:
        guess = int(input("请输入你猜的数字（1-100）："))
        count += 1

        if guess < secret_num:
            print("太小啦！再试试")
        elif guess > secret_num:
            print("太大啦！再试试")
        else:
            print(f"🎉恭喜你猜对了！答案就是{secret_num}")
            print(f"你一共猜了 {count} 次")
            break
    except ValueError:
        print("❌输入错误！请输入整数！")
