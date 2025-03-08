import unittest
from block_markdown import (
    block_to_block_type, 
    markdown_to_blocks,
    BlockType,
)

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
    
    def test_markdown_to_blocks_multiple_blank_lines(self):
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
    
    def test_blcok_type_heading(self):
        md = """
## I am H2
    """

        self.assertEqual(
            block_to_block_type(md),
            BlockType.HEADING
        )
    
    def test_blcok_type_heading_false(self):
        md = """
####I am H2
    """

        self.assertNotEqual(
            block_to_block_type(md),
            BlockType.HEADING
        )
    
    def test_blcok_type_code(self):
        md = """
```Python
I am a block of code
```
    """

        self.assertEqual(
            block_to_block_type(md),
            BlockType.CODE
        )
    
    def test_block_type_code_false(self):
        md = """
```Python
I am missing the closing triple ticks...
"""

        self.assertNotEqual(
            block_to_block_type(md),
            BlockType.CODE
        )
    
    def test_block_type_quote(self):
        md = """
>This is a inspirational quote!\nContinue
"""

        self.assertEqual(
            block_to_block_type(md),
            BlockType.QUOTE
        )