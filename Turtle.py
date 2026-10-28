import turtle

# 设置画笔
t = turtle.Turtle()
t.speed(5)  # 速度 1最慢，10最快，0极速
t.color("blue", "lightblue")

t.begin_fill()
# 画五角星
for _ in range(5):
    t.forward(200)
    t.right(144)
t.end_fill()

turtle.done()  # 保持窗口不关闭
