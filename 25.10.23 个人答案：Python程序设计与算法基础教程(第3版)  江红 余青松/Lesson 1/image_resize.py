import os
from PIL import Image


def batch_resize_images(source_dir='.', target_size=(640, 480), output_suffix='_640', 
                       recursive=False, quality=95, maintain_aspect_ratio=False):
    """
    批量调整JPG图片大小
    
    参数:
        source_dir: 源文件夹路径，默认为当前目录
        target_size: 目标尺寸，格式为(width, height)
        output_suffix: 输出文件后缀
        recursive: 是否递归处理子文件夹
        quality: 保存图片的质量，1-95
        maintain_aspect_ratio: 是否保持原图宽高比
    """
    # 遍历目录中的文件
    processed_count = 0
    
    if recursive:
        for root, _, files in os.walk(source_dir):
            processed_count += process_directory(root, files, target_size, output_suffix, 
                                               quality, maintain_aspect_ratio)
    else:
        files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
        processed_count += process_directory(source_dir, files, target_size, output_suffix, 
                                           quality, maintain_aspect_ratio)
    
    print(f"批量调整图片大小完成，共处理了 {processed_count} 个文件")


def process_directory(directory, files, target_size, output_suffix, quality, maintain_aspect_ratio):
    """处理单个目录中的文件"""
    processed_count = 0
    target_width, target_height = target_size
    
    for filename in files:
        # 检查文件是否为JPG格式
        if not (filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg')):
            continue
        
        # 跳过已经处理过的文件
        if output_suffix in filename:
            continue
        
        file_path = os.path.join(directory, filename)
        try:
            # 打开原始图片
            image = Image.open(file_path)
            
            # 调整图片大小
            if maintain_aspect_ratio:
                # 按比例调整，确保图片完全在目标尺寸内
                image.thumbnail(target_size, Image.Resampling.LANCZOS)
                resized_image = image
            else:
                # 直接调整到目标尺寸，可能会导致图片变形
                resized_image = image.resize(target_size, Image.Resampling.LANCZOS)
            
            # 生成输出文件名
            base_name, ext = os.path.splitext(filename)
            output_filename = f"{base_name}{output_suffix}{ext}"
            output_path = os.path.join(directory, output_filename)
            
            # 保存调整后的图片
            resized_image.save(output_path, quality=quality)
            print(f"已处理: {filename} -> {output_filename}")
            processed_count += 1
        except Exception as e:
            print(f"处理文件 '{filename}' 时出错: {e}")
    
    return processed_count


if __name__ == "__main__":
    # 配置参数
    SOURCE_DIR = '.'  # 当前目录
    TARGET_SIZE = (640, 480)  # 目标尺寸：宽度640，高度480
    OUTPUT_SUFFIX = '_640'  # 输出文件后缀
    RECURSIVE = False  # 是否递归处理子目录
    QUALITY = 95  # 图片保存质量
    MAINTAIN_ASPECT_RATIO = False  # 是否保持原图片的宽高比
    
    # 运行批量调整大小
    batch_resize_images(
        source_dir=SOURCE_DIR,
        target_size=TARGET_SIZE,
        output_suffix=OUTPUT_SUFFIX,
        recursive=RECURSIVE,
        quality=QUALITY,
        maintain_aspect_ratio=MAINTAIN_ASPECT_RATIO
    )