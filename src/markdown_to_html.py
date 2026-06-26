from ctypes.wintypes import POINT

from block_markdown import BlockTypes, block_to_block_type, markdown_to_blocks
from splitnode import split_nodes_delimiter
from textnode import TextTypes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        print(block)
        chama = split_nodes_delimiter([block], "**", TextTypes.TEXT)
        print(chama)
        if block_type is BlockTypes.PARAGRAPH:
            tag = "<p>"
    return blocks