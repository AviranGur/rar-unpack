import os, shutil, fnmatch
from zipfile import ZipFile, is_zipfile
from tarfile import TarFile, is_tarfile


def wild_card_match(name):
    names = ['*.zip', '*.tar', '*.tar.gz', '*.tar.bz2', '*.tar.xz']
    for n in names:
        if fnmatch.fnmatch(name, n):
            return True

def extracting_archive(file_path):
    shutil.unpack_archive(file_path, make_new_dir(file_path))

def is_path(to_check):
    return os.path.isdir(to_check)

def is_file(to_check):
    return os.path.isfile(to_check)

def to_archive(file_path):
    dirPath = file_path.split('.', 1)[0]
    readPath = get_file_path(file_path)
    shutil.make_archive(dirPath, 'xztar', readPath)

def get_files_paths(dir):
    file_paths = []
    with os.scandir(dir) as entries:
        for entry in entries:
            file_paths.append(entry.path)
    return file_paths

def unpack(file_or_path):
    if is_path(file_or_path):
        file_paths = get_files_paths(file_or_path)
        for file in file_paths:
            if wild_card_match(file):
                extracting_archive(file)
    else:
        if is_zipfile(file_or_path):
            extracting_archive(file_or_path)
        elif is_tarfile(file_or_path):
            extracting_archive(file_or_path)

def recunpack(file_or_path):
    if is_path(file_or_path):
        file_paths = get_files_paths(file_or_path)
        for file in file_paths:
            if wild_card_match(file):
                recunpack(file)
    else:
        if wild_card_match(file_or_path):
            extracting_archive(file_or_path)
            file_paths = get_files_paths(get_file_path(file_or_path))
            for file in file_paths:
                if wild_card_match(file):
                    recunpack(file)
                elif is_path(file_or_path):
                    recunpack(file)

def make_new_dir(dir_path):
    dir_path = get_file_path(dir_path)
    try:
        os.mkdir(dir_path)
        return dir_path
    except:
        return dir_path

def get_file_path(file_path):
    dir_path = file_path.split('.', 1)[0]
    dir_path += 'Unpacked'
    return dir_path
