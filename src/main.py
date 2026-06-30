
from markdown_to_html import markdown_to_html_node


def main():
    print("running main...")
    md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    print(f"Return value: {html}")
    print("Expected return value: <div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>")
        
main()