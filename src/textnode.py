from enum import Enum

class TextTypes(Enum):
    PLAIN = "text (plain)"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    Links = "[anchor text](url)"
    Images = "![alt text](url)"