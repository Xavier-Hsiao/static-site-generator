import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_single_bold(self):
        node = TextNode("I really **love** my cat!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("I really ", TextType.TEXT),
                TextNode("love", TextType.BOLD),
                TextNode(" my cat!", TextType.TEXT)
            ]
        )
    
    def test_missing_closing_symbol(self):
        node = TextNode("I really **love my cat!", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)
    
    def test_multiple_symbols(self):
        node = TextNode("My life is a **mess** and **I don't know** how to deal with it...", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("My life is a ", TextType.TEXT),
                TextNode("mess", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("I don't know", TextType.BOLD),
                TextNode(" how to deal with it...", TextType.TEXT)
            ]
        )