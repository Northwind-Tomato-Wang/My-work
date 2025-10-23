from PIL import Image
import os
import argparse

def batch_convert_jpg_to_png(source_dir=None, recursive=False):
    """
    批量将指定目录下的所有jpg文件转换为png文件
    
    参数:
        source_dir: 源目录路径，如果为None则使用当前目录
        recursive: 是否递归处理子目录
    """
    # 如果未指定源目录，使用当前目录
    if source_dir is None:
        source_dir = os.getcwd()
    
    # 确保源目录存在
    if not os.path.exists(source_dir):
        print(f"错误: 目录 '{source_dir}' 不存在")
        return
    
    print(f"开始批量转换jpg文件为png文件...")
    print(f"源目录: {source_dir}")
    print(f"递归处理子目录: {recursive}")
    
    # 统计转换的文件数量
    converted_count = 0
    
    try:
        # 遍历目录中的文件
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # 检查文件是否为jpg格式（不区分大小写）
                if file.lower().endswith('.jpg'):
                    # 构建完整的文件路径
                    jpg_path = os.path.join(root, file)
                    # 创建对应的png文件路径
                    png_path = os.path.join(root, os.path.splitext(file)[0] + '.png')
                    
                    try:
                        # 打开jpg文件并转换为png
                        with Image.open(jpg_path) as img:
                            img.save(png_path, 'PNG')
                        print(f"已转换: {jpg_path} -> {png_path}")
                        converted_count += 1
                    except Exception as e:
                        print(f"转换失败 '{jpg_path}': {str(e)}")
            
            # 如果不需要递归处理子目录，遍历完当前目录后就退出
            if not recursive:
                break
        
        print(f"\n批量转换完成！成功转换了 {converted_count} 个文件")
    except Exception as e:
        print(f"批量转换过程中发生错误: {str(e)}")

if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='批量将jpg文件转换为png文件')
    parser.add_argument('-d', '--dir', type=str, help='指定源目录路径，默认为当前目录')
    parser.add_argument('-r', '--recursive', action='store_true', help='是否递归处理子目录')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 调用批量转换函数
    batch_convert_jpg_to_png(args.dir, args.recursive)