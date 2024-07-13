from lib2to3.pytree import Leaf
import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode

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

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "Cute baby")
		parent_node = ParentNode("p", [child_node])
		self.assertEqual(parent_node.to_html(), "<p><span>Cute baby</span></p>")
	
	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "Young and sweet")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span><b>Young and sweet</b></span></div>")

	def test_to_html_with_many_children(self):
		test_node = ParentNode(
			"p",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "Italic text"),
				LeafNode(None, "Normal text"),
			]
		) 
		self.assertEqual(test_node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>")		

	def test_text_node_to_html_node(self):
		text_node = TextNode("I am bold", "bold")
		expected_html_node = LeafNode("b", "I am bold")
		generated_html_node = text_node.text_node_to_html_node()
		self.assertEqual(generated_html_node, expected_html_node)
	
	def test_text_node_to_html_node_link(self):
		text_node = TextNode("I am image", "image", "https://cpbl.com.tw")
		expected_html_node = LeafNode("img", "", {"src": "https://cpbl.com.tw"})
		generated_html_node = text_node.text_node_to_html_node()
		self.assertEqual(generated_html_node, expected_html_node)

if __name__ == "__main__":
	unittest.main()
