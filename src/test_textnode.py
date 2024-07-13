import unittest
from textnode import (
	TextNode,    
	text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
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

if __name__ == "__main__":
	unittest.main()