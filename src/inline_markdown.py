from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_node_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        else:
            parts = old_node.text.split(delimiter)
            if len(parts) != 3:
                raise Exception("Invalid markdown syntax")

            text_types = ["text", text_type, "text"]
            new_nodes.extend(
                list(
                    map(lambda i: TextNode(parts[i], text_types[i]), range(len(parts)))
                )
            )

    return new_nodes


def split_node_delimiter_multiple(old_nodes, delimiters, text_types):
    new_nodes = old_nodes
    for delimiter, new_text_type in zip(delimiters, text_types):
        new_node = split_node_delimiter(new_nodes, delimiter, new_text_type)
    return new_nodes
