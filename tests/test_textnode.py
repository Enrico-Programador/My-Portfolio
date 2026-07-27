import unittest
from src.textnode import TextNode, TextTypes, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextTypes.BOLD)
        node2 = TextNode("This is a text node", TextTypes.BOLD)
        self.assertEqual(node, node2)

    def test_diff(self):
        node = TextNode("This is a text node", TextTypes.LINK)
        node2 = TextNode("This is a different text node", TextTypes.BOLD)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextTypes.LINK, "www.google.com")
        node2 = TextNode("This is a text node", TextTypes.LINK, "www.google.com")
        self.assertEqual(node, node2)

    def test_url2(self):
        node = TextNode("This is a text node", TextTypes.LINK, None)
        node2 = TextNode("This is a text node", TextTypes.LINK, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextTypes.TEXT, "www.google.com")
        self.assertEqual("TextNode(This is a text node, text, www.google.com)", repr(node))

    def test_text(self):
        node = TextNode("This is a text node", TextTypes.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextTypes.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextTypes.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextTypes.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a text node", TextTypes.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "www.google.com"})

    def test_image(self):
        node = TextNode("This is a image node", TextTypes.IMAGE, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "www.google.com", "alt": "This is a image node"})

if __name__ == "__main__":
    unittest.main()