import os
import shutil
import sys

from copy_file import generate_pages_recursive, get_files
from extract_file import generate_page

base_path = sys.argv[0]
if base_path == None:
    base_path = '/'
list_dir = os.listdir(path='./static')
static_path = './static'
public_path = "./docs"
content_path = "./content"
template_path = "./template.html"

def main():
    print("running main...")
    
    
    print(f"base: {base_path}")
    if os.path.exists(path='./docs') == False:
        os.mkdir(path='./docs')
    else:
        shutil.rmtree(path='./docs')
        os.mkdir(path='./docs')
    
    get_files(static_path, list_dir, public_path)
    generate_page(os.path.join(content_path, "index.md"),
                  template_path,
                  os.path.join(public_path, "index.html"),
                  base_path)
    
    generate_pages_recursive(content_path, 
                             template_path, 
                             public_path,
                             base_path)

    
main()