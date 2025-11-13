import os
import sys
import argparse

def search_atlas_files(dir_path, search_text):
    result = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.lower().endswith('.atlas'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    file_content = f.read()
                if search_text in file_content:
                    result.append(file_path)
                    
    print(','.join(result))

def main():
    parser = argparse.ArgumentParser(description='在 .atlas 文件中搜索指定的文本内容')
    parser.add_argument('directory', help='要搜索的目录路径')
    parser.add_argument('text', help='要查找的文本内容')

    args = parser.parse_args()

    search_atlas_files(args.directory, args.text)

if __name__ == '__main__':
    main()