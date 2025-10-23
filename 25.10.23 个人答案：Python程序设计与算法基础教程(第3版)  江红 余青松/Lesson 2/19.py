# 使用turtle.fd和turtle.seth绘制等边三角形
import turtle

# 设置画笔速度和窗口标题
turtle.speed(1)  # 设置绘制速度，1-10，数字越大速度越快
window = turtle.Screen()
window.title("等边三角形绘制")

# 绘制边长为200像素的等边三角形
print("开始绘制等边三角形...")

# 第一条边：向前移动200像素
turtle.fd(200)

# 第二条边：设置方向为120度（相对于初始方向旋转120度），然后向前移动200像素
turtle.seth(120)
# turtle.right(120)  # 也可以使用right函数，效果相同
turtle.fd(200)

# 第三条边：设置方向为240度，然后向前移动200像素
turtle.seth(240)
# turtle.right(120)
turtle.fd(200)

# 回到初始方向
turtle.seth(0)

print("等边三角形绘制完成！")

# 保持窗口显示，点击关闭
window.mainloop()