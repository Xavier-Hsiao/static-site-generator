import os
from block_markdown import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line.strip("#").strip()
            return title
    raise ValueError("title text unfound!")

def generate_page(from_path, template_path, dst_path):
    print(f"Generating page from {from_path} to {dst_path} using {template_path}")
    with open(from_path) as file:
        markdown = file.read()
    with open(template_path) as t:
        template = t.read()
    
    html_node = markdown_to_html_node(markdown)
    print(f"Parent Node: {html_node}")
    html = html_node.to_html()
    print(f"html: {html}")

    title = extract_title(markdown)
    new_template = template.replace("{{ Title }}", title)
    new_template = new_template.replace("{{ Content }}", html)

    with open(dst_path, "w") as dst_file:
        dst_file.write(new_template)
    print(f"Page generated at {dst_file}")



