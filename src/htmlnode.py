class HTMLNode:
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        ...


    def props_to_html(self):
        ...


    def __repr__(self):
        ...
