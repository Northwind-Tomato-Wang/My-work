from PIL import Image
import os
import argparse

def batch_create_thumbnails(source_dir=None, thumbnail_size=(300, 200), quality=85, recursive=False):
    """
    批量为指定目录下的所有jpg文件创建缩略图
    
    参数:
        source_dir: 源目录路径，如果为None则使用当前目录
        thumbnail_size: 缩略图尺寸，默认为(300, 200)
        quality: JPEG保存质量(1-95)，默认为85
        recursive: 是否递归处理子目录
    """
    # 如果未指定源目录，使用当前目录
    if source_dir is None:
        source_dir = os.getcwd()
    
    # 确保源目录存在
    if not os.path.exists(source_dir):
        print(f"错误: 目录 '{source_dir}' 不存在")
        return
    
    print(f"开始批量创建缩略图...")
    print(f"源目录: {source_dir}")
    print(f"缩略图尺寸: {thumbnail_size[0]}x{thumbnail_size[1]}")
    print(f"JPEG质量: {quality}")
    print(f"递归处理子目录: {recursive}")
    
    # 统计生成的缩略图数量
    thumbnail_count = 0
    
    try:
        # 遍历目录中的文件
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # 检查文件是否为jpg格式（不区分大小写）
                if file.lower().endswith('.jpg') and not file.endswith('_s.jpg'):
                    # 构建完整的文件路径
                    jpg_path = os.path.join(root, file)
                    # 创建对应的缩略图文件路径，添加_s后缀
                    thumbnail_path = os.path.join(root, os.path.splitext(file)[0] + '_s.jpg')
                    
                    try:
                        # 打开原图并创建缩略图
                        with Image.open(jpg_path) as img:
                            # 使用thumbnail方法保持原图像比例创建缩略图
                            img.thumbnail(thumbnail_size, Image.LANCZOS)
                            # 保存缩略图，指定JPEG质量
                            img.save(thumbnail_path, 'JPEG', quality=quality)
                        print(f"已创建缩略图: {jpg_path} -> {thumbnail_path}")
                        thumbnail_count += 1
                    except Exception as e:
                        print(f"创建缩略图失败 '{jpg_path}': {str(e)}")
            
            # 如果不需要递归处理子目录，遍历完当前目录后就退出
            if not recursive:
                break
        
        print(f"\n批量创建缩略图完成！成功创建了 {thumbnail_count} 个缩略图")
    except Exception as e:
        print(f"批量处理过程中发生错误: {str(e)}")

if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='批量为jpg文件创建缩略图')
    parser.add_argument('-d', '--dir', type=str, help='指定源目录路径，默认为当前目录')
    parser.add_argument('-s', '--size', type=str, default='300x200', help='指定缩略图尺寸，格式为WxH，默认为300x200')
    parser.add_argument('-q', '--quality', type=int, default=85, help='指定JPEG保存质量(1-95)，默认为85')
    parser.add_argument('-r', '--recursive', action='store_true', help='是否递归处理子目录')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 解析尺寸参数
    try:
        width, height = map(int, args.size.split('x'))
        thumbnail_size = (width, height)
    except ValueError:
        print(f"警告: 无效的尺寸格式 '{args.size}'，使用默认尺寸300x200")
        thumbnail_size = (300, 200)
    
    # 验证质量参数
    if not (1 <= args.quality <= 95):
        print(f"警告: 无效的质量值 {args.quality}，使用默认值85")
        quality = 85
    else:
        quality = args.quality
    
    # 调用批量创建缩略图函数
    batch_create_thumbnails(args.dir, thumbnail_size, quality, args.recursive)