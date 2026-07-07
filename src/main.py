import os
import shutil
import sys

from copy_file import generate_pages_recursive, get_files
from extract_file import generate_page

default_basepath = '/'
list_dir = os.listdir(path='./static')
static_path = './static'
public_path = "./docs"
content_path = "./content"
template_path = "./template.html"

def main():
    print("running main...")
    base_path = default_basepath
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    print(f"BASE PATH = {base_path!r}")
    
    if os.path.exists(public_path) == False:
        os.mkdir(public_path)
    else:
        shutil.rmtree(public_path)
        os.mkdir(public_path)
    
    get_files(static_path, list_dir, public_path)
    
    generate_pages_recursive(content_path, 
                             template_path, 
                             public_path,
                             base_path)

    
main()