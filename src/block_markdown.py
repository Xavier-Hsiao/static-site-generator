from enum import Enum
from htmlnode import HTMLNode, ParentNode
import re

from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


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
        cleaned_block = block.strip()
        # ignore empty blocks
        if cleaned_block == "":
            continue
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

# convert block's inline markdown into textnodes as children list
def text_to_children(text):
    # convert text into textnode
    text_nodes = text_to_textnodes(text)
    # convert each textnode into LeafNode instance
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level > 6:
        raise ValueError("invalid heading markdown syntax!")
    
    # extract content, should take care of the space after #s
    content = block[level + 1:]
    children = text_to_children(content)

    return  ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block syntax!")
    content = block[4:-3]

    # code blocks should be surrounded by a `code` tag
    # nested in a `pre` tag
    raw_text_node = TextNode(content, TextType.TEXT)
    code_child_html_node = text_node_to_html_node(raw_text_node)
    code_html_node = ParentNode("code", [code_child_html_node])

    return ParentNode("pre", [code_html_node])

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block syntax")
        # get the real content of line!
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)

    return ParentNode("blockquote", children)

def unordered_list_to_html_node(block):
    lines = block.split("\n")
    li_items = []
    for line in lines:
        if not line.startswith("- "):
            raise ValueError("invalid unordered list syntax!")
        # get the real content of each line
        content = line[2:]
        li_children = text_to_children(content)
        li_items.append(ParentNode("li", li_children))
    return ParentNode("ul", li_items)

def ordered_list_to_html_node(block):
    lines = block.split("\n")
    li_items = []
    for line in lines:
        # get the real content of each line
        content = line[3:]
        li_children = text_to_children(content)
        li_items.append(ParentNode("li", li_children))
    return ParentNode("ol", li_items)

def paragraph_to_html_node(block):
    content = block.replace("\n", " ")
    children = text_to_children(content)
    return ParentNode("p", children)


# convert block into ParentNode based on its block type
def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return ordered_list_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html_node(block)
        case _:
            return paragraph_to_html_node(block)

def markdown_to_html_node(markdown):
    # split the markdwon into block strings list
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        # get the ParentNode representing block's html_node
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)
        
