from ast import If


class HTMLNode():
	"""docstring for HTMLNode"""
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError("Must be overridden by derived classes")
	
	def props_to_html(self):
		# original: {"href": "https://www.google.com", "target": "_blank"}
		# Return:  href="https://www.google.com" target="_blank"
		if self.props is None:
			return ""
		props_html = ""
		for key, value in self.props.items():
		 	props_html += f' {key}="{value}"'
		return props_html
	
	def __repr__(self):
		return f"HTMLNode(tag:{self.tag}, value:{self.value}, children:{self.children}, props: {self.props})"
	
	def __eq__(self, other):
		return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value is None:
			raise ValueError("Leafnode requires a value")
		if self.tag is None:
			return str(self.value)
		props_html = self.props_to_html()
		return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)
	
	def to_html(self):
		if self.tag is None:
			raise ValueError("ParentNode requires a tag")
		if self.children is None:
			raise ValueError("ParentNode must have children")
		
		# Recursion being called on a nested child node
		props_html = self.props_to_html()
		children_html = ""
		for child in self.children:
			children_html += child.to_html()
		return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"