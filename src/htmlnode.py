class HTMLNode():
	"""docstring for HTMLNode"""
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props
	def to_HTML(self):
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
		