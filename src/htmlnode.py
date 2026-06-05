
class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This function is not implemented yet.")
    
    def props_to_html(self):
        all_props = ""

        if self.props is None:
            return all_props
        
        for prop in self.props:
            all_props = all_props + f' {prop}="{self.props[prop]}"'
        print(all_props)

        return all_props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"