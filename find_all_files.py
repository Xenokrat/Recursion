from os import listdir
from os.path import isdir, join
from typing import List


def find_all_files(path: str) -> List[str]:
    files = []
    find_all_files_recr(path, files)
    return files


def find_all_files_recr(path: str, files: List[str]) -> None:
    dirs_and_files = listdir(path)
    dirs_here = []

    for item in dirs_and_files:
        if isdir(join(path, item)):
            dirs_here.append(item)
        else:
            files.append(item)

    for item in dirs_here:
        new_path: str = join(path, item)
        find_all_files_recr(new_path, files)
        
