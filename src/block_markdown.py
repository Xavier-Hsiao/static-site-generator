from enum import Enum
from htmlnode import HTMLNode
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

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

# Arg: a raw Markdown block of text
# Return: a BlockType object
def block_to_block_type(block):
    # should deal with multlines block
    lines = block.split("\n")

    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    elif len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.ORDERED_LIST
            i += 1
        return BlockType.ORDERED_LIST 
    else:
        return BlockType.PARAGRAPH

def detect_heading_tag(block):
    match block:
        case block.startswith("# "):
            return "h1"
        case block.startswith("## "):
            return "h2"
        case block.startswith("### "):
            return "h3"
        case block.startswith("#### "):
            return "h4"
        case block.startswith("##### "):
            return "h5"
        case block.startswith("###### "):
            return "h6"
        case _:
            raise ValueError("invalid heading markdown syntax!")

def extract_heading_content(heading_block):
    # find where the heading markers end and the actual content begins
    for i, char in enumerate(heading_block):
        if char != "#" and char != " ":
            return heading_block[i:].strip()
    return ""

def create_block_html_node_upon_type(block, type):
    match type:
        case BlockType.HEADING:
            heading_tag = detect_heading_tag(block)
            return HTMLNode(
                heading_tag,
                ...
            )

def markdown_to_html_node(markdown):
    # split the markdwon into block strings list
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        # determine the type of block
        block_type = block_to_block_type(block)
        # Todo: based on the type of block, create a new HTMLNode
        
