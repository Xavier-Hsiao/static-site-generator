class HTMLNode:
    # Children is list of HTMLNode objects
    # Props is a dict representing attributes 
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    # Will be overridden by child classes
    def to_html(self):
        raise NotImplementedError("not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return
        
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, props: {self.props})"