
import re

from extractmarkdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextTypes


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextTypes) -> list[TextNode]:
    
    new_nodes = []
    
    for nodes in old_nodes:
        if nodes.textType != TextTypes.TEXT:
            new_nodes.append(nodes)
            continue

        split_nodes = nodes.text.split(delimiter)
        if len(nodes.text.split(delimiter)) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        
        for i in range(0, len(split_nodes)):
            
            if i%2 == 0:
                next_node = TextNode(f"{split_nodes[i]}", TextTypes.TEXT)
                if next_node.text.strip() != "":
                    new_nodes.append(next_node)
                
            elif i%2 == 1:
                next_node = TextNode(f"{split_nodes[i]}", text_type)
                if next_node.text.strip() != "":
                    new_nodes.append(next_node)
                
    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    new_nodes_list = []
    
    for node in old_nodes:
        if node.textType != TextTypes.TEXT:
            new_nodes_list.append(node)
            continue
        extracted_images = extract_markdown_images(node.text)
        if len(extracted_images)<=0:
            
            if node.text.strip() == "":
                return []
            return [node]

        new_nodes.extend(node.text.split(f"![{extracted_images[0][0]}]({extracted_images[0][1]})", 1))
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
        
        return new_nodes_list + split_nodes_image([TextNode
                                            (remove_old,TextTypes.TEXT,)])
        
      
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
    
'''
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image" 

'''

#model: new_nodes = split_nodes_delimiter(new_nodes, "_", TextTypes.ITALIC) 

def text_to_textnodes(text: str):
    new_nodes = TextNode(
            text,
            TextTypes.TEXT,
            )
    new_nodes = split_nodes_delimiter([new_nodes], "**", TextTypes.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextTypes.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, 
                        "`", 
                        TextTypes.CODE,)
    new_nodes = split_nodes_image(new_nodes)
    #new_nodes = split_nodes_link(new_nodes)
    return new_nodes