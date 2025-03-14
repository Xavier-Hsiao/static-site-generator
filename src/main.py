import os
import shutil
import sys
from copy_static import copy_static
from generate_pages import generate_pages_recursive

def main():
    basepath = ""
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    # delete all the contents in /public
    # notice that `rmtree` will delete the folder itself
    print("Deleting docs folder...\n")
    if os.path.exists("./docs"):
        shutil.rmtree("./docs")
    os.mkdir("./docs")
    copy_static("./static", "./docs")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

main()