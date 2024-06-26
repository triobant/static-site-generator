import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
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


    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "Text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
                "Text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev")
            ],
            matches
        )


    def test_split_image(self):
        node = TextNode(
            "This is a ![story](https://en.wikipedia.org/wiki/The_Fresh_Prince_of_Bel-Air#/media/File:Fresh_Prince_Bel_Aire_logo.svg)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a ", text_type_text),
                TextNode("story", text_type_image, "https://en.wikipedia.org/wiki/The_Fresh_Prince_of_Bel-Air#/media/File:Fresh_Prince_Bel_Aire_logo.svg"),
            ],
            new_nodes,
        )


    def test_split_image_single(self):
        node = TextNode(
            "![single](https://i0.wp.com/www.moreradiance.com/wp-content/uploads/2017/05/How-to-Be-Happy-Being-Single.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("single", text_type_image, "https://i0.wp.com/www.moreradiance.com/wp-content/uploads/2017/05/How-to-Be-Happy-Being-Single.png"),
            ],
            new_nodes,
        )


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                ),
            ],
            new_nodes
        )


    def test_split_link(self):
        node = TextNode(
            "This is a [story](https://en.wikipedia.org/wiki/The_Fresh_Prince_of_Bel-Air)",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a ", text_type_text),
                TextNode("story", text_type_link, "https://en.wikipedia.org/wiki/The_Fresh_Prince_of_Bel-Air"),
            ],
            new_nodes,
        )


    def test_split_link_single(self):
        node = TextNode(
            "[single](https://moreradiance.com/how-to-be-happy-being-single/)",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("single", text_type_link, "https://moreradiance.com/how-to-be-happy-being-single/"),
            ],
            new_nodes,
        )


    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode(
                    "another link", text_type_link, "https://blog.boot.dev"
                ),
            ],
            new_nodes,
        )


    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
            nodes,
        )


if __name__ == "__main__":
    unittest.main()
