import os
import sys
import argparse

def search_skel_files(dir_path, search_texts):
    result = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.lower().endswith('.skel'):
                file_path = os.path.join(root, file)
                # 读取文件内容，并将其转换为文本格式
                with open(file_path, 'rb') as f:
                    file_content = f.read().decode('utf-8', errors='ignore')
                # 判断文件内容是否包含所有指定的文本内容
                if all(text.strip() in file_content for text in search_texts):
                    result.append(file_path)
                    
    print(','.join(result))

def main():
    parser = argparse.ArgumentParser(description='在 .skel 文件中搜索指定的文本内容')
    parser.add_argument('directory', help='要搜索的目录路径')
    parser.add_argument('texts', nargs='+', help='要查找的文本内容（支持多个文本）')

    args = parser.parse_args()

    search_skel_files(args.directory, args.texts)

if __name__ == '__main__':
    main()