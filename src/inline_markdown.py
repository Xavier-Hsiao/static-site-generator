import re
from textnode import TextType, TextNode

# create TextNodes from raw markdown strings
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        # We only split text-type objects
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        old_node_sections = old_node.text.split(delimiter)
        if len(old_node_sections) % 2 == 0:
            raise ValueError("invalid markdown syntax: probably missing closing symbols")
        
        for i in range(0, len(old_node_sections)):
            # handle leading and trailing empty string split
            if old_node_sections[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(old_node_sections[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(old_node_sections[i], text_type))
    
    return new_nodes

# Arg: raw markdown text
# Return: a list of tuples containing the "alt text" and "url"
def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

'''
Input:
node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)

Output:
new_nodes = split_nodes_link([node])
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]
'''
def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        # We only split text-type objects
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        # Todo: copy the text of the old_node
        original_text = old_node.text
        # Todo: extrat images from the old_node
        images = extract_markdown_images(original_text)
        # Todo: if there are no images -> return a list of the original TextNode
        if len(images) == 0:
            new_nodes.append(old_node)
            return old_nodes
        # Todo: loop throgh the images, use image as the delimiter and split the text into two sections
        for image in images:
            old_node_sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            # Todo: handle invalid sytax of missing closing symbol
            if len(old_node_sections) != 2:
                raise ValueError("invalid markdown syntax: probably missing closing symbols")
            # Todo: skip leading empty string 
            if old_node_sections[0] == "":
                continue
            new_nodes.append(TextNode(old_node_sections[0], TextType.TEXT))
            # Todo: append image-type node
            new_nodes.append(TextNode(
                image[0],
                TextType.IMAGE,
                image[1],
            ))
            # Todo: skip trailing empty string
            original_text = old_node_sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    
    return new_nodes