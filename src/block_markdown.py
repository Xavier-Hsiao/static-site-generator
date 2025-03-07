# Arg: a raw Markdown string
# Return: a list of block strings
def markdown_to_blocks(markdown):
    # split text by blank lines
    original_strings = markdown.split("\n\n")
    new_strings = []
    for block in original_strings:
        # ignore empty blocks
        if block == "":
            continue
        cleaned_block = block.strip()
        new_strings.append(cleaned_block)
    return new_strings