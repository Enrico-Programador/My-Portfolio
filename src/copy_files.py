import os
import shutil


def get_files(path, list_dir, copy_to='./public'):

    for file in list_dir:
        
        file_path = os.path.join(path, file)
        final_file_path = os.path.join(copy_to, file)

        if os.path.lexists(final_file_path) == True:
            continue
        elif os.path.isfile(file_path)==True:
            shutil.copy(file_path, copy_to)
        else:
            os.mkdir(final_file_path)
            list_dir = os.listdir(file_path)
            get_files(file_path, list_dir, final_file_path)