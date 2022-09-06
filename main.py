import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('--folder_path', type=str, help='folder that contains lots of ._* files')


def RemoveDotFile(folder_path):
    # 找到._开头的文件
    if not os.path.isdir(folder_path):
        print('文件夹路径错误')
        return

    file_list = [file for file in os.listdir(folder_path) if file.startswith('._')]

    if len(file_list) == 0:
        print('找不到._开头的文件')
        return

    print('找到以下文件：')
    for file in file_list:
        print(file)
    print('共', len(file_list), '个')
    print('是否删除(y/n)？', end='')
    while True:
        ch = input()
        if ch in ['y', 'n']:
            break

    print('')
    if ch == 'y':
        for file in file_list:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        print('已全部删除')
    elif ch == 'n':
        print('已取消')


if __name__ == '__main__':
    args = parser.parse_args()
    folder_path = args.folder_path
    RemoveDotFile(folder_path)
