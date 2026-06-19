import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from splitnode import split_nodes_delimiter, split_nodes_image, split_nodes_link
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
        
        self.assertEqual([
            TextNode("This is text with a ", TextTypes.TEXT),
            TextNode("code block", TextTypes.CODE),
            TextNode(" word", TextTypes.TEXT),
            TextNode("This is another text with a ", TextTypes.TEXT),
            TextNode("code block", TextTypes.CODE),
            TextNode(" word", TextTypes.TEXT),
                ], new_nodes)
        

    def test_split_nodes_delimiter3(self):
        node = TextNode("This is text with two `code block` word `code block` ", TextTypes.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextTypes.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with two ", TextTypes.TEXT),
            TextNode("code block", TextTypes.CODE),
            TextNode(" word ", TextTypes.TEXT),
            TextNode("code block", TextTypes.CODE),
                ])
        #new tests
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextTypes.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextTypes.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextTypes.TEXT),
                TextNode("bolded", TextTypes.BOLD),
                TextNode(" word", TextTypes.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextTypes.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextTypes.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextTypes.TEXT),
                TextNode("bolded", TextTypes.BOLD),
                TextNode(" word and ", TextTypes.TEXT),
                TextNode("another", TextTypes.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextTypes.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextTypes.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextTypes.TEXT),
                TextNode("bolded word", TextTypes.BOLD),
                TextNode(" and ", TextTypes.TEXT),
                TextNode("another", TextTypes.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextTypes.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextTypes.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextTypes.TEXT),
                TextNode("italic", TextTypes.ITALIC),
                TextNode(" word", TextTypes.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextTypes.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextTypes.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextTypes.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextTypes.BOLD),
                TextNode(" and ", TextTypes.TEXT),
                TextNode("italic", TextTypes.ITALIC),
            ],
            new_nodes,
        )
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextTypes.TEXT,
            )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextTypes.TEXT),
                TextNode("image", TextTypes.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextTypes.TEXT),
                TextNode(
                    "second image", TextTypes.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
            )
        
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextTypes.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextTypes.TEXT),
                TextNode("image", TextTypes.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextTypes.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextTypes.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextTypes.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextTypes.TEXT),
                TextNode("image", TextTypes.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextTypes.TEXT),
                TextNode(
                    "second image", TextTypes.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://wikipedia.org) with text that follows",
            TextTypes.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextTypes.TEXT),
                TextNode("link", TextTypes.LINK, "https://boot.dev"),
                TextNode(" and ", TextTypes.TEXT),
                TextNode("another link", TextTypes.LINK, "https://wikipedia.org"),
                TextNode(" with text that follows", TextTypes.TEXT),
            ],
            new_nodes,
        )