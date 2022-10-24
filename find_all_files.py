from os import listdir
from os.path import isdir, join, isfile


def find_all_files(path: str):
    dirs_and_files = listdir(path)

    dirs = [
        item for item in dirs_and_files
        if isdir(join(path, item))
    ]

    files = [
        item for item in dirs_and_files
        if isfile(join(path, item))
    ]

    for item in dirs:
        files.extend(find_all_files(join(path, item)))

    return files

