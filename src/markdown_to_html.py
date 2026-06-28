from ctypes.wintypes import POINT

from block_markdown import BlockTypes, block_to_block_type, markdown_to_blocks
from htmlnode import ParentNode
from splitnode import text_to_textnodes
from textnode import TextTypes, text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    final = "<div>"
    
    print(f"Blocks we are working with: {blocks}")
    for block in blocks:
        block_type = block_to_block_type(block)
        split = text_to_textnodes(block)
        nodes_list = []
        for nodes in split:
            leaf = text_node_to_html_node(nodes)
            
            nodes_list.append(leaf)

        if block_type == BlockTypes.PARAGRAPH:
            final = final + ParentNode("p", nodes_list).to_html().replace('\n', ' ') 
            
    return final+"</div>"