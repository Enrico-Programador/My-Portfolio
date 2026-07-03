import os
import shutil

from copy_files import get_files
from extract_file import extract_title


def main():
    print("running main...")
    shutil.rmtree(path='./public')
    os.mkdir(path='./public')
    list_dir = os.listdir(path='./static')
    path = './static'
    get_files(path, list_dir)
    


    
main()