import os
from markdown_to_html import markdown_to_html_node


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

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"generating file from {from_path} to {dest_path} using {template_path}")
    file_data = ""
    template_data = ""
    with open(f'{from_path}', encoding="utf-8") as f:
        file_data = f.read()
    with open(f'{template_path}', encoding="utf-8") as f:
        template_data = f.read()

    title = extract_title(file_data)
    content = markdown_to_html_node(file_data).to_html()
    dest_dir_path = os.path.dirname(dest_path)

    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(template_data.replace('{{ Title }}', f' {title} ')
                   .replace('{{ Content }}', f' {content} ')
                   .replace('href="/', f'href="{base_path}')
                   .replace('src="/', f'src="{base_path}'))
        
    