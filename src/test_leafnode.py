import unittest

class TestLeafNode(unittest.TestCase):
    def test_leafnode_with_tag_and_value(self):
        node = LeafNode(tag="p", value="This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")


    def test_leanode_without_tag(self):
        ...


    def test_leafnode_raises_value_error(self):
        ...


    def test_leafnode_with_props(self):
        ...


if __name__ == "__main__":
    unittest.main()
