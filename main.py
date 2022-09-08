import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('--folder_path', type=str, help='folder that contains lots of ._* files')


def RemoveDotFile(files):

    if len(files) == 0:
        print('找不到._开头的文件')
        return

    print('共', len(files), '个')
    print('是否删除(y/n)？', end='')
    while True:
        ch = input()
        if ch in ['y', 'n']:
            break

    print('')
    if ch == 'y':
        for file in files:
            if os.path.isfile(file):
                os.remove(file)
            elif os.path.isdir(file):
                os.rmdir(file)
        print('已全部删除')
    elif ch == 'n':
        print('已取消')


def TraverseDir(folder_path):
    q = list()
    files = list()

    if not os.path.isdir(folder_path):
        print('文件夹路径错误')
        return

    # 遍历所有文件
    q.append(folder_path)
    while len(q):
        folder = q.pop(0)

        # 遍历文件夹下的所有文件
        try:
            for file in os.listdir(folder):
                full_path = os.path.join(folder, file)

                # ._开头的文件加入列表中
                if file.startswith('._'):
                    files.append(full_path)
                    print(len(files), full_path)

                # 文件夹纳入待搜索队列
                elif os.path.isdir(full_path):
                    q.append(full_path)
        except:
            pass

    RemoveDotFile(files)


if __name__ == '__main__':
    args = parser.parse_args()
    folder_path = args.folder_path
    TraverseDir(folder_path)
