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