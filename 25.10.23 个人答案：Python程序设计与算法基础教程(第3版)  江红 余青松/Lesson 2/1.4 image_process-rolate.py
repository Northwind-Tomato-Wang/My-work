"""
图像旋转处理模块
提供图像逆时针或顺时针旋转90度的功能
"""

import numpy as np
from PIL import Image
import os


def rotate(image, direction='clockwise'):
    """
    将图像逆时针或顺时针旋转90度
    
    参数:
        image: PIL Image对象或numpy数组，原始图像
        direction: str，旋转方向，可选值为'clockwise'(顺时针)或'counterclockwise'(逆时针)
                  默认值为'clockwise'(顺时针)
    
    返回:
        PIL Image对象或numpy数组，旋转后的图像
        如果输入是PIL Image对象，返回PIL Image对象
        如果输入是numpy数组，返回numpy数组
    
    异常:
        TypeError: 当输入图像类型不是PIL Image或numpy数组时抛出
        ValueError: 当旋转方向参数无效时抛出
    
    示例:
        >>> from PIL import Image
        >>> import numpy as np
        >>> img = Image.open('example.jpg')
        >>> rotated_img = rotate(img, 'clockwise')
        >>> rotated_img.show()
        
        >>> img_array = np.array(img)
        >>> rotated_array = rotate(img_array, 'counterclockwise')
    """
    # 参数验证
    if not isinstance(image, (Image.Image, np.ndarray)):
        raise TypeError("输入图像必须是PIL Image对象或numpy数组")
        
    if direction not in ['clockwise', 'counterclockwise']:
        raise ValueError("旋转方向必须是'clockwise'(顺时针)或'counterclockwise'(逆时针)")
        
    # 处理PIL Image对象
    if isinstance(image, Image.Image):
        if direction == 'clockwise':
            # PIL的transpose方法中，ROTATE_90表示顺时针旋转90度
            return image.transpose(Image.ROTATE_270)  # 注意：PIL中的ROTATE_270实际上是顺时针旋转90度
        else:  # counterclockwise
            # ROTATE_90表示逆时针旋转90度
            return image.transpose(Image.ROTATE_90)
    
    # 处理numpy数组
    elif isinstance(image, np.ndarray):
        if direction == 'clockwise':
            # numpy的rot90函数，k=3表示顺时针旋转90度（等价于逆时针旋转270度）
            rotated_array = np.rot90(image, k=3)
        else:  # counterclockwise
            # numpy的rot90函数，k=1表示逆时针旋转90度
            rotated_array = np.rot90(image, k=1)
        
        # 保持数据类型一致
        return rotated_array.astype(image.dtype)


# 示例测试代码
if __name__ == "__main__":
    try:
        # 示例1：使用PIL Image对象
        print("测试PIL Image对象的旋转功能...")
        # 创建一个简单的测试图像
        width, height = 300, 200
        test_image = Image.new('RGB', (width, height), color='white')
        
        # 在图像上绘制一些内容以便观察旋转效果
        from PIL import ImageDraw
        draw = ImageDraw.Draw(test_image)
        draw.rectangle([(50, 50), (250, 150)], fill='blue')
        draw.text((100, 100), "测试", fill='white')
        
        # 测试顺时针旋转
        clockwise_rotated = rotate(test_image, 'clockwise')
        print(f"顺时针旋转后尺寸: {clockwise_rotated.size}")
        
        # 测试逆时针旋转
        counterclockwise_rotated = rotate(test_image, 'counterclockwise')
        print(f"逆时针旋转后尺寸: {counterclockwise_rotated.size}")
        
        # 保存结果图像（如果需要）
        if not os.path.exists('results'):
            os.makedirs('results')
        
        test_image.save('results/original_pil.png')
        clockwise_rotated.save('results/clockwise_rotated_pil.png')
        counterclockwise_rotated.save('results/counterclockwise_rotated_pil.png')
        print("PIL Image旋转结果已保存到results文件夹")
        
        # 示例2：使用numpy数组
        print("\n测试numpy数组的旋转功能...")
        # 创建一个简单的numpy数组图像
        array_image = np.zeros((200, 300, 3), dtype=np.uint8)  # 高度x宽度x通道
        array_image[50:150, 50:250, :] = [0, 0, 255]  # 蓝色矩形
        
        # 测试顺时针旋转
        clockwise_array = rotate(array_image, 'clockwise')
        print(f"顺时针旋转后形状: {clockwise_array.shape}")
        
        # 测试逆时针旋转
        counterclockwise_array = rotate(array_image, 'counterclockwise')
        print(f"逆时针旋转后形状: {counterclockwise_array.shape}")
        
        # 保存numpy数组结果为图像
        Image.fromarray(array_image).save('results/original_array.png')
        Image.fromarray(clockwise_array).save('results/clockwise_rotated_array.png')
        Image.fromarray(counterclockwise_array).save('results/counterclockwise_rotated_array.png')
        print("numpy数组旋转结果已保存到results文件夹")
        
        # 示例3：测试错误处理
        print("\n测试错误处理...")
        try:
            rotate("not_an_image", 'clockwise')
        except TypeError as e:
            print(f"类型错误测试通过: {e}")
            
        try:
            rotate(test_image, 'invalid_direction')
        except ValueError as e:
            print(f"值错误测试通过: {e}")
            
        print("\n所有测试完成！")
        
    except Exception as e:
        print(f"测试过程中发生错误: {e}")