from enum import Enum

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