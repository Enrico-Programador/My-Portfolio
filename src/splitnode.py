
from textnode import TextNode, TextTypes


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextTypes) -> list[TextNode]:
    new_nodes = []
    new_nodes.extend(old_nodes[0].text.split(delimiter))

    print(new_nodes)
    