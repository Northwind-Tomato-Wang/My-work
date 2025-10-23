# 图像拷贝函数实现
from PIL import Image
import numpy as np


def copy(image):
    """
    图像拷贝函数
    
    参数:
        image: PIL Image对象或numpy数组，表示原始图像
    
    返回:
        拷贝后的图像对象（与输入类型相同）
    
    异常:
        TypeError: 如果输入不是支持的图像类型
    """
    # 检查输入类型
    if isinstance(image, Image.Image):
        # 如果输入是PIL Image对象，使用copy方法创建副本
        return image.copy()
    elif isinstance(image, np.ndarray):
        # 如果输入是numpy数组，使用copy()方法创建深拷贝
        return image.copy()
    else:
        # 不支持的图像类型，抛出TypeError异常
        raise TypeError("输入必须是PIL Image对象或numpy数组")


# 示例使用（仅在直接运行该脚本时执行）
if __name__ == "__main__":
    # 尝试创建一个示例图像进行测试
    try:
        # 创建一个简单的测试图像
        test_image = Image.new('RGB', (100, 100), color='white')
        
        # 使用copy函数创建图像副本
        copied_image = copy(test_image)
        
        # 验证拷贝是否成功（检查是否为不同的对象）
        print(f"原始图像ID: {id(test_image)}")
        print(f"拷贝图像ID: {id(copied_image)}")
        print(f"拷贝成功: {test_image is not copied_image}")
        
        # 测试numpy数组类型的图像
        img_array = np.array(test_image)
        copied_array = copy(img_array)
        print(f"\n原始数组ID: {id(img_array)}")
        print(f"拷贝数组ID: {id(copied_array)}")
        print(f"数组拷贝成功: {img_array is not copied_array}")
        
        # 测试错误处理
        try:
            invalid_input = "这不是图像对象"
            copy(invalid_input)
        except TypeError as e:
            print(f"\n错误处理测试通过: {e}")
            
    except Exception as e:
        print(f"测试过程中发生错误: {e}")
        print("请确保已安装必要的库: pip install Pillow numpy")