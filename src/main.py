from extractmarkdown import extract_markdown_images
from htmlnode import LeafNode, ParentNode
from splitnode import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextTypes, text_node_to_html_node

def main():
    print("running main...")
    new_nodes = text_to_textnodes("This is **bolded text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
    print(f"Final nodes: {new_nodes}")
main()