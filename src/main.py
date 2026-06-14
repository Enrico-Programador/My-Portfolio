from htmlnode import LeafNode, ParentNode
from splitnode import split_nodes_delimiter
from textnode import TextNode, TextTypes, text_node_to_html_node

def main():
    print("running main...")
    node = TextNode("`code block`", TextTypes.CODE)
    new_nodes = split_nodes_delimiter([node], "`", TextTypes.CODE)
    print(new_nodes)
        
main()