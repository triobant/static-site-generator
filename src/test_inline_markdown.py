import unittest
from inline_markdown import (
    split_nodes_delimiter,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("The first **bolded** word node", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("The first ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word node", text_type_text)
            ],
            new_nodes
        )


    def test_delim_bold_double(self):
        node = TextNode(
            "The double **bolded** word and **second** node", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("The double ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("second", text_type_bold),
                TextNode(" node", text_type_text)
            ],
            new_nodes
        )


    def test_delim_bold_multiword(self):
        node = TextNode(
            "The multiword **bolded word** and **third** node", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("The multiword ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("third", text_type_bold),
                TextNode(" node", text_type_text)
            ],
            new_nodes
        )


    def test_delim_italic(self):
        node = TextNode("The third *italic* word and node", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("The third ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and node", text_type_text),
            ],
            new_nodes
        )


    def test_delim_bold_and_italic(self):
        node = TextNode("This is the fourth **bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is the fourth ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic)
            ],
            new_nodes
        )


    def test_delim_code(self):
        node = TextNode("The fifth `import getpass` is a good idea", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("The fifth ", text_type_text),
                TextNode("import getpass", text_type_code),
                TextNode(" is a good idea", text_type_text),
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()
