import os
import shutil
from copy_static import copy_static

SRC = "./static"
DST = "./public"

def main():
    # delete all the contents in /public
    # notice that `rmtree` will delete the folder itself
    print("Deleting public folder...\n")
    if os.path.exists(DST):
        shutil.rmtree(DST)
    os.mkdir(DST)
    copy_static(SRC, DST)

main()