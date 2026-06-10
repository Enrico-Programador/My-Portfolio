from htmlnode import LeafNode, ParentNode
from splitnode import split_nodes_delimiter
from textnode import TextNode, TextTypes, text_node_to_html_node

def main():
    print("running main...")
    node = TextNode("This is text with a `code block` word", TextTypes.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextTypes.CODE)
    

main()