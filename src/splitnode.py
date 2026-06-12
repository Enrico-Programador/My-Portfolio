
from textnode import TextNode, TextTypes


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextTypes) -> list[TextNode]:
    
    new_nodes = []
    new_nodes_list = []
    starting_index = 0

    for nodes in old_nodes:
        j = 0
        
        new_nodes.extend(nodes.text.split(delimiter))
        if nodes.textType is not TextTypes.TEXT:
            print("inserting non text value...")
            print(nodes)
            #print(TextNode(f"{new_nodes[starting_index]}", text_type))
            #next_node = TextNode(f"{new_nodes[starting_index+1]}", text_type)
            new_nodes_list.append(nodes)
        
            j += 1
        else:
            for i in range(starting_index, len(new_nodes)):
                    
                if j%2 == 1:
                    next_node = TextNode(f"{new_nodes[i]}", text_type)
                else:
                    next_node = TextNode(f"{new_nodes[i]}", TextTypes.TEXT)
                print(f"value: {next_node.text}")
                if next_node.text.strip() != "":
                    print("inserting...")
                    new_nodes_list.append(next_node)
                j += 1

        if j%2 == 0:
            raise Exception("Markdown was not closed")
                
        starting_index = starting_index + len(new_nodes)
        
    return new_nodes_list
    