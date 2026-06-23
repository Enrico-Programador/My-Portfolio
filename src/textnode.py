from enum import Enum
from htmlnode import LeafNode

class TextTypes(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"



class TextNode():
                #textype is a member of the Enum
    def __init__(self, text, textType, url=None):
        self.text = text
        self.textType = textType
        self.url = url

    def __eq__(self, other: "TextNode") -> bool:
        if self.text == other.text and self.textType.value == other.textType.value and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.textType.value}, {self.url})"
    

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    
    if text_node.textType.value not in TextTypes:
        raise Exception(f"{text_node.textType.value} is not a TextType")
    
    if text_node.textType.value == "text":
        return LeafNode(None, text_node.text)
    
    if text_node.textType.value == "bold":
        return LeafNode("b", text_node.text)
    
    if text_node.textType.value == "italic":
        return LeafNode("i", text_node.text)
    
    if text_node.textType.value == "code":
        return LeafNode("code", text_node.text)
    
    if text_node.textType.value == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    
    if text_node.textType.value == "image":
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})