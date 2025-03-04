import unittest

from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()