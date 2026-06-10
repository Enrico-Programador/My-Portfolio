
from textnode import TextNode, TextTypes


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextTypes) -> list[TextNode]:

    new_nodes = []
    new_nodes_list = []
    
    for nodes in old_nodes:
        i = 0
        new_nodes.extend(nodes.text.split(delimiter))
        
        for new in new_nodes:
            if i%2 == 1:
                next_node = TextNode(f"{new_nodes[i]}", text_type)
            else:
                next_node = TextNode(f"{new_nodes[i]}", TextTypes.TEXT)
            new_nodes_list.append(next_node)
            i+=1
    
    return new_nodes_list
    