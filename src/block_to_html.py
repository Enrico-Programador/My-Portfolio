from block_markdown import BlockTypes, block_to_block_type, markdown_to_blocks
from htmlnode import ParentNode
from splitnode import text_to_textnodes
from textnode import TextNode, TextTypes, text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    return_list = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block == "":
            continue

        if block_type == BlockTypes.HERO:
            return_list.append(block_type_hero(block))

        if block_type == BlockTypes.PARAGRAPH:
            return_list.append(block_type_paragraph(block, "p"))
            
        if block_type == BlockTypes.HEADING:
            return_list.append(block_type_heading(block))

        if block_type == BlockTypes.CODE:
            return_list.append(block_type_code(block))

        if block_type == BlockTypes.ORDERED_LIST:
            return_list.append(block_type_ordered_list(block, "ol"))

        if block_type == BlockTypes.UNORDERED_LIST:
            return_list.append(block_type_unordered_list(block, "ul"))

        if block_type == BlockTypes.QUOTE:
            return_list.append(block_type_quote(block, "blockquote"))

    return ParentNode("div", return_list)


def block_type_quote(block, block_type):
    split = text_to_textnodes(block.replace('\n', ' ').replace('> ', '').replace('>', ''))
    nodes_list = []
    for nodes in split:
        leaf = text_node_to_html_node(nodes)
        nodes_list.append(leaf)

    return ParentNode(block_type, nodes_list)

def block_type_unordered_list(block, block_type):
    block_list = block.split("\n")
    nodes_list = []
    for items in block_list:
        text = items[2:]
        parent = text_to_children(text, "li")
        nodes_list.append(parent)
    return ParentNode(block_type, nodes_list)

def block_type_ordered_list(block, block_type):
    items = block.split("\n")
    nodes_list = []
    for item in items:
        text = item[2:]
        children = text_to_children(text,"li")
        nodes_list.append(children)
    return ParentNode(block_type, nodes_list)

    

def block_type_code(block):
    block = block[4:-3]
    split = TextNode(
            block,
            TextTypes.TEXT,
            )
    child = text_node_to_html_node(split)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def block_type_heading(block):
    block = block.replace('\n', ' ')
    count = 0
    for letter in block[:6]:
        if letter == "#":
            count += 1
        else:
            break
    new_block = block[7:]
    to_replace = block[:7].replace('# ', '').replace('#','')
    new_block = to_replace + new_block 

    return text_to_children(new_block, f"h{count}")


def block_type_paragraph(block, block_type):
    return text_to_children(block, block_type)

def block_type_hero(block):
    block = block.replace(":::hero", '').replace(":::", '')
    children = []
    split = block.split('\n')
    for line in split:
        if line == "":
            continue

        node = text_to_textnodes(line)
        for child in node:
            children.append(text_node_to_html_node(child))
    
    hero = ParentNode("div", children, {"class": "hero"})
    return ParentNode("section", [hero], {"class": "hero-content"})



def text_to_children(block, block_type):
    split = text_to_textnodes(block.replace('\n', ' ').strip())
    nodes_list = []
    for nodes in split:
        leaf = text_node_to_html_node(nodes)
        nodes_list.append(leaf)
    
    return ParentNode(block_type, nodes_list)

