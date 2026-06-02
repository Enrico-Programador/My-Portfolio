from enum import Enum

class TextTypes(Enum):
    PLAIN = "text (plain)"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    Links = "[anchor text](url)"
    Images = "![alt text](url)"

class TextNode():
                #textype is a member of the Enum
    def __init__(self, text, textType, url):
        self.text = text
        self.textType = textType
        self.url = url

    def __eq__(self, other):
        if self.text == other.text:
            return True
        
    def __repr__(text, textType, url):
        return text.value, textType.value, url.value