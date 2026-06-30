import os
import shutil


def main():
    print("running main...")
    shutil.rmtree(path='./public')
    os.mkdir(path='./public')
    path = os.listdir(path='./static')
    get_files(path)

def get_files(path):
    for file in path:
        print(file)
        if os.path.isfile(os.path.join('./static',file))==False:
            print(os.path.join('./static',file))
    
main()