"""
图像平滑处理模块
提供图像平滑过滤功能，支持均值滤波和高斯滤波
"""

import numpy as np
from PIL import Image
import cv2
import os


def smooth(image, method='gaussian', kernel_size=(5, 5), sigma=1.0):
    """
    对图像进行平滑过滤处理
    
    参数:
        image: PIL Image对象或numpy数组，原始图像
        method: str，平滑方法，可选值为'average'(均值滤波)或'gaussian'(高斯滤波)
                默认值为'gaussian'(高斯滤波)
        kernel_size: tuple，卷积核大小，格式为(width, height)
                     默认值为(5, 5)
        sigma: float，高斯滤波的标准差，仅在method为'gaussian'时有效
               默认值为1.0
    
    返回:
        PIL Image对象或numpy数组，平滑过滤后的图像
        如果输入是PIL Image对象，返回PIL Image对象
        如果输入是numpy数组，返回numpy数组
    
    异常:
        TypeError: 当输入图像类型不是PIL Image或numpy数组时抛出
        ValueError: 当平滑方法参数无效或卷积核大小无效时抛出
    
    示例:
        >>> from PIL import Image
        >>> import numpy as np
        >>> img = Image.open('example.jpg')
        >>> smoothed_img = smooth(img, method='gaussian', kernel_size=(5, 5))
        >>> smoothed_img.show()
        
        >>> img_array = np.array(img)
        >>> smoothed_array = smooth(img_array, method='average', kernel_size=(3, 3))
    """
    # 参数验证
    if not isinstance(image, (Image.Image, np.ndarray)):
        raise TypeError("输入图像必须是PIL Image对象或numpy数组")
        
    if method not in ['average', 'gaussian']:
        raise ValueError("平滑方法必须是'average'(均值滤波)或'gaussian'(高斯滤波)")
        
    if not isinstance(kernel_size, tuple) or len(kernel_size) != 2:
        raise ValueError("卷积核大小必须是格式为(width, height)的元组")
        
    if not all(isinstance(k, int) and k > 0 and k % 2 == 1 for k in kernel_size):
        raise ValueError("卷积核的宽度和高度必须是正奇数")
    
    # 处理PIL Image对象
    if isinstance(image, Image.Image):
        # 将PIL Image转换为numpy数组进行处理
        img_array = np.array(image)
        
        # 执行平滑处理
        smoothed_array = _apply_smoothing(img_array, method, kernel_size, sigma)
        
        # 将处理后的numpy数组转换回PIL Image
        if len(smoothed_array.shape) == 3:
            return Image.fromarray(smoothed_array.astype(np.uint8))
        else:
            return Image.fromarray(smoothed_array.astype(np.uint8), mode='L')
    
    # 处理numpy数组
    elif isinstance(image, np.ndarray):
        # 执行平滑处理并保持数据类型一致
        smoothed_array = _apply_smoothing(image.copy(), method, kernel_size, sigma)
        return smoothed_array.astype(image.dtype)


def _apply_smoothing(img_array, method, kernel_size, sigma):
    """
    内部函数：对numpy数组图像应用平滑滤波
    
    参数:
        img_array: numpy数组，输入图像
        method: str，平滑方法
        kernel_size: tuple，卷积核大小
        sigma: float，高斯滤波的标准差
    
    返回:
        numpy数组，平滑后的图像
    """
    # 检查图像维度
    if len(img_array.shape) == 3:
        # 彩色图像（多通道）
        # 对于均值滤波，可以直接使用cv2.blur
        if method == 'average':
            return cv2.blur(img_array, kernel_size)
        # 对于高斯滤波，使用cv2.GaussianBlur
        else:  # gaussian
            return cv2.GaussianBlur(img_array, kernel_size, sigma)
    elif len(img_array.shape) == 2:
        # 灰度图像（单通道）
        if method == 'average':
            return cv2.blur(img_array, kernel_size)
        else:  # gaussian
            return cv2.GaussianBlur(img_array, kernel_size, sigma)
    else:
        raise ValueError("不支持的图像维度")


