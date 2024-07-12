import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
	def test_to_html_props(self):
		node = HTMLNode(
			"a",
			"This is a test link",
			None,
			{"href": "https://cpbl.com.tw", "class": "baseball"},
		)
		self.assertEqual(
			node.props_to_html(),
			' href="https://cpbl.com.tw" class="baseball"',
		)

	def test_to_html_no_children(self):
		node = LeafNode("p", "My cat is adorable")
		self.assertEqual(node.to_html(), "<p>My cat is adorable</p>")

	def test_to_html_no_tag(self):
		node = LeafNode(None, "I don't have any tag")
		self.assertEqual(node.to_html(), "I don't have any tag")

if __name__ == "__main__":
	unittest.main()
