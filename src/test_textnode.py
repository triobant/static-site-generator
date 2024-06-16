import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)


    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)


    def test_eq_url(self):
        node = TextNode("The third one", text_type_italic, "https://boot.dev")
        node2 = TextNode("The third one", text_type_italic, "https://boot.dev")
        self.assertEqual(node.url, node2.url)
        self.assertEqual(node, node2)


    def test_eq_url_false(self):
        node = TextNode("The fourth one", text_type_text, "https://boot.dev")
        node2 = TextNode("The fourth one", text_type_text)
        self.assertNotEqual(node.url, node2.url)


    def test_eq_url_none(self):
        node = TextNode("The fifth one", text_type_code, "https://boot.dev")
        node2 = TextNode("The fifth one", text_type_code)
        self.assertIsNone(node2.url)


    def test_repr(self):
        node = TextNode("The sixth one", text_type_image, "https://boot.dev")
        self.assertEqual(
                "TextNode(The sixth one, image, https://boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
