import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            "TEST101": "hellofriend"
        }
        node = HTMLNode("tag", "value", "children", props)
        node.props_to_html()

if __name__ == "__main__":
    unittest.main()