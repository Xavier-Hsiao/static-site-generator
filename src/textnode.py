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
		