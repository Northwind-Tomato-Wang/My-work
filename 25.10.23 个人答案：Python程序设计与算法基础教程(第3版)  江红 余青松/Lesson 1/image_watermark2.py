import os
from PIL import Image


def batch_add_image_watermark(source_dir='.', watermark_path='python-logo.png', recursive=False, 
                              output_suffix='_w', opacity=0.5, position='center'):
    """
    批量为JPG文件添加图片水印
    
    参数:
        source_dir: 源文件夹路径，默认为当前目录
        watermark_path: 水印图片路径
        recursive: 是否递归处理子文件夹
        output_suffix: 输出文件后缀
        opacity: 水印透明度，0-1之间
        position: 水印位置，可选'center', 'top-left', 'top-right', 'bottom-left', 'bottom-right'
    """
    # 检查水印文件是否存在
    if not os.path.exists(watermark_path):
        print(f"错误: 水印文件 '{watermark_path}' 不存在")
        return
    
    # 加载水印图片
    try:
        watermark = Image.open(watermark_path).convert('RGBA')
        watermark_width, watermark_height = watermark.size
    except Exception as e:
        print(f"加载水印图片失败: {e}")
        return
    
    # 调整水印透明度
    if opacity < 1.0:
        # 创建一个新的水印图像，应用透明度
        watermark_with_opacity = Image.new('RGBA', watermark.size)
        for x in range(watermark_width):
            for y in range(watermark_height):
                r, g, b, a = watermark.getpixel((x, y))
                watermark_with_opacity.putpixel((x, y), (r, g, b, int(a * opacity)))
        watermark = watermark_with_opacity
    
    # 遍历目录中的文件
    processed_count = 0
    
    if recursive:
        for root, _, files in os.walk(source_dir):
            processed_count += process_directory(root, files, watermark, watermark_width, 
                                                watermark_height, output_suffix, position)
    else:
        files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
        processed_count += process_directory(source_dir, files, watermark, watermark_width, 
                                            watermark_height, output_suffix, position)
    
    print(f"批量添加水印完成，共处理了 {processed_count} 个文件")


def process_directory(directory, files, watermark, watermark_width, watermark_height, 
                      output_suffix, position):
    """处理单个目录中的文件"""
    processed_count = 0
    
    for filename in files:
        # 检查文件是否为JPG格式
        if not (filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg')):
            continue
        
        # 跳过已经添加过水印的文件
        if output_suffix in filename:
            continue
        
        file_path = os.path.join(directory, filename)
        try:
            # 打开原始图片
            image = Image.open(file_path).convert('RGBA')
            image_width, image_height = image.size
            
            # 计算水印位置
            if position == 'center':
                pos_x = (image_width - watermark_width) // 2
                pos_y = (image_height - watermark_height) // 2
            elif position == 'top-left':
                pos_x, pos_y = 10, 10
            elif position == 'top-right':
                pos_x, pos_y = image_width - watermark_width - 10, 10
            elif position == 'bottom-left':
                pos_x, pos_y = 10, image_height - watermark_height - 10
            elif position == 'bottom-right':
                pos_x, pos_y = image_width - watermark_width - 10, image_height - watermark_height - 10
            else:
                pos_x = (image_width - watermark_width) // 2
                pos_y = (image_height - watermark_height) // 2
            
            # 创建一个新的图像作为结果
            result = Image.new('RGBA', (image_width, image_height), (255, 255, 255, 0))
            result.paste(image, (0, 0))
            result.paste(watermark, (pos_x, pos_y), watermark)
            
            # 转换回RGB并保存
            result_rgb = result.convert('RGB')
            
            # 生成输出文件名
            base_name, ext = os.path.splitext(filename)
            output_filename = f"{base_name}{output_suffix}{ext}"
            output_path = os.path.join(directory, output_filename)
            
            # 保存图片
            result_rgb.save(output_path, quality=95)
            print(f"已处理: {filename} -> {output_filename}")
            processed_count += 1
        except Exception as e:
            print(f"处理文件 '{filename}' 时出错: {e}")
    
    return processed_count


if __name__ == "__main__":
    # 配置参数
    SOURCE_DIR = '.'  # 当前目录
    WATERMARK_PATH = 'python-logo.png'  # 水印图片路径
    RECURSIVE = False  # 是否递归处理子目录
    OPACITY = 0.5  # 水印透明度
    POSITION = 'center'  # 水印位置
    
    # 运行批量添加水印
    batch_add_image_watermark(
        source_dir=SOURCE_DIR,
        watermark_path=WATERMARK_PATH,
        recursive=RECURSIVE,
        opacity=OPACITY,
        position=POSITION
    )