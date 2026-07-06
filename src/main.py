import os
import shutil

from copy_files import get_files
from extract_file import extract_title, generate_page


def main():
    print("running main...")
    if os.path.exists(path='./public') == False:
        os.mkdir(path='./public')
    else:
        shutil.rmtree(path='./public')
        os.mkdir(path='./public')
    list_dir = os.listdir(path='./static')
    path = './static'
    get_files(path, list_dir)
    generate_page("./content/index.md", "./template.html", "./public/index.html")
    

    
main()