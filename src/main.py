from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextTypes, text_node_to_html_node

def main():
    node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(TextTypes.BOLD)
    

main()