import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from splitnode import split_nodes_delimiter
from textnode import TextNode, TextTypes

class TestSplit_nodes_delimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextTypes.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextTypes.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextTypes.TEXT),
            TextNode("code block", TextTypes.CODE),
            TextNode(" word", TextTypes.TEXT),
                ])
        

    def test_split_nodes_delimiter2(self):
        node = TextNode("This is text with a `code block` word", TextTypes.TEXT)
        node2 = TextNode("This is another text with a `code block` word", TextTypes.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "`", TextTypes.CODE)
        '''
        self.assertEqual([
            TextNode("This is text with a ", TextTypes.TEXT),
            TextNode("code block", TextTypes.CODE),
            TextNode(" word", TextTypes.TEXT),
            TextNode("This is another text with a ", TextTypes.TEXT),
            TextNode("code block", TextTypes.CODE),
            TextNode(" word", TextTypes.TEXT),
                ], new_nodes)
                '''