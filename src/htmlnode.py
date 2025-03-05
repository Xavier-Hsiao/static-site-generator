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
            return ""
        
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, props: {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("value is required for LeadNode")
        # If there is no tag, the value should be returned as raw test
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, prorps=None):
        super().__init__(tag, None, children, prorps)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("value is required")
        if self.children is None:
            raise ValueError("at least one child HTML node is required")
        
        children_html = ""
        # Every child here is a LeafNode instance
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props})"        
