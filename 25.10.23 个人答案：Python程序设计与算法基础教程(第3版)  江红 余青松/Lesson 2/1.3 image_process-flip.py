# 图像翻转函数实现
from PIL import Image
import numpy as np


def flip(image, direction='horizontal'):
    """
    图像水平或垂直翻转函数
    
    参数:
        image: PIL Image对象或numpy数组，表示原始图像
        direction: 字符串，指定翻转方向，'horizontal'表示水平翻转，'vertical'表示垂直翻转
                  默认为'horizontal'
    
    返回:
        翻转后的图像对象（与输入类型相同）
    
    异常:
        TypeError: 如果输入不是支持的图像类型或direction参数无效
        ValueError: 如果direction参数不是'horizontal'或'vertical'
    """
    # 验证direction参数
    if not isinstance(direction, str):
        raise TypeError("direction参数必须是字符串")
        
    direction = direction.lower()  # 转换为小写以增加兼容性
    if direction not in ['horizontal', 'vertical']:
        raise ValueError("direction参数必须是'horizontal'或'vertical'")
        
    # 根据图像类型执行不同的翻转操作
    if isinstance(image, Image.Image):
        # 使用PIL的transpose方法进行翻转
        if direction == 'horizontal':
            # 水平翻转（左右翻转）
            flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        else:  # direction == 'vertical'
            # 垂直翻转（上下翻转）
            flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
        return flipped_image
        
    elif isinstance(image, np.ndarray):
        # 使用numpy的切片操作进行翻转
        if direction == 'horizontal':
            # 水平翻转（左右翻转）
            flipped_array = np.fliplr(image)
        else:  # direction == 'vertical'
            # 垂直翻转（上下翻转）
            flipped_array = np.flipud(image)
        return flipped_array
        
    else:
        # 不支持的图像类型，抛出TypeError异常
        raise TypeError("输入必须是PIL Image对象或numpy数组")


# 示例使用（仅在直接运行该脚本时执行）
if __name__ == "__main__":
    # 尝试创建一个示例图像进行测试
    try:
        # 创建一个简单的测试图像（白色背景上添加一些可识别的图案）
        test_image = Image.new('RGB', (300, 200), color='white')
        
        # 创建绘图对象
        draw = ImageDraw.Draw(test_image)
        
        # 绘制一个简单的图案，便于观察翻转效果
        draw.rectangle([50, 50, 100, 100], fill='red')
        draw.rectangle([200, 50, 250, 100], fill='blue')
        draw.ellipse([125, 125, 175, 175], fill='green')
        
        print("原始图像尺寸: {test_image.size}")
        
        # 测试水平翻转
        print("\n执行水平翻转...")
        flipped_horizontal = flip(test_image, 'horizontal')
        print("水平翻转完成。显示水平翻转后的图像...")
        flipped_horizontal.show()
        
        # 测试垂直翻转
        print("\n执行垂直翻转...")
        flipped_vertical = flip(test_image, 'vertical')
        print("垂直翻转完成。显示垂直翻转后的图像...")
        flipped_vertical.show()
        
        # 测试numpy数组类型的图像
        print("\n测试numpy数组类型的图像翻转...")
        img_array = np.array(test_image)
        
        # 水平翻转numpy数组
        flipped_array_horizontal = flip(img_array, 'horizontal')
        print(f"原始数组形状: {img_array.shape}")
        print(f"水平翻转后数组形状: {flipped_array_horizontal.shape}")
        
        # 垂直翻转numpy数组
        flipped_array_vertical = flip(img_array, 'vertical')
        print(f"垂直翻转后数组形状: {flipped_array_vertical.shape}")
        
        # 测试错误处理
        print("\n测试错误处理...")
        try:
            invalid_direction = "diagonal"
            flip(test_image, invalid_direction)
        except ValueError as e:
            print(f"方向错误处理测试通过: {e}")
            
        try:
            invalid_image = "这不是图像对象"
            flip(invalid_image, 'horizontal')
        except TypeError as e:
            print(f"图像类型错误处理测试通过: {e}")
            
    except Exception as e:
        print(f"测试过程中发生错误: {e}")
        print("请确保已安装必要的库: pip install Pillow numpy")


# 注意：示例代码中使用了ImageDraw，需要导入
from PIL import ImageDraw