import os
import shutil
from copy_static import copy_static
from generate_pages import generate_page, generate_pages_recursive

def main():
    # delete all the contents in /public
    # notice that `rmtree` will delete the folder itself
    print("Deleting public folder...\n")
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    os.mkdir("./public")
    copy_static("./static", "./public")
    # generate_page("./content/index.md", "./template.html", "./public/index.html")
    generate_pages_recursive("./content", "./template.html", "./public")

main()