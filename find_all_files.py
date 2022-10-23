from os import listdir
from os.path import isdir, join as os_join
from typing import List


def find_all_files(path: str) -> List[str]:
    dirs, files = [], []
    find_all_files_recr(path, dirs, files)
    return files


def find_all_files_recr(path: str, dirs: List[str], files: List[str]) -> None:
    dirs_and_files = listdir(path)
    dirs_here = []

    for item in dirs_and_files:
        if isdir(os_join(path, item)):
            dirs.append(item)
            dirs_here.append(item)
        else:
            files.append(item)

    for item in dirs_here:
        new_path: str = os_join(path, item)
        find_all_files_recr(new_path, dirs, files)
        
