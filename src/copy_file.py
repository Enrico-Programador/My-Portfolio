import os
import shutil

from extract_file import generate_page


def get_files(path, list_dir, copy_to):

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

#generate_page(from_path, template_path, dest_path)
                            #dir content        template.html   dir public
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    list_dir = os.listdir(path=dir_path_content)
    for file in list_dir:

        file_path = os.path.join(dir_path_content, file)
        final_file_path = os.path.join(dest_dir_path, file.replace(".md", ".html"))
        
        if os.path.lexists(final_file_path) == True:
            continue
        elif os.path.isfile(file_path)==True:
            generate_page(file_path, 
                          template_path, 
                          final_file_path,
                          base_path)
            
        else:
            os.mkdir(final_file_path)
            list_dir = os.listdir(file_path)
            generate_pages_recursive(file_path, template_path, final_file_path, base_path)
            