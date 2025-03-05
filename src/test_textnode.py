import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_text_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_type_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.LINK, "https://cpbl.com.tw")
        node2 = TextNode("This is a text node", TextType.LINK, "https://cpbl.com.tw") 
        self.assertEqual(node, node2)
    
    def test_url_eq_false(self):
        node = TextNode("This is a text node", TextType.LINK, "https://cpbl.com.tw")
        node2 = TextNode("This is a text node", TextType.LINK, "https://google.com")
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.LINK, "https://cpbl.com.tw")
        self.assertEqual(repr(node), f"TextNode(This is a text node, link, https://cpbl.com.tw)")
    
    def test_text_to_html_plaintext(self):
        text_node = TextNode("I love my cat", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "I love my cat")
    
    def test_text_to_html_image(self):
        text_node = TextNode("I love baseball", TextType.IMAGE, "https://cpbl.com.tw")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {
                "src": "https://cpbl.com.tw",
                "alt": "I love baseball"
            }
        )
    
    def test_text_to_html_bold(self):
        text_node = TextNode("I am bold", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "I am bold")
    
    def test_text_to_html_link(self):
        text_node = TextNode("I am link", TextType.LINK, "https://cpbl.com.tw")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "I am link")
        self.assertEqual(html_node.props, {"href": "https://cpbl.com.tw"})

if __name__ == "__main__":
    unittest.main()