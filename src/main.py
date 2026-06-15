from extractmarkdown import extract_markdown_images
from htmlnode import LeafNode, ParentNode
from splitnode import split_nodes_delimiter
from textnode import TextNode, TextTypes, text_node_to_html_node

def main():
    print("running main...")
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
main()