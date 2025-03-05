import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    # Test ParentNode
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "I'm a child node")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>I'm a child node</span></div>"
        )
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "I am a grandchild node")
        child_node = ParentNode("span", [grandchild_node], {"class": "second-layer"})
        parent_node = ParentNode("div", [child_node], {"class": "first-layer"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="first-layer"><span class="second-layer"><b>I am a grandchild node</b></span></div>'
        )
    
    def test_to_html_with_many_children(self):
        node = ParentNode(
            "h2",
            [   
                LeafNode("span", "I'm a wrapper"),
                LeafNode("b", "I'm bold"),
                LeafNode(None, "Normal text here!")
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<h2><span>I'm a wrapper</span><b>I'm bold</b>Normal text here!</h2>"
        )

if __name__ == "__main__":
    unittest.main()