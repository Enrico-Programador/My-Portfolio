from enum import Enum

class TextTypes(Enum):
    PLAIN = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "link"

class TextNode():
                #textype is a member of the Enum
    def __init__(self, text, textType, url):
        self.text = text
        self.textType = textType
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.textType == other.textType and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.textType}, {self.url})"