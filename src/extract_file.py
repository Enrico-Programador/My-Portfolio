

from block_markdown import markdown_to_blocks
from markdown_to_html import markdown_to_html_node


def extract_title(markdown):
    search = markdown.split()
    
    if search[0] != "#":
        raise Exception("No heading found")
    node = markdown_to_html_node(markdown)
    return node.to_html()