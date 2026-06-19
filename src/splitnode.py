from extractmarkdown import split_nodes_image_markdown, split_nodes_link_markdown
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
    for node in old_nodes:
        new_nodes = new_nodes + split_nodes_image_markdown([node])
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        new_nodes = new_nodes + split_nodes_link_markdown([node])
    return new_nodes
    
def text_to_textnodes(text: str):
    new_nodes = [TextNode(
            text,
            TextTypes.TEXT,
            )]
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextTypes.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextTypes.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextTypes.CODE,)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes