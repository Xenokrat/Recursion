from os import listdir
from os.path import isfile, join
from typing import List

# 1. получаем папку / файл
# 2. проверяем, что это, файл или папке
# 3. если это папка - получаем ее содержимое
def find_all_files(path: str):
    if isfile(path):
        return path
    items_list = list(map(lambda x: path + '/' + x, listdir(path)))
    return list(map(find_all_files, items_list))

if __name__ == '__main__':
    print(find_all_files('/home/pavel/test_delete'))
