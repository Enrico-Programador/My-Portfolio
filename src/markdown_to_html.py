from block_markdown import BlockTypes, block_to_block_type, markdown_to_blocks
from htmlnode import ParentNode
from splitnode import text_to_textnodes
from textnode import TextTypes, text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    return_list = []
    print(f"Blocks we are working with: {blocks}")

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockTypes.PARAGRAPH:
            return_list.append(block_type_paragraph(block))
            
    return ParentNode("div", return_list)


def block_type_paragraph(block):
    split = text_to_textnodes(block.replace('\n', ' '))
    nodes_list = []
    for nodes in split:
        leaf = text_node_to_html_node(nodes)
        nodes_list.append(leaf)

    return ParentNode("p", nodes_list)
