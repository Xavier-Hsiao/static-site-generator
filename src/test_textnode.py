import unittest
from textnode import (
	TextNode,    
	text_type_text,
    text_type_bold,
	text_type_link,
	text_type_image,
)

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", "bold", "https://google.com")
		node2 = TextNode("This is a text node", "bold", "https://google.com")
		self.assertEqual(node, node2)
	def test_eq_false(self):
		node = TextNode("This is a text node", "text")
		node2 = TextNode("This is a text node", "bold")
		self.assertNotEqual(node, node2)
	def test_eq_false2(self):
		node = TextNode("This is a text node", "text")
		node2 = TextNode("This is a text node2", "text")
		self.assertNotEqual(node, node2)
	def test_eq_url(self):
		node = TextNode("This is a text node", "italic", "https://cpbl.com.tw")
		node2 = TextNode("This is a text node", "italic", "https://cpbl.com.tw")
		self.assertEqual(node, node2)
	def test_repr(self):
		node = TextNode("This is a text node", "text", "https://google.com")
		self.assertEqual(
			"TextNode(This is a text node, text, https://google.com)", repr(node)
		)
	
	def test_delimiter_bold(self):
		node = TextNode("This is a **bold** text node", text_type_text)
		new_node = node.split_nodes_delimiter([node], "**", text_type_bold)
		self.assertListEqual(new_node, [
			TextNode("This is a ", text_type_text),
			TextNode("bold", text_type_bold),
			TextNode(" text node", text_type_text)
		])
	def test_none_text_node_unchanged(self):
		node = TextNode("This is a link node", "link")
		new_node = node.split_nodes_delimiter([node], "**", text_type_bold)
		self.assertListEqual(new_node, [node])
	
	def test_delimiter_double_bold(self):
		node = TextNode("I am **bold** plus **doubold**", text_type_text)
		new_node = node.split_nodes_delimiter([node], "**", text_type_bold)
		self.assertListEqual(new_node, [
			TextNode("I am ", text_type_text),
			TextNode("bold", text_type_bold),
			TextNode(" plus ", text_type_text),
			TextNode("doubold", text_type_bold)
		])
	
	def test_extract_image(self):
		text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
		test_node = TextNode(text, "image")
		expected = [
			("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
			("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
		]
		self.assertEqual(test_node.extract_markdown_images(text), expected)
	def test_extract_links(self):
		text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
		test_node = TextNode(text, "link")
		expected = [
			("to boot dev", "https://www.boot.dev"), 
			("to youtube", "https://www.youtube.com/@bootdotdev"),
		]
		self.assertEqual(test_node.extract_markdown_links(text), expected)

	def test_split_links(self):
		test_node = TextNode(
    		"This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    		text_type_text,
		)
		new_nodes = test_node.split_nodes_link([test_node])
		self.assertListEqual(new_nodes, [
			TextNode("This is text with a link", text_type_text),
			TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
			TextNode("and", text_type_text),
			TextNode(
				"to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
			),
		])
	def test_split_images(self):
		test_node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
		new_nodes = test_node.split_nodes_image([test_node])
		self.assertListEqual(
            [
                TextNode("This is text with an", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("and another", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )		
	
if __name__ == "__main__":
	unittest.main()