import os
import sys
import argparse
import struct

def get_png_size(file_path):
    with open(file_path, 'rb') as f:
        # PNG文件前8个字节是固定签名
        if f.read(8) != b'\x89PNG\r\n\x1a\n':
            return None

        # 读取IHDR chunk
        chunk_data = f.read(8)
        if len(chunk_data) < 8:
            return None

        chunk_length = struct.unpack('>I', chunk_data[:4])[0]
        chunk_type = chunk_data[4:8]

        if chunk_type != b'IHDR':
            return None

        # 读取宽度和高度 (各4字节，大端序)
        ihdr_data = f.read(chunk_length)
        if len(ihdr_data) < 8:
            return None

        width = struct.unpack('>I', ihdr_data[:4])[0]
        height = struct.unpack('>I', ihdr_data[4:8])[0]

        return width, height

def rename_png_files(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.lower().endswith('.png'):
                file_path = os.path.join(root, file)

                size = get_png_size(file_path)
                if size is None:
                    print(f"警告: {file_path} 不是有效的PNG文件，跳过")
                    continue

                width, height = size
                new_file_name = f'size_{width}x{height}.png'
                new_file_path = os.path.join(root, new_file_name)

                if os.path.exists(new_file_path):
                    n = 1
                    while True:
                        new_file_name = f'size_{width}x{height}_{n}.png'
                        new_file_path = os.path.join(root, new_file_name)
                        if not os.path.exists(new_file_path):
                            break
                        n += 1

                os.rename(file_path, new_file_path)
                print(f"重命名: {file} -> {new_file_name}")

def main():
    parser = argparse.ArgumentParser(description='根据 PNG 图片尺寸重命名文件')
    parser.add_argument('directory', help='要处理的目录路径')

    args = parser.parse_args()

    rename_png_files(args.directory)

if __name__ == '__main__':
    main()