from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextTypes

def main():
    node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(TextTypes.BOLD)
    node2 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
    print_node = node2.to_html()
    print(print_node)

main()