

from block_markdown import markdown_to_blocks
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