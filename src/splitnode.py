
import re

from extractmarkdown import extract_markdown_images, extract_markdown_links
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
    
    for node in old_nodes:
        extracted_images = extract_markdown_images(node.text)
        if len(extracted_images)<=0:
            if node.text.strip() == "":
                return []
            return [node]

        new_nodes.extend(node.text.split(f"[{extracted_images[0][0]}]({extracted_images[0][1]})",1))
        remove_old = new_nodes.pop()
        new_nodes.append(TextNode(f"{extracted_images[0][0]}", TextTypes.IMAGE, f"{extracted_images[0][1]}"))

        j = 0
        for nodes in new_nodes:
            if isinstance(nodes, TextNode):
                next_node = nodes
            else:
                next_node = TextNode(nodes, TextTypes.TEXT)
                
            if next_node.text.strip() != "":
                new_nodes_list.append(next_node)
            j += 1

        if j%2 == 1:
            raise Exception("Markdown was not closed")
        
        return new_nodes_list + split_nodes_image([TextNode(remove_old,TextTypes.TEXT,)])
        
      
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    new_nodes_list = []

    for node in old_nodes:
        extracted_links = extract_markdown_links(node.text)

        if len(extracted_links) <= 0:
            if node.text.strip() == "":
                return []
            return [node]

        new_nodes.extend(node.text.split(f"[{extracted_links[0][0]}]({extracted_links[0][1]})", 1,))

        remove_old = new_nodes.pop()

        new_nodes.append(TextNode(extracted_links[0][0],TextTypes.LINK,extracted_links[0][1],))

        j = 0
        for nodes in new_nodes:
            if isinstance(nodes, TextNode):
                next_node = nodes
            else:
                next_node = TextNode(nodes, TextTypes.TEXT)

            if next_node.text.strip() != "":
                new_nodes_list.append(next_node)

            j += 1

        if j % 2 == 1:
            raise Exception("Markdown was not closed")

        return new_nodes_list + split_nodes_link([TextNode(remove_old, TextTypes.TEXT)])