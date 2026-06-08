from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextTypes

def main():
    node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(TextTypes.BOLD)
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    parent_node.to_html()

main()