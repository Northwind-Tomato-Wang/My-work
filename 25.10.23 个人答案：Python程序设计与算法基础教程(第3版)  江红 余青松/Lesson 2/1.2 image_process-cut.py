# 图像剪裁函数实现
from PIL import Image
import numpy as np


def crop(image, box):
    """
    图像剪裁函数
    
    参数:
        image: PIL Image对象或numpy数组，表示原始图像
        box: 四元组(x1, y1, x2, y2)，表示剪裁区域的左上角和右下角坐标
             其中(x1, y1)是左上角坐标，(x2, y2)是右下角坐标
    
    返回:
        剪裁后的图像对象（与输入类型相同）
    
    异常:
        TypeError: 如果输入不是支持的图像类型或box参数格式不正确
        ValueError: 如果剪裁区域超出原始图像范围或参数无效
    """
    # 验证box参数
    if not isinstance(box, (tuple, list)) or len(box) != 4:
        raise TypeError("box参数必须是包含四个元素的元组或列表")
        
    try:
        # 确保box中的元素是整数
        x1, y1, x2, y2 = map(int, box)
    except (ValueError, TypeError):
        raise TypeError("box参数中的元素必须是整数")
        
    # 检查剪裁区域的有效性
    if x1 >= x2 or y1 >= y2:
        raise ValueError("剪裁区域无效：x1必须小于x2，y1必须小于y2")
        
    # 根据图像类型执行不同的剪裁操作
    if isinstance(image, Image.Image):
        # 获取原始图像尺寸
        width, height = image.size
        
        # 检查剪裁区域是否在图像范围内
        if x1 < 0 or y1 < 0 or x2 > width or y2 > height:
            raise ValueError(f"剪裁区域超出图像范围。图像尺寸: {width}x{height}")
            
        # 使用PIL的crop方法剪裁图像
        cropped_image = image.crop((x1, y1, x2, y2))
        return cropped_image
        
    elif isinstance(image, np.ndarray):
        # 获取原始图像尺寸
        if len(image.shape) == 2:  # 灰度图像
            height, width = image.shape
        elif len(image.shape) == 3:  # 彩色图像
            height, width, _ = image.shape
        else:
            raise TypeError("不支持的numpy数组形状")
        
        # 检查剪裁区域是否在图像范围内
        if x1 < 0 or y1 < 0 or x2 > width or y2 > height:
            raise ValueError(f"剪裁区域超出图像范围。图像尺寸: {width}x{height}")
            
        # 使用numpy切片剪裁图像
        cropped_array = image[y1:y2, x1:x2]
        return cropped_array
        
    else:
        # 不支持的图像类型，抛出TypeError异常
        raise TypeError("输入必须是PIL Image对象或numpy数组")


# 示例使用（仅在直接运行该脚本时执行）
if __name__ == "__main__":
    # 尝试创建一个示例图像进行测试
    try:
        # 创建一个简单的测试图像（白色背景上添加一些颜色块）
        test_image = Image.new('RGB', (300, 200), color='white')
        
        # 创建绘图对象
        draw = ImageDraw.Draw(test_image)
        
        # 绘制几个彩色块
        draw.rectangle([50, 50, 150, 150], fill='red')
        draw.rectangle([150, 50, 250, 150], fill='blue')
        
        # 定义剪裁区域（剪裁红色块）
        crop_box = (50, 50, 150, 150)
        
        # 使用crop函数剪裁图像
        cropped_image = crop(test_image, crop_box)
        
        # 显示原始图像和剪裁后的图像信息
        print(f"原始图像尺寸: {test_image.size}")
        print(f"剪裁区域: {crop_box}")
        print(f"剪裁后图像尺寸: {cropped_image.size}")
        
        # 保存剪裁后的图像（可选）
        # cropped_image.save("cropped_example.jpg")
        
        # 显示剪裁后的图像
        print("显示剪裁后的图像...")
        cropped_image.show()
        
        # 测试numpy数组类型的图像
        print("\n测试numpy数组类型的图像剪裁...")
        img_array = np.array(test_image)
        cropped_array = crop(img_array, crop_box)
        print(f"原始数组形状: {img_array.shape}")
        print(f"剪裁后数组形状: {cropped_array.shape}")
        
        # 测试错误处理
        print("\n测试错误处理...")
        try:
            invalid_box = (0, 0, 100, 50)  # 有效
            invalid_image = "这不是图像对象"
            crop(invalid_image, invalid_box)
        except TypeError as e:
            print(f"错误处理测试通过: {e}")
            
    except Exception as e:
        print(f"测试过程中发生错误: {e}")
        print("请确保已安装必要的库: pip install Pillow numpy")


# 注意：示例代码中使用了ImageDraw，需要导入
from PIL import ImageDraw