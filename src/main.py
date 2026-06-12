from htmlnode import LeafNode, ParentNode
from splitnode import split_nodes_delimiter
from textnode import TextNode, TextTypes, text_node_to_html_node

def main():
    print("running main...")
    node = TextNode("**bold** and _italic_", TextTypes.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextTypes.BOLD)
    print(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextTypes.ITALIC)
    print(new_nodes)

main()