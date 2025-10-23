from PIL import Image, ImageFilter
import os

# 确保中文显示正常（如果需要在图像上添加中文文字）
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]

# 定义要使用的图像路径
# 你可以修改为你自己的图像路径，或者在运行时让用户输入
image_path = "example.jpg"

# 检查图像文件是否存在
# 如果不存在，我们可以创建一个简单的测试图像
if not os.path.exists(image_path):
    print(f"未找到图像文件 '{image_path}'，创建测试图像...")
    # 创建一个简单的测试图像（红、绿、蓝渐变）
    width, height = 300, 300
    test_img = Image.new('RGB', (width, height), color='white')
    pixels = test_img.load()
    
    for i in range(width):
        for j in range(height):
            r = int(255 * i / width)
            g = int(255 * j / height)
            b = int(255 * (1 - i/width) * (1 - j/height))
            pixels[i, j] = (r, g, b)
    
    test_img.save(image_path)
    print(f"测试图像已保存为 '{image_path}'")

# 打开原始图像
original_img = Image.open(image_path)

# 获取原始图像的尺寸
width, height = original_img.size

# 创建一个新图像，尺寸为原始图像的2倍（2×2网格）
new_width = width * 2
new_height = height * 2
combined_img = Image.new('RGB', (new_width, new_height))

# 在左上方放置原始图像
combined_img.paste(original_img, (0, 0))

# 在右上方放置CONTOUR滤镜处理的图像
contour_img = original_img.filter(ImageFilter.CONTOUR)
combined_img.paste(contour_img, (width, 0))

# 在左下方放置EMBOSS滤镜处理的图像
emboss_img = original_img.filter(ImageFilter.EMBOSS)
combined_img.paste(emboss_img, (0, height))

# 在右下方放置FIND_EDGES滤镜处理的图像
edges_img = original_img.filter(ImageFilter.FIND_EDGES)
combined_img.paste(edges_img, (width, height))

# 添加文字标签说明每个图像
from PIL import ImageDraw, ImageFont

draw = ImageDraw.Draw(combined_img)
# 尝试加载字体，使用默认字体如果指定的字体不可用
try:
    font = ImageFont.truetype("simhei.ttf", 20)  # 尝试加载中文字体
except IOError:
    font = ImageFont.load_default()  # 使用默认字体

draw.text((10, 10), "原始图像", fill="white", font=font)
# 为了在深色背景上更清晰地显示文字，为CONTOUR和FIND_EDGES添加黑色文字
if width > 50 and height > 50:
    draw.text((width + 10, 10), "CONTOUR滤镜", fill="black", font=font)
    draw.text((10, height + 10), "EMBOSS滤镜", fill="white", font=font)
    draw.text((width + 10, height + 10), "FIND_EDGES滤镜", fill="black", font=font)

# 显示组合图像
combined_img.show()

# 保存组合图像
combined_img.save("combined_result.jpg")
print("组合图像已保存为 'combined_result.jpg'")