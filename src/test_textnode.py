import unittest
from textnode import TextNode

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

if __name__ == "__main__":
	unittest.main()