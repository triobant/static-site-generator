import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
                "div",
                "Hello, world!",
                None,
                {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
                node.props_to_html(),
                ' class="greeting" href="https://boot.dev"',
        )


    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


    def test_leafnode_with_tag_and_value(self):
        node = LeafNode(tag="p", value="This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")


    def test_leafnode_raises_value_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag="p", value=None)
            node.to_html()


    def test_leafnode_with_props(self):
        node = LeafNode(tag="a", value="Click me", props={"href": "https://www.example.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.example.com">Click me</a>')


if __name__ == "__main__":
    unittest.main()
