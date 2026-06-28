from ctypes.wintypes import POINT

from block_markdown import BlockTypes, block_to_block_type, markdown_to_blocks
from splitnode import split_nodes_delimiter, text_to_textnodes
from textnode import TextTypes, text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    final = ""
    for block in blocks:
        block_type = block_to_block_type(block)
        split = text_to_textnodes(block)
        print(split)
        for nodes in split:
            leaf = text_node_to_html_node(nodes)
            final = final + leaf.to_html()
    return final