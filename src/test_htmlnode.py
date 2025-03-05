import unittest

from htmlnode import HTMLNode, LeafNode

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
    
    # Test Leafnode
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "I love my cat!")
        self.assertEqual(node.to_html(), "<p>I love my cat!</p>")
    
    def test_leaf_to_html_anchor(self):
        node = LeafNode("a", "I love my cat!", {"href": "https://cpbl.com.tw"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://cpbl.com.tw">I love my cat!</a>'
        )
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "I have no tag")
        self.assertEqual(node.to_html(), "I have no tag")

if __name__ == "__main__":
    unittest.main()