# 示例测试代码
if __name__ == "__main__":
    try:
        # 示例1：使用PIL Image对象
        print("测试PIL Image对象的平滑功能...")
        
        # 创建一个简单的测试图像或尝试打开现有图像
        try:
            # 尝试打开当前目录中的图像
            test_image = Image.open('test_image.jpg')
            print("成功打开现有图像")
        except FileNotFoundError:
            # 如果没有图像文件，创建一个带有噪声的测试图像
            print("未找到图像文件，创建测试图像...")
            width, height = 400, 300
            test_image = Image.new('RGB', (width, height), color='white')
            
            # 添加一些内容
            from PIL import ImageDraw
            draw = ImageDraw.Draw(test_image)
            draw.rectangle([(100, 75), (300, 225)], fill='blue')
            draw.ellipse([(150, 100), (250, 200)], fill='red')
            draw.text((170, 140), "测试", fill='white')
            
            # 添加一些随机噪声以便观察平滑效果
            img_array = np.array(test_image)
            noise = np.random.randint(0, 50, img_array.shape, dtype=np.uint8)
            noisy_array = np.clip(img_array + noise, 0, 255).astype(np.uint8)
            test_image = Image.fromarray(noisy_array)
            
            # 保存噪声图像
            test_image.save('noisy_test_image.jpg')
            print("已创建带噪声的测试图像: noisy_test_image.jpg")
        
        # 测试均值滤波
        average_smoothed = smooth(test_image, method='average', kernel_size=(5, 5))
        print(f"均值滤波后尺寸: {average_smoothed.size}")
        
        # 测试高斯滤波
        gaussian_smoothed = smooth(test_image, method='gaussian', kernel_size=(5, 5), sigma=1.5)
        print(f"高斯滤波后尺寸: {gaussian_smoothed.size}")
        
        # 保存结果图像
        if not os.path.exists('results'):
            os.makedirs('results')
        
        test_image.save('results/original_pil.png')
        average_smoothed.save('results/average_smoothed_pil.png')
        gaussian_smoothed.save('results/gaussian_smoothed_pil.png')
        print("PIL Image平滑结果已保存到results文件夹")
        
        # 示例2：使用numpy数组
        print("\n测试numpy数组的平滑功能...")
        # 将PIL图像转换为numpy数组
        array_image = np.array(test_image)
        
        # 测试均值滤波
        average_array = smooth(array_image, method='average', kernel_size=(7, 7))
        print(f"均值滤波后形状: {average_array.shape}")
        
        # 测试高斯滤波
        gaussian_array = smooth(array_image, method='gaussian', kernel_size=(7, 7), sigma=2.0)
        print(f"高斯滤波后形状: {gaussian_array.shape}")
        
        # 保存numpy数组结果为图像
        Image.fromarray(array_image).save('results/original_array.png')
        Image.fromarray(average_array.astype(np.uint8)).save('results/average_smoothed_array.png')
        Image.fromarray(gaussian_array.astype(np.uint8)).save('results/gaussian_smoothed_array.png')
        print("numpy数组平滑结果已保存到results文件夹")
        
        # 示例3：测试不同卷积核大小
        print("\n测试不同卷积核大小的效果...")
        small_kernel = smooth(test_image, method='gaussian', kernel_size=(3, 3))
        large_kernel = smooth(test_image, method='gaussian', kernel_size=(9, 9))
        
        small_kernel.save('results/small_kernel_smoothed.png')
        large_kernel.save('results/large_kernel_smoothed.png')
        print("不同卷积核大小的结果已保存到results文件夹")
        
        # 示例4：测试错误处理
        print("\n测试错误处理...")
        try:
            smooth("not_an_image", method='gaussian')
        except TypeError as e:
            print(f"类型错误测试通过: {e}")
            
        try:
            smooth(test_image, method='invalid_method')
        except ValueError as e:
            print(f"值错误测试通过: {e}")
            
        try:
            smooth(test_image, kernel_size=(4, 4))  # 偶数大小的卷积核
        except ValueError as e:
            print(f"卷积核大小错误测试通过: {e}")
            
        print("\n所有测试完成！")
        
    except Exception as e:
        print(f"测试过程中发生错误: {e}")
        import traceback
        traceback.print_exc()