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

if __name__ == "__main__":
    unittest.main()
