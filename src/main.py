import os
import shutil

from copy_file import get_files
from extract_file import generate_page

list_dir = os.listdir(path='./static')
static_path = './static'
public_path = "./public"
content_path = "./content"
template_path = "./template.html"

def main():
    print("running main...")
    if os.path.exists(path='./public') == False:
        os.mkdir(path='./public')
    else:
        shutil.rmtree(path='./public')
        os.mkdir(path='./public')
    
    get_files(static_path, list_dir)
    generate_page(os.path.join(content_path, "index.md"),
                  template_path,
                  os.path.join(public_path, "index.html"),)
    

    
main()