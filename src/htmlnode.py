
class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode has no value")
        if self.tag == None:
            return f"{self.value}"
        
        htmlText = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return htmlText
    
    def props_to_html(self):
        all_props = ""

        if self.props is None:
            return all_props
        
        for prop in self.props:
            all_props = all_props + f' {prop}="{self.props[prop]}"'

        return all_props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"