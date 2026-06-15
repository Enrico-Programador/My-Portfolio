
from textnode import TextNode, TextTypes


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextTypes) -> list[TextNode]:
    
    new_nodes = []
    new_nodes_list = []
    starting_index = 0

    for nodes in old_nodes:
        j = 0
        
        new_nodes.extend(nodes.text.split(delimiter))
        
        for i in range(starting_index, len(new_nodes)):
                    
            if j%2 == 1:
                next_node = TextNode(f"{new_nodes[i]}", text_type)
            else:
                next_node = TextNode(f"{new_nodes[i]}", nodes.textType)
                
            if next_node.text.strip() != "":
                new_nodes_list.append(next_node)
            j += 1

        if j%2 == 0:
            raise Exception("Markdown was not closed")
                
        starting_index = starting_index + len(new_nodes)
    
        
    return new_nodes_list
    