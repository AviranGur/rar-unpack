import os, shutil, fnmatch
from zipfile import ZipFile, is_zipfile
from tarfile import TarFile, is_tarfile
def wild_card_match(name):
    names = ['*.zip', '*.tar', '*.tar.gz', '*.tar.bz2', '*.tar.xz']
    for n in names:
        if fnmatch.fnmatch(name, n):
            return True
def extracting_archive(filePath):
    shutil.unpack_archive(filePath, make_new_dir(filePath))
def is_path(tocheck):
    return os.path.isdir(tocheck)
def is_file(tocheck):
    return os.path.isfile(tocheck)
def to_archive(filePath):
    dirPath = filePath.split('.', 1)[0]
    readPath = get_file_path(filePath)
    shutil.make_archive(dirPath, 'xztar', readPath)
def get_files_paths(dir):
    filePaths = []
    with os.scandir(dir) as entries:
        for entry in entries:
            filePaths.append(entry.path)
    return filePaths
def unpack(fileOrPath):
    if is_path(fileOrPath):
        filePaths = get_files_paths(fileOrPath)
        for file in filePaths:
            if wild_card_match(file):
                extracting_archive(file)
    else:
        if is_zipfile(fileOrPath):
            extracting_archive(fileOrPath)
        elif is_tarfile(fileOrPath):
            extracting_archive(fileOrPath)
def recunpack(fileOrPath):
    if is_path(fileOrPath):
        filePaths = get_files_paths(fileOrPath)
        for file in filePaths:
            if wild_card_match(file):
                recunpack(file)
    else:
        if wild_card_match(fileOrPath):
            extracting_archive(fileOrPath)
            filePaths = get_files_paths(get_file_path(fileOrPath))
            for file in filePaths:
                if wild_card_match(file):
                    recunpack(file)
                elif is_path(fileOrPath):
                    recunpack(file)
def make_new_dir(dirPath):
    dirPath = get_file_path(dirPath)
    try:
        os.mkdir(dirPath)
        return dirPath
    except:
        return dirPath
def get_file_path(filePath):
    dirPath = filePath.split('.', 1)[0]
    dirPath += 'Unpacked'
    return dirPath
