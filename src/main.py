from blockmarkdown import markdown_to_blocks
from extractmarkdown import extract_markdown_images
from htmlnode import LeafNode, ParentNode
from splitnode import split_nodes_delimiter, text_to_textnodes
from textnode import TextNode, TextTypes, text_node_to_html_node

def main():
    print("running main...")
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    print(f"Return value: {blocks}")
main()