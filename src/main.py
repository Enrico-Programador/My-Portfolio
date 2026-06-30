
from markdown_to_html import markdown_to_html_node


def main():
    print("running main...")
    md = """
# this is an h1

this is paragraph text

## this is an h2
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    print(f"Return value: {html}")
    print("Expected return value: <div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>")

main()