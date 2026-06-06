import unittest
from textnode import TextNode, TextTypes

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
        self.assertEqual("TextNode(This is a text node, TextTypes.TEXT, www.google.com)", repr(node))

if __name__ == "__main__":
    unittest.main()