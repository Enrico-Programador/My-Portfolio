
import re

from extractmarkdown import extract_markdown_images
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


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    new_nodes_list = []
    print(old_nodes)
    for node in old_nodes:
        extracted_images = extract_markdown_images(node.text)
        if len(extracted_images)<=0:
            return [node]
        
        print(extracted_images)

        
        new_nodes.extend(node.text.split(f"![{extracted_images[0][0]}]({extracted_images[0][1]})", 1))
        remove_old = new_nodes.pop()
        new_nodes.append(TextNode(f"{extracted_images[0][0]}", TextTypes.IMAGE, f"{extracted_images[0][1]}"))
        return new_nodes + split_nodes_image([TextNode(remove_old,TextTypes.TEXT,)])
        #will run for all images found in the node
        for i in range(len(extracted_images)):
            pass
      





















        '''
        for images in extracted_images:
            
            next_node = TextNode(f"{new_nodes[i]}", node.textType)
            if next_node.text.strip() != "":
                new_nodes_list.append(next_node)

            next_node = TextNode(f"{images[1]}", TextTypes.IMAGE, f"{images[0]}")
            if next_node.text.strip() != "":
                new_nodes_list.append(next_node)
            
            j += 1
            i += 1
            '''
            