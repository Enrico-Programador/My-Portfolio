    
import unittest
from block_markdown import BlockTypes, block_to_block_type, markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks(self): 
        md = """
1. This is a
2. ordered list
3. very ordered
"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockTypes.ORDERED_LIST
            )
        md = """
- This is a
- unordered list
- very unordered
"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockTypes.UNORDERED_LIST
            )
        md = """
> This is a
>quote paragraph
> very quoty
"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockTypes.QUOTE
            )
        
        md = """``` This is a
>code paragraph
- with code```"""

        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockTypes.CODE
            )
        md = """###### This is a
>heading paragraph
- with a heading```
"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockTypes.HEADING
            )
        
        md = """
1. #This is a
>normal paragraph```
- anything special
"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockTypes.PARAGRAPH
            )



        
if __name__ == "__main__":
    unittest.main()