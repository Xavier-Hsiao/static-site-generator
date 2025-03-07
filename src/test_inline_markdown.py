import unittest

from inline_markdown import (
    split_nodes_delimiter, 
    extract_markdown_images, 
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)
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
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        node = TextNode(
            "I have been to [baseball](https://www.cpbl.com.tw) and [google](https://www.google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("I have been to ", TextType.TEXT),
                TextNode("baseball", TextType.LINK, "https://www.cpbl.com.tw"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "google", TextType.LINK, "https://www.google.com"
                ),
            ],
            new_nodes,
        )
    
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )

if __name__ == "__main__": 
    unittest.main()