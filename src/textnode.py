from htmlnode import LeafNode
import re

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
	
	def extract_markdown_images(self, text):
		matched_list = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
		return matched_list

	def extract_markdown_links(self, text):
		matched_list = re.findall(r"\[(.*?)\]\((.*?)\)", text)
		return matched_list	
	
	def split_nodes_link(self, old_nodes):
		new_nodes = []
		for old_node in old_nodes:
			if old_node.text_type is not text_type_text:
				new_nodes.append(old_node)
				continue

			links = old_node.extract_markdown_links(old_node.text)
			original_text = old_node.text

			# Handle invalid links
			if len(links) == 0:
				new_nodes.append(old_node)
				continue
			
			for link in links:
				sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
				# Handle not-closed link markdown
				if len(sections) != 2:
					raise ValueError("Invalid markdown, link markdown not closed")
				# Make sure that the first part is valid text
				if sections[0] != "":
					new_nodes.append(TextNode(sections[0].strip(), text_type_text))

				new_nodes.append(TextNode(link[0], text_type_link, link[1]))
				original_text = sections[1]
			
			# Append the section after the final link
			if original_text != "":
				new_nodes.append(TextNode(original_text.strip(), text_type_text))
		
		return new_nodes
	
	def split_nodes_image(self, old_nodes):
		new_nodes = []
		for old_node in old_nodes:
			if old_node.text_type is not text_type_text:
				new_nodes.append(old_node)
				continue

			images = old_node.extract_markdown_links(old_node.text)
			original_text = old_node.text

			# Handle invalid links
			if len(images) == 0:
				new_nodes.append(old_node)
				continue
			
			for image in images:
				sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
				# Handle not-closed link markdown
				if len(sections) != 2:
					raise ValueError("Invalid markdown, image markdown not closed")
				# Make sure that the first part is valid text
				if sections[0] != "":
					new_nodes.append(TextNode(sections[0].strip(), text_type_text))

				new_nodes.append(TextNode(image[0], text_type_image, image[1]))
				original_text = sections[1]
			
			# Append the section after the final link
			if original_text != "":
				new_nodes.append(TextNode(original_text.strip(), text_type_text))

		return new_nodes
	
	



