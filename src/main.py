from extractmarkdown import extract_markdown_images
from htmlnode import LeafNode, ParentNode
from splitnode import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextTypes, text_node_to_html_node

def main():
    print("running main...")
    node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://wikipedia.org) with text that follows",
            TextTypes.TEXT,
        )
    new_nodes = split_nodes_link([node])
    print(f"Final nodes: {new_nodes}")
main()