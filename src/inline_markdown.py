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