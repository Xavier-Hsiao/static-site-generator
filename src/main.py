from textnode import Textnode
def main():
	test_node = Textnode("This is a text node", "bold", "https://www.boot.dev")
	test_node_2 = Textnode("This is a text node", "bold", "https://www.boot.dev")
	print(repr(test_node))
main()