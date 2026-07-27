from enum import Enum


class BlockTypes(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    filtered_blocks = []

    for block in blocks:
        if block == "":
            continue
        
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
    
def block_to_block_type(markdown_text):
    if markdown_text.startswith(("# ", "## ", "### ","#### ","##### ","###### ")):
        return BlockTypes.HEADING
    if markdown_text.startswith(("```")) and markdown_text.endswith(("```")):
        return BlockTypes.CODE
    
    paragraphs = markdown_text.split("\n")
    is_quote = True
    is_unordered_list = True
    is_ordered_list = True
    i = 1
    
    for p in paragraphs:
        
        if p == "":
            continue

        if p.startswith((">")) and is_quote == True:
            pass
        else:
            is_quote = False

        if p.startswith(("- ")) and is_unordered_list == True:
            pass
        else:
            is_unordered_list = False
        
        if p.startswith(f"{i}. ") and is_ordered_list == True:
            pass
        else:
            is_ordered_list = False
            
        if is_quote == False and is_unordered_list == False and is_ordered_list == False:
            break
        i += 1

    if is_quote == True:
        return BlockTypes.QUOTE
    if is_unordered_list == True:
        return BlockTypes.UNORDERED_LIST
    if is_ordered_list == True:
        return BlockTypes.ORDERED_LIST
    
    return BlockTypes.PARAGRAPH