import os
import shutil
import sys
import argparse

def move_files_by_ext_to_target_dir(dir_path, extension, target_dir_name):
    target_dir_path = os.path.join(dir_path, target_dir_name)

    if not os.path.exists(target_dir_path):
        os.makedirs(target_dir_path)

    for root, dirs, files in os.walk(dir_path):
        # 跳过目标目录，避免重复处理
        if os.path.abspath(root) == os.path.abspath(target_dir_path):
            continue

        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                target_file_path = os.path.join(target_dir_path, file)

                if os.path.exists(target_file_path):
                    # 正确处理文件名：分离基础名和扩展名
                    base_name = file[:-len(extension)]  # 去掉扩展名，保留完整的base_name
                    n = 1
                    while True:
                        new_name = f'{base_name}_{n}{extension}'
                        target_file_path = os.path.join(target_dir_path, new_name)
                        if not os.path.exists(target_file_path):
                            break
                        n += 1

                print(f"移动: {file_path} -> {target_file_path}")
                shutil.move(file_path, target_file_path)

def main():
    parser = argparse.ArgumentParser(description='按文件扩展名移动文件到指定目录')
    parser.add_argument('directory', help='源目录路径')
    parser.add_argument('extension', help='文件扩展名（例如: .png, .json）')
    parser.add_argument('target_dir', help='目标目录名称')

    args = parser.parse_args()

    extension = args.extension
    if not extension.startswith('.'):
        extension = '.' + extension

    move_files_by_ext_to_target_dir(args.directory, extension, args.target_dir)

if __name__ == '__main__':
    main()