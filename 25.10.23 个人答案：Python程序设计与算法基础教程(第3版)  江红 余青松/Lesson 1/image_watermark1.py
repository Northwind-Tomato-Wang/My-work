from PIL import Image, ImageDraw, ImageFont
import os
import argparse

def batch_add_watermark(source_dir=None, watermark_text="Python", recursive=False, 
                        font_size=40, opacity=128, position="bottom-right", 
                        color=(255, 255, 255)):
    """
    批量为指定目录下的所有jpg文件添加文字水印
    
    参数:
        source_dir: 源目录路径，如果为None则使用当前目录
        watermark_text: 水印文本内容，默认为"Python"
        recursive: 是否递归处理子目录
        font_size: 水印字体大小，默认为40
        opacity: 水印透明度(0-255)，默认为128（半透明）
        position: 水印位置，可选值: "top-left", "top-right", "bottom-left", "bottom-right", "center"
        color: 水印颜色，默认为白色(255, 255, 255)
    """
    # 如果未指定源目录，使用当前目录
    if source_dir is None:
        source_dir = os.getcwd()
    
    # 确保源目录存在
    if not os.path.exists(source_dir):
        print(f"错误: 目录 '{source_dir}' 不存在")
        return
    
    print(f"开始批量添加水印...")
    print(f"源目录: {source_dir}")
    print(f"水印文本: {watermark_text}")
    print(f"字体大小: {font_size}")
    print(f"透明度: {opacity}")
    print(f"水印位置: {position}")
    print(f"递归处理子目录: {recursive}")
    
    # 统计添加水印的文件数量
    watermarked_count = 0
    
    try:
        # 遍历目录中的文件
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # 检查文件是否为jpg格式（不区分大小写）且不是已经添加水印的文件
                if file.lower().endswith('.jpg') and not file.endswith('_w.jpg'):
                    # 构建完整的文件路径
                    jpg_path = os.path.join(root, file)
                    # 创建对应的带水印的文件路径，添加_w后缀
                    watermarked_path = os.path.join(root, os.path.splitext(file)[0] + '_w.jpg')
                    
                    try:
                        # 打开原图
                        with Image.open(jpg_path).convert('RGBA') as base:
                            # 创建一个可用于绘图的新图像
                            txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
                            
                            # 获取绘图对象
                            draw = ImageDraw.Draw(txt)
                            
                            # 尝试加载字体，如果指定字体不可用则使用默认字体
                            try:
                                # 尝试使用系统中的无衬线字体
                                if os.name == 'nt':  # Windows
                                    font = ImageFont.truetype("arial.ttf", font_size)
                                else:  # macOS/Linux
                                    font = ImageFont.truetype("Arial.ttf", font_size)
                            except IOError:
                                # 如果找不到指定字体，使用默认字体
                                font = ImageFont.load_default()
                                print(f"警告: 无法加载指定字体，使用默认字体处理 '{jpg_path}'")
                            
                            # 获取文本大小
                            try:
                                # 对于较新版本的PIL/Pillow
                                text_width, text_height = draw.textsize(watermark_text, font=font)
                            except AttributeError:
                                # 对于较旧版本的PIL/Pillow
                                bbox = draw.textbbox((0, 0), watermark_text, font=font)
                                text_width = bbox[2] - bbox[0]
                                text_height = bbox[3] - bbox[1]
                            
                            # 根据位置参数计算水印放置位置
                            img_width, img_height = base.size
                            
                            margin = 20  # 边距
                            if position == "top-left":
                                x, y = margin, margin
                            elif position == "top-right":
                                x, y = img_width - text_width - margin, margin
                            elif position == "bottom-left":
                                x, y = margin, img_height - text_height - margin
                            elif position == "bottom-right":
                                x, y = img_width - text_width - margin, img_height - text_height - margin
                            elif position == "center":
                                x, y = (img_width - text_width) // 2, (img_height - text_height) // 2
                            else:
                                # 默认放在右下角
                                x, y = img_width - text_width - margin, img_height - text_height - margin
                            
                            # 绘制水印文本
                            draw.text((x, y), watermark_text, font=font, fill=color + (opacity,))
                            
                            # 将水印合成到原图上
                            watermarked = Image.alpha_composite(base, txt)
                            
                            # 转换回RGB模式并保存
                            watermarked.convert('RGB').save(watermarked_path, 'JPEG', quality=90)
                            
                        print(f"已添加水印: {jpg_path} -> {watermarked_path}")
                        watermarked_count += 1
                    except Exception as e:
                        print(f"添加水印失败 '{jpg_path}': {str(e)}")
            
            # 如果不需要递归处理子目录，遍历完当前目录后就退出
            if not recursive:
                break
        
        print(f"\n批量添加水印完成！成功处理了 {watermarked_count} 个文件")
    except Exception as e:
        print(f"批量处理过程中发生错误: {str(e)}")

if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='批量为jpg文件添加文字水印')
    parser.add_argument('-d', '--dir', type=str, help='指定源目录路径，默认为当前目录')
    parser.add_argument('-t', '--text', type=str, default='Python', help='指定水印文本内容，默认为"Python"')
    parser.add_argument('-s', '--size', type=int, default=40, help='指定水印字体大小，默认为40')
    parser.add_argument('-o', '--opacity', type=int, default=128, help='指定水印透明度(0-255)，默认为128')
    parser.add_argument('-p', '--position', type=str, default='bottom-right',
                        choices=['top-left', 'top-right', 'bottom-left', 'bottom-right', 'center'],
                        help='指定水印位置，默认为右下角')
    parser.add_argument('-r', '--recursive', action='store_true', help='是否递归处理子目录')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 验证透明度参数
    if not (0 <= args.opacity <= 255):
        print(f"警告: 无效的透明度值 {args.opacity}，使用默认值128")
        opacity = 128
    else:
        opacity = args.opacity
    
    # 调用批量添加水印函数
    batch_add_watermark(args.dir, args.text, args.recursive, args.size, opacity, args.position)