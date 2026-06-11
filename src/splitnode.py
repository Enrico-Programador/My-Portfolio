
from textnode import TextNode, TextTypes


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextTypes) -> list[TextNode]:
    
    new_nodes = []
    new_nodes_list = []
    old_len_nodes = 0
    for nodes in old_nodes:
        j = 0
         
        new_nodes.extend(nodes.text.split(delimiter))
        #if len(new_nodes) % 2 != 0:
            #raise ValueError("invalid markdown, formatted section not closed")
        
        actual_len = len(new_nodes) - old_len_nodes
        old_len_nodes = len(new_nodes)
        print(f"length: {actual_len}")

        for i in range(actual_len, len(new_nodes)):
            
            if j%2 == 1:
                next_node = TextNode(f"{new_nodes[i]}", text_type)
            else:
                next_node = TextNode(f"{new_nodes[i]}", TextTypes.TEXT)
            new_nodes_list.append(next_node)
            j += 1
    print(f"new nodes list: {new_nodes_list}")
    return new_nodes_list
    