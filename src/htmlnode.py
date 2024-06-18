class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError("to_html method not implemented")


    def props_to_html(self):
        if self.props == None:
            return ""

        final_str = ""
        for key, value in self.props.items():
            final_str += f' {key}="{value}"'
        return final_str


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
