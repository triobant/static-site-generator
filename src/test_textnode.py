import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)


    def test_text_type(self):
        node = TextNode("The second one", "bold")
        node2 = TextNode("The second one", "italic")
        self.assertNotEqual(node.text_type, node2.text_type)


    def test_url(self):
        node = TextNode("The second one", "bold", "https://boot.dev")
        node2 = TextNode("The second one", "italic")
        self.assertNotEqual(node.url, node2.url)
        self.assertIsNone(node2.url)


if __name__ == "__main__":
    unittest.main()
