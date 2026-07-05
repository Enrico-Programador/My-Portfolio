
from os import read


def extract_title(markdown):
    search_heading = markdown.split()
    if search_heading[0] != "#":
        raise Exception("No heading found")
    
    split_md = markdown.split("\n\n")
    first_heading = ''
    for items in split_md:
        if items.strip() == "":
            continue
        else:
            first_heading = items.strip().lstrip("#").strip()
            break
    return first_heading

def generate_page(from_path, template_path, dest_path):
    print(f"generating file from {from_path} to {dest_path} using {template_path}")
    with open(f'{from_path}', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)