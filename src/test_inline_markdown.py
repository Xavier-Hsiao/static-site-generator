import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
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
    
    def test_code_symbol(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )
    
    def test_double_italic(self):
        node = TextNode("Counting the _star_ in the sky, it was like _a lullaby_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Counting the ", TextType.TEXT),
                TextNode("star", TextType.ITALIC),
                TextNode(" in the sky, it was like ", TextType.TEXT),
                TextNode("a lullaby", TextType.ITALIC)
            ]
        )
    
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ]
        )
    
    def test_extract_markdown_links(self):
        text = "This is text with a link [to cpbl website](https://www.cpble.com.tw) and [to youtube](https://www.youtube.com)"
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("to cpbl website", "https://www.cpble.com.tw"),
                ("to youtube", "https://www.youtube.com"),
            ]
        )

if __name__ == "__main__": 
    unittest.main()