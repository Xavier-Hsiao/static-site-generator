from genericpath import isdir, isfile
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
    html = html_node.to_html()

    title = extract_title(markdown)
    new_template = template.replace("{{ Title }}", title)
    new_template = new_template.replace("{{ Content }}", html)

    with open(dst_path, "w") as dst_file:
        dst_file.write(new_template)
    print(f"Page generated at {dst_file}")

def generate_pages_recursive(dir_path_content, template_path, dst_dir_path):
    if not os.path.exists(dir_path_content):
        raise ValueError("content directory notfound!")
    content_list = os.listdir(dir_path_content)

    for content in content_list:
        content_path = os.path.join(dir_path_content, content)
        dst_path = os.path.join(dst_dir_path, content)

        if os.path.isdir(content_path):
            os.mkdir(dst_path)
            generate_pages_recursive(content_path, template_path, dst_path)

        if os.path.isfile(content_path) and content.endswith(".md"):
            dst_path = dst_path.replace(".md", ".html")
            generate_page(content_path, template_path, dst_path)




