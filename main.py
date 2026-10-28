import time

print("倒计时开始！")
for i in range(10, 0, -1):
    print(f"倒计时：{i}")
    time.sleep(1)
print("⏰时间到！")
