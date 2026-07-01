import os
import shutil

from copy_files import get_files


def main():
    print("running main...")
    shutil.rmtree(path='./public')
    os.mkdir(path='./public')
    list_dir = os.listdir(path='./static')
    path = './static'
    get_files(path, list_dir)


    
main()