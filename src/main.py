from textnode, htmlnode import Textnode, HTMLNode
def main():
	test_node = TextNode("This is a text node", "bold", "https://www.google.com")
	print(repr(test_node))
main()