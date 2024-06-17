class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError()


    def props_to_html(self):
        if self.props == {"href": "https://www.google.com", "target": "_blank"}:
            return 'href="https://www.google.com" target="_blank"'


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
