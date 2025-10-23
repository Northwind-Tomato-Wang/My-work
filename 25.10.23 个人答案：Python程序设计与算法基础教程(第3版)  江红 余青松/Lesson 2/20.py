# 使用循环结构，使用turtle.right和turtle.fd函数绘制菱形四边形
import turtle

# 设置窗口和画笔属性
screen = turtle.Screen()
screen.title("菱形四边形绘制")
turtle.speed(1)  # 设置绘制速度

def draw_diamond(side_length):
    """使用循环结构绘制边长为side_length的菱形四边形"""
    # 菱形的内角为60度和120度交替
    # 外角为120度和60度交替
    angles = [120, 60, 120, 60]  # 外角列表
    
    print(f"开始绘制边长为{side_length}像素的菱形四边形...")
    
    # 使用循环结构绘制四条边
    for i in range(4):
        turtle.fd(side_length)  # 向前移动side_length像素
        turtle.right(angles[i])  # 向右转对应角度
        print(f"已绘制第{i+1}条边，转向角度：{angles[i]}度")
    
    print("菱形四边形绘制完成！")

# 绘制边长为200像素的菱形四边形
draw_diamond(200)

# 保持窗口显示，点击关闭
screen.mainloop()