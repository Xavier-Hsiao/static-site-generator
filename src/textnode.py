from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode():
	"""docstring for Textnode"""
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url
	def __eq__(self, other):
		return (
			self.text == other.text
			and self.text_type == other.text_type
			and self.url == other.url)
	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"
	
	def text_node_to_html_node(self):
		supported_text_types = {
			text_type_text: LeafNode(tag=None, value=self.text),
			text_type_bold: LeafNode(tag="b", value=self.text),
			text_type_italic: LeafNode(tag="i", value=self.text),
			text_type_code: LeafNode(tag="code", value=self.text),
			text_type_link: LeafNode(tag="a", value=self.text, props={"href": self.url}),
			text_type_image: LeafNode(tag="img", value="", props={"src": self.url})
		}

		if self.text_type not in supported_text_types:
			raise ValueError(f"Unsupported text type: {self.text_type}")
		
		return supported_text_types[self.text_type]
	
	def split_nodes_delimiter(self, old_nodes, delimiter, text_type):
		new_nodes = []
		for old_node in old_nodes:
			# Add non-text type to new_nodes without modification
			if old_node.text_type is not text_type_text:
				new_nodes.append(old_node)
				continue
			split_nodes = []
			parts = old_node.text.split(delimiter)
			# Handle not-closed markdown format
			if len(parts) % 2 == 0:
				raise ValueError("Unvalid markdown format, missing close tag")
			# Use index to determine the part of node is text or other type
			for i in range(len(parts)):
				# Handle unexpected whitespace
				if parts[i] == "":
					continue
				if i % 2 == 0:
					split_nodes.append(TextNode(parts[i], text_type_text))
				else:
					split_nodes.append(TextNode(parts[i], text_type))
			new_nodes.extend(split_nodes)
		return new_nodes