import unittest
from inline_markdown import (
    split_node_delimiter,
    split_node_delimiter_multiple,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_split_node_delimiter_single(self):
        node = TextNode("The seventh `import getpass` is a good idea", text_type_text)
        new_nodes = split_node_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("The seventh ", text_type_text),
                TextNode("import getpass", text_type_code),
                TextNode(" is a good idea", text_type_text),
            ],
            new_nodes
        )


    def test_split_nodes_delimiter_multi(self):
        node = TextNode("The eigth `import functools` is a good idea", text_type_text)
        node2 = TextNode("The ninth **bolded** word node", text_type_text)
        new_nodes = split_node_delimiter_multiple([node, node2], ["`", "**"], [text_type_code, text_type_bold])
        self.assertListEqual(
            [
                TextNode("The eigth", text_type_text),
                TextNode("import functools", text_type_code),
                TextNode(" is a good idea", text_type_text),
                TextNode("The ninth ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word node", text_type_text)
            ],
            new_nodes
        )


#        node = TextNode("The tenth *italic and **bolded** word* node", text_type_bold)
