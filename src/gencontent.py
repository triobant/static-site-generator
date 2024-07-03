import os
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    ...


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")
