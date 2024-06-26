markdown = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

def markdown_to_blocks(markdown):
    blocks = []
    splitted = markdown.split("\n\n")
    for block in splitted:
        if block != "":
            blocks.append(block.strip())
    return blocks

print(markdown_to_blocks(markdown))
