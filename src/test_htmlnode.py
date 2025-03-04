import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "This is a test anchor tag", None, {"href": "https://cpbl.com.tw", "class": "test"})
        self.assertEqual(node.props_to_html(), ' href="https://cpbl.com.tw" class="test"')
    
    def test_props_to_html_false(self):
        node = HTMLNode("a", "This is a test anchor tag", None, {"href": "https://cpbl.com.tw", "class": "test"})
        self.assertNotEqual(node.props_to_html(), 'href="https://cpbl.com.tw" class="test"')
    
    def test_value(self):
        node = HTMLNode("div", "Value test")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Value test")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    def test_repr(self):
        node = HTMLNode("a", "This is a test anchor tag", None, {"href": "https://cpbl.com.tw", "class": "test"})
        self.assertEqual(
            repr(node), 
            "HTMLNode(a, This is a test anchor tag, children: None, props: {'href': 'https://cpbl.com.tw', 'class': 'test'})"
        )

if __name__ == "__main__":
    unittest.main()