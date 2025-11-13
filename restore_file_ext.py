import os
import sys
import argparse
import mimetypes

def is_text_file(file_path):
    """检测是否为文本文件"""
    with open(file_path, 'rb') as f:
        try:
            f.read().decode('utf-8')
            return True
        except UnicodeDecodeError:
            return False

def detect_file_type(file_path):
    """使用多种方法检测文件类型"""

    # 1. 首先尝试 mimetypes (基于扩展名，如果有的话)
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type:
        return mime_type

    # 2. 基于文件头检测
    with open(file_path, 'rb') as f:
        header = f.read(16)  # 读取前16字节

    # PNG文件头
    if header.startswith(b'\x89PNG\r\n\x1a\n'):
        return 'image/png'

    # JSON文件检测 (简单检查是否以 { 或 [ 开头)
    try:
        content = header.decode('utf-8', errors='ignore').strip()
        if content.startswith(('{', '[')):
            # 读取更多内容确认是JSON
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    import json
                    json.load(f)
                    return 'application/json'
                except:
                    pass
    except:
        pass

    # XML文件检测
    try:
        content = header.decode('utf-8', errors='ignore').strip()
        if content.startswith('<?xml') or content.startswith('<'):
            return 'text/xml'
    except:
        pass

    # 3. 如果都检测不到，返回None
    return None

def restore_file_ext(dir_path):
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        if os.path.isdir(file_path):
            restore_file_ext(file_path)
        else:
            # 跳过已有扩展名的文件
            if '.' in file_name and not file_name.startswith('.'):
                print(f"跳过已有扩展名的文件: {file_name}")
                continue

            file_type = detect_file_type(file_path)

            if file_type == 'image/png':
                new_file_path = file_path + '.png'
            elif file_type == 'application/json':
                new_file_path = file_path + '.json'
            elif file_type == 'text/xml':
                new_file_path = file_path + '.xml'
            else:
                if is_text_file(file_path):
                    # 如果是 UTF-8 编码的文本文件，将文件名后缀改为 .atlas
                    new_file_path = file_path + '.atlas'
                else:
                    # 如果是二进制文件，将文件名后缀改为 .skel
                    new_file_path = file_path + '.skel'

            os.rename(file_path, new_file_path)
            print(f"重命名: {file_name} -> {os.path.basename(new_file_path)}")

def main():
    parser = argparse.ArgumentParser(description='根据文件类型自动添加文件扩展名 (纯Python版本)')
    parser.add_argument('directory', help='要处理的目录路径')

    args = parser.parse_args()

    restore_file_ext(args.directory)

if __name__ == '__main__':
    main()