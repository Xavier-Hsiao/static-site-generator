import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
	unittest.main()
